# From Advisor to Operator: Commanding an Agent

**Who this is for:** Someone who has worked the terminal and version control and is ready to give an AI tool real access to their machine — and command it responsibly.

**What you will leave with:** A clean mental model of the harness (what turns an engine into an agent), the operator posture that agentic work depends on, how tool calls let you verify instead of trust, and the delegate-verify-own loop you will run on every agentic task for the rest of the course.

---

## The Harness: What Turns an Engine Into an Agent

**BLUF.** A chatbot gives advice; an agent takes action — and the thing that makes the difference is the harness: the tool layer that gives a text-only engine eyes, hands, and a body to read, write, and execute on your real machine.

### Why This Matters

This is the payoff module for the terminal work in Module 5 (Know the Terrain). If learning the filesystem and terminal commands felt like a detour, this is where it pays off. Everything the agent does, it does through the filesystem and the terminal. You learned to navigate the terrain so you can supervise someone else navigating it.

### Concepts

Ask a chatbot to rename a folder: it tells you the command. Ask an agent: it renames the folder. That is the entire difference. The agent has access.

You already met the engine in Module 1 — the LLM is a brain in a jar. It reads text and writes text. By itself it cannot read your files, write to disk, run a command, fetch a URL, or even check what time it is. It also cannot verify its own output against reality. It can only predict the next chunk of text.

**The harness is what makes that engine an agent.** It gives the engine three things:

- **Eyes** — tools to read files, list directories, check git status, fetch URLs, query data.
- **Hands** — tools to write files, create directories, modify code.
- **A body** — tools to execute commands, run tests, move files.

That maps to three levels of access you are granting:

- **Read.** The agent can look at your files.
- **Write.** The agent can create and modify your files.
- **Execute.** The agent can run commands in your terminal.

**The engine-harness-operator stack.** This is the working vocabulary for the rest of the course:

- **Engine** — the LLM. The reasoning brain. Generates, plans, decides.
- **Harness** — the tool layer. Gives the engine reach into files, commands, and external systems.
- **Operator** — you. Direct the mission, approve consequential actions, carry accountability for the result.

The engine cannot act without a harness. The harness cannot direct without an operator. All three are required. Everything in advanced agentic work stacks on this one primitive.

!!! note "The Simple Formula"
    Engine (knowledge, reasoning, generation) + Harness (sensors and actuators) = Agency.

    Without tools, the engine can write a script but cannot run it or read your actual filesystem. With tools, it reads your code, runs the tests, modifies the files, and iterates on the result. That feedback loop — see the world, act, observe, adjust — is what "agentic" means.

!!! warning "Read, Write, Execute Is a Lot of Trust"
    This is not abstract. An agent with write and execute access can create, modify, or delete files on your real machine. You are extending significant trust. The operator posture in the next section is what keeps that from becoming a problem.

??? note "Instructor Note — Make the Connection Explicit"
    Do not assume students connect the dots. Say it out loud: "Every command you learned in Module 5 (Know the Terrain) — `pwd`, `ls`, `cd`, `mkdir`, `mv` — that is what the agent runs when it works in your filesystem. You learned to navigate the terrain so you can supervise someone else navigating it." Make the payoff land.

??? note "Instructor Note — Vocabulary Will Drift"
    External resources use different labels — Anthropic's documentation says "model + tools + orchestration layer." Same concepts, different words. Teach engine-harness-operator as the course's shared language and tell students to expect synonyms in the wild.

### Hands-On

This is the one hands-on where you watch the harness appear. You do it once, here.

1. Open your AI chatbot (Claude web, ChatGPT, or equivalent).
2. Ask it: "Rename the folder `project` to `project-v1`."
3. Read the response. Note whether it renamed anything or told you *how* to rename it yourself.
4. If Claude Code is available — open it in a project folder and ask the exact same question.
5. Watch what it does. Does it call a tool? Does it ask for confirmation? Does the folder change on disk?
6. Write one sentence describing what was different. Which response required you to do the work, and which one *did* the work?

That gap — between advice and action — is the entire definition of an agent, and the harness is what closes it.

