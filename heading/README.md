# Heading Indicator

A heading indicator: the compass card turns under the lubber line to the live heading, with a cyan bug on the selected one.

See it live at [tofupilot.com/panels#heading](https://tofupilot.com/panels#heading).

## How It Works

`ui.hdg` turns the whole compass card the other way with `rotate(calc(var(--value) * -1deg))`, so the heading reads under the fixed lubber line. The cyan bug is a group inside the card bound to `ui.hdg_bug`: it turns with the card and sits on the selected heading.

| File | Role |
|---|---|
| `procedure.yaml` | The phase, its measurements and limits, and `ui.panel` |
| `phases/heading.py` | The test |
| `plugs/turntable.py` | The instrument, mocked |
| `panels/heading.html` | The panel |

## Run It

```bash
tofupilot run heading
```

Replace the mock in `plugs/turntable.py` with your turntable's driver to use it on a real bench.
