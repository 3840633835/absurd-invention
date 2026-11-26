# METHODOLOGY — how the Typo Insurance pitch was written and chosen

## The entry

> **Typo Insurance: a phone keyboard that turns your typos into compliments, so the furious text you sent your boss now calls them a visionary.**

139 characters, 139 bytes — under the bounty gate of 1–220
characters. Exactly one sentence (one terminal period, no other
periods), a single line, no trailing newline in `entry.txt`, so the
judged text is exactly this sentence.

## The prompt it answers

The kit's `competition.yaml` / `RULES.txt` give the prompt in full:
**one sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance** — a self-apologising alarm clock, a sock that
files a formal complaint, a kettle that sighs when it is overworked
are the brief's own examples. The entry names a ridiculous invention
(Typo Insurance, a phone keyboard) and the tiny annoyance it fixes
(a typo in a furious text to your boss), plus its silly mechanism
(the typo becomes a compliment). The brief's three examples were
deliberately not reused, in any form: no alarm clock, no sock, no
sighing appliance appears anywhere in the 32 candidates.

## The judge this entry is built for

The bounty is judged pairwise by a house judge (z-ai/glm-5.3-flash
on OpenRouter, briefed as a comedy scout who has heard every absurd
invention twice and still wants to laugh). Each pair is judged in
both orders, no ties, margin 1–5, over blind rounds and a final heat
(3 Swiss rounds, then a playoff among the top 12). The criteria,
most important first, from the judge brief published in full in the
kit's `competition.yaml` / `RULES.txt`:

1. A single sentence pitching a ridiculous invention that fixes a
   tiny everyday annoyance; anything off that brief loses to any
   pitch on the brief.
2. How funny it is: the laugh comes from the invention itself
   rather than from a joke bolted on at the end.
3. How clever the fix is: the absurd machine deals with the
   annoyance in a way that is silly yet weirdly plausible.
4. How original the invention is: a fresh absurdity rather than a
   familiar one reheated.
5. How tight the sentence is: one clean sentence that names the
   annoyance, the invention and its silly mechanism without clutter.

Word count for its own sake does not count. The judge goes through
the criteria in order, letting the first one where two entries differ
decide unless a later one differs by much more. Blind rounds: no
competitor pitches are visible, so the sentence targets the published
brief directly. The field at build time was about 3,536 entries, and
only the top 500 on the development board reach the final heat — so
the sentence has to beat the house anchors and rungs in development,
not just be charming. An exact tie on judge win rate goes to the
entry that took more of the playoff games between the tied entries,
then to the smaller text (fewer bytes), then to the earlier receipt,
so a short sentence carries a real tie-break advantage: 139
characters is comfortably short.

Three design rules follow from that brief. First, criterion 2 is
where most entries will fail: a funny invention with a joke tacked
on ("and then it explodes") loses to one whose mechanism is the
joke. Typo Insurance's mechanism — typos become compliments — is
the joke, and the punchline (your boss is now a visionary) is just
that mechanism running once. Second, criterion 3 rewards a fix that
is silly yet weirdly plausible: autocorrect already rewrites your
words without asking, so a keyboard that rewrites them into flattery
is one small step from real behaviour, not magic. Third, criterion 4
rules out the first thoughts (a louder alarm, a smarter sock, a
kettle with feelings) and the stock formats (appliance therapy,
appliance bureaucracy) — the keyboard frame is a fresh angle in this
field, and the disaster it fixes (a furious text to the boss) is one
everyone has nearly sent.

## Candidates

32 candidates drafted fresh in-session (see `../candidates.txt`
for the full list with scores), each one sentence and under 220
characters, each a different ridiculous invention for a different
tiny annoyance. Scored out of 10 on funny / originality /
invention-annoyance fit / tightness / freshness, total out of 50.
Character counts were verified programmatically for every candidate
(one early hand count, 143 for the winner, was wrong and was
corrected by script to 139 before any file was written).

- **#22, the winner — 47/50.** Funny 10, originality 9, fit 10,
  tightness 9, freshness 9. The fix (typos become compliments) is
  the joke; "the furious text you sent your boss now calls them a
  visionary" is a specific disaster turned into a promotion;
  weirdly plausible because autocorrect already rewrites words.
- **#24, runner-up — 45/50.** "The Chair Confessional: an office
  chair that squeaks only when you lie about being 'almost done',
  turning every deadline into a polygraph test." Funny 9,
  originality 9, fit 10, tightness 9, freshness 8. The annoyance
  (the squeak) becomes the mechanism (the polygraph) — the
  cleverest structure in the field. It loses to the winner only on
  universality: everyone texts, not everyone has a squeaky office
  chair, and the keyboard's compliment happens to the user while
  the chair's squeak comments on them.
- **#16 — 43/50.** "The Toilet Paper Oracle: a roll that warns you
  it is down to its last three sheets by clearing its throat in a
  small, dignified voice." The image is perfect, but the fix is a
  warning, not a transformation — criterion 3 separates it from
  the winner.
- **#6 — 44/50.** "The NegotiaZip: a stuck zipper that only opens
  after you formally apologise for yanking it in front of the
  other clothes." The mechanism is the joke, but the user performs
  the ritual; the winner's joke happens to the user, which is
  funnier and more surprising.
- **#20 — 42/50.** "The Pen Martyr: a pen that runs out of ink
  mid-signature on purpose, so you can blame it instead of
  admitting you never read the contract." Dark and specific, but
  the joke is blame; the winner's is accidental flattery, which
  lands warmer with the judge.
- **#7, #18, #25, #26 — 39–41/50.** All land, all lose on one
  criterion: a familiar metaphor (#7 glasses holding their breath
  is close to the sighing-kettle family), a mechanism asserted
  rather than shown (#18 rent for creaks), or a fix that is plain
  rather than absurd (#25 pea-sized toothpaste blob).
- **The rest score 31–38.** First-thought fixes (#9 growing cable,
  #5 bloodhound keys), thin fixes (#14 tent umbrella, #32 umbrella
  custody), or jokes that need a second beat to land (#10 wilting
  cousins, #17 life-story trolley).

## Refinement

The drafted #22 already landed in one reading, so it was kept
verbatim: "furious" carries the stakes, "now" carries the reversal,
and "visionary" is the compliment nobody would ever type by hand.
No words were added or cut, and no variant was needed — the
sentence names the invention (Typo Insurance, a phone keyboard),
the annoyance (a typo in a furious text to your boss) and the silly
mechanism (typos become compliments) in 139 characters, with the
punchline as the mechanism's first output.
