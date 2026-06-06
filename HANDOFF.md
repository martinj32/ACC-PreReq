---
session: 2026-06-06
status: planning complete, build not started
---

# Handoff Note -- ACC Course Build

## Completed This Session

- Moved 9 source markdown files from WSL (`\\wsl$\Ubuntu\home\jmart\ACC-Student-Files\PreReq`) to `C:\Users\jmart\ACC-Content\`
- Created `ACC-Course-Build-Plan.md` with full plan, stack decisions, and task checklist
- Initialized git repo in ACC-Content
- Initial commit with all source files and plan (commit: dc5e2a7)
- Updated `claude_context/projects.md` with ACC-Content project entry
- Saved project memory (`project_acc_course.md`) and updated MEMORY.md
- Added feedback memory: do not check ACC-Student-Files git status during /liftoff

## In Progress

Nothing in progress. This was a planning session only.

## Next Steps

1. Ask Jake for any additional source material to finalize course scope
2. Set up folder structure: `slides/`, `site/`, `teaching-guide/`, `source/`
3. Move source .md files into `source/`
4. Install MkDocs + Material theme: `pip install mkdocs mkdocs-material`
5. Run `mkdocs new .` to scaffold the site config
6. Configure `mkdocs.yml` navigation (Mental Models, M1-M8, Teaching Guide)
7. Begin building website pages from source files
8. Begin building slide decks with python-pptx

## Context for Next Session

- **Project location:** `C:\Users\jmart\ACC-Content\`
- **Plan file:** `ACC-Course-Build-Plan.md` -- read this first
- **Stack:** MkDocs + Material theme (website), python-pptx (slides)
- **Scope:** Mental Models (35 min) + 8-module Prereq Course. ACC main course (3 days) not yet designed -- Jake will provide more source material
- **No GitHub remote yet** -- repo is local only. Set up remote before pushing.
- **Source files are already committed** -- do not move or rename without updating git
