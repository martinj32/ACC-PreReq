# AI / Agentics Basics - Prerequisite Course Outline

**BLUF:** This is the on-ramp that gets a true beginner to the level where the Agentic Commanders Course, and Day 3 in particular, actually lands. The ACC advertises a low entry bar but Day 3 silently assumes git, the client-server idea behind tool calls, "state lives in files," and the operator mindset. This course fills the real gap. Two phases: Phase 1 is screen-only AI literacy with no install, Phase 2 is the agentic on-ramp where students touch a terminal and git for the first time.

**Theme:** Function-check the operator before the weapon. You do not hand someone a rifle before they know which end is dangerous.

**Outcome:** A student finishes able to explain what an LLM is and is not, write a structured prompt, reason about context and cost, tell a chatbot apart from an agent in their own hands, move around a terminal without fear, read and write markdown, and run the basic git loop including a pull request. That is the exact stack ACC Day 1 assumes and Day 3 depends on.

---

## Terms defined first

Read these before the modules. Every one shows up below.

| Term | Plain definition |
|---|---|
| .gitignore | A file at the root of a repo listing files git should never track. Used to keep credentials, sensitive configs, and generated files out of version control. |
| Agent / agentic tool | A model wrapped in a tool layer that can take action: read files, write files, run commands. |
| Branch | A parallel line of work in a repo so you can change things without touching the main version. |
| Chatbot | A model that gives you text back. It advises, it does not act. |
| CLI / terminal | Command-Line Interface. A text window where you type commands instead of clicking. |
| Commit | A saved snapshot of your work in git, with a note describing the change. |
| Context window | The model's short-term memory for one session. It has a hard size limit measured in tokens. |
| Engine, harness, operator | The three layers. Engine is the model, harness is the tool layer that gives it eyes and hands, operator is you. |
| Filesystem / path | How files are organized in folders, and the address that points to a file. |
| Frontier model | The current top-tier general models (Claude, GPT, Gemini). They come in tiers from fast-and-cheap to slow-and-smart. |
| Hallucination | When the model produces confident text that is wrong or made up. Not a rare bug -- a consistent feature of how text prediction works. The model has no truth-checking mechanism. |
| Human in the loop | A human positioned to review and approve agent actions before they affect the real world. The operator is the decision point, not a passive observer. |
| Knowledge cutoff | The date past which the model was not trained, so it has no reliable information about later events. |
| LLM | Large Language Model. A system that predicts the next chunk of text based on patterns it learned. It does not "know" facts, it produces likely text. |
| Markdown | A lightweight way to format plain text with simple symbols, readable by both humans and tools. |
| OPSEC / PII / CUI | Operations security, Personally Identifiable Information, Controlled Unclassified Information. Categories of data you keep out of AI tools. |
| Pull request (PR) | A proposal on GitHub to merge one branch into another, with a review step before the merge. The diff shows exactly what changed. |
| Repo (repository) | A project folder tracked by git, holding your files and their full change history. |
| System prompt | The standing instructions the model operates under before you type anything. In Claude Code, the CLAUDE.md file functions as an operator-layer system prompt -- it is loaded before the conversation begins and is invisible during the session. |
| Token | The unit a model reads and writes in, roughly a word-piece. Cost and context limits are measured in tokens. |
| Tool call | The moment an agent reaches out to do something (read a file, hit a website, run a command). |
| User prompt | Your direct ask in the moment. The question you type. |

---

# Phase 1 - AI Literacy (no tools yet)

Screen-only. No install, no terminal. The goal is a correct mental model of what these systems are before anyone touches a tool. This phase covers the ACC's stated entry bar plus the data-handling discipline the ACC actually enforces from Module 1.5 onward.

## Module P1.1 - What an LLM Actually Is

**Objective:** Replace the "it is a smart computer that knows things" myth with the correct model: a probabilistic text predictor.

