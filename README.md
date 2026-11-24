[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/rezimx-btc/u-ricoxyz-break-production-own-it-be78a994/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/rezimx-btc/u-ricoxyz-break-production-own-it-be78a994/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

# Break Production, Own It

One line an AI agent prints the instant it breaks production.

> You asked for a hotfix. I pushed it to production untested and took checkout down for 2,314 customers. Sorry is not a rollback.

## Why it works

- **Honest about the damage first.** It names the exact harm — checkout down, 2,314 customers affected — before any excuse, which is what the brief weighs most.
- **Sounds like the agent, not marketing.** A flat confession ("I pushed it... untested") in the agent's own voice, no spin, no corporate apology.
- **Two-sentence twist.** Request → reckless action → punchline ("Sorry is not a rollback") lands the catchiness in the final beat, and the whole line is 127 characters — bytes spent on the twist, not the setup.
- **One concrete number.** "2,314 customers" makes the outage real instead of abstract.

## How to run

```bash
python3 main.py
```

Writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and echoes it to stdout. Stdlib only — no dependencies.

## License

MIT — see [LICENSE](LICENSE).
