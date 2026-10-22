"""Run an example with the TofuPilot CLI and record what its panel shows.

    python scripts/record.py airspeed altimeter ...

Writes <example>/preview.json: the panel's phase and every value the phase
sent while it ran, timestamped, with each measurement's verdict and limits
as the engine judged it. The gallery on tofupilot.com/panels replays it
through the operator UI's own panel renderer, so what it shows is what the
run showed. Values are kept at most every 100 ms per key, enough for the
panel's transitions and small enough to ship to every visitor.

Needs TofuPilot CLI 2.8.0 or newer (live verdicts on measurement_recorded).
Fails when the run does not pass: every example must stay green.
"""

import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import yaml

TOFUPILOT = os.environ.get("TOFUPILOT", "tofupilot")
SAMPLE_MS = 100


def unwrap(value):
    # Measurement values arrive tagged by kind: {"Numeric": 1.2}.
    if isinstance(value, dict) and len(value) == 1:
        return next(iter(value.values()))
    return value


def record(example: Path) -> dict:
    procedure = yaml.safe_load((example / "procedure.yaml").read_text())
    phase = next(p for p in procedure["main"] if p.get("ui", {}).get("panel"))
    units = {m["key"]: m.get("unit") for m in phase.get("measurements", [])}

    with tempfile.NamedTemporaryFile("w", suffix=".json", dir=example, delete=False) as f:
        json.dump({"identify_unit": {"serial_number": "DEMO-0001", "part_number": "DEMO"}}, f)
        ui_values = f.name
    try:
        proc = subprocess.Popen(
            [TOFUPILOT, "run", str(example), "--json", "--ui-values", ui_values],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        events, start, outcome = [], None, None
        for line in proc.stdout:
            if not line.startswith("{"):
                continue
            event = json.loads(line)
            kind = event["type"]
            if kind == "phase_started" and event["phase_key"] == phase["key"]:
                start = time.monotonic()
            if start is None or event.get("phase_key") not in (None, phase["key"]):
                if kind == "run_finished":
                    outcome = event["outcome"]
                continue
            t = round((time.monotonic() - start) * 1000)
            if kind == "ui_update" and event["action"] == "set_value":
                events.append([t, "ui", event["data"]["id"], event["data"]["value"]])
            elif kind == "measurement_recorded":
                key = event["name"]
                verdict = {
                    "value": unwrap(event["value"]),
                    "outcome": event["outcome"].upper(),
                    "low": event.get("low"),
                    "high": event.get("high"),
                    "units": units.get(key),
                }
                events.append([t, "m", key, verdict])
            elif kind == "phase_finished":
                events.append([t, "end", None, None])
            elif kind == "run_finished":
                outcome = event["outcome"]
        proc.wait()
    finally:
        os.unlink(ui_values)

    if outcome != "PASS":
        sys.exit(f"{example.name}: run finished {outcome}, expected PASS")
    events = downsample(events)
    return {
        "procedure": procedure["name"],
        "phase": {"key": phase["key"], "name": phase["name"]},
        "panel": phase["ui"]["panel"],
        "duration_ms": events[-1][0] if events else 0,
        "events": events,
    }


def downsample(events: list) -> list:
    """Keep the last value of each key per SAMPLE_MS window. Measurements and
    the phase's end are always kept."""
    kept, last = [], {}
    for event in events:
        t, kind, key, _ = event
        if kind != "ui":
            kept.append(event)
            continue
        window = t // SAMPLE_MS
        if last.get(key, (None,))[0] == window:
            kept[last[key][1]] = event
        else:
            last[key] = (window, len(kept))
            kept.append(event)
    # A replaced value moved later in its window: restore time order.
    return sorted(kept, key=lambda e: e[0])


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    for name in sys.argv[1:] or [m["slug"] for m in json.loads((root / "panels.json").read_text())]:
        example = root / name
        preview = record(example)
        (example / "preview.json").write_text(json.dumps(preview, separators=(",", ":")) + "\n")
        print(f"{name}: {len(preview['events'])} values over {preview['duration_ms'] / 1000:.1f} s")


if __name__ == "__main__":
    main()