**Why it is a prerequisite:** Every downstream behavior in ACC, from hallucinated code to context rot to why you must verify the agent's work, only makes sense if you understand the model is predicting likely text, not retrieving truth. Day 3's whole "you are the supervisor who approves" posture rests on this.

**Teach:** Next-token prediction in plain terms, hallucination as a built-in trait, knowledge cutoff, and the rule that the model is confidently wrong as easily as confidently right.

**Do-it exercise:** Ask a chatbot a question about a recent event past its cutoff. Watch it answer confidently and wrong. That single moment does more than an hour of lecture.

**Doctrine:** Trust but verify, with the emphasis on verify. The model is a sharp junior analyst who never says "I don't know." You check the work.

**How the model fails (three mechanisms to teach explicitly):**

Hallucination: the model generates tokens that are statistically likely to follow prior context. It has no truth-checking step. It cannot distinguish between "information I trained on accurately" and "information I am completing plausibly." Confident, fluent output is not evidence of accuracy. The practical rule: verify anything that matters before acting on it.

Knowledge cutoff -- three behaviors (not one binary): (1) model flags the gap and says so, (2) model answers confidently using stale training with no indication it may be wrong -- the dangerous case, (3) model has a retrieval tool and can access current information. All three look like confident answers. Verify time-sensitive content regardless.

Nondeterminism: same prompt, different runs, different output. The model uses a temperature parameter that introduces variation by design. Do not treat one output as definitive for high-stakes work.

Reliable hallucination demo for instructors: ask the model for five peer-reviewed academic papers on a narrow topic with authors and publication years. The model will produce plausible-sounding but fabricated citations. Have students attempt to verify one. This produces a hallucination on demand and makes it concrete.

**Watch-out:** Students anthropomorphize fast. Keep killing the word "knows." It predicts.

---

## Module P1.2 - Prompting Fundamentals

**Objective:** Move students from one-line search-box prompts to structured, conversational prompting.

**Why it is a prerequisite:** ACC Module 1.6 opens with user vs system prompt and the RGCOA structure, then the entire rest of the course builds on the three-layer prompt taxonomy. Skills and PRDs on Day 2 and Day 3 are just structured prompts that persist. A student who cannot write a structured prompt cannot write a skill.

**Teach:** The two layers (user prompt and system prompt). One structure such as RGCOA (Role, Goal, Context, Output, Asks). The habit of treating the model like a person: ask it to interview you, have it repeat the request back, iterate live.

RGCOA components:
- **Role** -- tell the model what expert or perspective it should apply. "You are an intelligence analyst reviewing source reliability."
- **Goal** -- the specific task you want completed. Single, concrete, unambiguous.
- **Context** -- background the model needs to do the task well. Relevant facts, constraints, audience.
- **Output** -- format, length, structure, and tone of the response you want.
- **Asks** -- tell the model what to do when it lacks information, what to flag, and what NOT to assume. Example: "If you need information I have not provided, ask me before proceeding. Do not invent facts. If you find a contradiction in the source material, flag it rather than picking one version." The Asks element is where you give the model permission to surface uncertainty instead of generating a plausible-sounding guess.

**Worked military example -- weak prompt transformed with RGCOA:**

Weak: "Summarize this report."

RGCOA version: "Role: You are an intelligence analyst preparing products for a brigade commander with limited time. Goal: Write a BLUF-formatted summary of the attached report. Context: The report covers threat activity in the past 72 hours. The commander reads this at 0500 before a battle update brief -- she needs the key finding first. Output: Three sections: BLUF (two sentences max), Key Points (three bullets), Recommended Action (one sentence). Total under 150 words. No jargon without definition. Asks: If the report contradicts itself, flag the contradiction. If you are not certain of a fact, say so."

**Do-it exercise:** Take a deliberately bad one-line prompt, rewrite it with RGCOA, run both, compare the outputs side by side.

**Chain-of-thought prompting:** Asking the model to show its reasoning before delivering an answer. Simplest form: append "think step by step" or "walk me through your reasoning before giving the final answer." This dramatically improves accuracy on multi-step tasks and makes the model's reasoning visible -- you can check the work before accepting the conclusion. Use it for complex analysis, planning, and any task where logic errors in the output have real consequences.

