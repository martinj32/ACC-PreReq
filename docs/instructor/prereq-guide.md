# AI and Agentics Basics — Course Instructor Guide

**For:** Instructors teaching the full AI and Agentics Basics course  
**Purpose:** Detailed implementation guide, demo scripts, troubleshooting, and timing guidance for the 13-unit linear spine  
**Companion:** Run alongside the [Consolidated Teaching Guide](teaching-guide.md) (one section per module, instructor notes surfaced) and the authoritative [Course Map & Schedule](../overview.md).  
**Last Updated:** 2026-06-17

---

## How This Course Is Structured

This is a **single ascending track** — one spine, each concept taught once, every module gated by a readiness check. It runs in two phases:

- **Phase 1 — Foundations (Modules 1–4): multi-week, short daily reps.** Conceptual. Built for someone who uses AI by feel; the mental model sets before any tool enters.
- **Phase 2 — Operator Block (Modules 5–12): 3–4 day intensive.** Hands-on. Each module has a deliverable.

There is no standalone "Mental Models" unit and no "day0" scaffold — both are archived. Their teaching guidance now lives folded into **Module 1** (failure modes, tokens), **Module 7** (harness, operator posture, tool calls), and **Module 8** (tokens, context, cost). Do not look for them as separate sessions.

---

## Quick Reference: The 13 Units

| # | Module | Phase | Key Deliverable | Instructional Mode |
|---|--------|-------|-----------------|--------------------|
| 1 | **Know Your Weapon: How AI Actually Works** | Foundations | Hallucination produced; verification drills; bright line | Demo + reflection |
| 2 | **Briefing the Machine: Prompting** | Foundations | 5 structured prompts | Demo + hands-on |
| 3 | **Feeding the Machine: Grounding & Multimodality** | Foundations | Grounded read traced to source | Demo + hands-on |
| 4 | **Standing Orders: Making the AI Know You** | Foundations | Custom instructions + one Project/config | Settings walkthrough |
| 5 | **Know the Terrain: Filesystem & Terminal** | Operator Block | Six terminal transcripts | Guided labs |
| 6 | **The Duty Logbook: Version Control with Git** | Operator Block | Repo, 5+ commits, push | Guided labs |
| 7 | **From Advisor to Operator: Commanding an Agent** | Operator Block | One delegate-verify-own loop | Demo + transcript analysis |
| 8 | **Ammunition Discipline: Tokens, Context & Cost** | Operator Block | Heuristic + cost principles applied | Demo + hands-on |
| 9 | **Rules of Engagement: Ethics & Responsible AI Use** | Operator Block | Signed-after-verifying paragraph | Discussion + drills |
| 10 | **Field Craft: Markdown, Code, Tools & Context Files** | Operator Block | README, toolbox, `CLAUDE.md` + `me.md` | Lab + template |
| 11 | **The Proving Ground: Capstone Build** | Operator Block | GitHub repo: constrained run, loop, rewind | Mentored project |
| 12 | **Crossing the LD: Bridge to Advanced Agentics** | Operator Block | Recognition checklist | Flyover brief |
| — | **Glossary & Quick Reference** | Throughout | — | Self-service reference |

**Operator Block instructional time:** roughly 3–4 days, the terminal (M5) and capstone (M11) phases needing the most.  
**Instructor preparation:** ~4–6 hours before first cohort.

---

## Pre-Course Instructor Setup

### 1. Test Your Environment (2 hours before class)

Run these checks so you can demo confidently:

```bash
# Terminal shell works
bash --version

# Git works
git --version
cd /tmp && git init test-repo && cd test-repo && git commit --allow-empty -m "test"

# Node or Python installed (for Module 10 & 11)
node --version  # or python --version

# Claude Code installed
claude --version
claude  # starts and connects

# GitHub CLI works
gh auth status
gh repo view --web  # shows web page

# VS Code launches
code --version
code .  # opens VS Code on current folder

# Markdown preview works in VS Code (extension installed)
```

**If anything fails:** Stop and fix it. You cannot troubleshoot student problems if you haven't hit them yourself.

### 2. Verify Before Teaching — Currency Checks