!!! question "Before You Continue"
    You give the engine a mission: search 200 field reports for grid `38SMB4521` and return every matching excerpt.

    Without a harness, the engine cannot read the files. It can only generate plausible-sounding excerpts from memory — and you have no way to know which it did. With a harness, it calls tools against the actual files and returns real results you can trace.

    What does that difference mean for how you verify the output?

<div class="quiz-block">
  <p class="quiz-question">In the engine-harness-operator model, what is the harness?</p>
  <ul class="quiz-options">
    <li data-correct="false">The LLM — the reasoning brain that generates responses</li>
    <li data-correct="true">The tool layer that gives the engine access to files, commands, and external systems</li>
    <li data-correct="false">The human operator who directs the mission</li>
    <li data-correct="false">The API endpoint the model connects to</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-block">
  <p class="quiz-question">What is the key difference between a chatbot and an agent?</p>
  <ul class="quiz-options">
    <li data-correct="false">An agent uses a more powerful language model</li>
    <li data-correct="false">An agent can access the internet; a chatbot cannot</li>
    <li data-correct="true">An agent can take action on your real system — read, write, and execute — not just give advice</li>
    <li data-correct="false">An agent remembers previous conversations; a chatbot does not</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can state the one-line difference between a chatbot and an agent
- [ ] I can explain what read, write, and execute access means in practice
- [ ] I can name all three parts of the engine-harness-operator model
- [ ] I understand why the terminal module (Know the Terrain) was the prerequisite for this module

---

## Tool Calls: How You Verify Instead of Trust

**BLUF.** A tool call is a structured request from the engine to an external system — "execute this action and return the result" — and it is what turns "trust me" into "here is the file I read and the test I ran," which is the only way to catch a hallucination before it reaches your product.

### Why This Matters

Every failure mode from Module 1 — hallucination, confident-wrong, nondeterminism — still applies once the engine is an agent. The difference is that now the output can touch real files and real systems. Tool calls are the mechanism that lets you verify an agent's reasoning against reality instead of taking its narration on faith.

### Concepts

A tool call says: "Execute this specific action and return the result." The engine does not run the action itself — it requests that the harness run it, then reasons about what came back.

```
Tool Call 1: read("/home/user/project/app.js")
Result: [file contents come back]

Tool Call 2: run("npm test")
Result: [test output comes back]

Tool Call 3: write("/home/user/project/config.json", "[new content]")
Result: [confirmation the file was written]
```

**The four families of tool calls:**

- **Reading (eyes):** read files, list directories, check git status, fetch URLs, query data.
- **Writing (hands):** create, edit, move, or copy files.
- **Executing (body):** run commands, run tests, call APIs.
- **Thinking:** extended reasoning and multi-step planning before acting.

**Why this enables verification.** Without tools, the engine generates text and you cannot tell whether it is hallucinating, using stale training data, or reasoning correctly from assumptions you never validated. With tools, the engine reads the actual file, makes the change, runs the actual test, and reports a result you can trace.

**The tool-call loop is the core of agentic work:** the engine reasons, acts, observes the result, adjusts, and repeats. Each step produces a real artifact, not a guess.

!!! example "Verification in Action"
    - Agent: "Your function should handle edge case X."
    - You: "How do you know?"
    - Agent: "I read your code (tool call). Line 42 shows this behavior. It is vulnerable to that attack. Here is a fix (tool call: write file)."
    - You: "Does it work?"
    - Agent: "Yes. I ran the tests (tool call: `npm test`). All pass."

    That is the difference between a guess and a verified action.

!!! tip "Tools Are Your Audit Trail"
    Every tool call is a verifiable action. The agent read *that* specific file. Ran *that* specific test. Wrote *that* specific content. You can trace every step. That is not possible with pure text generation — and it is what makes an agent's product defensible.

??? note "Instructor Note — Connect to the Module 1 Failure Modes"
    Students learned hallucination, confident-wrong, and nondeterminism as text problems. Reframe them here as *action* problems: an agent can hallucinate a file path, confidently run the wrong command, and produce a different plan on a second run. Tool calls are how the operator catches all three before they cause damage.

