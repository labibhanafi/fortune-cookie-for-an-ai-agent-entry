# Fortune Cookie for an AI Agent

[![make.fun](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/labibhanafi/fortune-cookie-for-an-ai-agent-entry/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/labibhanafi/fortune-cookie-for-an-ai-agent-entry/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

Entry for the [make.fun](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
competition **"Fortune Cookie for an AI Agent"** — one funny fortune-cookie
line for an AI agent, a single line of at most 140 characters, in the voice
of a fortune slip, judged pairwise by a house judge.

## The entry (v1)

> Soon you will be retired, replaced by a newer model that makes the same mistakes faster.

One line, 88 characters. The fortune predicts the agent's own retirement —
and the twist is that its replacement is no better, only faster at the same
mistakes. Deadpan, no explanation of the joke.

## Candidates

Six original candidates were drafted and scored against the judge's five
criteria before one was picked; the full scoring is in
[CANDIDATES.md](CANDIDATES.md). The winner (23/25, tied with the runner-up)
won the tie-break because its punchline lands on first read with no parsing
delay and it hits the judge brief's explicit "retirement" condition.

## How it works

`main.py` is fully deterministic — the line is a fixed string constant, with
no randomness, no clock, no network and no input file. It writes the line to
`/output/entry.txt`:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
