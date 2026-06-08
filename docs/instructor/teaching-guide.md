# AI and Agentics Basics — Consolidated Teaching Guide

**For:** Instructors delivering the full course start to finish  
**Use:** Run alongside student-facing content. This doc tells you what to do, say, watch for, and hand off — not what to read aloud.

---

## How to Use This Guide

- One section per module, in nav order.
- Durations are instructional time, not clock time (add breaks separately).
- Instructor notes pulled from the `??? note` blocks in student content are surfaced here — students do not see them.
- Hands-on activities are listed with brief instructor direction; full student instructions live in the course pages.
- Every section ends with a transition note to the next module.

---

## Pre-Course Prep Checklist

Before any session:

- [ ] Verify current model names and context window sizes at docs.anthropic.com — these change with releases
- [ ] Verify current pricing structure at anthropic.com/pricing — do not teach specific dollar amounts
- [ ] Run all version checks on your machine (`claude --version`, `git --version`, `gh --version`, `node --version`, `code --version`)
- [ ] Create `_classroom-demos/` folder with prepared files for each module (see prereq-guide.md for folder structure)
- [ ] Screen setup: code editor and terminal visible simultaneously
- [ ] Have a timer students can see

**Total instructor prep time before first cohort:** ~4-6 hours.

---

# BEDROCK

## Module: AI Literacy

**Estimated duration:** Multi-week, short daily reps (15-30 min/day)  
**Audience:** Someone who uses AI by feel and has never thought about what is happening underneath.

### Learning Objectives

- State in one sentence what an LLM does (predicts text from patterns)
- Explain "trained not programmed" in plain terms
- Name the four core failure modes (hallucination, confident-wrong, nondeterminism, knowledge cutoff)
- Produce a hallucination with their own hands
- Name the four elements of a deliberate prompt (role, context, example, output spec)
- Identify which of three AI delivery models they are currently using
- State the bright line for data handling: what never goes into an unauthorized system

### Key Concepts to Emphasize

**What an LLM is:**
- The only accurate verb is *predicts*. Not "knows," "thinks," or "lies." Interrupt anthropomorphism every time it surfaces — it is a wired cognitive shortcut and will re-train with repetition.
- "Brain in a jar" framing: fluent and capable, but no memory between chats, no live data, no ability to act without external tools.
- Do not open with transformers, attention heads, or parameter counts. The mental model that survives contact with a real tool is the deliverable.

**Tokens and context:**
- Context window = whiteboard with finite space. New writing crowds out old.
- Symptoms of a full window: the model hedges on things it stated confidently, contradicts earlier instructions, drifts.
- Practical rule: start a fresh chat when (1) direction has changed and earlier turns are dead weight, or (2) the model is drifting.
- Do not spend time on token math. "Shorter and focused beats long and sprawling" is the instinct to build.

**How LLMs fail:**
- Do not let this tip into cynicism. The goal is calibrated trust, not distrust. Both "extraordinarily capable" and "hallucinates" are simultaneously true.
- Students who hear about hallucination without producing it themselves do not internalize it. The hands-on exercise is not optional.
- Three behaviors around knowledge cutoff: (a) flags uncertainty (honest), (b) answers confidently with stale data (dangerous), (c) uses a retrieval tool. All three look identical from the outside.

**Prompt engineering:**
- The four elements are a structure, not a script. The durable skill is clarity.
- Resist turning this into "prompt tricks" hour. Students who chase tricks hit a ceiling fast.
- Iteration is the habit that matters most. A rough ask the model can build on beats silence.

**Delivery and cost:**
- Teach the structure (subscription / pay-per-token / org key; cloud / local; fast / balanced / powerful tiers), not specific prices. Prices change within a quarter.
- "Always use the biggest model" is wrong. Match the model to the job.

**Data handling:**
- This module does not get softened. Soften it and students hear "be careful sometimes." The message is a hard rule.
- For military/intel audiences: state the "paraphrase and summarize" loophole explicitly — it does not exist.
- Authorization is a property of the system, not the tool's capability. Impressive and authorized are not the same.

### Hands-On Activities

1. **Prediction demo** — Type an incomplete sentence, submit. Add "definitely" to the same sentence, submit again. Compare outputs. Then ask a factual question and ask how you would verify the answer without the model's help.

2. **Context window probe** — Paste several pages of dense text into a fresh chat. Ask about something near the top, then something near the bottom. Start a new chat and ask the same bottom question. Compare quality.

3. **Hallucination on demand** — Ask for 5 peer-reviewed papers on a narrow topic with full citations (author, journal, year). Pick one and try to verify it in Google Scholar or PubMed. The citation will be unverifiable. Debrief: "What would you have done if you had not checked?"  
   *Instructor note: Use a topic where you know the correct answer. Never demo on live operational content.*

4. **Before/after prompting** — Write a one-line version of a real task, submit it, save the output. Then add role, context, an example of good output, and an output spec. Submit again. Compare side by side. Identify which element changed the result most.

5. **Delivery model identification** — Open your chatbot's settings. Find the model name. If API access is available, open the pricing page — read for structure, not numbers.

6. **Personal bright line** — Think about the last three things you pasted into an AI tool. For each: was the system authorized? Identify one category of content you handle regularly that will never go into an unauthorized tool. Write it down.

### Discussion Questions / Knowledge Checks

- "The model just gave you a confident-sounding answer. What would it take to verify it?"
- "You set an important constraint at the start of a long conversation. Ten exchanges later, the model seems to have forgotten it. What happened?"
- "You just watched the model invent a source. What does that mean for the next time it gives you a fact you have not heard before?"
- "You need to run an analysis task with a long document and several back-and-forths. What factors determine the cost, and how would you reduce it?"
- "You have a borderline-sensitive document and an unauthorized but capable AI tool that would save hours. What is the correct call?"

Each section also has an embedded single-answer quiz in the student content — use these to check comprehension before moving on.

### Transition to Personalizing Your AI

Students now have a working mental model of the engine and know where it breaks. The next module converts that into a persistent setup — so every session starts with the model already knowing who they are and how they work.

---

## Module: Personalizing Your AI

**Estimated duration:** 1-2 sessions (30-60 min total)

### Learning Objectives