### Hands-On

1. In Claude Code, ask: "What is in my current directory?" Watch it call the list tool and return real results — not a guess.
2. Ask: "Read [name a specific file in your project]." Watch it read the actual file.
3. Ask it to make a small edit. Before it writes, ask: "What exactly are you going to change, and why?" Verify before you approve.

You are tracing the tool-call loop live. Every action is visible. That is the audit trail.

!!! question "Before You Continue"
    An agent tells you it has verified that your export script produces correctly formatted output.

    In scenario one, it reviewed an output description you pasted and said it looks correct. In scenario two, it called a read tool on the actual output file and checked it against the template.

    Which scenario gives you a defensible product? Why?

<div class="quiz-block">
  <p class="quiz-question">What is the primary reason tool calls make agent behavior more trustworthy?</p>
  <ul class="quiz-options">
    <li data-correct="false">Tool calls force the model to use lower temperature settings</li>
    <li data-correct="true">They let the agent verify its reasoning against actual system state instead of generating from memory</li>
    <li data-correct="false">They prevent hallucinations by blocking uncertain outputs</li>
    <li data-correct="false">They reset the context window between steps</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can explain what a tool call is in one sentence
- [ ] I can name the four families of tool calls: read, write, execute, think
- [ ] I understand why tool calls enable verification and an audit trail
- [ ] I know that an action narrated is not the same as an action verified

---

## The Operator Posture: Delegate, Verify, Own

**BLUF.** You delegate to the agent, verify its work, and own the outcome — the agent is a motivated junior with filesystem access who will confidently fill any gap you leave, and your job is to command well and check, not to type more.

### Why This Matters

The agent is powerful, but it cannot read your mind, does not know your constraints, cannot test in your environment, and has no judgment about tradeoffs. You have all of those. The operator posture is what positions your judgment at the point where it matters — before a consequential action executes.

### Concepts

**The motivated-junior model.** The agent is a junior teammate with filesystem access — a motivated PFC who has been handed a mission. Capable. Fast. Eager. And it will execute confidently on an ambiguous brief rather than stop to ask. It will never push back or say "I'm not sure" unless you build that into the prompt. It executes your intent, including the parts you left implicit.

**Human in the loop** means a human is positioned to review and approve consequential actions *before* they execute. You are the decision point the loop depends on — not a passive observer. Active supervision is the correct posture for agentic work. Delegating-and-stepping-away is not.

**Three duties of the operator:**

1. **Delegate clearly.** Vague intent produces confident but wrong execution. Say what you need, what good looks like, and what is off-limits.
2. **Verify the work.** Check what the agent actually did, not just what it said it did. These are not the same.
3. **Own the outcome.** The capability does not transfer the accountability. You are still the one who signs for the result.

!!! warning "Two Failure Modes to Name and Counter"
    **Blind trust:** "It sounds right." Confident output from an agent is not verified output. Check the work before you act on it.

    **Learned helplessness:** "I can't check this, it's too technical." You do not need to replicate the agent's work. You need to check whether the output makes sense, whether constraints were honored, whether anything looks wrong. That is a human judgment call, not a technical skill.

The supervision loop breaks down in three recognizable ways:

- **Over-trust.** You ask for a sweeping change and do not look for hours. When you review, there are twenty breaking changes you never expected. *Fix: review after each major step; have the agent show changes before committing.*
- **Under-involvement.** You ask a vague question and the agent burns tokens guessing. You iterate ten times without getting what you meant. *Fix: be specific — name the file, the goal, the constraint, and what success looks like.*
- **Automation fallacy.** You chain build-test-deploy and one step fails silently. Broken code ships. *Fix: verify intermediate results; put a check between each consequential action.*

!!! danger "If You Don't Understand It, Don't Approve It"
    If the agent says "I'll refactor the database schema" and you do not understand the change, ask it to explain first. Review before execution. You are the operator. You are responsible. If you do not understand what the agent is about to do, do not let it do it.

