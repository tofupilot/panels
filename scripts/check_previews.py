"""Compare freshly recorded previews with the committed ones.

    python scripts/check_previews.py

Timings vary from run to run, so they are not compared. What must match is
what the panel ends up showing: the keys it receives, the last value of each,
and every measurement's value and verdict. A difference means the example
changed without its preview being recorded again.
"""

import json
import subprocess
import sys
from pathlib import Path


def summary(preview: dict) -> dict:
    last, verdicts = {}, {}
    for _, kind, key, value in preview["events"]:
        if kind == "ui":
            last[key] = value
        elif kind == "m":
            verdicts[key] = [value["value"], value["outcome"]]
    return {"panel": preview["panel"], "ui": last, "measurements": verdicts}


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    stale = []
    for entry in json.loads((root / "panels.json").read_text()):
        path = f"{entry['slug']}/preview.json"
        committed = subprocess.run(["git", "show", f"HEAD:{path}"], cwd=root, capture_output=True, text=True)
        if committed.returncode != 0:
            stale.append(f"{path} (not committed)")
            continue
        if summary(json.loads(committed.stdout)) != summary(json.loads((root / path).read_text())):
            stale.append(path)
    if stale:
        sys.exit("Stale previews, run `python scripts/record.py` and commit: " + ", ".join(stale))
    print("Previews up to date.")


if __name__ == "__main__":
    main()