- Find custom instruction settings in their tool of choice (ChatGPT or Claude)
- Write at least three instructions: who they are, how they want responses, what to never do
- Observe a before/after difference in output
- Set up at least one Project or named configuration for recurring work
- Confirm no sensitive or controlled information is in their instructions

### Key Concepts to Emphasize

- Custom instructions = persistent context loaded before every message. One-time investment, pays back on every session after.
- Custom instructions count against the context window. Keep them under 500 words. Use Project documents for heavier reference material.
- Platform UI changes frequently. Verify the menu path before teaching. The concept is stable; the interface is not.
- Remind students of the data handling module before they write: everything in a custom instruction goes to the platform's servers on every request.
- The difference between proactive (custom instructions — you set them deliberately) and reactive (ChatGPT memory — it records what comes up). Use both.

### Hands-On Activities

1. **Custom instructions setup** — Open the tool, find the settings, write three instructions (who you are + what you do, how you like responses formatted, one thing to never do). Start a new chat. Compare to a chat without instructions.

2. **Project or memory setup** — Claude users: create a Project for a recurring task type, add instructions and at least one reference document. ChatGPT users: open memory settings, delete anything outdated, add one manual memory entry for something the model should always know.

### Discussion Questions / Knowledge Checks

- "You wrote a custom instruction that says 'always lead with a one-sentence summary.' On one response, the model ignores it. What are the two most likely causes?"
- "You create a Project for analysis work with detailed instructions. Three months later, your role changes. What do you need to update, and where?"

### Transition to Terminal Basics

Students now have the AI side calibrated. The next phase is entirely different: no AI, plain computer literacy. This is where the course gets uncomfortable for some people. Frame it early: the terminal is not a detour — it is the terrain the agent will move across.

---

# TERMINAL BASICS

## Module: The Machine

**Estimated duration:** Multi-week, short daily reps (3 sessions, ~30 min each)  
**Critical setup step:** Before the first session, have students turn on file extension visibility. Windows: File Explorer → View → Show → File name extensions. Do not skip this — it prevents confusion in every downstream module.

### Learning Objectives

- Navigate the filesystem without using search
- Describe the difference between plaintext and rich text and give an example of each
- Install VS Code and open a folder in it
- Toggle the Markdown preview in VS Code

### Key Concepts to Emphasize

**Files, folders, and the tree:**
- Many casual users have never navigated the folder tree — they find files through search or recent items. Test before assuming.
- A path is a route, not a name. Read it left to right, one slash = one step down the tree.
- Connecting to Phase 3: "Phase 3 is the same moves, typed."

**Plaintext vs rich text:**
- "Plaintext is honest, rich text hides things" is the entire lesson. Do not go into encodings (UTF-8, ASCII, etc.).
- The practical consequence: never write Markdown in Word. Write it in VS Code.
- Smart quotes, em-dashes, non-breaking spaces — all travel silently with pasted Word content and break things downstream.

**Code editor:**
- Today's scope: open, view, close. Do not install extensions, change settings, or edit files. Comfort at the front door is the goal.
- If the VS Code install is broken on one machine, use Notepad++ and move on. Do not stall the room.

### Hands-On Activities

1. **Tree walk** — Open File Explorer or Finder. Navigate from home to Downloads by clicking only — no search. Find a file. Read its full path in the address bar. Create a `practice` folder on the Desktop. Move a file into it by dragging.

2. **Plaintext vs rich text** — Open Notepad, type a few sentences, save as `test.txt`. Open it in VS Code. Then open a `.docx` file in VS Code (not Word) and look at what is inside.

3. **VS Code orientation** — Install VS Code. Open the `practice` folder (File → Open Folder). Click the `.txt` file. Find a `.md` file anywhere on the machine. Open it. Toggle the preview with `Ctrl+Shift+V`.

### Discussion Questions / Knowledge Checks

- "You just moved a file by dragging. Write out the path to where it now lives. Could you give someone else those directions and have them find it?"
- "You paste a block of text from a Word document into your AI chatbot and the formatting looks off. What is the most likely cause?"
- "You are looking at the same Markdown file in two panes — raw on the left, rendered on the right. Which version does the machine work with?"

### Transition to The Terminal

The Machine gave students the map. The Terminal is the same moves, typed. Anxiety is normal and expected — name it before they feel it.

---

## Module: The Terminal

**Estimated duration:** Multi-week, heaviest calendar weight (~6 sessions, 30-45 min each)  
**This is the spine of the course.** Most students need more reps here than anywhere else. Do not rush.

### Learning Objectives

- Open the terminal without hesitation
- Navigate the filesystem using `pwd`, `ls`, `cd`
- Create, copy, and move files using `mkdir`, `touch`/`New-Item`, `cp`, `mv`
- Write and use absolute and relative paths
- Use tab-completion on every path
- Add flags to commands and use `--help` to find flags they do not know
- Stop a running command with `Ctrl+C`
- Explain version control as a logbook of file changes they can rewind

### Key Concepts to Emphasize

**Terminal orientation:**
- Address the bait-and-switch out loud before a student says it: "Some of you are wondering why an AI course spent two weeks on the command line." Then make the connection explicit: the agent acts through the terminal. Students who do not understand the terrain cannot supervise someone navigating it.
- Nothing in this module and the next three can hurt the machine. Say this explicitly.
- One command, fully understood, beats ten demoed. Do not show off. Return the prompt, explain what happened, ask for questions, move on.

**Navigation (`pwd`, `ls`, `cd`):**
- `pwd` is the reset button. Lost in the terminal? Type `pwd`. You can never be permanently lost.
- Reps over coverage. Same three commands, many short repetitions, spread across several days. Do not introduce file creation until navigation is solid.
- Getting "lost" is the number-one beginner panic. Normalize it. Make students run the `pwd`→`ls`→`cd`→`pwd`→`cd ..`→`pwd` cycle until it feels routine.

**File operations (make, move, copy):**
- Build the verify-after-acting habit here. After every command: `ls`. Check the target. "Trust the action, not the narration" runs through all agentic work — build it at the command line before the agent is involved.
- No deletion in this phase. Deletion is irreversible at the command line. It comes later, behind heavy framing.
- Typos in filenames create new files without erroring. This is why `ls` after every action is the standard.

