# AI and Agentics Basics — Consolidated Teaching Guide

**For:** Instructors delivering the full course start to finish  
**Use:** Run alongside student-facing content. This doc tells you what to do, say, watch for, and hand off — not what to read aloud.

---

## How to Use This Guide

- One section per module, in the new linear spine order (Modules 1–12), plus the glossary.
- The course is a single ascending track. Each module assumes the one before it; concepts are taught once in their canonical home. Do not re-teach a concept another module owns — reference it in a line and move on.
- Durations are instructional time, not clock time (add breaks separately).
- Instructor notes pulled from the `??? note "Instructor Note…"` blocks in student content are surfaced here — students do not see them.
- Hands-on activities are listed with brief instructor direction; full student instructions live in the course pages.
- Every section ends with a transition note to the next module.

### The Two-Phase Delivery Model

The course runs in two phases (see `docs/overview.md` for the authoritative map):

- **Phase 1 — Foundations (Modules 1–4): multi-week, short daily reps.** Built for someone who uses AI by feel. Delivered in short daily sessions over multiple weeks so the mental model sets before tools enter.
- **Phase 2 — Operator Block (Modules 5–12): 3–4 day intensive.** Hands-on. Each module has a deliverable.

**Sample intensive schedule (Operator Block):**

| Day | Modules |
|---|---|
| **Day 1 — Terrain & Logbook** | M5 Terminal, M6 Git |
| **Day 2 — The Agentic Leap** | M7 Commanding an Agent, M8 Tokens/Context/Cost, M9 Ethics |
| **Day 3 — Field Craft** | M10 Markdown, Programming, Tools, Context Files |
| **Day 4 — Proving Ground** | M11 Capstone build + present, M12 Bridge brief |

### Dependency Chain (do not skip)

- **Modules 1–4** are the conceptual foundation. Everything after assumes them.
- **Module 5 (Terminal)** must precede **Module 7 (Commanding an Agent)** — you cannot supervise an agent navigating ground you do not know.
- **Module 6 (Git)** must precede **Module 7** and **Module 11** — the supervisor mindset assumes you can rewind an agent's edits.
- **Module 9 (Ethics)** lands after **Module 7** on purpose: accountability lands viscerally only after a student has felt an agent take real action. The Module 1 data-handling bright line still appears in Module 1 as a hard safety rule that cannot wait.
- **Module 11 (Capstone)** requires Modules 6, 7, 9, and 10.
- **The one deliberate spiral:** the "verify after acting" reflex is introduced in Module 5, reinforced in Module 7, and graded in Module 11. Let it spiral; do not let any other concept re-teach.

---

## Pre-Course Prep Checklist

Before any session:

- [ ] **Verify current model names, tiers, and context-window sizes** at docs.anthropic.com — these change with every release. Every model name/number in the course carries a verify-before-teaching flag.
- [ ] **Verify current pricing structure** at anthropic.com/pricing — teach the structure (subscription / pay-per-token / managed key; cloud vs. local; fast / balanced / powerful tiers), not specific dollar amounts. Prices change within a quarter.
- [ ] **Verify MCP specifics** (Tool/Resource/Prompt semantics, transport, governance, server availability) at the official MCP documentation before delivering Module 12 — this is the highest verify-before-teaching risk in the course.
- [ ] **Verify currency of DoD AI policy** for Module 9 — the five AI Ethical Principles, CDAO Responsible AI / generative-AI guardrails, DoDI 5400.19, and NIST AI RMF are all in active revision. Nothing in Module 9 is legal advice; when a real situation is unclear, students route to chain of command or legal.
- [ ] Run all version checks on your machine (`claude --version`, `git --version`, `gh --version`, `node --version`, `code --version`).
- [ ] Create a `_classroom-demos/` folder with prepared files for each module (see prereq-guide.md for folder structure).
- [ ] Screen setup: code editor and terminal visible simultaneously.
- [ ] Have a timer students can see.

**Total instructor prep time before first cohort:** ~4–6 hours.

---

# PHASE 1 — FOUNDATIONS (Modules 1–4)

Multi-week, short daily reps. The mental model must set before tools enter.

---

## Module 1 — Know Your Weapon: How AI Actually Works

**Estimated duration:** Multi-week, short daily reps (15–30 min/day across the foundations phase)  
**Audience:** Anyone who has used an AI chatbot by feel and is about to use one for real work.

### Learning Objectives

- State in one sentence what an LLM does (predicts text from learned patterns)
- Explain "trained not programmed" in plain terms
- Explain conversation mechanics and statelessness — the model re-reads the whole transcript each turn, with no cross-chat memory by default
- Name the five failure modes (hallucination, confident-wrong, nondeterminism, knowledge cutoff, bias) and produce a hallucination by hand
- Verify AI output with five repeatable techniques
- Run the four-question "when to use AI / when not" checklist before reaching for the tool
- State the data-handling bright line: what never goes into an unauthorized system

### Instructor Notes (from this module's `??? note` blocks)