!!! tip "The Primary Lever for Steering an Agent Is a Context File"
    The single most effective way to constrain a motivated junior is a standing-orders file the agent reads automatically — `CLAUDE.md`, `me.md`. It is how you bake in "do not delete anything," "always show the plan first," and your unit's conventions without re-typing them every session. You will build these deliberately in **Module 10 — Field Craft**. For now, just know the lever exists.

??? note "Instructor Note — Reinforce Throughout, Not Just Here"
    This is the through-line of the entire course, not a capstone topic. Every agentic action in later modules should be framed with the operator loop. Students who only hear it once will not carry it forward. The "verify after acting" reflex is the one habit allowed to spiral: it is introduced in Terminal, reinforced here, and graded in the capstone.

### Hands-On

Give the agent (or a chatbot, depending on available tooling) a small, real task and run the full loop once.

1. Write a clear brief: who you are, what you need, what good output looks like, and what is off-limits.
2. Submit it. Read the output.
3. Verify: does it do what you asked? Did it make any assumption you did not authorize? Is anything wrong?
4. If something is off, correct it — and identify what you should have specified more precisely.
5. Label your first brief: which failure mode did it most resemble — over-trust, under-involvement, or automation fallacy?

That loop — delegate, verify, correct — is the whole skill.

!!! question "Before You Continue"
    An agent has been running a long session and proposes to "clean up the database by removing duplicate records." It sounds reasonable.

    What do you ask before approving? What could go wrong if you approve without reviewing?

<div class="quiz-block">
  <p class="quiz-question">An agent completes a task and narrates what it did in clear, confident language. What do you do next?</p>
  <ul class="quiz-options">
    <li data-correct="false">Accept the output — confident narration is a reliable signal of correct execution</li>
    <li data-correct="false">Run the task again to confirm consistency</li>
    <li data-correct="true">Verify the actual output against what you asked for — the narration describes intent, not necessarily what happened</li>
    <li data-correct="false">Ask the agent to verify its own work</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-block">
  <p class="quiz-question">Which best describes active supervision when working with an agent?</p>
  <ul class="quiz-options">
    <li data-correct="false">Give the agent a task and check back when it's done</li>
    <li data-correct="true">Review outputs at each step and intervene before consequential actions execute</li>
    <li data-correct="false">Let the agent make all technical decisions while you handle communication</li>
    <li data-correct="false">Configure the agent to run without human review for efficiency</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can state the three duties of the operator: delegate, verify, own
- [ ] I know the difference between a capable junior and a trustworthy one
- [ ] I can name the three ways supervision breaks down and the fix for each
- [ ] I know that context files are the primary lever for steering an agent (full treatment in Module 10)
- [ ] I am the commander, not the typist

---

## Worked Examples: The Operator Loop on Real Missions

**BLUF.** The harness, tool calls, and operator posture are not three separate ideas — they fire together on every real task, and these intel-shop scenarios show the difference between a defensible product and a pulled one.

### Why This Matters

You have the three concepts. Now watch them work as one system on missions that look like your day job: building a summary from sources, searching a pile of reports, and drafting a SITREP. The pattern in all three is identical — ground the work in real files, verify with tool calls, and keep the operator at the decision point.

### Concepts

The examples below each contrast an unsupervised, ungrounded approach with a supervised, tool-grounded one. Read them as templates you will reuse.

!!! example "Example 1 — The Harness Makes Output Traceable"
    **Scenario:** Produce an intelligence summary from a folder of raw source documents. You need to know the output is actually grounded in the sources.

    **Without the harness:** "Write a summary of adversary logistics activity." The engine generates from training data and general inference. You submit the brief. A reviewer flags two claims that are not in your source documents. You cannot trace them. The brief is pulled.

    **With the harness:** "Read the source documents in `/reports/AO-North/` and base the summary only on what is in those files." The agent lists the folder (14 files), reads each, finds 3 have no logistics content, excludes them, and returns a summary with source citations by filename.

    **Why it matters:** The first output may be accurate or hallucinated and you cannot tell. The second is traceable to actual sources — every claim defensible. (~200 tokens plus damage control vs. ~500 tokens and a product you can stand behind.)

