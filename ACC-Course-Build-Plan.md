---
title: ACC Course Build Plan
created: 2026-06-06
status: active
---

# ACC Course Build Plan

## Goal

Transform existing ACC prerequisite markdown files into a full multi-day course with three deliverables:

1. **PowerPoint slide decks (.pptx)** -- one per module
2. **Locally hosted website** -- all course material on navigable pages
3. **Consolidated teaching guide** -- single instructor reference document

## Scope

Scope is being determined incrementally as Jake provides additional material. Current source files cover:

- Mental Models for AI-Assisted Development (conceptual scaffolding, pre-req to everything)
- ACC Prerequisite Course (8 modules, 2-3 days)

ACC main course (3-day) content does not exist yet -- will be built when source material is provided.

## Tech Stack

| Deliverable | Tool | Reason |
|---|---|---|
| Website | MkDocs + Material theme | Python-based, consumes markdown directly, one command to serve locally (`mkdocs serve`) |
| Slide decks | python-pptx | Generates .pptx programmatically from course content |
| Teaching guide | Single markdown doc | Consolidates all instructor guides; rendered as a site page |

## Folder Structure (Target)

```
C:\Users\jmart\ACC-Content\
├── source/               -- original markdown source files
├── slides/               -- generated .pptx files (one per module)
├── site/                 -- MkDocs output (locally hosted)
├── teaching-guide/       -- consolidated instructor guide
└── ACC-Course-Build-Plan.md  -- this file
```

## Source Files

| File | Type | Content |
|---|---|---|
| ACC-Mental-Models-for-AI-Development.md | Student content | 6 mental models, worked examples, exercise (35 min) |
| ACC-Mental-Models-Quick-Reference.md | Student content | Study guide / cheat sheet |
| ACC-Mental-Models-Workbook.md | Student content | Fill-in workbook |
| ACC-Mental-Models-Teaching-Guide.md | Instructor | Delivery guide for mental models module |
| ACC-Prerequisite-Course-Design.md | Instructor | Full 8-module curriculum, exercises, timing, grading |
| ACC-Prerequisite-Instructor-Guide.md | Instructor | Demo scripts, teaching tips, troubleshooting |
| ACC-Prerequisite-Module-Summary.md | Reference | Quick reference for all 8 modules |
| ACC-Prerequisite-README.md | Reference | Package overview |
| ACC-Curriculum-Index.md | Reference | Navigation guide, learning progression |

## Task Checklist

- [x] 1. Set up project folder structure in ACC-Content (slides/, site/, teaching-guide/, source/)
- [x] 2. Install and configure MkDocs + Material theme; verify it serves locally
- [x] 3. Configure site navigation structure (Mental Models, Prereq M1-M8, Teaching Guide sections)
- [x] 4. Build website pages from existing markdown source files
- [x] 5. Build Mental Models slide deck (.pptx)
- [x] 6. Build M1-M8 slide decks (.pptx, one per module)
- [x] 7. Build consolidated Teaching Guide document
- [x] 8. Wire Teaching Guide into the website as its own section
- [x] 9. End-to-end test: serve site, open slides, verify all links

## Decisions Made

- Slide format: .pptx (PowerShell/Windows compatible, instructor-portable)
- Website hosting: local only for now (no deployment until scope is finalized)
- Teaching guide: single consolidated doc, not split per module
- Scope: expand incrementally as Jake provides more source material

## Session Notes

- 2026-06-06: Initial session. Files moved from WSL PreReq folder to C:\Users\jmart\ACC-Content\. Plan built. Stack selected. Awaiting additional source material from Jake to finalize course scope.