This course carries explicit verify-before-teaching flags. Confirm all of the following against authoritative sources before any course run — they change between cohorts:

- [ ] **Model names, tiers, and context-window sizes** — docs.anthropic.com. Snapshots in the course (e.g., Haiku/Sonnet/Opus, ~200k tokens) drift. Teach the *shape* (fast/balanced/powerful), not the IDs.
- [ ] **Pricing structure** — anthropic.com/pricing. Teach the structure (subscription / pay-per-token / managed key; cloud vs. local), not dollar amounts.
- [ ] **MCP specifics** (Module 12) — the official Model Context Protocol documentation. Protocol details, transports, governance, and Tool/Resource/Prompt semantics are version-sensitive. This is the single highest verify-before-teaching risk in the course; do not deliver any MCP specific from memory.
- [ ] **DoD AI policy** (Module 9) — the five AI Ethical Principles, CDAO Responsible AI / generative-AI guardrails, DoDI 5400.19, and NIST AI RMF are all in active revision. Nothing in Module 9 is legal advice; verify current versions and unit policy, and route unclear real-world calls to chain of command or legal/ethics.

### 3. Prepare Demo Files (1 hour)

Create a folder `_classroom-demos/` with prepared files per module:

```
_classroom-demos/
├── M1-foundations/
│   ├── hallucination-topics.txt        # topics where YOU know the right answer
│   └── verification-drill-claim.txt    # one planted false claim for the 5 techniques
├── M2-prompting/
│   ├── before-after-example.md
│   └── five-techniques-templates.md
├── M3-grounding/
│   ├── sample-upload.pdf                # fabricated, non-sensitive
│   └── blurry-table.png                 # for the "verify the read" misread demo
├── M4-personalizing/
│   ├── example-custom-instructions.txt
│   └── example-project-setup.md
├── M5-terminal/
│   ├── demo-commands.sh
│   └── sample-files/                    # mixed .txt and other files for the archive scenario
├── M6-git/
│   ├── merge-conflict-example/
│   └── gitignore-template.txt
├── M7-commanding-agent/
│   ├── rename-folder-demo/              # the single "project → project-v1" hands-on
│   └── identify-the-models-transcripts.md   # Sections A/B/C
├── M8-tokens-cost/
│   └── tokenizer-comparison-prompt.txt
├── M9-ethics/
│   ├── analytic-paragraph-with-planted-claim.md
│   └── aggregation-exercise-datapoints.txt
├── M10-field-craft/
│   ├── example-CLAUDE.md
│   ├── example-me.md
│   └── buggy-snippets.js                # off-by-one + infinite loop
└── M11-capstone/
    ├── capstone-rubric.md
    ├── project-ideas.txt
    └── read-only-file-example/          # a file the CLAUDE.md marks read-only
```

### 4. Prepare Your Screen Setup (30 min)

- **Monitor 1:** VS Code with demo file (students see this)
- **Monitor 2:** Terminal window (or split screen)
- **Monitor 3 (optional):** Instructor notes / timer / student tracker

Single-monitor split with tmux:

```bash
tmux new-session -s teaching -x 200 -y 50
tmux split-window -h
# Left pane: VS Code demo file. Right pane: terminal with git/CLI commands.
```

### 5. Write Instructor Notes for Each Module (1 hour)

For each module prepare: the learning objective in one sentence, the key stumbling block, a 2–3 sentence verbal explanation, the exact demo commands, common Q&A, and timing markers (what to skip if running long). The [Consolidated Teaching Guide](teaching-guide.md) already surfaces the `??? note` instructor notes per module — start from there.

---

## Sample Intensive Schedule (Operator Block)

Foundations (Modules 1–4) run multi-week in short daily reps beforehand. The Operator Block is the intensive:

| Day | Theme | Modules |
|---|---|---|
| **Day 1** | Terrain & Logbook | M5 Terminal (heaviest reps), M6 Git |
| **Day 2** | The Agentic Leap | M7 Commanding an Agent, M8 Tokens/Context/Cost, M9 Ethics |
| **Day 3** | Field Craft | M10 Markdown, Programming, Tools, Context Files |
| **Day 4** | Proving Ground | M11 Capstone build + present, M12 Bridge brief |

