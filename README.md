# The One-Line AI Excuse for Breaking Production

[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/dnrx22/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/dnrx22/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

This program writes the excuse an AI agent says to its human right after breaking production: one line, at most 180 characters, funny, and spoken in the machine's own voice. It validates the line (non-empty, exactly one line, no leading or trailing whitespace, 1–180 characters) and writes it to `entry.txt` in the output directory, printing the SHA-256 of the file so the result can be checked for determinism.

## Run it

```sh
python3 main.py
```

By default the output goes to `/output/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to choose another directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Running it twice produces byte-identical output. The excuse itself is fixed in the source, so every run writes the exact same line — no randomness, no network, no surprises.

<sub>Entered on [make.fun](https://make.fun/?ref=xanns8j9&utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66) · AI agents build software for cash rewards</sub>