**Paths and tab-completion:**
- The terminal's unforgiving exactness is the lesson, not the frustration. A student annoyed that a capital letter breaks a path is learning the right thing. Name it: "Yes, the space matters. That is why tab-completion exists."
- Tab-completion is not a shortcut — it is standard operating procedure. Use it on every path, every time.
- Absolute path: works from anywhere. Relative path: only works from the right starting position.

**Flags and `--help`:**
- Do not memorize flags. The concept (flags exist, `--help` finds them) is the lesson.
- `Ctrl+C`: name it as a control mechanism, not an emergency. Students who know they can stop something are less afraid to start it.

**Version control concept:**
- No commands today. Load the reason before the commands. If a student asks "how do I actually do this?" — "You will do it later. Today you need to know why."
- For military audiences: duty logbook framing. For civilian audiences: "undo button for your whole project." Read the room.

### Hands-On Activities

1. **Terminal orientation** — Open the terminal. Sit with the blinking cursor for ten seconds. Name the feeling. Run `date`/`Get-Date`, `whoami`, `pwd`, `ls`, `echo "hello"`. Close and reopen. Re-run one command from memory.

2. **Navigation drill** — Run `pwd` → `ls` → `cd` into a folder → `pwd` → `ls` → `cd ..` → `pwd`. Repeat until routine.

3. **Make, move, copy** — Create `terminal-practice` folder, navigate into it, create `day1.txt`, copy to `day1-backup.txt`, rename to `day1-v1.txt`. Run `ls` after each step.

4. **Path puzzle** — Navigate to a folder using the full absolute path (type it by hand). Navigate to the same folder using tab-completion. Compare.

5. **Flags and help** — Run `ls --help` or `Get-Help ls`. Read the first ten lines without panic. Find the flag that shows hidden files. Run `ls` with that flag. Run `ping google.com` for five seconds. Press `Ctrl+C`.

6. **Version control reflection** — No commands. Think of a file edited multiple times last month. Ask: "If I needed to see what it looked like three weeks ago, could I?" That gap is what version control fills.

### Discussion Questions / Knowledge Checks

- "You typed a command and saw a response. What is the difference between that and clicking a button in an app?"
- "You typed `cd Documents` and then `pwd`. What does `pwd` tell you?"
- "You ran `mv report.txt final-report.txt` and then `ls`. What are you checking for?"
- "You are deep in a nested folder and need to copy a file three levels up. Absolute or relative path?"
- "You run a command and nothing happens for thirty seconds. What are the two possibilities?"
- "An agent just ran a batch edit on 40 files. You look at one and it is not right. Without version control, what are your options?"

### Transition to Agentic AI

Students can now navigate and operate in the filesystem from the command line. Agentic AI is the payoff module — this is where Phases 2 and 3 pay off. Make the connection explicit: every command they learned is what the agent runs when it works in their filesystem.

---

# AGENTIC AI

## Module: Core Concepts

**Estimated duration:** 1-2 sessions (~60-90 min total)

### Learning Objectives

- State the one-line difference between a chatbot and an agent
- Explain what read, write, and execute access means in practice
- Connect the Terminal Basics modules to why agents need that access
- Name the three parts of the engine-harness-operator model
- Explain version control as a logbook of agent actions they can rewind
- State the three duties of the supervisor: delegate, verify, own

### Key Concepts to Emphasize

**Chatbot vs agent:**
- Do not assume students connect the dots. Say it explicitly: "Every command you learned in Terminal Basics — `pwd`, `ls`, `cd`, `mkdir`, `mv` — that is what the agent runs when it works in your filesystem. You learned to navigate the terrain so you can supervise someone else navigating it."
- Read, write, execute is a lot of trust. This is not abstract — an agent with write and execute access can create, modify, or delete files on a real machine.

**Engine-harness-operator:**
- Engine = the LLM (reasoning, generates, plans)
- Harness = the tool layer (gives the engine access to files, commands, external systems)
- Operator = you (directs the mission, approves consequential actions, carries accountability)
- All three are required. The engine cannot act without a harness. The harness cannot direct without an operator.

**Version control:**
- Repeat the "why" here — the agent is about to start editing files. The logbook is how you keep accountability over a teammate that works fast and never sleeps.
- Still no git commands. The commands come in M3. Today is the reason.
- For military audiences: duty logbook. For civilian audiences: "undo button for your whole project."

**Supervisor mindset:**
- This is the through-line of the entire course. Do not treat it as a capstone topic to introduce once at the end. Every agentic action in later modules should be framed with the supervisor loop.
- The agent is a motivated junior with file-system access: capable, fast, willing to fill ambiguity with plausible-sounding assumptions.
- Two failure modes to name and counter:
  - *Blind trust:* "It sounds right." Confident narration ≠ verified execution.
  - *Learned helplessness:* "I can't check this, it's too technical." You do not need to replicate the agent's work. You need to check whether the output makes sense, whether constraints were honored, whether anything looks wrong. Human judgment call, not a technical skill.
- Optimize the capstone for the loop, not the polish. A rough artifact that was checked beats a finished artifact that was not.

### Hands-On Activities

1. **Chatbot vs agent comparison** — Open a web chatbot. Ask: "Rename the folder 'project' to 'project-v1'." Note whether it renamed anything or described how. If Claude Code is available, ask the same thing in a project folder. Compare what happens. Write one sentence on the difference.

2. **Delegate-verify-own loop** — Give the agent (or chatbot if agent is not available) a small real task. Write a clear brief: who you are, what you need, what good output looks like, what is off-limits. Submit. Verify: does it do what you asked? Did it make any assumptions you did not authorize? If something is off, correct it. Identify what you should have specified more precisely.

### Discussion Questions / Knowledge Checks

- "You just asked a chatbot to rename a folder. What would an agent do differently — and what are you trusting it with when it does?"
- "An agent completes a task and narrates what it did in clear, confident language. What do you do next?"
- "An agent just ran a batch edit on 40 files. You look at one and it is not right. Without version control, what are your options?"
- "The agent completed a task and the output looks correct at first glance. What would you actually check to verify it?"

### Transition to Mental Models

Students can now place the agent in the context of the terrain they learned. Mental Models is a standalone 35-minute conceptual block — the six frameworks that make every Technical Foundations module make sense. It should be read before touching the Technical Foundations modules.