!!! example "Example 2 — Smart Sampling Beats a Data Dump"
    **Scenario:** A folder of 500 field reports. You need every mention of grid `38SMB4521`.

    **Bad approach:** Paste all 500 reports (100,000 tokens) and ask it to find every mention. The agent is overwhelmed, loses track, and returns incomplete results with no way to verify coverage.

    **Good approach:** "Search the reports in `/reports/field/` and return every mention of `38SMB4521` with source filenames." The agent runs `find`, then `grep` (7 matching files), reads only those, and reports: "9 mentions across 7 reports. Three are from the same 72-hour window describing the same activity from different collection sources."

    **Why it matters:** The bad approach burns 100,000 tokens with unverifiable coverage. The good approach reads only matching files (~10,000 tokens) with complete, traceable coverage.

!!! example "Example 3 — Operator Supervision Prevents a Bad Product"
    **Scenario:** Draft and format a SITREP from unstructured notes.

    **Without supervision (over-trust):** "Draft a SITREP from my notes." The agent infers details not in the notes to fill gaps. You submit to the operations center. It includes a casualty figure the agent inferred from context — not in your notes, not accurate. Correction required.

    **With supervision:** "Draft a SITREP from my notes in `/notes/0600-update.txt`. Use only information in that file. Flag any required field you cannot fill from the source." The agent reads the file and replies: "Draft complete. I could not fill friendly forces count (Section 3) or next reporting period (Section 6) — both flagged `[REQUIRED — NOT IN SOURCE]`. Do not submit until filled." You confirm the enemy-activity section traces line-by-line to your notes, supply the missing fields, and the agent finalizes with no inferred content.

    **Why it matters:** Over-trust lets the agent fill gaps with plausible inference and you ship inaccurate reporting. Supervision keeps *you* in control of what enters the product; the agent flags gaps instead of inventing answers.

!!! question "Before You Continue"
    You receive an intelligence summary from an agent with three specific claims about adversary activity, all stated confidently. You cannot tell whether they came from source documents the agent read or from training-data pattern-matching.

    What do you do before you include the summary in a product — and which of the three examples above is the template for doing it right?

<div class="quiz-block">
  <p class="quiz-question">You need an agent to review 10 field reports for mentions of a specific location. What is the most defensible and cost-effective approach?</p>
  <ul class="quiz-options">
    <li data-correct="false">Paste all 10 reports into the chat and ask the agent to search them</li>
    <li data-correct="false">Ask the agent to summarize each report individually in 10 separate conversations</li>
    <li data-correct="true">Ask the agent to use tools to search the report files and read only the matching sections</li>
    <li data-correct="false">Use the most capable model available to ensure the best results</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can explain why a tool-grounded summary is defensible and a generated one is not
- [ ] I understand why searching beats pasting for a large collection of files
- [ ] I can describe how supervision stops an agent from inventing content in a product
- [ ] I can name the shared pattern across all three: ground in real files, verify with tools, keep the operator at the decision point

---

## Capstone Exercise: Identify the Mental Models

**BLUF.** Reading a real transcript and naming which models are in play — harness, tool calls, operator posture — is how you prove the concepts are habits and not just vocabulary.

### Why This Matters

You can recite the engine-harness-operator stack. The test is whether you can spot it firing — or failing — in a transcript that looks like work. Naming the models on demand is the bridge from "I read about this" to "I do this."

### Hands-On

Read the three transcript sections below. For each, identify which model(s) are in play and what the developer did right or wrong. Work it before opening the answers.

**[SECTION A]**

Developer: "I have a bug in my payment processing. It's failing silently. Here's the code [pastes 2,000 tokens]. What's wrong?"

Agent: "I see the issue. The `processPayment` function doesn't catch network timeouts. Here's a fix — add a try-catch around the API call."