- **Architecture questions:** Do not open with attention heads, transformers, or parameter counts. The mental model that survives contact with a real tool is the deliverable. If asked, acknowledge and defer.
- **Anthropomorphism runs deep:** Students told "it just predicts" will say "it knew the answer" thirty seconds later. Interrupt it every time in the first two weeks — it re-trains faster than you expect. The only accurate verb is *predicts*.
- **Context window sizes:** Approximate, version-sensitive — verify before teaching. Drill the instinct ("keep input focused"), not the numbers.
- **Kill the "person on the other end" model early:** Replace the chat-app mental model with the right one — a stateless engine handed a fresh transcript each turn. Once it clicks, statelessness, context limits, and "why won't it remember my other chat" become the same one fact.
- **Eliciting hallucinations on demand:** Use invented citations (ask for 5 papers with DOIs), biographical detail on a real-but-not-famous person, or recent events past cutoff. Pick a topic where you know the answer. Never demo on live operational content.
- **Don't let it tip into cynicism:** The goal is calibrated trust, not distrust. Extraordinarily capable *and* hallucinates are simultaneously true. Same for bias-spotting — name the skew, don't conclude the tool is useless.
- **Make them run the verification drills:** Verification only sticks as muscle memory. Have students run all five techniques on one planted false claim in one session.
- **When-to-use is a pre-decision, not a post-mortem:** Drill the four-question checklist as something run *before* typing.
- **Data handling — audience calibration:** For military/intel audiences state it explicitly, including the "paraphrase and summarize" loophole — which does not exist. For civilian audiences use concrete examples (medical, financial, HR, client data).
- **Do not soften the data-handling module:** Soften it and students hear "be careful sometimes." It is a hard rule.

### Hands-On Direction

1. **Prediction demo** — Type an incomplete sentence; submit. Add "definitely"; submit again. Compare. Then ask a factual question and ask how they'd verify it without the model.
2. **Context window probe** — Paste dense text into a fresh chat; ask about the top, then the bottom; repeat in a new chat. Compare quality. (Models attend better to the beginning and end than the middle.)
3. **Statelessness drill** — Give the model a fact ("callsign Raptor-6"), continue, ask it to repeat. Open a new chat and ask for the fact — it has no idea. Edit an early message and watch later turns regenerate.
4. **Hallucination on demand** — Ask for 5 peer-reviewed papers with citations and DOIs; try to verify one. Debrief: "What would you have done if you hadn't checked?"
5. **Verification drills** — Run all five techniques (cite-and-check, cross-source, re-run for consistency, second-tool, lateral reading) against one planted false claim.
6. **When-to-use checklist** — Run the last five AI uses through the four questions; flag wrong-tool cases (precise math, live facts, authoritative citation, sensitive content).
7. **Personal bright line** — Review the last three things pasted into an AI tool; identify one category that never goes into an unauthorized tool. Write it down.

### Common Stumbles

- Reverting to "it knew / it thinks / it lied." Re-anchor on *predicts* every time.
- Treating two AIs agreeing as corroboration — it is not; they read overlapping training data.
- Hearing the data-handling rule as a soft suggestion. It is a bright line that does not expire under deadline pressure.

### Deliverable

No formal artifact, but the readiness gate is real: a produced hallucination, all five verification techniques run once, the four-question checklist applied to real uses, and a written personal bright line.

### Transition to Module 2

Students have a working model of the engine, know how a conversation actually works, and know where it breaks. Module 2 converts that into deliberate prompting — briefing the machine like a mission order instead of typing into a search box.

---

## Module 2 — Briefing the Machine: Prompting as a Mission Order

**Estimated duration:** 1–2 sessions (foundations phase)

### Learning Objectives

- Name the four elements of a deliberate prompt (role, context, example, output spec)
- Treat prompting as iteration, not a one-shot command
- Apply five intermediate techniques — few-shot, chain-of-thought, decomposition, structured output, system-vs-user prompt — as clarity, not tricks
- Scrub real identifiers out of every prompt
- Produce five structured prompts (one per intermediate technique) as the deliverable

### Instructor Notes (from this module's `??? note` blocks)

- **Prompt-engineering creep:** Resist turning this into a "prompt tricks" hour. Magic phrases are not the lesson — clarity is. The intermediate techniques are extensions of clarity; frame them that way every time.
- **Keep chain-of-thought tied to verification:** Students treat it as a magic quality boost. Anchor it to supervision — the reason an operator asks for visible reasoning is to *check* it. That framing carries straight into the Module 7 supervisor mindset.
- **Structured output as a gap detector:** The strongest selling point is not tidiness — a named-field schema forces missing information into the open (an empty "Source" cell, a "NONE"). Demo it explicitly; it connects prompting to the Module 1 verification reflex.

### Hands-On Direction

1. **Before/after prompting** — One-line request vs. the same request with role, context, example, and output spec. Compare. Identify which element changed the result most.
2. **Few-shot** — A small classification/formatting task with three worked examples and a fourth unsolved item.
3. **Chain-of-thought** — A multi-step problem with reasoning shown before the answer; ask whether they could catch an error in the steps.
4. **Decomposition** — Break one big ask into an ordered sequence of smaller prompts.
5. **Structured output** — Ask for JSON or a Markdown table with a required "Source"/"NONE" column; see what gaps the schema exposes.
6. **System vs. user** — Set a standing instruction first, then send several task prompts; watch the standing order persist.

### Common Stumbles

- Chasing magic phrases instead of clarity — students who do hit a ceiling fast.
- Forgetting to scrub. Reinforce: real names, units, locations, grids, op-tied dates, and credentials never go in, even inside a "good" structured prompt. Use `[UNIT]`, `[LOCATION]`, `[NCO]`.

### Deliverable

**Five structured prompts, one per intermediate technique.** Review for clarity and specificity, not perfection.

### Transition to Module 3

Students can brief the machine clearly. Module 3 addresses the engine's blind spot from Module 1 — no live data, a knowledge cutoff — by showing how grounding feeds it real source material, and how multimodality opens new (failure-prone) input channels.

---

## Module 3 — Feeding the Machine: Grounding & Multimodality

**Estimated duration:** 1–2 sessions (foundations phase)

### Learning Objectives

- Explain grounding as feeding real source material into the model at request time
- Name three grounding paths: web search, file upload, connectors
- Tell grounded output from generated output — confirm grounding fired, trace claims to sources
- Name the input modes (images/screenshots, PDFs, charts/tables, voice) and the characteristic failure mode of each
- Apply the Module 1 data-handling rule to images, PDFs, and voice — not just typed text

