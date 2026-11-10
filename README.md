# Client Material Analyser

A repeatable process for running client **websites, emails and presentations**
through a saved set of criteria (starting with **The Nine Agreements**) and
getting back a scored report with evidence, suggested rewrites and the
questions to ask the client.

## How to use it

Open a Claude Code session on this repo and say something like:

- `Run https://example.com through the nine agreements`
- `Assess this email against the nine agreements` (then paste the email)
- `Analyse the attached deck using nine-agreements` (upload the .pptx/.pdf/.key/.pages)

Claude uses the `analyse-client-material` skill (`.claude/skills/`) to:

1. **Gather** the content: fetch the site's key buyer pages, or extract the email or slide text.
2. **Score** each criterion 0–3 with direct quotes as evidence.
3. **Cross-check** the whole piece (for the Nine Agreements: order, proof gaps, cost of waiting, urgency).
4. **Report**: save to `reports/`, and optionally as a shareable doc.

## Repo layout

| Path | What it is |
|------|------------|
| `criteria/` | One file per criteria set. `nine-agreements.md` is the first one. |
| `criteria/_TEMPLATE.md` | Copy this to add a new criteria set. |
| `templates/report-template.md` | The structure every report follows. |
| `reports/` | Finished assessments. |
| `scripts/extract_pages_text.py` | Pulls text out of Apple Pages files (`.pages`). |
| `.claude/skills/analyse-client-material/` | The process instructions Claude follows. |

## Adding your own criteria

Copy `criteria/_TEMPLATE.md` to `criteria/<name>.md` and fill in each criterion
(what it means, what to look for, what strong looks like, red flags, questions
to ask). Or paste the criteria to Claude and ask it to save them as a new set.
