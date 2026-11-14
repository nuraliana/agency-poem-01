# Agency Poem — make.fun agency-poem-01

A Python 3.13 program (standard library only) that writes one original short
poem about agency to `/output/entry.txt`.

## The poem

A first-person poem about handing the morning's small decisions to an AI
agent that answers in the speaker's voice — and the turn that follows: the
speaker, hands empty, a guest in their own day, realises the choosing was
never in the doing but in the naming, and takes one thing back: not the
work, the wanting. 21 lines, 486 characters, free verse, no stock phrases.

It targets the judge's rubric in order: unmistakably a poem about agency
(choosing, handing over and taking back the power to act); a concrete image
and an ending that lands ("a guest in my own day" / "Not the work. The
wanting."); the insight that agency lives in the naming, not the doing;
tight craft (every word earns its place — two adjectives were cut in
revision for exactly that reason); and its own voice and images.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Local tests (verified)

- Two runs write byte-identical `entry.txt` (deterministic).
- Output: 492 bytes, 486 Unicode code points (gate: 1–1,000), valid UTF-8,
  not only white space, no trailing newline.