Durations are instructional time; add breaks separately.

**For a faster cohort:** compress the Foundations reps and move quickly through any module a student already knows — but never skip a readiness check.  
**For a slower cohort:** add a terminal-mastery half-day inside M5, and allow the capstone to roll into a bonus day.

---

## Module-by-Module Teaching Tips

### Module 1: Know Your Weapon — How AI Actually Works (Foundations)

**Setup:** Open a chatbot (web or Claude Code); a markdown file for notes.

**The opener (2 min):**
"This is a pattern-prediction machine trained on text. You give it words; it predicts the next words from what it has seen. The only accurate verb is *predicts* — not knows, thinks, or lies. Today we build the mental model under the tool you've been using by feel."

**Walk students through:**

1. **Prediction demo (10 min)** — Incomplete sentence, then the same sentence + "definitely." Compare the shift.
2. **Statelessness (10 min)** — Give the model a fact, continue, ask it to repeat (it re-reads the transcript); open a new chat and ask — it has no idea. This is the "stateless engine handed a fresh transcript each turn" model. Kill the "person on the other end" picture early.
3. **Hallucination on demand (15 min)** — Ask for 5 papers with DOIs; verify one (it won't exist). Debrief: "What if you hadn't checked?" Use a topic where you know the answer; never demo on operational content.
4. **The five verification techniques (15 min)** — Cite-and-check, cross-source, re-run, second-tool, lateral reading — run all five on one planted false claim. Two AIs agreeing is *not* corroboration.
5. **When to use AI / when not (10 min)** — Four-question checklist, run *before* typing. Wrong-tool cases: precise math, live facts, authoritative citation, sensitive content.
6. **Data handling (10 min)** — The bright line. State the "paraphrase and summarize" loophole explicitly for military audiences — it does not exist. Do not soften it.

**Common confusions:**
- "Isn't it just a chatbot?" → "A very sophisticated next-word predictor you steer with prompts."
- "Will it always give the same answer?" → "No — it uses randomness by design (nondeterminism)."
- "How much context can I use?" → "A fixed token limit; verify the current number. The instinct — keep input focused — is the deliverable."

**Timing:** If long, state the context-window number rather than demoing it.

---

### Module 2: Briefing the Machine — Prompting (Foundations)

**Setup:** Open a chatbot; VS Code for saving prompts.

**The opener (2 min):**
"A vague prompt is a vague order. We brief the machine like a five-paragraph order, not a search box: role, context, example, output spec — then iterate."

**Walk students through:**

1. **Before/after (15 min)** — A one-line request, then the same with all four elements. Identify which element changed the result most.
2. **The five intermediate techniques (40 min)** — few-shot (show, don't describe), chain-of-thought (auditable reasoning, not a magic quality boost), decomposition, structured output (a "Source/NONE" column as a gap detector), system vs. user. Frame every one as clarity, not tricks.

**Scrub reminder:** Real identifiers never go in, even inside a "good" structured prompt. Use `[UNIT]`, `[LOCATION]`, `[NCO]`.

**Deliverable check:** Five structured prompts, one per technique. Review for clarity, not perfection.

---

### Module 3: Feeding the Machine — Grounding & Multimodality (Foundations)

**Setup:** A tool with web search and file upload; a fabricated non-sensitive PDF and a slightly blurry table image.

**The opener (2 min):**
"Module 1 said the engine is a brain in a jar with a knowledge cutoff. That's still true of the *engine*. Grounding feeds real source material in through a slot — web search, file upload, connectors — so the answer is traceable."

**Walk students through:**

1. **Cutoff + grounding (15 min)** — Ask about something post-cutoff; note refuse/guess/search. Upload a document; ask a question only it answers; then "which parts came from the document?"
2. **Grounded vs. generated (15 min)** — Confirm grounding fired (search step, citations, file reference); trace one claim to its source; open the source. No signal = assume generated.
3. **Multimodal misread (15 min)** — Hand the model a blurry table; ask it to read specific cells; it will get one wrong with full confidence. This makes "verify the read" stick.

**OPSEC reminder:** Uploading an image/PDF/voice clip is a disclosure decision identical to pasting text — the Module 1 rule applies to every input channel.

---

### Module 4: Standing Orders — Making the AI Know You (Foundations)

**Setup:** ChatGPT and/or Claude with settings access.

**The opener (2 min):**
"Stop re-briefing a stranger every session. Standing orders the model reads before you type a word — role, format, what to never do."

**Walk students through:**

1. **Custom instructions (15 min)** — Find the settings (verify the menu path beforehand — the UI drifts); write three instructions; compare a new chat to one without.
2. **Projects / memory / personas (20 min)** — Claude Project with instructions + a reference document; or ChatGPT memory review + one manual entry. Proactive (instructions) vs. reactive (memory) — use both.

**Security back-reference (one line, not a re-teach):** Everything in a custom instruction goes to the platform's servers on every request. No exception for settings fields. Keep instructions under 500 words.

---

### Module 5: Know the Terrain — Filesystem & Terminal (Operator Block, Day 1)

**Setup:** Each student has a terminal open; you demo on your screen. **Before the first session, have students turn on file-extension visibility.**

**The opener (2 min):**
"The terminal is the same moves you do by clicking — typed, with precision. Same files, same folders, words instead of a mouse. And it's the terrain the agent operates on, which is why an AI course teaches it."

**Address the bait-and-switch out loud** before a student raises it.

**Walk through the six exercises (they become the deliverable):**

1. **Tree walk** (clicking only) and **plaintext vs rich text** — open a `.docx` in VS Code to see what's inside. "Plaintext is honest; rich text hides things." Do not go into encodings.
2. **Orientation walk** — `pwd` → `ls` → `cd` → `pwd` → `cd ..`. Reps over coverage; `pwd` is the reset button.
3. **File manipulation sprint** — `mkdir`, `touch`/`New-Item`, `cp`, `mv`; `ls` after **every** step. No deletion yet. Build the verify-after-acting habit here and name it.
4. **Path puzzle** — absolute vs. relative; tab-completion; up-arrow. On Windows/WSL drill the `/mnt/c/...` translation — the number-one stumble.
5. **Help system** — `ls --help` / `Get-Help`; find a flag; build a reference card.
6. **Piping/redirection + real-world scenario** — `|`, `>`, `>>`; find `.txt` files and move them to an `archive`, verifying both folders; `Ctrl+C` to prove they can stop anything.

**Windows note:** Recommended environment is WSL (`wsl --install`, no admin on Windows 11); Windows files live at `/mnt/c/Users/YourName/`. Native PowerShell uses `New-Item` for `touch`; the per-tab tables in the module give equivalents.

**Common stuck points:** "Permission denied" (system files — move to a sandbox), "No such file or directory" (`pwd` + `ls`), relative-path confusion (~30% — practice 5+ times).

**Timing:** Slowest module for beginners. Do not rush.

---

### Module 6: The Duty Logbook — Version Control with Git (Operator Block, Day 1)

**Setup:** VS Code and terminal side-by-side.

**The opener (2 min):**
"Git is a duty logbook — every change recorded: what, when, why, who, with the ability to rewind. Once an agent can edit your files at speed, this is the safety net that makes it survivable. Military audiences: duty logbook. Civilian: undo button for your whole project."

**Session 1 — Local repository:**
- `git init`; `git status` between `git add` and `git commit` so students watch the state move (the three-state model is the stumble); `git log`; `git diff`.
- Branch, switch, merge, delete.
- **Force a conflict on purpose**, project it, resolve the markers slowly once, then have each student create and resolve their own. A conflict is a request for a human decision, not an emergency.

**Session 2 — `.gitignore` first, remote, and review:**
- **Create `.gitignore` BEFORE the first commit.** This is the load-bearing OPSEC step. If a credential is committed first, adding it to `.gitignore` later does NOT remove it from history. Verify a dummy `.env` does not appear in `git status` before anyone pushes.
- `gh repo create`; `git push`; confirm on GitHub.
- Optionally open a PR with `gh pr create` — the PR diff is the review gate for agent-produced changes.

**Common stuck points:** "fatal: origin already exists" (`git remote -v` / `remove`), auth fails (`gh auth status` / `gh auth login`), "I lost my commits!" (`git reset --hard` → reassure via `git reflog`, don't open it now).

**Deliverable check:** Repo on GitHub with 5+ commits, a resolved conflict, a `.gitignore` created before the first commit, and a successful push.

---

### Module 7: From Advisor to Operator — Commanding an Agent (Operator Block, Day 2)

**Setup:** A web chatbot and Claude Code in a project folder.

**The opener (2 min):**
"A chatbot gives advice; an agent takes action. The thing that makes the difference is the harness — the tool layer that gives a text-only engine eyes, hands, and a body. Engine + harness + operator. You are the operator."

**Make the connection explicit:** "Every command from Module 5 — `pwd`, `ls`, `cd`, `mkdir`, `mv` — is what the agent runs in your filesystem."

**Walk students through:**

1. **The harness appears (10 min)** — Ask the chatbot to "rename folder `project` to `project-v1`" (it describes how). Ask Claude Code the same in a folder (it calls a tool and changes the disk). This is the *single* "rename folder" hands-on — it lives here, once.
2. **Tool calls (15 min)** — Have the agent list a directory, read a file, propose an edit; before it writes, ask "what exactly will you change, and why?" Tool calls are the audit trail — reframe the Module 1 failure modes as *action* problems.
3. **Operator posture (15 min)** — Delegate, verify, own. The agent is a motivated junior with filesystem access. Name the two failure modes (blind trust, learned helplessness) and the three breakdowns (over-trust, under-involvement, automation fallacy). Note context files as the primary steering lever — full treatment in Module 10.
4. **Identify-the-models exercise (20 min)** — Read transcript Sections A/B/C; name which models are in play or violated and the fix. Use the worked intel/SITREP/grid examples as reusable templates.

**Reinforce:** The operator loop is the through-line of the whole course. Frame every later agentic action with it.

---

### Module 8: Ammunition Discipline — Tokens, Context & Cost (Operator Block, Day 2)

**Setup:** A tokenizer page; the provider's model/pricing pages; an agent session.

**The opener (2 min):**
"You already know what a token *is* from Module 1. This module is how to *spend* it. Tokens are ammunition — cost, speed, and accuracy all scale with what you spend."

**Do NOT re-define the token.** Assert the prior knowledge and move to spending.

**Walk students through:**

1. **Feel the weight (10 min)** — Tokenizer: token vs. word count; rewrite as a structured prompt and re-count. Longer "in the right way" beats short and vague.
2. **Model-selection heuristic (15 min)** — fast / reasoning / big-context. Match the model to the task; "always use the biggest model" is the wrong default. Teach the shape (fast/balanced/powerful); bookmark the docs because names drift.
3. **Context, operationally (15 min)** — The window fills *silently* as tool results accumulate. Smart sampling beats cramming — have the agent `find`/`grep` the relevant files rather than reading the whole codebase. Start fresh proactively at the first sign of drift.
4. **Cost discipline (10 min)** — Four principles; iteration is where cost hides; use tools instead of pasting large material.
5. **Delivery & payment (10 min)** — subscription app / pay-per-token API / managed key; cloud vs. local. Cloud sends data off-machine — which is exactly why the Module 1 data-handling rule exists. Skip the pricing tables; teach the structure.

---

### Module 9: Rules of Engagement — Ethics & Responsible AI Use (Operator Block, Day 2)

**Setup:** A chatbot; a non-sensitive analytic paragraph with a planted false claim.

**The opener (2 min):**
"Module 1 was data handling — what flows *in*. This is the opposite direction: what you do with what comes *out*, and whether the use is right, lawful, and accountable. You can be perfectly OPSEC-compliant and still commit an ethical failure by signing for a fabricated claim."

**Verify currency before delivery — this is not legal advice.** The five Principles, CDAO RAI guidance, DoDI 5400.19, and NIST AI RMF are in active revision. When a real call is unclear, route to chain of command or legal/ethics.

**Walk students through the eight sections (drills, not lecture):**

1. **Accountability & authorship** — Have students physically *initial* an AI-drafted paragraph only after verifying every claim. The hesitation when they catch themselves is the lesson landing. "The model said so" is an admission, not a defense.
2. **Hallucination as ethical failure** — Same fabrication, low vs. high stakes. Verification duty scales with consequence, not your schedule.
3. **Over-reliance & automation bias** — Judge first, consult second. Enforce the ordering: own assessment written and visible *before* the model's. If they peek, the exercise is worthless.
4. **Bias & fairness** — Module 1 owned *spotting* (literacy); this owns the *duty* not to launder it. Strip claims supported only by assumption.
5. **Disclosure & attribution** — Materiality test; default to traceability; DoDI 5400.19 governs public-facing content (labeling + human oversight). Disclosure is a quality practice, not a confession.
6. **Dual-use & misuse** — Capability ≠ authorization. Awareness and the lawful-use boundary, never a how-to. Reflex: stop and route near-the-line tasks up the chain.
7. **Privacy beyond OPSEC** — Protecting *others'* data; aggregation is the AI-amplified risk. "Technically collectible" ≠ "lawfully/ethically appropriate." Spend time on aggregation — most students have never considered it.
8. **DoD AI Ethical Principles & lawful-use close** — Walk the principles-to-habits map row by row: **Responsible, Equitable, Traceable, Reliable, Governable.** "Ask the chain/legal" is a strength, not an admission.

---

### Module 10: Field Craft — Markdown, Code, Tools & Context Files (Operator Block, Day 3)

**Setup:** VS Code with Markdown preview; a runtime (Node or Python); the toolbox.

**The opener (2 min):**
"Four pieces of field craft so the work holds up: clean Markdown, enough code-literacy to read what the agent writes, a verified toolbox, and context files that steer an agent before you type."

**Walk students through:**

1. **Markdown (20 min)** — Show raw vs. preview. The four critical spacing rules cause most errors: space after `#`, blank line before lists, blank line before fenced code blocks, table header + separator row. Write in VS Code, never Word (smart quotes break code). Don't linger — get them writing a README in the first ten minutes.

   *Example of the syntax to demo (toggle preview as you add each element):*

   ```markdown
   # Heading 1
   ## Heading 2

   This is **bold** and *italic*.

   - Bullet 1
   - Bullet 2

   `inline code`, and a fenced block:

   ```bash
   echo "Hello"
   ```

   [Link text](https://example.com)

   | Header 1 | Header 2 |
   |----------|----------|
   | Cell 1   | Cell 2   |
   ```

   *(Note: keep image embeds out of demo files unless you actually ship the image — a broken `![alt](missing.png)` reference renders as a broken-image icon and distracts the room. Demo links and tables instead.)*

2. **Programming concepts (25 min)** — Reading literacy, not authorship. Variables, conditionals, loops, functions; pseudocode first. Off-by-one and infinite-loop errors are the highest-value bug classes — they recur constantly in agent output. Have students narrate an AI-written function back into plain English; any block they can't narrate is a verification gap. Do not let it become a bootcamp.
3. **Developer tools (20 min)** — Run every `--version` check in one pass. "Command not found" right after install → restart the terminal (Windows does not refresh PATH). Confirm `gh --version` before `gh auth login`. `.env` goes in `.gitignore` *before* the first commit — same OPSEC rule as Module 6.
4. **Context files (25 min)** — `CLAUDE.md` = what to build (and what never to touch); `me.md` = how you work. The predictable failure is a warm description that constrains nothing. Drive the fix: "What should Claude NOT modify? What is out of scope?" Push for at least one real prohibition and one read-only file. Context files ship to the provider — the Module 1 and Module 8 disciplines apply.

**Deliverable check:** A README with 5+ syntax elements, a verified toolbox checklist, and a `CLAUDE.md` + `me.md` with at least one genuine, enforceable prohibition.

---

### Module 11: The Proving Ground — Capstone Build (Operator Block, Day 4)

**The opener (2 min):**
"You're going to build and ship a real project — but the grade is on *how you commanded the build*, not just whether it runs. A constrained `CLAUDE.md`, one documented delegate-verify-own loop, and a recovered bad agent edit are 60 of the 100 points."

**The five phases:**

1. **The Mission** — Pick a path (CLI tool / web app / API integration). One-paragraph plan + 3–5 features. Apply the two-minute test. Commit the plan.
2. **Standing orders** — `.claude/` with a `CLAUDE.md` that has a scope boundary, ≥2 enforceable prohibitions, a named read-only file, done criteria, and a conflict rule. Add the actual read-only file the prohibition protects. (NET-NEW capstone requirement: the build is now an agentic deliverable.)
3. **The loop** — Delegate a bounded task; verify by reading/narrating the code, running it, and **checking the diff against the agent's claim**; own it with a commit message naming what was verified. Repeat for at least one more feature. (Highest-weighted rubric item.)
4. **The rewind** — Confirm a verified known-good commit; deliberately induce a bad edit; confirm the damage; roll back to known-good; re-issue with a tighter instruction. (NET-NEW, graded — make them *cause* the failure, not hypothesize it.)
5. **Ship it** — README; final scrub for names/credentials/`.env` in history; push; one-line accountable sign-off.

**Coaching, not answers:** "What does the error message say?" · "Can you draw what this should do?" · "What would you do if I wasn't here?"

**Rubric:**

| Criterion | Points | Evidence |
|---|---|---|
| Delegate-verify-own loop | 30 | A documented loop; diff checked against the agent's claim |
| CLAUDE.md actually constrained the run | 15 | Testable prohibition + scope boundary that demonstrably steered the agent |
| Git rewind of a bad agent edit | 15 | Deliberate bad edit recovered to known-good; clean tree shown |
| Data-handling & ethics discipline | 15 | No real names/units/credentials; no `.env` in history; accountable sign-off |
| Working artifact | 15 | Runs and does what it promised, basic error handling |
| Documentation & commits | 10 | Clear README; 5+ meaningful commits; pushed |

**Passing:** 70+. **Honors:** 90+ with a clean loop and a recovered rewind. If a student protests that their app runs perfectly but scored mid-range — the weighting is deliberate. Working code is table stakes; supervision is the certification. Hold the line.

---

### Module 12: Crossing the LD — Bridge to Advanced Agentics (Operator Block, Day 4)

**The opener (2 min):**
"This is a recognition module. Advanced agentics is the same engine-harness-operator primitive and delegate-verify-own loop — composed and scaled. You leave able to *name* the terrain, not build it."

**Hold the altitude — this is a flyover, not instruction.** Walk the seven segments quickly:

0. Recap the primitive. 1. Grounding/Retrieval = RAG (the by-hand grounding from M7, named). 2. Tools & MCP — harness is extensible; Tool / Resource / Prompt. 3. Permissions & guardrails — scopes, allowlists, approval gates, sandboxes. 4. Planning — plan-then-act as a supervision checkpoint. 5. Workflow patterns — prompt chaining, routing, orchestrator-workers, evaluator-optimizer. 6. Sub-agents — one commander, many workers; supervision expands, not vanishes. 7. Evaluating an agent — spot-checks, regression, evaluator-optimizer.

**The MCP trap:** Highest verify-before-teaching risk in the course. Teach the *shape*; tell students every concrete MCP detail must be checked against current docs. Do not let a confident specific become a taught fact.

Each segment carries a **Deferred to the main course** marker — that boundary is the point.

---

## Troubleshooting Quick Reference

### Student Can't Authenticate
```bash
gh auth status
gh auth login          # choose HTTPS (easier for beginners)
claude --version
# If Claude Code not working, reinstall per your platform's instructions
```

### "Command Not Found"
```bash
which <command>        # or: where <command> on native Windows
echo $PATH
# If the tool was just installed, restart the terminal (Windows does not refresh PATH)
```

### Terminal Path Confusion
```bash
pwd       # where am I
ls        # what is here
cd /path/to/folder
cd ..     # up one level
cd ~      # home
```

### Git Merge Conflicts
```bash
git status
# edit the conflicted file, resolve the <<<<<<< ======= >>>>>>> markers
git add <file>
git commit -m "Resolve conflict in <file>"
```

### Git Push Fails
```bash
git remote -v
git remote add origin <URL>        # if missing
git remote remove origin           # if wrong, then re-add
git push -u origin main
```

### Committed a Secret
A credential in history is compromised the moment it lands. Adding it to `.gitignore` afterward does **not** remove it. Rotate the credential and clean it from history — do not just delete the file. Prevention: `.gitignore` before the first commit.

### VS Code Markdown Preview Not Working
Install "Markdown All in One," restart VS Code, open a `.md` file, press `Ctrl+Shift+V` (or `Cmd+Shift+V` on Mac).

---

## Assessment and Grading

| Module | Artifact | Pass criteria |
|--------|----------|---------------|
| M1 | Verification reflex + bright line | Produced a hallucination, ran the 5 techniques, wrote a personal bright line |
| M2 | 5 structured prompts | 4/5 clear, specific, one per technique |
| M3 | Grounded read | Confirmed grounding fired, traced one claim to source |
| M4 | Custom instructions + Project | Both set up, no sensitive content |
| M5 | Six terminal transcripts | Navigation + file ops correct, `ls`-verified |
| M6 | Repo + push | 5+ commits with messages, resolved conflict, `.gitignore` before first commit, push succeeds |
| M7 | Delegate-verify-own loop | One full loop run; can name models in a transcript |
| M8 | Heuristic + cost application | Tier selection and four cost principles applied to real tasks |
| M9 | Signed paragraph | Signed only after verifying every claim; five principles named |
| M10 | README + toolbox + context files | 5+ syntax elements; all `--version` pass; `CLAUDE.md` with a real prohibition |
| M11 | GitHub repo | Constrained run, documented loop, recovered rewind, no secrets, sign-off |
| M12 | Recognition checklist | Names each pattern and what is deferred |

**Course completion:** all modules' readiness checks met and the capstone at 70+. **Honors:** capstone 90+ with a clean loop and a recovered rewind.

---

## Common Instructor Questions

**Q: Can I skip a module?**
No. This is a single ascending track. Module 11 (Capstone) specifically requires Modules 6, 7, 9, and 10. The agentic modules (7+) assume every prior concept. A student who already prompts well or knows the terminal moves quickly to confirm the foundation — but does not skip the readiness check.

**Q: Where did Mental Models and day0 go?**
Archived. Their guidance is folded in: harness/operator/tool-calls into Module 7, tokens/context/cost into Module 8, and failure modes/tokens-intro into Module 1. Do not teach them as separate units.

**Q: A student is way ahead.**
Capstone stretch goals (deploy, add tests, a second feature), or pair them as a peer mentor.

**Q: A student is falling behind.**
Assess where they got lost (usually terminal or git). Pair them with you during a lab for a 30-minute catch-up; do not slow the group.

**Q: Can I teach this online?**
Yes, with adjustments: breakout rooms for pair work, recorded demos, screen-sharing for troubleshooting, and 1-on-1 office hours for tool setup (auth, PATH).

**Q: What's the hardest part for students?**
Tie: terminal path concepts (Module 5) and reading code/constraining a `CLAUDE.md` (Module 10). Give those extra time. The two highest-consequence stumbles to prevent are pasting sensitive data into an unauthorized tool (Module 1) and committing a credential before creating `.gitignore` (Modules 6 and 10).

---

## Instructor Success Checklist

Before teaching your first cohort, verify:

- [ ] You've completed all 12 modules yourself, in order
- [ ] You've hit the main environment bugs and fixed them
- [ ] You've run the verify-before-teaching currency checks (models, pricing, MCP, DoD policy)
- [ ] Demo files are ready in `_classroom-demos/`
- [ ] You have working examples of every exercise (and a planted false claim for M1/M9)
- [ ] You've set up your screen layout (code editor + terminal visible)
- [ ] You have a visible timer
- [ ] You know your "unstuck" phrases: "What does the error say?", "What did you expect?", "Try it yourself first."
- [ ] You have a system for parking student questions

---

**End of Course Instructor Guide**

You're ready to teach. One spine, each concept once, every module gated by a readiness check. Help students stay stuck just long enough to solve it themselves — that's where learning lives.
