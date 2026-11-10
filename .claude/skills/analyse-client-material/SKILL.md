---
name: analyse-client-material
description: Assess a client's website, email(s) or presentation against a saved criteria set (e.g. the Nine Agreements) and produce a scored report with evidence, rewrites and client questions. Use when the user says "run X through the nine agreements", "assess this site/email/deck against <criteria>", or pastes client material and names a criteria set.
---

# Analyse client material against criteria

## Inputs
1. **The material** (one or more):
   - **Website:** a URL.
   - **Email:** pasted text, an uploaded .eml/.txt, or a Gmail thread the user names.
   - **Presentation/document:** an uploaded .pptx, .pdf, .key, .pages, .docx, or a Google Slides/Docs link.
2. **The criteria set:** a file in `criteria/` (e.g. `nine-agreements`). If the user doesn't name one and there is more than one, ask which. If the user gives new criteria inline, offer to save them to `criteria/<name>.md` using `criteria/_TEMPLATE.md`.
3. **Optional context:** the client's offer, audience, or price, if the user gives it. Never invent these.

## Step 1: Gather the content
- **Website:** fetch the URL given. Then find and fetch the pages a buyer would see: home, about, the main offer/services/sales page(s), pricing, testimonials/case studies, and any webinar/landing page. Default cap is 8 pages unless the user says otherwise. If a fetch returns little text (JS-rendered site), render it with Playwright (pre-installed) and take the visible text. Note any images that carry key claims and any gated pages you couldn't read.
- **Email:** use the full text, including subject line and P.S.
- **Presentation:** extract text slide by slide, keeping slide numbers (use the pptx/pdf skills; for `.pages` files, unzip into a fresh scratch folder and run `python3 -I scripts/extract_pages_text.py <dir>/Index/*.iwa <dir>/Index/Tables/*.iwa`).
- Keep a record of what was read, so every finding can cite a location (page URL, slide number, paragraph).

## Step 2: Score each criterion
Read the criteria file in full. For each criterion, in order:
- Quote the strongest evidence verbatim, with its location. **Never paraphrase a quote or score on evidence you didn't see.**
- Score it on the file's scale (default 0–3). Apply its "rule of thumb": no specific example or number means a gap.
- Say what's missing, give one concrete recommendation, and write a short example rewrite in the client's own voice (plain words, how they'd say it to one customer).
- List the criteria file's client questions that the material leaves unanswered.

## Step 3: Cross-checks
Run every cross-check in the criteria file (for the Nine Agreements: sequence, missing proof in 6–7, vague cost in 1 and 8, deadline with no reason in 9, voice).

## Step 4: Write the report
- Follow `templates/report-template.md`.
- Save it to `reports/<client-slug>-<criteria-name>-<YYYY-MM-DD>.md`.
- If the user wants a shareable copy, also create a doc (Claude Docs) with the same content. They can export it to Word or PDF.
- In chat, give only the summary: overall score, top 3 fixes, and the report link/path.

## Quality bar
- Be honest and specific; a low score with clear evidence is more useful than flattery.
- Assess the material as a first-time prospect with no call would experience it.
- Keep rewrites as suggestions; flag any that rely on numbers the client must supply (e.g. "£[X] a month").