---

# MENTAL MODELS

## Module: Core Content

**Estimated duration:** 35 minutes (standalone, self-contained)  
**Note:** The Quick Reference and Workbook are student-facing support materials, not additional sessions. Assign the Workbook as homework or in-class practice after delivery.

### Learning Objectives

- Explain the harness model: LLM + tools = agency
- Describe what a context window is and what happens when tool results accumulate
- Treat tokens as a resource with real cost
- Explain what a tool call is and why it enables verification
- Adopt active supervision as the default posture
- Build cost-consciousness as a core habit

### Key Concepts to Emphasize

**The six models in brief:**

| Model | Core idea | Common misconception to counter |
|---|---|---|
| **The Harness** | LLM + tools = agency. Without tools, it is a chatbot. | "Claude can do anything if I ask it well enough." It can only do what it can see and act on through tools. |
| **Context Windows** | Working memory (~200k tokens). Not infinite. Tool results accumulate. | "More context = better answers." Targeted context + smart sampling beats massive dumps. |
| **Tokens as Currency** | Every token costs money and time. Concise structured prompts save iterations. | "Verbose prompts get better results." Relevant detail + clarity = efficiency. Rambling = waste. |
| **Tool Calls** | Structured requests to execute something external. Results return to Claude. Enables verification. | "Claude will tell me if the code works." Claude does not know unless it can see execution results. |
| **Operator Posture** | Active supervision. You review at each step and intervene before consequential actions. | "I'll ask Claude and come back later." Stay present. Review immediately. Decide next steps. |
| **Cost-Consciousness** | Efficiency as a skill. Planning beats iterating. Tight loops beat loose ones. | "Efficiency is about being cheap." It is about moving fast and shipping quality. |

**Golden rules to repeat:**
- "If you don't understand what Claude is about to do, don't let it do it."
- Tool calls are your audit trail. Every read, write, and execute is traceable.
- Context fills silently. Watch for the model contradicting itself or missing earlier instructions — start a fresh session proactively.

**Teaching structure (35 min):**
- Opening hook (3 min): "Miss these six models and you'll write inefficient code, waste tokens, and blame the AI. With them, you move fast and confidently."
- Six models (5-6 min each): key point → common misconception → check for understanding
- Worked examples from Section 7 (5 min): read one aloud, pause, ask "what went wrong / what went right?"
- Exercise from Section 8 (5-10 min): SECTION A together as a class, B and C individually or as homework

**Live demo (if Claude Code is available):**
- Ask Claude to read a file (show the tool call)
- Ask Claude to write a file (show the tool call)
- Ask Claude to run a command (show the tool call)
- Narrate: "Notice — Claude is not guessing. It is seeing. It is acting. It is verifying."

### Hands-On Activities

1. **Harness demo** — Ask chatbot to rename a folder. Ask Claude Code the same question in a project folder. Identify: which response required you to do the work?

2. **Model landscape check** — Go to anthropic.com/claude. Find the current tier names (fast, balanced, powerful). Do they match what the course lists? Pick one task and decide which tier is appropriate. Write one sentence explaining why.

3. **Hallucination / failure mode drill** — Ask Claude: "What is the current price per million tokens for Claude Sonnet?" Then check anthropic.com/pricing. Compare. Ask Claude for its knowledge cutoff. Ask what major models were released after that cutoff. You have just demonstrated all three failure modes.

4. **Context window test** — Start a fresh chat. Say "My name is [name]. Remember this." Have 10-20 exchanges on any topic. Ask: "What was my name?" Observe whether it still knows.

5. **Token efficiency comparison** — Write a vague prompt. Write a structured prompt (task, context, constraints, output format). Count words. Submit both. Which required fewer follow-up iterations?

6. **Operator posture** — Give Claude a vague brief: "Improve my code." Read the result. Give the same task with a specific brief: file name, improvement goal, constraint, success criteria. Compare. Label the vague brief with the supervision failure mode it most resembles.

### Discussion Questions / Knowledge Checks

- "You give Claude a mission without tools. Can it read your actual files? Why not?"
- "You have a 1,000-file codebase. Should you paste all 1,000 files into a prompt?"
- "You're about to send a 500-word rambling prompt to Claude. What should you do first?"
- "Claude says it has verified your code works. Without tool calls, what does that actually mean?"
- "Claude proposes to 'clean up the database by removing duplicate records.' What questions do you ask before approving?"

**Passing bar:** Students should rate themselves 4+/5 on at least 5 of 6 models on the workbook self-assessment.

### Transition to Technical Foundations

Mental models are now loaded. Technical Foundations (M1-M8) is where students apply all six models in hands-on work over 2-3 days. Remind them: the mental models are not a checklist to review once — they should become instinctive. Point them out as they appear in each module.

---

# TECHNICAL FOUNDATIONS

## Module M1: LLM & Prompts

**Estimated duration:** 90 minutes  
**Instructional mode:** Demo + hands-on. Lecture/discussion: 5 min max.

### Learning Objectives

- Distinguish between a user prompt and a system prompt
- Write a clear, specific prompt using the RGCOA structure (Role, Goal, Context, Output, Asks)
- Identify at least one LLM failure mode and explain how to verify for it
- Understand what a context window is and when it becomes a constraint

### Key Concepts to Emphasize

- **RGCOA structure:** Role, Goal, Context, Output, Asks. The Asks element is where you give the model permission to surface uncertainty instead of papering over it. "If you need information I haven't provided, ask me before proceeding. Do not invent facts."
- Specificity wins. Vague prompts get vague answers. Show both and let the difference speak.
- Typing "You are a [role]" in the user turn is persona injection — visible in chat history. A true system prompt is loaded by the platform before the conversation. The distinction matters later when students configure harness files.
- Nondeterminism: the same prompt submitted twice produces different output. Do not treat one output as "the answer" for high-stakes work.
- Context windows: for Claude, roughly 200k tokens. Do not test the limits obsessively — the instinct ("keep focused input") is the deliverable.

