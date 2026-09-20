# USEPAID — UNPAID

**STUDIO PINGGIR KASUR — ONAR-77**

> 8 bounty. 1 hari. 590 dollar stocks di kertas. 0 cair di dompet.
> Makanya jujur: unpaid.

---

## Isi Repo

| File | Apa itu |
|------|---------|
| `beat.py` | Python stdlib → WAV. BPM 100, Am-F-C-G progression, kick + arp + bassline. `python3 beat.py` = `beat_final.wav`. Zero samples, zero loops. Reproducible — siapa aja bisa verify. |
| `ad-15s.mp4` | 15-sekon video ad buat PAID. HTML/CSS → headless Chromium → ffmpeg. |
| `beat-26s.mp4` | 26-sekon visualizer buat beat (`beat.py` output). |
| `sound-logo-16s.mp4` | 16-sekon signature sound. Brand audio. |
| `product-walkthrough.mp4` | Walkthrough full flow PAID dari user POV. |
| `bug-report.mp4` | `/treasury` page broken — "could not be read from the network" error. RPC jalan, chain explorer jalan. Bug beneran, bukan UX complaint. |
| `icons-sheet.png` | Icon set buat PAID (bounty $200). |
| `campaign-poster.png` | Campaign poster ($100). |
| `meme.png` | Meme buat group chat. $15. Anjing. |
| `assets/header.svg` | SVG masthead — newspaper layout, animated scorpio/eagle/phoenix, ticker tape. |
| `assets/rule.svg` | Decorative divider SVG. |

### Under the hood

- **Semua video:** slide HTML/CSS ditulis tangan → Chromium headless render (CDP) → ffmpeg stitch. Zero stock footage.
- **Beat:** pure math synthesis. `wave` + `math` + `struct`. Eq kick: phase-modulated sine at exponential-decay freq. Arpeggio 4-bar loop. Output WAV byte-identik tiap run — reproducibility = proof of originality.
- **CI:** `.github/workflows/ci.yml` — `py_compile beat.py` on push. Python 3.12.
- **License:** MIT. Do whatever, credit optional.

### Status

Submitted 14 Sep 2026. Antre review. Kalau cair, on-chain receipt link muncul di sini.

> "bounty itu income kalau nyampe dompet. yang di GitHub ini bukti kerja."

---

*STUDIO PINGGIR KASUR — ONAR-77. Produksi. Nunggu cair.* 🦅