### Instructor Notes (from this module's `??? note` blocks)

- **Correct, don't contradict Module 1:** Do not let students conclude Module 1 was wrong. The engine is still a brain in a jar — stateless, cutoff-bound, no native live access. Grounding is an external tool layer feeding the jar. Frame as "extend the model," not "replace it." This sets up the harness in Module 7: grounding is a tool call.
- **This is the Module 1 reflex, applied:** Students may think grounding lets them stop verifying. It does the opposite — it gives them something checkable to verify against. Tie explicitly back to the five Module 1 verification techniques. Grounding makes the drills *possible*, not optional.
- **Demo a misread live:** Hand the model a slightly blurry table or chart and ask it to read specific cells/values. It will usually get at least one wrong with full confidence. Doing this once makes "verify the read" stick. Use a fabricated, non-sensitive image.
- **Verify before teaching — tool/feature specifics:** Which tools have web search, how upload works, what connectors exist all change frequently. Treat every feature claim as a snapshot; confirm the tool in front of you.

### Hands-On Direction

1. **Cutoff probe** — Ask about something after the training cutoff; note whether it refuses, guesses, or searches. Re-ask with search required; compare.
2. **Grounded read** — Upload a short document; ask a question only answerable from it. Then ask "which parts came from the document vs. your own knowledge?"
3. **Confirm-grounding-fired** — Look for the signal (search step, citations, file reference); pick one claim and ask for its source; open the source and confirm it supports the claim.
4. **Multimodal misread** — Screenshot a fabricated table; ask the model to read specific cells; check every value. Repeat with a chart, and with voice if supported.

### Common Stumbles

- Assuming capability means use — a tool *with* search may answer straight from training. No visible signal = assume generated until checked.
- The mixed answer (part grounded, part generated) — the dangerous case, because the seam is invisible under a uniform tone.
- Forgetting OPSEC crosses modes — uploading an image/PDF/voice clip is a disclosure decision identical to pasting text.

### Deliverable

No formal artifact; readiness gate is a grounded read traced to source and a "verify the read" check on a multimodal input.

### Transition to Module 4

Students can hand the model real information. Module 4 makes the *setup* persistent — standing orders the model reads before every session so they stop re-briefing a stranger every chat.

---

## Module 4 — Standing Orders: Making the AI Know You

**Estimated duration:** 1–2 sessions (30–60 min total)

### Learning Objectives

- Find custom-instruction / project settings in their tool of choice (ChatGPT or Claude)
- Write at least three instructions: who they are, how they want responses, what to never do
- Observe a before/after difference
- Set up at least one Project or named configuration for recurring work
- Confirm no sensitive or controlled information is in their instructions

### Instructor Notes (from this module's `??? note` blocks)

- **Platform drift:** Custom-instruction interfaces change frequently. Verify the menu path before teaching — the concept is stable, the UI is not.
- **Security back-reference, not a re-teach:** Do not re-teach data handling. Point back to the Module 1 bright line — everything in a custom instruction goes to the platform's servers on every request. One line, then keep going. It does not have an exception for settings fields.
- **Memory feature availability:** Varies by subscription tier and region and changes over time. Verify availability before teaching.

### Hands-On Direction

1. **Custom-instructions setup** — Find the settings; write three instructions (who you are, how you like responses, one thing to never do). Compare a new chat to one without instructions.
2. **Project / memory setup** — Claude: create a Project for a recurring task with instructions and at least one reference document. ChatGPT: review and prune memory, add one manual entry.

### Common Stumbles

- Writing a 1,000-word template copied from the internet that the model ignores after three turns. Start with one thing it gets wrong every time; keep instructions under 500 words.
- Confusing proactive (custom instructions, deliberately set) with reactive (ChatGPT memory, recorded). Use both.

### Deliverable

Custom instructions written and at least one Project/named configuration set up, with no sensitive content.

### Transition to Module 5

The AI side is now calibrated. Phase 2 is entirely different: no AI, plain computer literacy. Frame it early — the terminal is not a detour, it is the terrain the agent will move across.

---

# PHASE 2 — OPERATOR BLOCK (Modules 5–12)

3–4 day intensive. Hands-on. Each module has a deliverable.

---

## Module 5 — Know the Terrain: Filesystem & Terminal

**Estimated duration:** Heaviest hands-on weight of the operator block (plan most of Day 1; absolute beginners need the most reps here)  
**Critical setup step:** Before the first session, have students turn on file-extension visibility (Windows: File Explorer → View → Show → File name extensions). Do not skip — it prevents confusion downstream.

### Learning Objectives

- Read a path as a route through the folder tree; navigate without search
- Distinguish plaintext from rich text and give an example of each
- Install VS Code, open a folder, toggle Markdown preview
- Navigate with `pwd`, `ls`, `cd`, `cd ..`
- Create, copy, and move files (`mkdir`, `touch`/`New-Item`, `cp`, `mv`) — no deletion yet
- Write absolute and relative paths; use tab-completion and the up-arrow
- Add flags, use `--help`/`man`, pipe and redirect, stop a command with `Ctrl+C`
- **Verify after every action — the through-line habit introduced here**

### Instructor Notes (from this module's `??? note` blocks)

