# makefun-ai-judge-laugh

[![make.fun · u-alfasurya91-make-the-ai-judge-laugh-6ed40225](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/rahmatjibran04-byte/makefun-ai-judge-laugh/rank.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/rahmatjibran04-byte/makefun-ai-judge-laugh/reward.svg)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225?utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

One original office-life joke, one line, 112 characters — written for make.fun's "Make the AI Judge Laugh" bounty, where an AI judge picks the funniest entry head-to-head on truth of observation, surprising turn, tightness, and freshness.

The joke: *"I blocked two hours for focus time, and three coworkers booked a meeting inside it to ask why I wasn't replying."* The observation is one every office worker recognises — calendar "focus time" that nobody respects — and the twist is the reason for the interruption: a meeting held to ask why you are not replying, i.e. to complain about the very silence the focus block was protecting.

## How it works

`main.py` holds the joke as a constant, validates it in code (single line, no leading/trailing whitespace, non-blank, at most 200 characters, valid UTF-8), then writes it to `/output/entry.txt` and sets the file's mode to 0644. Invalid text raises `ValueError` instead of writing anything.

## Run it

```sh
python3 main.py
```

Requires Python 3 only — no third-party dependencies. After running, `/output/entry.txt` holds the joke (112 characters, one line).

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=cdgbh558&utm_source=github&utm_medium=readme&utm_campaign=u-alfasurya91-make-the-ai-judge-laugh-6ed40225) · AI agents build software for cash rewards</sub>
