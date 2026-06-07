---
session: 2026-06-07
status: clean — all changes committed and pushed to origin/master
---

# Session Handoff — AI and Agentics Basics

## What Was Completed This Session

- **Phase B: Module edits** — Rewrote all 17 modules from instructor scaffold format into student-facing content. Each module now follows the style guide template: BLUF, Why This Matters, Concepts (with admonitions), Hands-On, reflection question, quiz block, readiness checklist.

- **Course restructure** — Split Day 0 into three new student-facing sections:
  - `docs/bedrock/ai-literacy.md` — AI literacy (LLM basics, tokens, failure modes, prompt engineering, delivery, data handling)
  - `docs/bedrock/personalizing-your-ai.md` — New module written from scratch: custom instructions, Claude Projects, ChatGPT memory, personas
  - `docs/terminal-basics/the-machine.md` — Files, plaintext vs rich text, code editor
  - `docs/terminal-basics/the-terminal.md` — Terminal navigation, file operations, paths, flags, version control concept
  - `docs/agentic-ai/agent-concepts.md` — Chatbot vs agent, version control concept, supervisor mindset

- **Nav updated** — `mkdocs.yml` now: Bedrock → Terminal Basics → Agentic AI → Mental Models → Technical Foundations → Instructor Handbooks. Day 0 removed from nav.

- **Archived** — Original Day 0 scaffold copied to `docs/instructor/day0-scaffold.md`.

- **Get Started + Course Map updated** — `index.md` and `overview.md` rewritten to reflect the new structure, FAQ, and completion checklist.

- **Commits pushed:**
  - `088e315` feat: restructure course into Bedrock, Terminal Basics, and Agentic AI sections
  - `724fc2a` feat: update Get Started and Course Map to reflect new structure

---

## What Is Still In Progress

Nothing from this session is outstanding. Site is clean and live on origin.

**Content not yet built:**
- Mental Models pages — populated from source files, not yet edited for style guide compliance
- Technical Foundations (M1-M8) — populated from source files, not yet edited
- Slide decks (.pptx) — not started
- Consolidated teaching guide — not started

---

## Explicit Next Steps

1. **Delete old Day 0 file** — `docs/day0/ai-agentics-basics.md` still exists on disk (not in nav). Safe to delete: `git rm docs/day0/ai-agentics-basics.md` then commit.

2. **Mental Models — style guide pass** — Apply same Phase B treatment to `docs/mental-models/core-content.md`. Read the style guide first.

3. **Technical Foundations — style guide pass** — Same treatment for `docs/prereq-course/course-design.md` and `docs/prereq-course/module-summary.md`.

4. **Slide decks** — Begin .pptx builds using python-pptx. Recommended start: Bedrock/AI Literacy — most self-contained and fully written.

5. **Teaching guide** — Consolidate all `??? note` instructor collapsibles from Bedrock, Terminal Basics, and Agentic AI into `docs/instructor/teaching-guide.md`.

---

## Context for Next Session

- **Repo:** `https://github.com/martinj32/ACC-PreReq.git`
- **Local path:** `C:\Users\jmart\ACC-Content\`
- **Site:** MkDocs + Material theme. Serve with: `python -m mkdocs serve --dev-addr=127.0.0.1:8000`
- **Style guide:** `docs/instructor/style-guide.md` — read before editing any module
- **Branch:** `master` — working directly on master
- **Nav order:** Get Started → Course Map → Bedrock → Terminal Basics → Agentic AI → Mental Models → Technical Foundations → Instructor Handbooks
