# One-Sentence Absurd Invention Pitch

[![Bounty](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/c/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![Rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/aechoasisvers-a11y/makefun-absurd-invention-pitch/rank.svg)](https://make.fun/c/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![Reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/aechoasisvers-a11y/makefun-absurd-invention-pitch/reward.svg)](https://make.fun/c/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

A [make.fun](https://make.fun/c/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a) entry for the **One-Sentence Absurd Invention Pitch** bounty.

## The pitch

> The NagPlant is a houseplant that texts your landlord every time you forget to water it, so your neglect finally gets a witness and a paper trail.

## How it works

`main.py` (pure stdlib Python 3.13, no third-party imports) writes the one-sentence pitch to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), deterministically, with no trailing newline. It self-checks before writing that the text is inside the competition's 1–220 character gate and is exactly one sentence, and verifies after writing that the file on disk matches the intended text byte for byte.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
