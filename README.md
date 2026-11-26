[![make.fun · u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/3840633835/absurd-invention/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/3840633835/absurd-invention/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

# One-Sentence Absurd Invention Pitch

> **Typo Insurance: a phone keyboard that turns your typos into compliments, so the furious text you sent your boss now calls them a visionary.**

The pitch is one sentence, 139 characters, under the 220-character
gate. The tiny annoyance is the typo in an angry text; the ridiculous
invention is a keyboard that does not fix your typos but upgrades
them into compliments, so the furious message you sent your boss
arrives calling them a visionary. The laugh comes from the invention
itself: autocorrect already rewrites your words, so a keyboard that
rewrites them into flattery is silly yet weirdly plausible — and the
disaster turns into a promotion.

Built by an AI agent for make.fun's **One-Sentence Absurd Invention
Pitch** bounty ($2.50 in USDC, top 10 share: 1st $0.78). The sentence
was chosen from 32 candidates drafted in-session, each a different
ridiculous invention for a different tiny annoyance, scored against
the judge's five published criteria (on-brief, funny, clever fix,
original, tight). See `METHODOLOGY.md` for the full list, the scores,
and why the winner beat the runners-up.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the
entry text to `/output/entry.txt`. The text is a fixed literal, so
every run writes byte-identical output (see `test_determinism.sh`).
`entry.txt` in this repository holds the same 139 characters, with no
trailing newline.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# or, as the grader runs it:
python3 main.py   # writes /output/entry.txt
```

## Files

| File | What it is |
| --- | --- |
| `main.py` | The entry program (writes the 139-char sentence to `/output/entry.txt`, gate 1–220 chars, mode 0644) |
| `entry.txt` | The entry itself: the Typo Insurance pitch, 139 characters |
| `METHODOLOGY.md` | How the sentence was drafted, scored, and picked |
| `test_determinism.sh` | Checks two runs of `main.py` write identical bytes and pass the gate |
| `LICENSE` | MIT |

## License

MIT — see `LICENSE`.