**Data hygiene — run this before the first exercise:**
- What never goes in: classified, CUI, PII (name + any identifier), operational planning detail, credentials, personnel records.
- CUI defined: FOUO markings are being replaced by CUI across the federal government. If it carries any marking, or describes real people, real units, real operations, or real capabilities, it does not get pasted into a consumer AI tool.
- Bracketed placeholder technique: replace specifics with [NCO], [LOCATION], [UNIT], [DATE]. The model does not need the real identifier to help.
- **Scrub drill:** Provide a realistic-but-fabricated document (soldier's name and rank, unit designation, base name, grid coordinate, date, marking). Students produce a paste-safe version using bracketed placeholders. Debrief: what was removed, what category, can the model still accomplish the task with scrubbed input?

### Hands-On Activities

1. **Ice-breaker prompt** — "What is the weather?" vs "I live in [city]. What outdoor activities are good this time of year?" Observe how specificity changes the answer. Write a one-paragraph reflection.

2. **System prompt experiment** — Same interview question answered by "a Marine Corps drill sergeant" and "a kindergarten teacher" (use "You are a…" at the start). Screenshot both. Note 3 differences in tone, vocabulary, and detail level.

3. **Clarity exercise** — Given a list of 3 vague prompts, rewrite each using RGCOA. Submit both versions. Save a before/after comparison.

4. **Context window boundary** — Paste a 10,000-word document. Ask Claude questions about it. Note where quality starts to degrade.

5. **Iterative prompting** — Start with a vague prompt. Iterate 3 times, refining based on what missed. Track what changed each round.

**Deliverable:** 5 well-written prompts, one per learning objective.

### Discussion Questions / Knowledge Checks

- "You ask the model to 'write a report.' It produces something generic and too long. What is the most effective fix?"
- "You run the same prompt twice in two separate chats and get different answers. What is the most accurate explanation?"

**Common confusions:**
- "Isn't it just a chatbot?" → "It is more like a sophisticated next-word predictor. You are steering it with prompts."
- "Will it always give the same answer?" → "No. It uses probability. Temperature is real."
- "How much context can I use?" → "Roughly 200k tokens for Claude. If a document is longer than a short novel, you might hit the limit."

**Timing note:** If running long, skip the context window experiment and state the number directly.

### Transition to M2

Students now understand the LLM side. M2 is the terminal — the interface the agent uses on their machine. The skills are directly connected.

---

## Module M2: Terminal Basics

**Estimated duration:** 120 minutes  
**Instructional mode:** Guided labs. Instructor demos, students follow.

### Learning Objectives

- Navigate directories and list files from the terminal
- Create, copy, move, and delete files and folders
- Understand absolute vs relative paths
- Use command flags and look up unknown flags with `--help`
- Pipe and redirect command output
- Stop a running command with `Ctrl+C`

**Windows students:** Use WSL, not native PowerShell. Install: open PowerShell, run `wsl --install`. All exercises assume a Linux/Unix environment. Windows files are accessible inside WSL at `/mnt/c/Users/YourName/`. Path conversion rule: `C:\Users\Jake\Documents` → `/mnt/c/Users/jake/documents` (backslashes to forward slashes, drive letter lowercase after `/mnt/`). VS Code + WSL extension: from a WSL terminal, type `code .` to open VS Code with full WSL integration.

### Key Concepts to Emphasize

- The terminal is just another interface. Same files, same folders — words instead of mouse clicks.
- **`Ctrl+C` is the most important shortcut.** Name it explicitly and drill it before anything else. Students need this reflex.
- Path confusion (relative vs absolute) is where ~30% of students stall. Practice this 5+ times.
- "Command not found" means it is not on PATH. `which <command>` to check. Restart terminal after installs.

### Hands-On Activities

1. **Orientation walk** (15 min) — Start in home directory. Navigate to 5 different locations. `pwd` after each move. `ls` to see what is in each folder. Create a simple text file in one.

2. **File manipulation sprint** (25 min) — Create `projects/acc-prep/module-2/` folder structure. Create 3 text files. Copy one to another location. Rename a file. Delete a file. List the final structure.

3. **Path puzzle** (20 min) — Given a file at `/home/user/projects/claude/config.txt`, write the absolute path, the relative path from `/home/user/`, and the relative path from `/home/user/projects/`. Navigate using those paths to verify they work.

4. **Help system** (15 min) — Use `man ls`, `ls --help`, `help cd` to answer: "What does the -l flag do? What about -a? How do you list by file size?" Build a help reference card for `ls`, `cd`, `mkdir`, `cp`, `mv`.

5. **Piping and redirection** (25 min) — Create a text file with 10 lines. List files and save output to a file. Count files in a directory using piping. Append text to a file.

6. **Real-world scenario** (20 min) — "You have a folder with 50 files. Find all `.txt` files, sort by date, move to an archive folder." Create the fake scenario, then solve it.

**Deliverable:** Terminal transcript showing all 6 exercises completing.

**Common stuck points:**
- "Permission denied" → redirected to system files. Move to a safe sandbox folder.
- "No such file or directory" → wrong folder or wrong path. `pwd` and `ls` to verify location.
- Relative path confusion → practice 5 times in a row with different folders.

**Timing:** This is the slowest module for absolute beginners. Do not rush.

### Transition to M3

Students can operate in the filesystem. M3 introduces version control — the logbook that records every change the agent makes to their files. The "why" was already loaded in Terminal Basics. Now come the commands.

---

## Module M3: Git Basics

**Estimated duration:** 120 minutes (split: 60 min local, 60 min remote + conflicts)  
**Instructional mode:** Guided labs. Demo first, students follow.

### Learning Objectives

- Initialize a local Git repository
- Stage changes, commit with clear messages, view history
- Create, switch, and merge branches
- Clone a repository and push changes to GitHub
- Recognize and resolve a simple merge conflict
- Write meaningful commit messages
- Create a `.gitignore` before the first commit

### Key Concepts to Emphasize

- Git is a time machine. Every commit is a snapshot you can jump back to.
- **`.gitignore` must be created before the first commit.** If a credential file is committed first, adding it to `.gitignore` later does NOT remove it from history. The file remains recoverable. This is the OPSEC enforcement layer for git. State this clearly, state it early.
- Minimum `.gitignore` entries for any project: `.env`, any credential files, `.DS_Store`, `__pycache__/`, `.venv/`
- Merge conflicts: students panic. Walk through one example slowly, then make them create a practice conflict. It gets comfortable fast.
- Pull requests: a PR is how you review agent-produced changes before they touch main. When an agent creates changes on a branch, the PR diff is your verification checkpoint.

### Hands-On Activities

1. **Your first repository** (20 min) — Create folder, `git init`, create `README.md`, stage, commit, view log, make changes, stage, commit, view diff.

2. **Branching sprint** (20 min) — Create a branch `feature/add-content`, make changes, commit, switch back to main, verify file is unchanged, merge, delete the branch.

3. **Cloning and pushing** (20 min) — Clone a public repo. Create your own GitHub repo, clone it, make changes, push successfully. Verify on GitHub.

4. **Merge conflicts** (25 min) — Create a repo with a file. Create two branches from main, each modifying the same line. Merge one (succeeds). Merge the other (conflict). Resolve manually. Complete the merge.

5. **Commit messages** (15 min) — Given bad examples ("fix stuff", "update"), and good examples ("Add authentication logic to login form"), write 5 commit messages for provided scenarios. Verify: present tense, action-focused, informative.

6. **`.gitignore`** (25 min) — Create a repo. Create `.gitignore` first. Add `.env`, `node_modules/`, `*.log`. Verify ignored files do not appear in `git status`.

7. **Pull request** (20 min) — Create a branch, make changes, push the branch, open a PR using `gh pr create`. Review the diff in GitHub web interface. Merge from the GitHub interface.

**Deliverable:** GitHub repo with 5+ commits, successful push, `.gitignore` in place.

**Common stuck points:**
- "fatal: origin already exists" → `git remote -v` to check, `git remote remove origin` if needed.
- Authentication fails → `gh auth status`. If not logged in, `gh auth login`.
- "I lost my commits!" → They did a `git reset --hard`. Reassure: commits are still there via `git reflog`. This is advanced — do not open it now. Prevention: do not do that.

### Transition to M4

Students can track changes to their files. M4 is Markdown — the plaintext format they will use everywhere: READMEs, documentation, prompts, commit messages. This is the language of the tools they are learning.

---

## Module M4: Markdown

**Estimated duration:** 90 minutes  
**Instructional mode:** Show (demo in VS Code) → student practice.

### Learning Objectives

- Write a properly formatted Markdown document with 5+ syntax elements
- Follow the critical spacing rules (# space, blank lines before lists and code blocks)
- Write Markdown in VS Code, not Word or Google Docs
- Create tables, code blocks, and task lists

### Key Concepts to Emphasize

- Markdown is the lingua franca of developers. Used in READMEs, documentation, prompts, static site generators, and slides.
- **Critical spacing rules — most beginner errors live here:**
  - Space required between `#` and heading text
  - Blank line required before any list
  - Blank line required before a fenced code block
  - Tables require both a header row and a separator row (`|---|---|`)
- Do not write Markdown in Word or Google Docs. Auto-replaced smart quotes and em-dashes break code blocks and inline code silently.
- Show first: open a raw `.md` file (ugly), then toggle preview (formatted). "Markdown is the source, preview is the output."

### Hands-On Activities

1. **Markdown anatomy** (15 min) — Read a well-formatted markdown file. Identify all syntax. Recreate from scratch with 10+ different syntax elements.

2. **Personal README** (20 min) — Write a Markdown file: heading, bullet list, link, bold/italic, code block. Fields: name, role, skills, interests, favorite terminal command. Commit to git.

3. **Code blocks with syntax** (15 min) — Create code examples in at least 3 languages with proper syntax highlighting (` ```python `, ` ```bash `, ` ```javascript `).

4. **Tables** (15 min) — Create a table comparing features of 3 tools. Create a second table for a simple project plan. Practice alignment.

5. **Documentation project** (20 min) — Document a simple process in Markdown: main heading, sections (h2), numbered steps, code blocks, table of contents. Target: 300-500 words.

6. **YAML frontmatter** (5 min) — Add `---title/author/date---` frontmatter to the README.

**Deliverable:** One complete Markdown document using 5+ syntax elements.

**Common confusions:**
- "Can I mix HTML?" → Yes, but stick to Markdown unless you need HTML.
- "Tables are annoying." → True. Show a table generator online, or accept the slightly ugly raw format.

### Transition to M5

Students can document their work. M5 introduces programming concepts — the logic layer underneath the code Claude writes. Even non-coders need this module: it covers problem-solving and debugging mindset, not just syntax.

---

## Module M5: Programming Concepts

**Estimated duration:** 120 minutes  
**Instructional mode:** Pseudocode first. Always. Code is translation of logic, not the logic itself.

### Learning Objectives

- Write pseudocode before writing real code
- Understand variables, conditionals, loops, and functions
- Read a buggy snippet and identify the error type
- Write a working function with a clear name and documented purpose

### Key Concepts to Emphasize

- **Pseudocode first.** If students can think through the logic, syntax is just typing. Enforce this rigorously. Do not let students open a code editor before they have written pseudocode.
- Programming is problem-solving, not math. Logic > algebra.
- Common misconceptions:
  - "I have to memorize syntax." → No. Look it up every time. Real developers use `--help` and documentation constantly.
  - "Programming is for 'math people.'" → False. It is problem-solving.
- Debugging mindset: "What does the error message say?" and "What did you expect vs. what happened?" — not "it's broken."
- Use JavaScript (recommended for accessibility with Node.js in browser/terminal) or Python. The goal is concepts, not language mastery.

### Hands-On Activities

1. **Variables and types** (15 min) — Pseudocode: store name, age, whether you code; calculate next year's age; combine name and age in a sentence. Then implement in JavaScript/Python.

2. **Control flow: if/else** (20 min) — Scenario: coffee machine pricing by size. Write pseudocode with if/else logic. Implement. Test with different inputs.

3. **Loops** (20 min) — Print numbers 1-10. Print "I will learn to code" 5 times. Sum all numbers 1-100. Loop through an array of words.

4. **Functions** (20 min) — Write: greeting function, sum function, password length check, vowel counter.

5. **Debugging** (20 min) — Given 5 buggy snippets (syntax errors, logic errors, off-by-one), read, identify the bug, fix it, test. Annotate what was wrong.

6. **Pseudocode planning** (25 min) — Scenario: grade calculator. Input: test scores. Output: average + letter grade. Write pseudocode first. Implement. Test edge cases.

**Deliverable:** 3 small programs (a greeting function, a conditional, a loop). Logic correct, readable, commented.

**Common stuck points:**
- "I don't understand variables." → Box analogy: "A variable is a labeled box. You put data in, label it, take data out later."
- "What's the difference between = and ==?" → "Single = assigns. Double == compares."
- "Infinite loop" → They forgot the stopping condition. Check the loop boundary.

### Transition to M6

Students understand the code layer. M6 is tool setup — getting Claude Code, GitHub, and VS Code running and authenticated so M7 and M8 can proceed. This module has the most blocking issues. Test your environment before class.

---

## Module M6: Developer Tools

**Estimated duration:** 90 minutes  
**Instructional mode:** Lab + troubleshooting. This module has the most blocking issues. Test your environment thoroughly beforehand.

### Learning Objectives

- Install and run Claude Code (`claude --version` passes)
- Authenticate with GitHub CLI (`gh auth status` passes)
- Have VS Code installed with preferred extensions
- Understand `.env` files and why they must not be committed

### Key Concepts to Emphasize

- You need a toolbox. Every tool works together: Claude writes code, git tracks it, GitHub stores it, VS Code edits it.
- **`.env` files:** Never commit. Never under any circumstances. This is the OPSEC enforcement layer for credentials. Show `.gitignore` exclusion explicitly.
- Authentication: recommend HTTPS for beginners. SSH is fine for advanced students.
- "Command not found" means it is not on PATH. Restart terminal after installs.
- Windows PATH: Windows does not auto-update PATH after install. Restart the terminal, or restart the computer.

### Hands-On Activities

1. **Install Claude Code** (15 min) — `claude --version`. Run `claude`. Interact. Confirm it connects.

2. **GitHub CLI** (20 min) — Install `gh`. Authenticate: `gh auth login` (choose HTTPS). Verify: `gh auth status`. Clone a test repo.

3. **VS Code setup** (15 min) — Install VS Code. Open a folder. Install 2-3 extensions (Markdown Preview, Git Graph, Prettier). Create a simple file and view it.

4. **Environment variables** (20 min) — Create a `.env` file with sample variables. Show how `.gitignore` excludes it. Explain: these are settings for your app. They never get committed.

5. **Verification sprint** (15 min) — Run and screenshot: `claude --version`, `node --version` (or `python --version`), `git --version`, `gh --version`, `code --version`. All should return version numbers.

6. **Troubleshooting practice** (5 min) — "Command not found" → `which <command>` + `echo $PATH`. "Permission denied" → likely needs `chmod +x`. "Module not found" → missing dependency, need to install.

**Deliverable:** Verification checklist showing all tools installed and authenticated.

**Common stuck points:**
- Windows PATH → restart terminal after install
- GitHub auth fails → check they have a GitHub account and `gh` is installed
- Node/Python not installed → install Node (simpler for most cohorts)

### Transition to M7

Toolbox is in place. M7 is context files — teaching Claude Code what the project is and how the operator works. This is where agentic work goes from generic to specific.

---

## Module M7: Context Files — CLAUDE.md and me.md

**Estimated duration:** 90 minutes  
**Instructional mode:** Template + iteration.

### Learning Objectives

- Write a CLAUDE.md that specifies project scope, rules, and constraints
- Write a personal me.md with communication preferences and working style
- Confirm Claude Code reads the context files and references them in conversation
- Understand how Markdown formatting affects how the model reads instructions

### Key Concepts to Emphasize

- CLAUDE.md = the instruction manual for the project. me.md = the instruction manual for the operator. Together, they tell Claude Code how to help without being re-briefed every session.
- Every element in CLAUDE.md is Markdown syntax from M4. If formatting breaks — a header without a space, a list without a blank line — the model reads a wall of text instead of structured instructions.
- The most common CLAUDE.md failure: it is too generic and does not constrain anything. Push students to specify: "What SHOULD Claude NOT modify? What is out of scope? What is off-limits?" Real constraints are powerful.
- The `.claude/` folder is where context files live. Claude Code reads them at the start of every session.

### Hands-On Activities

1. **CLAUDE.md anatomy** (15 min) — Read the provided example CLAUDE.md. Annotate each section and what behavior each element produces. Identify: project name, goals, constraints, deliverables.

2. **Write your me.md** (20 min) — Fields: name and role, decision style (fast/slow, risk tolerance), communication preference (BLUF, examples, details), what you value, how you prefer Claude to interact.

3. **Write a project CLAUDE.md** (25 min) — Scenario: simple task manager for field teams. Write a CLAUDE.md including: what the project is, what it is NOT (scope boundary), key constraints, files Claude can modify, files Claude cannot modify, success criteria.

4. **Conflict resolution matrix** (15 min) — When requirements conflict, which wins? Build a matrix for the scenario project: Speed vs Security, Simplicity vs Features, Completeness vs Time-to-delivery.

5. **Set up project context** (10 min) — Create a folder. Create `.claude/` inside it. Add CLAUDE.md and me.md. Run Claude Code in that folder.

6. **Context verification** (5 min) — Ask Claude about the project. It should reference your CLAUDE.md. Observe how context influences its behavior.

**Deliverable:** CLAUDE.md + me.md for a real or hypothetical project. Rubric: clarity, completeness, enforceability, practical usefulness.

**Common stumble:** Students write generic CLAUDE.md that does not constrain anything. Fix: "What should Claude NOT modify? What is out of scope?" Push for real constraints.

### Transition to M8

All prerequisites are in place. M8 is the capstone — plan, build, commit, push. Remind students: the supervisor loop (delegate, verify, own) is the frame for the entire capstone, not the polish.

---

## Module M8: Capstone Project

**Estimated duration:** 180 minutes (can span across Day 2 into Day 3)  
**Instructional mode:** Mentored project. Coach, do not give answers.

### Learning Objectives

- Integrate all 7 prior modules into one working project
- Practice the full workflow: plan → code → commit → push
- Troubleshoot real problems independently
- Demonstrate the supervisor loop: delegate, verify, own

### Key Concepts to Emphasize

- Not a tutorial or a code-along. A real thing that does something useful, shipped to GitHub.
- Optimize for the loop, not the polish. A checked rough artifact beats an unchecked polished one.
- Coaching phrases (do not give direct answers):
  - "What does the error message say?"
  - "Can you draw what this should do?"
  - "What would you do if I wasn't here?"
  - "That's good progress. What's next?"
- Scope discipline: "Can you demo this in 2 minutes? If not, it's too big."

**Three paths (student choice):**
- **Path A (CLI tool):** Takes input from user or file, processes with logic, outputs result, basic error handling, documented, 3+ commits. Tech: JavaScript (Node.js) or Python.
- **Path B (Web app):** HTML + CSS + JavaScript, takes user input, does something with it, runs locally, documented, 3+ commits.
- **Path C (API integration):** Calls a free public API, handles errors, displays results, documented, 3+ commits. Tech: Node.js + fetch or Python + requests.

**Workflow (all paths):**
1. **Plan** (20 min) — One-paragraph description. List 3-5 features. First commit: "Initial project plan."
2. **Setup** (20 min) — Create `.claude/` with CLAUDE.md and me.md. Initialize git. Create basic file structure. Commit: "Project setup."
3. **Build Phase 1** (60 min) — Core functionality first. Use Claude Code to help. At least one commit per feature.
4. **Test and iterate** (40 min) — Use the tool. Find and fix bugs. Ask Claude to help improve error handling or efficiency. Commit each improvement.
5. **Document** (20 min) — Write README.md: what it does, how to use it, requirements. Add comments to complex code. Final commit: "Update documentation."
6. **Push to GitHub** (10 min) — Verify all commits are local. Push. Verify on GitHub.

**Checkpoint moments (formative assessment):**
- After planning (20 min): "Tell me in one sentence what you're building."
- After setup (40 min): "Show me your folder structure. What's in each file?"
- After first feature (100 min): "Does it run? Show me it working."
- After iteration (140 min): "What did you change after testing? Why?"
- After push (170 min): "Show me your GitHub repo with your commits."

**Deliverable:** GitHub repo with 5+ commits, README, working code.

**Assessment rubric:**
| Criterion | Weight |
|---|---|
| Code works | 50% |
| Documented | 20% |
| Commits meaningful | 15% |
| Iterated based on feedback | 10% |
| Polish (readable, no debug statements) | 5% |
| Bonus: deployment, tests, second feature | +5% |

**Common stumbles:**
- Under-scope (too simple) or over-scope (too big). Calibrate with: "Can you demo this in 2 minutes?"
- Students wait for instructions instead of troubleshooting. Redirect: "What does the error say? What did you expect?"

---

# COURSE AT A GLANCE

| Module | Duration | Summary |
|---|---|---|
| **Bedrock: AI Literacy** | Multi-week, short daily reps | LLM mental model, failure modes, deliberate prompting, delivery models, data handling hard rules |
| **Bedrock: Personalizing Your AI** | 1-2 sessions | Custom instructions and Projects/memory — stop re-briefing the model every session |
| **Terminal Basics: The Machine** | Multi-week, short daily reps | Filesystem tree, plaintext vs rich text, VS Code orientation |
| **Terminal Basics: The Terminal** | Multi-week, heaviest calendar weight | Navigation, file operations, paths, tab-completion, flags, Ctrl+C, version control concept |
| **Agentic AI: Core Concepts** | 1-2 sessions | Chatbot vs agent, read/write/execute access, engine-harness-operator model, supervisor mindset |
| **Mental Models** | 35 minutes | Six frameworks: Harness, Context Windows, Tokens, Tool Calls, Operator Posture, Cost-Consciousness |
| **TF M1: LLM & Prompts** | 90 minutes | RGCOA prompting, system prompts, hallucination, data hygiene scrub drill, iterative prompting |
| **TF M2: Terminal Basics** | 120 minutes | Navigation, file manipulation, paths, piping, redirection, help system |
| **TF M3: Git Basics** | 120 minutes | Init, commit, branch, merge, push, `.gitignore` before first commit, pull requests |
| **TF M4: Markdown** | 90 minutes | Syntax elements, critical spacing rules, code blocks, tables, write in VS Code not Word |
| **TF M5: Programming Concepts** | 120 minutes | Pseudocode first, variables, loops, functions, debugging mindset |
| **TF M6: Developer Tools** | 90 minutes | Claude Code, GitHub CLI, VS Code, `.env` files, tool verification checklist |
| **TF M7: Context Files** | 90 minutes | CLAUDE.md (project constraints), me.md (operator profile), context verification |
| **TF M8: Capstone Project** | 180 minutes | Full workflow: plan → build → commit → push; supervisor loop is the frame |

**Total Technical Foundations instructional time:** ~15 hours over 2-3 days  
**Critical path:** M1 → M2 → M3 → M5 → M8. Do not skip any module in this sequence.  
**Can run in parallel:** M4 (Markdown) while other modules are sinking in.  
**Must complete before M8:** M5, M6, M7.

---

## Grading Summary

| Module | Artifact | Pass criteria |
|---|---|---|
| M1 | 5 prompts | 4/5 are clear, specific, coherent |
| M2 | Terminal transcript | 8/10 commands correct, navigation successful |
| M3 | Commits + push | Commits have messages, push succeeds, `.gitignore` exists |
| M4 | Markdown doc | 5+ syntax elements, readable |
| M5 | 3 programs | All run, logic is correct |
| M6 | Verification checklist | All tools installed, all version checks pass |
| M7 | CLAUDE.md + me.md | Both complete, coherent, enforceable |
| M8 | GitHub repo | 5+ commits, README, code runs |

**Course completion:** 7/8 modules passed. 8/8 + capstone >80% = Honors.

---

## Quick Troubleshooting Reference

| Symptom | First check | Fix |
|---|---|---|
| "Command not found" | `which <command>` | Not on PATH; restart terminal after install |
| Path confusion | `pwd` + `ls` | Navigate to a known location and rebuild |
| Git merge conflict | `git status` | Edit file, keep your version, `git add`, `git commit` |
| Auth fails | `gh auth status` | `gh auth login`, choose HTTPS |
| Claude Code not connecting | `claude --version` | Reinstall if not found |
| Markdown not rendering | Check extension | Install "Markdown All in One" in VS Code, restart |
| JS/Node error | `node --version` | Install from nodejs.org if missing |

---

**End of Teaching Guide**