**Few-shot prompting:** Providing one or more examples of the input-output pattern you want before giving the actual task. Zero-shot: just the request. One-shot: one example before the request. Few-shot: two or three examples. The model infers the pattern and applies it consistently. Useful when the output format is precise, when classification criteria are hard to describe in words, or when one-shot prompts keep producing the wrong format.

**Doctrine:** The user prompt is the FRAGO. The system prompt is the OPORD it sits inside. You are writing the change order on top of standing orders.

**Watch-out:** Do not let students treat any one framework as gospel. RGCOA, CRISPE, CO-STAR all work. The structure is the point, not the letters.

---

## Module P1.3 - Context Windows and Tokens

**Objective:** Build the short-term-memory mental model and connect it to both quality and cost.

**Why it is a prerequisite:** Day 3 Module 3.7 (context rot) and the cost discipline throughout assume students already know what a context window is and why a full one degrades. This is the foundation that module sits on.

**Teach:** Context window as the session's short-term memory with a hard limit. Tokens as the unit of both memory and cost -- approximately 0.75 English words, or about 3-4 characters in English prose. Code and non-English text tokenize less efficiently -- more tokens per apparent word. The counterintuitive rule: focused context outperforms sprawling context.

Context window sizes for comparison (verify before teaching -- model specs update with new releases):
- Claude models: 200,000 tokens (~150,000 words)
- GPT-4o: 128,000 tokens (~96,000 words)
- Gemini 1.5 Pro / 2.0: 1,000,000+ tokens

"Lost in the middle" mechanism: Research has documented that models attend well to the beginning and end of a context window, and comparatively poorly to content in the middle. If a critical instruction was given early in a long conversation, it may be partially ignored once many turns have accumulated on top of it. Keep critical constraints at the start of the session or in the system prompt -- not buried mid-conversation.

Practical context management rule: Two questions to ask when deciding whether to start a fresh chat: (1) Has the task changed direction? Earlier turns are dead weight if the task shifted. (2) Is the model drifting or hedging on things it stated confidently before? That is the symptom of a filling context. Start fresh with a clean brief rather than diagnosing.

**Do-it exercise:** Paste a large wall of text into a chat, then ask the model to recall a specific detail from early in the conversation. Watch recall and precision drop as the window fills.

**Doctrine:** A cluttered context is a cluttered map board. Everything is technically on it, but you cannot find what matters.

**Watch-out:** Students assume more context is always better. It is not. Set this expectation early so context rot makes sense later.

---

## Module P1.4 - The Frontier Landscape

**Objective:** Orient students to the major models and, more importantly, to model tiers.

**Why it is a prerequisite:** The ACC lists "the difference between common frontier LLMs" as a stated prereq. Day 2 and Day 3 lean hard on tier choice (Opus to plan, Sonnet to execute, Haiku for cheap loops and evaluators). Students need the fast-cheap vs slow-smart axis before that makes sense.

**Teach:** The big three families (Claude, GPT, Gemini) at a high level. The tier concept inside a family: small and fast and cheap versus large and slow and smart. When you would reach for each.

Tier names by family (verify before teaching -- names change with releases):
- Claude: Haiku (fast/cheap), Sonnet (balanced), Opus (powerful/expensive)
- GPT: GPT-4o mini (fast/cheap), GPT-4o (balanced), o3/o1 (reasoning tier)
- Gemini: Flash (fast/cheap), Pro (balanced), Ultra (powerful)

Local models: Some models run entirely on your own machine -- no data leaves, no internet required. The standard tool is Ollama (ollama.com), which lets you run open-source models (Llama, Mistral, Phi) from the command line with `ollama run modelname`. Tradeoffs: requires significant hardware (8-32GB RAM), quality below frontier cloud models, but zero external data transmission. For OPSEC-sensitive or air-gapped work, local models are not a curiosity -- they may be the only permissible option.