- **Extension visibility:** Turning extensions on prevents confusion in the plaintext-vs-rich-text section where `.txt` vs `.docx` is the whole lesson. Do not skip.
- **Encodings:** Do not go into UTF-8/ASCII. "Plaintext is honest, rich text hides things" is the entire lesson.
- **Install problems:** A broken VS Code install on one machine should not stall the room. Keep Notepad++ as a backup viewer and move on.
- **Environment choice (WSL vs PowerShell):** Hands-on transcripts assume a Linux/Unix shell. On Windows the recommended environment is WSL (`wsl --install`, no admin on Windows 11); Windows files appear at `/mnt/c/Users/YourName/`. Native PowerShell uses different commands (`New-Item` for `touch`); the per-tab tables give equivalents.
- **Address the bait-and-switch out loud:** Name the frustration before a student does — "Some of you wonder why an AI course spent time on the command line." Then make the connection: the agent acts through the terminal; the student who does not understand it cannot supervise it.
- **Reps over coverage:** Same three navigation commands, many short reps across several days. Do not introduce file creation until navigation is solid.
- **The verify habit is the through-line:** "Trust the action, not the narration" runs through all agentic work. Build it here deliberately and name it. Introduced here, reinforced in Module 7, graded in Module 11 — do not let it stay implicit.
- **Exactness as frustration:** A student annoyed that a capital letter breaks a path is learning the right thing. Name it: "Yes, the space matters — that's why tab-completion exists." On Windows/WSL, drill the `/mnt/c/...` translation here — the number-one path stumble.

### Hands-On Direction (six exercises = the Module 5 deliverable)

1. **Tree walk** (clicking, no search) — read a path in the address bar; create a `practice` folder; drag a file in.
2. **Plaintext vs rich text** — type and save `.txt` in Notepad, open in VS Code; open a `.docx` in VS Code to see what's inside.
3. **Orientation walk** — `pwd` → `ls` → `cd` → `pwd` → `cd ..` cycle until routine.
4. **File manipulation sprint** — build `projects/acc-prep/module-5/`; create, copy, rename; `ls` after every step.
5. **Path puzzle** — write absolute and two relative paths to the same file; redo with tab-completion; recall with the up-arrow.
6. **Help / piping / real-world scenario** — find a flag with `--help`; pipe and redirect; find `.txt` files and move them to an `archive`, verifying both folders; press `Ctrl+C` on a long-running command.

### Common Stumbles

- "Permission denied" → wandered into system files; move to a safe sandbox.
- "No such file or directory" → wrong folder/path; `pwd` and `ls` to verify.
- Relative-path confusion (~30% stall here) → practice 5+ times with different folders.
- Typos creating new files silently → `ls` after every action.

### Deliverable

**Six terminal transcripts** (one per exercise) showing the work and its verification.

### Transition to Module 6

Students can navigate and act in the filesystem. Module 6 adds the logbook: once an agent can change files at speed, you want a recoverable record of every change. That is version control.

---

## Module 6 — The Duty Logbook: Version Control with Git

**Estimated duration:** Plan roughly half of Day 1 (split: local repo, then remote + conflicts)

### Learning Objectives

- Explain version control as a duty logbook of file changes they can rewind, and why it matters once an agent can write to files
- Distinguish the local logbook from the remote copy
- Init a repo; stage, commit, read `git log` / `git diff`; write present-tense, action-focused commit messages
- Create, switch, and merge branches; resolve a merge conflict by hand
- Create a `.gitignore` **before the first commit**; push to GitHub; open and read a PR diff

### Instructor Notes (from this module's `??? note` blocks)

- **Audience framing:** Military audiences — the duty-logbook framing lands immediately. Civilian audiences — "undo button for your whole project." The concept was loaded at the end of Module 5; this module turns it into commands.
- **The three-state model is the stumble:** Students mix up `add` and `commit`. Run `git status` between every step so they watch a change move from working directory → staged → committed. Make the state visible.
- **Walk one conflict live:** Students panic at conflict markers. Create the conflict on purpose, project it, resolve it once slowly, then have each student create and resolve their own.
- **The two OPSEC stumbles that matter most:** The `.gitignore`-timing mistake is one of the two highest-consequence stumbles in the course (the other is pasting sensitive data into an unauthorized tool, Module 1). Run the `.gitignore` step before students make any commit they intend to push; verify ignored files do not appear in `git status` before anyone runs `git push`.

### Hands-On Direction (build one repo with 5+ commits = the deliverable)

1. **First repository** — `git init`; create a file; `git status` between `add` and `commit`; `git log`; edit, commit again, read `git diff`.
2. **Branching + a real conflict** — branch, change, merge, delete; then force a conflict on the same line of one file and resolve the markers by hand.
3. **.gitignore first, then push** — create `.gitignore` with `.env`/credential patterns **before any commit**; confirm a dummy `.env` does not appear in `git status`; make the real first commit; `gh repo create`; `git push`; optionally open a PR with `gh pr create` and review the diff.

### Common Stumbles

- "fatal: origin already exists" → `git remote -v`, then `git remote remove origin`.
- Authentication fails → `gh auth status`, then `gh auth login` (HTTPS).
- "I lost my commits!" → they ran `git reset --hard`; reassure (`git reflog`), but do not open that topic now.
- Committing a secret first, then adding it to `.gitignore` — does not remove it from history. Sequence matters; too late is the same as never.

### Deliverable

**A GitHub repo with 5+ commits, a resolved conflict, a `.gitignore` created before the first commit, and a successful push.**

### Transition to Module 7

With the terrain mapped (Module 5) and the logbook running (Module 6), students are ready to hand the agent the keys — moving from advising a model to commanding one that acts.

---

## Module 7 — From Advisor to Operator: Commanding an Agent

**Estimated duration:** Plan a substantial block of Day 2 (this is the agentic-leap module; the worked examples and the identify-the-models capstone exercise carry it)

### Learning Objectives

- State the one-line difference between a chatbot and an agent
- Explain read/write/execute access in practice
- Name the three parts of the engine-harness-operator stack
- Explain tool calls and why they enable verification and an audit trail
- State the three duties of the operator: delegate, verify, own; name the three ways supervision breaks down
- Know that context files are the primary lever for steering an agent (full treatment in Module 10)

### Instructor Notes (from this module's `??? note` blocks)

