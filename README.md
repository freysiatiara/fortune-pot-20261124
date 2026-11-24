# Fortune in a Pot

[![make.fun](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/freysiatiara/fortune-pot-20261124/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/freysiatiara/fortune-pot-20261124/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)

One kind, funny fortune for a houseplant in a pot — written for the
[Fortune in a Pot bounty](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
on [make.fun](https://make.fun).

## The fortune

> Your newest leaf will unfurl this week, and your keeper will brag about you to everyone who visits the windowsill.

## How it works

`main.py` (Python 3, standard library only) writes that single line to the
output path the grader names — `ENTRY_OUTPUT` when set, otherwise
`OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR` plus `entry.txt`, otherwise
`/output/entry.txt` — using a plain `open`/`write` and setting the file
mode to `0644` explicitly.

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `entry.txt` — the fortune text, exactly as written by `main.py`
- `LICENSE` — MIT