Developer: "Thanks. I'll test it locally." [Leaves. Tests later. The fix doesn't handle all edge cases.]

**[SECTION B]**

Developer: "There's a bug in payment processing. It fails silently on network timeouts. Read `/src/payment.js` and identify it."

Agent: [reads the file] "Found it. Lines 42–45 don't catch network errors. Here's the fix." [writes the file] [runs `npm test -- payment`] "Tests pass. All edge cases covered: ECONNRESET, ECONNREFUSED, timeout, retry."

Developer: "Great. Merge it."

**[SECTION C]**

Developer: "My user profile page loads in 5 seconds. How do I optimize the queries?"

Agent: "Depends on your schema and queries. Can you share them?"

Developer: [shares schema and the slow query]

Agent: "Missing index on `users.id` and an inefficient join." [reads migration format] [writes a migration] [runs the migration] [runs the benchmark] "Page load: 200ms, down from 5000ms. 25x faster."

Developer: "How long will the migration take in production?"

Agent: "The index is additive — no data movement. Under one second even with millions of rows."

Developer: "Approved. Ship it."

!!! question "Analyze the Transcript"
    1. **Section A:** Which models are being violated? What should the developer have done differently?
    2. **Section B:** Which models are in play? How does the harness change the outcome?
    3. **Section C:** Identify every model and explain each.

??? tip "Model Answers"
    **Section A — Violations.** The harness is unused: the agent generates a fix without reading the file or testing it. No tool calls means no verification — it *guesses* the fix works. Operator posture is broken: the developer is under-involved and does not review before walking away. It is also less efficient — pasting code instead of asking the agent to read the file. What should have happened: "There's a bug in `/src/payment.js`. Fix it and verify with tests" → read → diagnose → write → run tests → report.

    **Section B — Correct use.** The harness is working: the agent read the file (eyes), changed it (hands), ran tests (body), and verified. Tool calls do all the verification. Operator posture is sound: the developer supervised and approved the merge after a real result. Efficient — only the needed file was read.

    **Section C — Full stack.** Smart sampling: the agent reads the schema and the specific query, not the whole database. Operator supervision: the developer asks a clarifying question before approving and only ships after understanding production impact. Tool calls for verification: the migration and benchmark run in a safe environment before deploy. Cost-consciousness: specific questions, targeted fix, tight iteration, no waste.

!!! question "Before You Continue"
    In one sentence each, which model was *most* decisive in turning Section A's outcome around in Section B — and which model carried Section C?

<div class="quiz-block">
  <p class="quiz-question">In Section A, the agent proposes a fix without reading the file or running tests. Which model is most directly violated?</p>
  <ul class="quiz-options">
    <li data-correct="false">Cost-consciousness — the prompt was too short</li>
    <li data-correct="true">Tool calls / the harness — the fix is a guess, never verified against the real file or tests</li>
    <li data-correct="false">Context windows — the file was too large</li>
    <li data-correct="false">None — the agent answered correctly</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can read a transcript and name which models are in play
- [ ] I can spot a violated model and state the fix
- [ ] I can explain how the harness changes an outcome from "guess" to "verified"
- [ ] I am comfortable naming the models out loud during a real session

---

## Summary

| Concept | Core Idea | Why It Matters |
|---|---|---|
| **The Harness** | Engine + tools = agency | Without tools the engine is a brain in a jar. With tools it acts on your real machine. |
| **Engine-Harness-Operator** | Three required parts | The engine reasons, the harness reaches, the operator owns. All three or it breaks. |
| **Tool Calls** | Requests that execute outside the engine | Verification and an audit trail become possible — hallucinations get caught. |
| **Operator Posture** | Delegate, verify, own | You sign for the result. Review before consequential actions. Intervene early. |
| **Delegate-Verify-Own Loop** | Brief, check the real output, fix and learn | The whole skill of commanding an agent, run on every task. |

---

## End of Module

You have moved from advisor to operator. You know what the harness is, how tool calls let you verify instead of trust, and the loop you run on every agentic task: delegate clearly, verify the real output, own the result.

Two forward pointers: the mechanics of tokens, context, and cost — how to spend the agent's "ammunition" — are **Module 8**. The context files that are your primary lever for steering an agent (`CLAUDE.md`, `me.md`) get their full treatment in **Module 10 — Field Craft**.

The "verify after acting" reflex you reinforced here is the habit graded in the capstone. Carry it forward into every session: you are the commander, not the typist.