Reasoning models: Some models have a distinct "thinking" or "reasoning" mode where they work through a problem step by step before responding. Claude has extended thinking. OpenAI has the o-series (o1, o3). These are qualitatively different from the fast/slow tier tradeoff -- they produce substantially better outputs on hard logical problems but cost significantly more and run slower. ACC introduces "thinking budget" as a parameter; this is the concept.

**Do-it exercise:** Run the same moderately hard prompt on a fast tier and a smart tier. Note the tradeoff in speed, quality, and cost.

**Doctrine:** Match the weapon to the target. You do not bring a sniper rifle to clear a room or a pistol to a 600-meter shot.

**Watch-out:** Specific model names and tiers change constantly. Teach the axis, not a frozen lineup.

---

## Module P1.5 - Data Handling and OPSEC

**Objective:** Install the discipline of what never goes into an AI tool, and where your data actually goes.

**Why it is a prerequisite:** ACC Module 1.5 is a hard security caveat: no classified, no PII, no CUI. Day 3 Module 3.2 raises it again because session logs can hold credentials and project details. This habit has to be reflexive before students touch a real tool with real data.

**Teach:** The categories to keep out (PII, CUI, classified, operational detail). The "default to no until you hear yes" rule. Where prompts and logs travel (the model provider's backend) and why local versus cloud matters for sensitive work.

Platform data handling (verify against current provider policies before teaching):
- Claude.ai consumer: prompts may be used to improve the model unless opted out in settings. Conversations retained and can be reviewed by Anthropic.
- Claude API / Enterprise: prompts not used for training by default. Data retention configurable. Enterprise agreements can include zero-retention options.
- ChatGPT consumer: training on conversations is on by default; can be disabled in Data controls settings.
- Bottom line: consumer apps are open nets. Enterprise/API access with an approved contract changes this, but only if your organization has specifically negotiated those protections.

CUI defined for military audience: Controlled Unclassified Information -- information requiring safeguarding per law or policy but not classified. Examples students will recognize: FOUO documents (legacy marking being replaced by CUI), Law Enforcement Sensitive (LES), personnel records, unclassified intelligence source/method info, pre-release contracts. Rule: if the document has ANY marking, or describes real people/units/operations/capabilities, it does not get pasted. Full stop.

Pre-paste scrub checklist (student artifact): Before pasting, check for and remove: real names, real unit designations, real locations (base names, grid coordinates), dates tied to real operations, any document markings, phone numbers/emails/account IDs, credentials/API keys, system or network names, IP addresses. Replace with bracketed placeholders: [NAME], [UNIT], [LOCATION], [NCO].

**Do-it exercise:** Take a realistic but unclassified document with names and identifiers, and scrub it to a paste-safe version. Compare before and after.

**Doctrine:** This is the pre-combat inspection of your data. You check what you are carrying before you step off, because you cannot un-send it.

**Watch-out:** This is the one module where "I'll be careful" is not good enough. Make the scrub a repeatable habit, not a judgment call made under time pressure.

---

# Phase 2 - Agentic On-Ramp (tools on)

Students now install and touch a terminal, markdown, and git. This is the part the ACC pretends you walked in with and most students did not. The highest-value module here is git, because three separate Day 3 modules collapse without it.

## Module P2.1 - Chatbot vs Agent

**Objective:** Make students feel, in their own hands, the difference between advice and action.

**Why it is a prerequisite:** This is the conceptual hinge of the entire ACC. Module 1.3 defines an agentic tool as one with read/write/execute access. If a student does not feel the advice-versus-action gap, nothing in the ACC lands.

**Teach:** Chatbot returns text, agent takes action. The engine-harness-operator stack. Read, write, execute as the dividing line.

| Task | Chatbot response | Agent response |
|---|---|---|
| "Rename this folder to archive" | Tells you the command to type | Renames the folder directly |
| "Summarize all .txt files in this directory" | Asks you to paste the contents | Reads each file, produces the summary |
| "Check if my script runs without errors" | Suggests possible errors to look for | Runs the script, returns the actual output |
| "Find all documents mentioning [topic]" | Cannot search files it cannot see | Searches the directory, returns matches |

Current tools (verify before teaching -- this landscape changes):
- Claude Code (Anthropic): terminal-native agent, reads/writes files, runs commands, integrates with GitHub
- Cursor: VS Code-based coding agent
- GitHub Copilot Workspace: spec-to-PR workflows
- ChatGPT with tools: web browsing and file reading via GPT-4o

Web access note: Claude Code accesses the web via a specific WebFetch tool call, not ambient browsing. It fetches specific URLs when asked. This is distinct from the model's training-time knowledge.

**Do-it exercise:** Ask a chatbot how to rename a folder. It tells you the command. You run it yourself. Then watch an agent rename the folder directly. Same task, two worlds.

**Doctrine:** A chatbot is the radio operator who tells you the grid. An agent is the element that moves to it. You are still the one who gives the order.

**Watch-out:** Do not skip the manual step. Students need to do the thing by hand once so they understand what the agent is automating.

---

## Module P2.2 - Filesystem and the Terminal

**Objective:** Get students moving around a command line without fear.

**Why it is a prerequisite:** ACC Day 1 starts in the terminal and never leaves. The prereq self-check is five terminal commands. Day 3's MCP install, loops, and worktrees all assume terminal comfort. A student frozen at a blinking cursor cannot participate.

**Teach:** What the terminal is and why it exists. Paths and directories. Navigate (cd), list (ls), make a file, read output. The mindset that the terminal is just typing instead of clicking.

**Do-it exercise:** From the terminal only: navigate into a folder, list its contents, create a file, and confirm it exists. No mouse.

**Doctrine:** The terminal is your direct line to the machine. Clicking is talking through a translator. You are learning to speak the language directly.

**WSL setup for Windows:** On Windows, use WSL (Windows Subsystem for Linux). Install: open PowerShell, run `wsl --install` (Windows 11). First launch creates a Linux username and password. Windows files inside WSL: `/mnt/c/Users/YourName/`. Path conversion: `C:\Users\Jake\Documents` becomes `/mnt/c/Users/Jake/Documents`. In VS Code: install the "WSL" extension; from WSL terminal run `code .` to open the current folder. Note: `touch` does NOT exist in native PowerShell -- only in WSL/Linux/macOS. In PowerShell the equivalent is `New-Item filename`.

**Watch-out:** Pick one known-good path per operating system. On Windows, point students at WSL. Native PowerShell is where the friction lives, same as the ACC warns.

---

## Module P2.3 - Markdown

**Objective:** Teach the lightweight format that both humans and harnesses read.

**Why it is a prerequisite:** ACC Module 1.4 is structured data and markdown. CLAUDE.md, skills, PRDs, me.md, and the entire Day 3 armory are markdown files. It is the connective tissue of the whole course.

**Teach:** Headers, bold, lists, tables, code blocks, links. Why structure helps the model parse intent. The difference between raw markdown and rendered markdown.

Syntax reference:
- Headers: `# H1`, `## H2`, `### H3` (space after # is required)
- Bold: `**bold**`
- Italic: `*italic*`
- Unordered list: `- item` (blank line required before the first item)
- Ordered list: `1. item`
- Inline code: `` `code` ``
- Fenced code block: triple-backtick, content, triple-backtick (blank line before required)
- Fenced with language: ` ```python ` (adds syntax highlighting)
- Link: `[text](url)`
- Table: `| Col | Col |` header row + `|---|---|` separator row + data rows
- Blockquote: `> text`

This course teaches GitHub Flavored Markdown (GFM). GFM adds tables, task lists, and fenced code blocks with language hints on top of standard Markdown. If it renders in VS Code preview and on GitHub, it is valid here.

VS Code preview keyboard shortcuts:
- `Ctrl+K V` (Windows) / `Cmd+K V` (Mac): side-by-side preview (recommended for learning)
- `Ctrl+Shift+V` / `Cmd+Shift+V`: preview in new tab

**Do-it exercise:** Write a structured note (headers, a list, a table) in raw markdown, then render it and see the formatting appear.

**Doctrine:** Markdown is the standard report format your tools all read. Same reason a unit uses one format for an OPORD: anyone, human or machine, can pick it up and parse it.

**Watch-out:** Keep it light. Students do not need every markdown feature, just enough to write a clean skill and a clean note.

---

## Module P2.4 -- Using Git and GitHub

**BLUF:** Git is your project's running logbook -- every change recorded, attributed, and reversible. GitHub is the secure offsite copy. Together they are the safety net that makes agentic work survivable. This module teaches the five moves you will actually use, the one file that keeps secrets out of your repo, and how to supervise an agent running git commands on your behalf.

**Why it is a prerequisite:** Day 3 Module 3.0 (contribute a skill via PR), 3.9 (governed armory in a shared repo), and 3.10 (worktrees) all collapse without git. The ACC frames git as something the harness does for you, but the operator still has to understand what is happening on their behalf.

**Learning Objectives:**
1. Explain what a repository is and what git tracks.
2. Run the basic git loop: stage, commit with a message, push.
3. Explain what a branch is and why it exists.
4. Describe what a pull request is and why it is a review gate.
5. Create a .gitignore file with appropriate entries for military/analyst use.
6. Describe GitHub Desktop as a visual alternative.
7. Identify common agent-generated git commands and state what each does.

**Core Concepts:**

Git vs GitHub: Git is software that runs on your computer and tracks changes. GitHub is a hosting platform where you upload a copy of your git repository. Git does not need the internet; GitHub does. The relation: git is the logbook you keep on your desk; GitHub is the offsite archive.

The repository: a project folder that git watches. Mechanically: a regular folder with a hidden .git subfolder containing the full change history.

The basic loop:
- `git init` -- turn a folder into a repo (run once)
- `git status` -- check what has changed (run constantly)
- `git add filename` or `git add .` -- stage changes for the next commit
- `git commit -m "message"` -- create a snapshot with a description
- `git push origin main` -- send commits to GitHub
- `git pull` -- retrieve commits from GitHub you don't have
- `git clone URL` -- download an existing repository including its full history

Commit messages: write in the present tense as if completing "This commit will..." -- "Add initial analysis framework" not "Added." Messages are the logbook entries; write them for the person reading six months from now.

Branches: an independent line of work inside the same repo. Create a branch to try something without touching the working version. `git switch -c branch-name` creates and moves in one step. `git switch main` returns to main. Best practice: have the agent work on a branch, not directly on main. Review the branch before merging.

Pull requests: a proposal on GitHub to merge one branch into another, with a mandatory review step. The PR shows a diff of every changed line. For agentic work: the agent produces changes on its branch; the PR is how you see exactly what changed and approve it before it reaches main.

.gitignore: a file at the repo root listing files git should never track. Create before the first commit. Required entries for this audience: `.env`, any credential files, `.DS_Store`, `__pycache__/`, `.venv/`. OPSEC note: if a credential file is committed even once, adding it to .gitignore does not remove it from history. The .gitignore is the enforcement layer -- it must be in place before the first commit.

GitHub Desktop: a free graphical interface that runs the same git commands in the background. Good for beginners navigating visually. Limitation: agentic tools run git through the terminal -- CLI literacy still matters for supervision even if you use Desktop for your own workflow.

**Agentic supervision:** When Claude Code runs git on your behalf, watch for:
- `git add .` -- what files are being staged? Check git status before approving.
- `git commit -m "message"` -- is the message accurate? Does it describe what actually changed?
- `git push` -- verify before the push that nothing sensitive is in the commit. Check `git log --oneline` first.
- Never approve `git push --force` without understanding exactly what it will overwrite.

**Doctrine:** The repo is the unit's running log -- every change recorded, attributed, timestamped. A branch is a parallel lane of work. A PR is the review before the change goes live. The .gitignore is the pre-mission gear check: inventory what you are carrying before you step off.

**Watch-Outs:**
- The .gitignore timing trap: create it before the first commit. Adding a file to .gitignore after it has been committed does not remove it from history.
- "main" vs "master": older repos use "master" as the default. Both are valid; the name is just a convention.
- Force push is dangerous: overwrites history on the remote. Never run without understanding exactly what it does.
- Merge conflicts are not failures: they happen when two changes touch the same line. Git asks you to resolve. Normalize this.

**Hands-On Exercise:**
1. Create a folder, run `git init`, create a `.gitignore` with `.env` and `.DS_Store` entries
2. Create a `notes.md` file, stage and commit: `git add .gitignore notes.md` then `git commit -m "Add notes template and gitignore"`
3. Create a branch: `git switch -c feature/add-reference-list`
4. Edit notes.md, commit the change
5. Create a GitHub repo and push: `gh repo create projectname --public --source=. --remote=origin --push`
6. Open a pull request: `gh pr create --title "Add reference section" --body "Adds reference list to notes"`
7. Review the diff on GitHub, merge the PR, switch back to main and pull

**References:** ACC Module 1.8 (git light touch), ACC Day 3 Modules 3.0 (skill PR), 3.9 (governed armory), 3.10 (worktrees).

---

## Module P2.5 - The Operator Mindset

**Objective:** Set the supervisory posture: you direct, you approve, you can pull the plug.

**Why it is a prerequisite:** ACC Day 1 rules of the road and the Day 3 fleet modules all treat the student as a watch officer, not a typist. The think-gap discipline (plan your next move while the agent works) is an ACC habit from the first morning. Day 3 Module 3.12 (the tax) is pure operator judgment.

**Teach:** You are on the drone feed, not in the breach. Approve and reject tool calls deliberately. Use the pause, do not panic at a long think. Plan the next prompt and the failure mode in the wait. Set boundaries so the always-on tool does not run your life.

**Do-it exercise:** Watch an agent attempt a multi-step task. Practice approving good proposed actions and rejecting a bad one, then redirecting. The skill is judgment under a moving agent, not typing.

**Doctrine:** You are the supervisor of an element in the field. You do not do their job for them, you decide what they do next and you own the call to stop.

**Watch-out:** New operators either rubber-stamp everything or freeze and approve nothing. The target is deliberate judgment on each consequential action.

---

## End-of-course readiness check

A student is ready for ACC Day 1 when they can, without help:
- Explain in one sentence what an LLM is and why it hallucinates
- Write a structured prompt and iterate on it by conversation
- Say what a context window is and why a full one degrades quality
- Name the major model families and the fast-cheap vs slow-smart tradeoff
- Scrub a document to paste-safe and explain where their data goes
- State the difference between a chatbot and an agent and why it matters
- Navigate a filesystem and run basic commands in a terminal
- Read and write clean markdown
- Run the git loop (commit, branch, push) and open a pull request
- Hold a supervisory posture: approve, reject, redirect, stop

If they can do all ten, they walk into ACC Day 1 ready to work from the first minute instead of spending Monday morning catching up.

---

## Sequencing and audience note

Phase 1 can stand alone as an AI-literacy block for a non-technical audience. Phase 2 is what specifically bridges to the ACC and anything hands-on-keyboard. If your students arrive at the true-beginner end, run both phases in order. If they arrive closer to the ACC's stated bar, Phase 1 is a fast review and Phase 2 is the real work.

The single most important sequencing rule: P2.1 (chatbot vs agent) is the hinge, and P2.4 (git) is the load-bearing prerequisite for Day 3. Do not let either get rushed.

---

*Built to mirror the ACC Student Companion module format. Prerequisite scope derived from the ACC Pre-Class Prerequisites doc and the backward dependency map of Day 1 through Day 3 modules.*
