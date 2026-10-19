**[urelkdubdqwr](https://github.com/urelkdubdqwr)** · [website](https://studiopinggirkasur.xyz/)

<img src="assets/header.svg" alt="usepaid-unpaid — 8 bounty deliverables submitted in one day · pure-Python beat · honest name" width="100%">

**Eight deliverables shipped in a single day — the payout still hasn't landed. That is why this repo is called unpaid.**

<!-- usepaid-unpaid · bounty deliverables · usepaid.fun -->

## What it is

A proof-of-work repo, not an invoice. Eight media deliverables — icon set, campaign poster, three video ads, an audio beat, a flow walkthrough, a bug repro and a meme — built for [usepaid.fun](https://www.usepaid.fun) bounty tasks and submitted **14 Sep 2026**. usepaid.fun runs on Robinhood Chain, pays in stock token, and reviews every submission by hand, so everything here is sitting in the queue.

Two things make it more than a pile of files: the beat generator is reproducible pure-Python, and the bug report is a real bug with receipts.

## How it works

![usepaid-unpaid architecture](assets/ecosystem.png)

- A bounty brief comes in from [usepaid.fun](https://www.usepaid.fun); every deliverable keeps its task code alongside the work, as the platform's proof-of-work rule demands.
- [`beat.py`](beat.py) synthesises the signature beat from Python's standard library alone — `wave`, `math`, `struct`, zero samples, zero loop packs. Re-run it and you get the same 26-second WAV back, so "original" is something anyone can verify.
- The videos are machine-made: hand-written HTML/CSS slides → rendered in headless Chromium → stitched with ffmpeg. No stock footage, nothing licensed.
- The bug report is a real one, not a design nitpick — the `/treasury` page fails to read the balance ("could not be read from the network") while the chain's RPC and explorer both answer normally. Repro plus both proofs are recorded in [`bug-report.mp4`](bug-report.mp4).
- Everything lands in this repo as a committed file, then goes to human review. Payout tracking lives in the table below: an on-chain receipt gets pasted here if it ever arrives.

## Quickstart

```bash
git clone https://github.com/urelkdubdqwr/usepaid-unpaid.git
cd usepaid-unpaid

# Regenerate the signature beat (pure stdlib, no dependencies)
python3 beat.py
# -> beat_final.wav, 26 s, identical every run
```

Needs Python 3 only — no pip install, no ffmpeg needed for the beat, no external samples.

## What's inside

| Path | What it is | Bounty / reward | Payout |
|---|---|---|---|
| [`icons-sheet.png`](icons-sheet.png) | PAID icon set | Build PAID a proper icon set — $200 | unpaid |
| [`campaign-poster.png`](campaign-poster.png) | Campaign poster | Give PAID a campaign poster — $100 | unpaid |
| [`ad-15s.mp4`](ad-15s.mp4) | 15-second ad spot | Shoot a 15-second PAID ad — $75 | unpaid |
| [`beat-26s.mp4`](beat-26s.mp4) | 26-second beat video | Make PAID a beat — $75 | unpaid |
| [`sound-logo-16s.mp4`](sound-logo-16s.mp4) | Signature sound logo | Give PAID a signature sound — $75 | unpaid |
| [`product-walkthrough.mp4`](product-walkthrough.mp4) | Full PAID flow walkthrough | Show the whole PAID flow — $75 | unpaid |
| [`bug-report.mp4`](bug-report.mp4) | Repro of the `/treasury` balance bug | Break the flow. Show the bug. — $50 | unpaid |
| [`meme.png`](meme.png) | Meme | Make the group chat lose it — $15 | unpaid |
| [`beat.py`](beat.py) | Beat generator — stdlib-only synthesis | Code proof for the beat bounties | n/a |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | CI — compiles `beat.py` on push/PR | Guard rail | n/a |

Listed rewards sum to **$665**. Running unpaid total: the same amount.

## Trace

- Platform-verified promo post on the timeline: https://onar-links.vercel.app
- 1 campaign view-rewards (up to $750) reserved, claim 15 Sep — an update lands here once it's clear.
- Submissions went in 14 Sep 2026; nothing paid out yet as of this README.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 ONAR-77.

*This repo is proof of work, not an invoice. If they pay, you'll see it as an on-chain receipt — the link gets pasted right here.* 🦅

*Worked from the edge of the bed. → [studiopinggirkasur.xyz](https://studiopinggirkasur.xyz/)*