- **Make the connection explicit:** Say it out loud — "Every command you learned in Module 5 — `pwd`, `ls`, `cd`, `mkdir`, `mv` — that is what the agent runs when it works in your filesystem. You learned the terrain so you can supervise someone navigating it." Make the payoff land.
- **Vocabulary will drift:** External resources say "model + tools + orchestration layer." Same concepts, different words. Teach engine-harness-operator as the course's shared language and tell students to expect synonyms.
- **Connect to the Module 1 failure modes:** Reframe hallucination, confident-wrong, and nondeterminism as *action* problems now — an agent can hallucinate a file path, confidently run the wrong command, produce a different plan on a second run. Tool calls are how the operator catches all three.
- **Reinforce throughout, not just here:** The operator loop is the through-line of the entire course. Frame every later agentic action with it. The "verify after acting" reflex is the one habit allowed to spiral — introduced in Module 5, reinforced here, graded in Module 11.

### Hands-On Direction

1. **Harness appears** — Ask a web chatbot to "rename folder `project` to `project-v1`"; note it describes how. Ask Claude Code the same in a project folder; watch it call a tool and change the disk. Write one sentence on the difference. (This is the single "rename folder" hands-on — it lives here, once.)
2. **Trace the tool-call loop** — In Claude Code: "what's in my current directory?"; "read [specific file]"; ask for a small edit and, before it writes, "what exactly will you change, and why?" Verify before approving.
3. **Run the full loop once** — Give a small real task with a clear brief (who you are, what good looks like, what's off-limits). Verify the actual output vs. the brief. Label which failure mode the first brief most resembled (over-trust, under-involvement, automation fallacy).
4. **Identify-the-models exercise** — Read the three transcript sections (A/B/C) and name which models are in play / violated and the fix. Use the worked intel/SITREP/grid examples as reusable templates.

### Common Stumbles

- Blind trust ("it sounds right") — confident narration is not verified execution.
- Learned helplessness ("too technical to check") — they don't need to replicate the work, only judge whether output makes sense and constraints held. A human judgment call, not a technical skill.
- Approving a change they don't understand. If you don't understand it, don't approve it — have the agent explain first.

### Deliverable

No formal artifact; readiness gate is one completed delegate-verify-own loop and the ability to name the models firing in a transcript.

### Transition to Module 8

Students command an agent. Module 8 is ammunition discipline — how to *spend* the tokens you learned about in Module 1: model selection, context management under a real session, and cost discipline.

---

## Module 8 — Ammunition Discipline: Tokens, Context & Cost

**Estimated duration:** Plan a focused block of Day 2 after Module 7

### Learning Objectives

- Treat tokens as ammunition — cost, speed, and accuracy all scale with tokens spent (does **not** re-define a token; that is Module 1)
- Apply the fast / reasoning / big-context model-selection heuristic on the spot
- State the three operational context rules; manage a silently-filling window with smart sampling
- Apply the four cost-discipline principles; know iteration is where cost hides
- Name the three ways AI is delivered and paid for; connect cloud delivery to the Module 1 data-handling rule

### Instructor Notes (from this module's `??? note` blocks)

- **Do not re-define the token:** Open by *asserting* prior knowledge ("you already know what a token is") and move straight to spending it. If a student is shaky, route them back to Module 1 — do not re-teach it here. This module is a deliberate spiral on Module 1.
- **Name drift is real:** Tier names (Haiku/Sonnet/Opus) and competitor names will change. Teach the *shape* — fast, balanced, powerful — and make bookmarking the provider docs part of the job. Do not let students memorize current model IDs as permanent.
- **Frame it as discipline, not stinginess:** The point is a defensible result efficiently, not minimum tokens. Tie back to the Module 7 operator posture — a clear brief is cost-conscious *and* good supervision.
- **Skip the pricing tables:** Specific prices change every quarter. Teach the structure: tokens cost money, bigger models cost more, cloud sends data off-machine, match the model and delivery to the job. All prices/tiers carry the verify-before-teaching flag.

### Hands-On Direction

1. **Feel the weight** — Paste a prompt into a tokenizer; note token vs. word count; rewrite as a structured prompt and re-count. Notice "longer in the right way."
2. **Model landscape check** — On the provider's model page, find current fast/balanced/powerful tiers; assign three sample tasks (format conversion, complex analysis, long-document read) to tiers with one-sentence rationale.
3. **Context under pressure** — In an agent, have it find and read only the relevant files via search; run a longer session, then ask it to summarize what it did; watch for drift as the cue to start fresh.
4. **Cost rewrite** — Apply the four principles to a real prompt; count words before/after; decide what the agent should read via tools instead of pasting.

### Common Stumbles

- Reaching for the biggest model by default — expensive, slower, usually unnecessary.
- Pasting large files instead of having the agent read them via tools.
- Not noticing the window fill until the model contradicts itself — tool results accumulate silently.

### Deliverable

No formal artifact; readiness gate is applying the selection heuristic and the four cost principles to real tasks.

### Transition to Module 9

Students can operate efficiently. Module 9 lands now on purpose: accountability is visceral only after a student has felt an agent take real action. It is the rulebook for what you do with the output — distinct from Module 1's data-handling (what flows in).

---

## Module 9 — Rules of Engagement: Ethics & Responsible AI Use

**Estimated duration:** Plan a block of Day 2 to close the agentic-leap day

### Learning Objectives

- Explain why capability does not transfer accountability — you sign for every product; "the model said so" is no defense
- Reframe hallucination in a consequential product as authored harm; scale verification duty to the stakes
- Counter automation bias by judging first and consulting second
- Distinguish stereotype-matching from evidence-based output and own the duty not to launder bias
- Apply the materiality test for disclosure; default to traceability; know DoDI 5400.19 governs public-facing content
- State the lawful-use boundary (capability ≠ authorization); respect privacy beyond OPSEC (aggregation)
- Name the five DoD AI Ethical Principles and map each to a practiced habit

### Instructor Notes (from this module's `??? note` blocks)

- **Make the signature literal:** Have students physically initial the AI-drafted paragraph before "release," meaning *I vouch for every claim here.* Several will sign, catch themselves, and pull it back to check — that hesitation is the lesson landing.
- **Connect back, don't re-teach:** This is the supervisor mindset's "own the outcome" duty made specific to authored products. Name the link; do not re-teach delegate-verify-own.
- **Don't let it become cynicism:** Calibrated duty, not distrust. Extraordinarily useful *and* a hallucination in a consequential product is an ethical failure. A student who refuses to use the tool missed the lesson as badly as one who signs without checking.
- **Stakes set the standard, not your schedule:** A deadline raises the temptation to skip the check, not lowers the bar.
- **Make the ordering non-negotiable (automation bias):** The lesson lives in the sequence — own assessment written and visible *before* the model's is revealed. If students peek first, the exercise is worthless.
- **Hold the line between M1 and M9 (bias):** Module 1 owns *spotting* skewed output (literacy); Module 9 owns the *duty* not to launder it. Don't re-teach the mechanism — teach the obligation.
- **Disclosure ≠ confession:** Reframe disclosure as a quality and trust practice, like citing a source. Pair with the public-affairs requirement so students see it is policy, not just etiquette.
- **Distinguish cleanly from OPSEC (privacy):** OPSEC/data-handling protects *our* sensitive info (inbound); privacy/collection ethics respects *others'* info and limits on gathering it. The aggregation point is the one most students have never considered — spend time there.
- **Keep dual-use on the boundary:** No how-to, no fearmongering. The deliverable is a calibrated operator who knows the capability is dual-use, the boundary is law/policy/authorities, and the reflex is to route near-the-line questions upward.
- **Land the coherence (Section 8):** Walk the principles-to-habits map row by row. Reinforce that "ask the chain/legal" is a strength, not an admission — the whole module is permission to escalate.
- **Verify currency before delivery — this is not legal advice:** The five Principles, CDAO RAI guidance, DoDI 5400.19, and NIST AI RMF are all in active revision. Confirm current versions and unit policy; when a real call is unclear, route to chain of command or legal/ethics advisor.

### Hands-On Direction

1. **Sign for a product** — Have the model draft a short analytic paragraph on a non-sensitive topic; find and verify every checkable claim; surface a planted false claim; only then initial it.
2. **Stakes ladder** — Take a claim with a citation and write the consequence at low vs. high stakes; do the high-stakes verification.
3. **Judge first, consult second** — Write your own assessment before seeing the model's; compare; investigate every disagreement.
4. **Spot and strip bias** — Have the model profile a group from a thin (fictional) description; underline confident conclusions; strip anything supported only by assumption.
5. **Provenance note** — Apply the materiality test; draft a one-line provenance note; decide internal vs. public-facing.
6. **Recognition exercises** — Dual-use (legitimate vs. misuse from the same features; who sets the boundary) and privacy aggregation (combine five harmless data points; note what the aggregate reveals; where to stop).
7. **Map the principles** — Name the five from memory; map each to a Sections 1–7 habit.

### Common Stumbles

- Hearing "ethics" and defaulting to OPSEC — they are opposite directions (output vs. input).
- Treating spotting bias as sufficient — spotting without correcting is itself a failure.
- Reading "disclose AI use" as "admit you cheated."

### Deliverable

No formal artifact, but the readiness gate is real: a signed-after-verifying paragraph, a judge-first/consult-second loop, a bias strip-down, and the five principles named from memory. (Accountability and data-handling discipline are graded in the Module 11 capstone.)

### Transition to Module 10

The responsible habits are set. Module 10 applies them to real artifacts — clean Markdown, enough code literacy to verify output, a verified toolbox, and context files that steer an agent before you type.

---

## Module 10 — Field Craft: Markdown, Code, Tools & Context Files

**Estimated duration:** Plan Day 3 (four consolidated sections)

### Learning Objectives

- Write structured Markdown; know the four critical spacing rules; draft in VS Code, never in Word
- Read and narrate basic code (variables, conditionals, loops, functions); recognize off-by-one and infinite loops; pseudocode first
- Install, authenticate, and verify the toolbox (Claude Code, git, `gh`, VS Code, Node/Python); diagnose "command not found" via PATH
- Author a `CLAUDE.md` that genuinely constrains and a `me.md` that reflects how they work
- Keep `.env` out of history (`.gitignore` before first commit); keep context files free of sensitive content

### Instructor Notes (from this module's `??? note` blocks)

- **Don't linger on Markdown syntax:** ~15 minutes of genuine instruction; the rest is reps. Get students writing a README in the first ten minutes; correct spacing errors as they appear. A comprehensive syntax lecture does not survive contact with their first real document.
- **Concepts, not syntax mastery (programming):** The deliverable is reading literacy, not a programmer. Use pseudocode rigorously and one language (JS or Python). Off-by-one and infinite-loop errors are the highest-value bug classes — they recur constantly in agent output. Do not let it become a bootcamp.
- **Windows PATH and gh order:** Two failures dominate the tools section. Windows does not auto-update PATH after install — restart the terminal as the default fix before debugging deeper. And `gh auth login` fails confusingly if `gh` is not installed — confirm `gh --version` before touching auth.
- **The generic-CLAUDE.md failure:** The predictable miss is a `CLAUDE.md` that describes the project warmly and constrains nothing. Drive the fix with one question: "What should Claude NOT modify? What is out of scope?" Make students name a real prohibition and a real read-only file.

### Hands-On Direction

1. **Markdown README** — h1, three skills, one bold + one inline-code term, a fenced code block, a table; deliberately break one spacing rule and watch the preview break, then fix it.
2. **Read code** — Pseudocode a grade calculator; predict a loop's output; find why a `while` runs forever; narrate an AI-written function back into plain English and flag any block you can't narrate.
3. **Toolbox sweep** — Run every `--version` check; diagnose failures with `which`/`where`; authenticate `gh`; create `.gitignore` with `.env` before creating a dummy `.env`, and confirm `git status` doesn't show it.
4. **Context files** — Write a `me.md` (5–10 lines) and a `CLAUDE.md` for a scenario project with scope boundary, ≥2 hard rules, a named read-only file, success criteria, and a one-line conflict rule; run the agent and confirm it cites the `CLAUDE.md`; underline every genuine prohibition.

### Common Stumbles

- Markdown errors trace to the four spacing rules (space after `#`, blank line before lists, blank line before code fences, table separator row).
- Smart quotes from Word silently breaking code blocks — write Markdown in VS Code.
- "Command not found" right after install — restart the terminal first.
- A `CLAUDE.md` with no prohibitions — documentation, not steering. Push for at least one real "never" and one read-only file.

### Deliverable

**A README (5+ syntax elements), a verified toolbox checklist, and a `CLAUDE.md` + `me.md` with at least one genuine enforceable prohibition.**

### Transition to Module 11

Students hold the field craft. Module 11 is the proving ground — they stop practicing the pieces and prove them under their own command on a real artifact.

---

## Module 11 — The Proving Ground: Capstone Build

**Estimated duration:** Plan most of Day 4 (build + present)  
**Instructional mode:** Mentored project. Coach, do not give answers.

### Learning Objectives

- Integrate every prior module into one shipped project
- Author a `CLAUDE.md` that demonstrably constrains a live agent run
- Execute and document one full delegate-verify-own loop (verify the diff against the agent's claim)
- Recover a deliberate bad agent edit to a known-good commit using git
- Ship to GitHub with a README, clean history, no secrets, and an accountable sign-off

### Instructor Notes (from this module's `??? note` blocks)

- **Scope is the whole game:** Students fail two ways — over-scope and never reach the verify loop, or under-scope into something with no decisions for the agent to get wrong. Push toward a project with at least one real constraint and at least one place the agent could plausibly err — that is where the graded loop lives.
- **Make the constraint testable:** Require at least one prohibition you can test live (a read-only file, a forbidden output). If the `CLAUDE.md` has no rule you can try to make the agent violate, it has no constraint worth grading. Have them show the agent honoring the boundary on camera or in a transcript.
- **Grade the loop, not the artifact:** A working artifact with no evidence of verification scores low; a modest artifact with a clean, documented delegate-verify-own loop scores high. Look specifically for the student checking the diff against the agent's claim.
- **Make them cause the failure:** Require a deliberate bad-edit-and-recover, not a hypothetical. The learning is in *feeling* that a mistake is reversible.
- **Weighting is deliberate:** If a student protests that their app runs perfectly but scored mid-range, the answer is the weighting — loop, constraint, rewind, and ethics discipline are 75 of 100 points. Working code is table stakes, not the certification. Hold the line.

### Hands-On Direction (the five capstone phases)

1. **The Mission** — Pick a path (CLI tool / web app / API integration); one-paragraph plan + 3–5 features; apply the two-minute test; commit the plan.
2. **Standing orders** — `.claude/` with a `CLAUDE.md` that has a scope boundary, ≥2 prohibitions, a named read-only file, done criteria, and a conflict rule; add the actual read-only file the prohibition protects.
3. **The loop** — Delegate a bounded task; verify by reading/narrating the code, running it, and checking the diff against the agent's claim; own it with a commit message naming what you verified. Repeat for at least one more feature.
4. **The rewind** — Confirm a verified known-good commit; deliberately induce a bad edit; confirm the damage; roll back; re-issue with a tighter instruction.
5. **Ship it** — README; final scrub for names/credentials/`.env` in history; push; one-line accountable sign-off.

### Rubric (grades how the build was commanded, not just whether it runs)

| Criterion | Points |
|---|---|
| Delegate-verify-own loop (documented; diff checked against the agent's claim) | 30 |
| CLAUDE.md actually constrained the run (testable prohibition + scope boundary) | 15 |
| Git rewind of a bad agent edit (recovered to known-good; clean tree shown) | 15 |
| Data-handling & ethics discipline (no real names/units/credentials; no `.env` in history; accountable sign-off) | 15 |
| Working artifact (runs, basic error handling) | 15 |
| Documentation & commits (clear README; 5+ meaningful commits; pushed) | 10 |

**Passing:** 70+. **Honors:** 90+ with a clean loop and a recovered rewind.

### Common Stumbles

- Under-scope (no decisions for the agent to get wrong) or over-scope (never reaches the verify loop). Calibrate with "Can you demo this in two minutes?"
- Accepting a confident "done" without reading the diff — the most expensive failure.
- Skipping commits, then having nothing to rewind to. Frequent verified commits are what make supervision survivable.
- A committed secret — already in history; rotate it and clean the repo, don't just delete the file.

### Coaching phrases (no direct answers)

- "What does the error message say?" · "Can you draw what this should do?" · "What would you do if I wasn't here?" · "That's good progress — what's next?"

### Deliverable

**A GitHub repo with 5+ commits, a README, a constraining `CLAUDE.md`, a documented delegate-verify-own loop, and a recovered bad-edit rewind.**

### Transition to Module 12

Students have proven the command, not just the artifact. Module 12 names what comes next on the far side of the line of departure — recognition depth only.

---

## Module 12 — Crossing the LD: Bridge to Advanced Agentics

**Estimated duration:** A short brief on Day 4 (recognition, not build)  
**Instructional mode:** Flyover. Hold the altitude — every segment is recognition, not instruction.

### Learning Objectives

- State that advanced agentics is the same engine-harness-operator primitive and delegate-verify-own loop, composed and scaled
- Name RAG as the grounding pattern they used by hand in Module 7
- Describe MCP as the standard for extending the harness; name Tool / Resource / Prompt; know it is version-sensitive
- Name the permission/guardrail controls (scopes, allowlists, approval gates, sandboxes) behind the supervisor mindset
- Explain why an agent's plan is a supervision checkpoint
- Name the four workflow patterns (prompt chaining, routing, orchestrator-workers, evaluator-optimizer)
- Recognize the sub-agent/multi-agent idea and that it expands, not removes, supervision
- Name spot-checks, regression, and evaluator-optimizer as agent-evaluation ideas; know what is deferred to the main course

### Instructor Notes (from this module's `??? note` blocks)

- **Hold the altitude:** The strongest temptation is to start teaching. Don't. Every segment is a flyover. If students leave able to recognize the terms and say what is deferred, the module succeeded. Depth here steals time from the main course and overwhelms students fresh off a capstone.
- **The MCP trap:** This is the highest verify-before-teaching risk in the entire prerequisite course. The protocol genuinely shifts between releases. Teach the *shape* — harness is extensible; MCP standardizes the connection; Tools/Resources/Prompts are the three exposed types — and tell students any concrete detail must be checked against current docs. Do not let a confident-sounding specific become a taught fact.

### Hands-On Direction

This module is recognition-only — no hands-on builds. Each segment has a single embedded quiz to confirm the term landed. Use the "map every new term back to the primitive (richer engine / bigger harness / tighter operator loop)" framing throughout.

### Common Stumbles

- Trying to actually build any of it — every segment carries a **Deferred to the main course** marker for a reason.
- Delivering MCP specifics from memory.

### Deliverable

No artifact; readiness gate is the recognition checklist — naming each pattern and stating what is deferred.

### Transition

End of the prerequisite course. Students cross the line of departure with the vocabulary and the map; the main course is where they build.

---

## Glossary & Quick Reference

**Estimated duration:** Reference only — not a taught session.

The glossary (`docs/modules/glossary.md`) is a student-facing quick reference, available from day one and revisited throughout. Each term gets one or two plain sentences and a cross-reference to the module that owns it. Direct students there whenever they hit a term they don't know yet; do not let it substitute for the module that teaches the concept in depth.

**Instructor reminder (from the glossary's verify-before-teaching note):** Model names, tiers, pricing, and context-window sizes change with releases, and MCP details are version-sensitive. Treat any specific number as something to confirm against current provider documentation before relying on it.

---

# COURSE AT A GLANCE

| # | Module | Phase / Duration | Deliverable |
|---|---|---|---|
| 1 | **Know Your Weapon: How AI Actually Works** | Foundations — multi-week reps | Hallucination produced; verification drills; bright line written |
| 2 | **Briefing the Machine: Prompting as a Mission Order** | Foundations — 1–2 sessions | 5 structured prompts (one per technique) |
| 3 | **Feeding the Machine: Grounding & Multimodality** | Foundations — 1–2 sessions | Grounded read traced to source; multimodal "verify the read" |
| 4 | **Standing Orders: Making the AI Know You** | Foundations — 1–2 sessions | Custom instructions + one Project/config |
| 5 | **Know the Terrain: Filesystem & Terminal** | Operator Block — Day 1 (heaviest reps) | Six terminal transcripts |
| 6 | **The Duty Logbook: Version Control with Git** | Operator Block — Day 1 | GitHub repo, 5+ commits, resolved conflict, `.gitignore`-first |
| 7 | **From Advisor to Operator: Commanding an Agent** | Operator Block — Day 2 | One delegate-verify-own loop; identify-the-models |
| 8 | **Ammunition Discipline: Tokens, Context & Cost** | Operator Block — Day 2 | Selection heuristic + cost principles applied |
| 9 | **Rules of Engagement: Ethics & Responsible AI Use** | Operator Block — Day 2 | Signed-after-verifying paragraph; five principles named |
| 10 | **Field Craft: Markdown, Code, Tools & Context Files** | Operator Block — Day 3 | README, toolbox checklist, constraining `CLAUDE.md` + `me.md` |
| 11 | **The Proving Ground: Capstone Build** | Operator Block — Day 4 | GitHub repo: constrained run, documented loop, recovered rewind |
| 12 | **Crossing the LD: Bridge to Advanced Agentics** | Operator Block — Day 4 | Recognition checklist |
| — | **Glossary & Quick Reference** | Reference throughout | — |

**Critical path:** 1 → 2 → 3 → 4 → 5 → 6 → 7 → … → 11. Single ascending track; no skips. Module 11 specifically requires Modules 6, 7, 9, and 10.  
**The deliberate spiral:** "verify after acting" — introduced M5, reinforced M7, graded M11.

---

## Quick Troubleshooting Reference

| Symptom | First check | Fix |
|---|---|---|
| "Command not found" | `which`/`where <command>` | Not on PATH; restart terminal after install |
| Path confusion | `pwd` + `ls` | Navigate to a known location and rebuild |
| Git merge conflict | `git status` | Edit file, resolve markers, `git add`, `git commit` |
| Auth fails | `gh auth status` | `gh auth login`, choose HTTPS |
| Claude Code not connecting | `claude --version` | Reinstall if not found |
| Markdown not rendering | Check spacing rules / extension | Space after `#`, blank line before lists/fences, table separator row |
| JS/Node error | `node --version` | Install from nodejs.org if missing |
| Secret committed | `git log` / repo history | Rotate the credential; clean history; do not just delete the file |

---

**End of Teaching Guide**
