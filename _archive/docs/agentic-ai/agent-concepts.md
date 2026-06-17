# Agentic AI — Core Concepts

**Who this is for:** Someone who has completed Bedrock and Terminal Basics and is ready to understand what it means to give an AI tool real access to their machine.

**What you will leave with:** A clear model of the difference between a chatbot and an agent, why version control matters once an agent can edit your files, and the supervisor mindset that responsible agentic work depends on.

---

## Chatbot vs Agent

**BLUF.** A chatbot gives advice; an agent takes action — the difference is read, write, and execute access to your real files and the terminal you just learned, which is exactly why Terminal Basics existed.

### Why This Matters

This is the payoff module for Terminal Basics. If learning the filesystem and terminal commands felt like a detour, this is where it pays off. Everything the agent does, it does through the filesystem and the terminal. You learned to navigate the terrain so you can supervise someone else navigating it.

### Concepts

Ask a chatbot to rename a folder: it tells you the command. Ask an agent: it renames the folder.

That is the entire difference. The agent has access.

**Three levels of access:**

- **Read.** The agent can look at your files.
- **Write.** The agent can create and modify your files.
- **Execute.** The agent can run commands in your terminal.

The LLM is the engine. A harness with tools is what gives it hands. You are the operator who points it at the right problem and pulls the plug when it heads somewhere wrong. Engine plus harness plus operator — everything in advanced agentic work stacks on this primitive.

!!! warning "Read, Write, Execute Is a Lot of Trust"
    This is not abstract. An agent with write and execute access can create, modify, or delete files on your real machine. You are extending significant trust. The supervisor mindset in the next section is what keeps that from becoming a problem.

??? note "Instructor Note — Make the Connection Explicit"
    Do not assume students connect the dots. Say it out loud: "Every command you learned in Terminal Basics — `pwd`, `ls`, `cd`, `mkdir`, `mv` — that is what the agent runs when it works in your filesystem. You learned to navigate the terrain so you can supervise someone else navigating it." Make the payoff land.

### Hands-On

**Step 1 — The chatbot side.**

1. Open your AI chatbot (Claude web, ChatGPT, or equivalent).
2. Ask it: "Rename the folder 'project' to 'project-v1'."
3. Read the response. Note whether it renamed anything or told you how to rename it yourself.

**Step 2 — The agent side (if Claude Code is available).**

4. Open Claude Code in a project folder.
5. Ask the same question: "Rename the folder 'project' to 'project-v1'."
6. Watch what it does. Does it call a tool? Does it ask for confirmation? Does the folder change on disk?

**Step 3 — Compare.**

7. Write one sentence describing what was different between the two responses.
8. Identify: which response required you to do the work, and which one did the work?

That gap — between advice and action — is the entire definition of an agent.

!!! question "Before You Continue"
    You just asked a chatbot to rename a folder. What would an agent do differently — and what are you trusting it with when it does?

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
- [ ] I understand why Terminal Basics was the prerequisite for this module
- [ ] I can name all three parts of the engine-harness-operator model

---

## Why Version Control Exists

**BLUF.** When an agent can change your files, you want a logbook of every change — what changed, when, and why, with the ability to go back — and that logbook is version control.

### Why This Matters

The agent is about to start editing files. Without version control, one bad run can overwrite work with no way to recover it. This module plants the "why" before the commands, because the commands only make sense when the reason is already loaded.

### Concepts

Every time a file changes, version control records a snapshot: what changed, when, and a note about why. Stored locally on your machine. Every snapshot can be rewound.

Version control is the duty logbook. Every change recorded: what, when, why, who. The agent is about to start making entries in your files; the logbook is how you keep accountability over a teammate who works fast and never sleeps.

**Two layers:**

- **Local logbook.** Your machine keeps the record. You can always rewind to any previous snapshot without needing the internet.
- **Remote copy.** The same history synchronized to a cloud server. Backup — and the mechanism for teammates working on the same files.

No commands today. You are loading the reason. The commands come when you work with git directly.

!!! note "Why Software People Seem to Remember Everything"
    They do not. They have the log. "Who changed this and when?" is a two-second lookup. "What did this file look like last Tuesday?" is one command. The logbook is doing the remembering.

??? note "Instructor Note — Resist Teaching Git Commands Here"
    The concept is the prerequisite; hands-on git work teaches the commands. Overloading now defeats the gentle ramp. If a student asks "how do I actually do this," tell them: "You will do it in the next session. Today you need to know why."

??? note "Instructor Note — Audience Framing"
    For a military audience, the duty logbook framing lands immediately. For a civilian audience, "undo button for your whole project" works better. Read the room.

### Hands-On

No commands today. Do this instead:

1. Think about a file you have edited multiple times over the past month.
2. Ask yourself: "If I needed to see what it looked like three weeks ago, could I?"
3. Ask yourself: "If something went wrong, what would I lose?"

That gap — between what you want to recover and what you can currently recover — is what version control fills.

!!! question "Before You Continue"
    An agent just ran a batch edit on 40 files. You look at one and it is not right. Without version control, what are your options? With version control, what changes?

<div class="quiz-block">
  <p class="quiz-question">Why does version control matter specifically once an agent can edit your files?</p>
  <ul class="quiz-options">
    <li data-correct="false">Agents edit files faster than humans, so you need a backup</li>
    <li data-correct="false">Version control prevents the agent from making mistakes</li>
    <li data-correct="true">The agent can make many changes quickly — version control gives you a complete record and the ability to rewind any of them</li>
    <li data-correct="false">Agents require version control to function</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can explain version control as a logbook of file changes I can rewind
- [ ] I understand why it matters once an agent has write access
- [ ] I can distinguish the local logbook from the remote copy
- [ ] I am not yet expected to know any git commands

---

## The Supervisor Mindset

**BLUF.** You delegate to the agent, verify its work, and own the outcome — the agent is a capable, fast, assumption-prone junior who will confidently fill gaps you did not address, and your job is to command well and check, not to type more.

### Why This Matters

Every failure mode from Bedrock — hallucination, confident-wrong, nondeterminism — applies to agent actions, not just text output. The difference is that agent actions touch real files and real systems. The supervisor mindset is what keeps that from becoming a problem.

### Concepts

**The motivated-junior model.** The agent is a junior teammate with file-system access. Capable. Fast. Willing to fill ambiguity with plausible-sounding assumptions. It will never push back or say "I'm not sure" unless you build that into the prompt. It executes your intent — including the parts you left implicit.

**Three duties of the supervisor:**

1. **Delegate clearly.** Vague intent produces confident but wrong execution. Say what you need, what good looks like, and what is off-limits.
2. **Verify the work.** Check what the agent actually did, not just what it said it did. These are not the same.
3. **Own the outcome.** The capability does not transfer the accountability. You are still the one who signs for the result.

!!! warning "Two Failure Modes to Name and Counter"
    **Blind trust:** "It sounds right." Confident output from an agent is not verified output. Check the work before you act on it.

    **Learned helplessness:** "I can't check this, it's too technical." You do not need to replicate the agent's work. You need to check whether the output makes sense, whether constraints were honored, whether anything looks wrong. That is a human judgment call, not a technical skill.

!!! example "The Delegate-Verify-Own Loop in Practice"
    You ask the agent to reorganize a folder of files by date.

    - **Delegate:** "Move all files with a date in the filename into subfolders organized by year. Do not delete anything. Show me what you plan to do before you do it."
    - **Verify:** Check that files landed where they should. Spot-check three of them. Confirm nothing was deleted.
    - **Own:** If one file landed in the wrong folder, you catch it, fix it, and note what to specify more precisely next time.

??? note "Instructor Note — Reinforce Throughout, Not Just at the End"
    This is the through-line of the entire course, not a capstone topic. Every agentic action in later modules should be framed with the supervisor loop. Students who only hear it once at the end will not carry it forward.

??? note "Instructor Note — Capstone Exercise"
    Optimize the capstone for the loop, not the polish. A finished artifact with no verification is a worse outcome than a rough artifact that was checked. The win is the mindset: delegate, verify, own.

### Hands-On

Give the agent (or chatbot, depending on available tooling) a small real task:

1. Write a clear brief: who you are, what you need, what good output looks like, and what is off-limits.
2. Submit it. Read the output.
3. Verify: does it do what you asked? Did it make any assumptions you did not authorize? Is anything wrong?
4. If something is off, correct it. Identify what you should have specified more precisely.

That loop — delegate, verify, correct — is the whole skill.

!!! question "Before You Continue"
    The agent completed a task and the output looks correct at first glance. What would you check to actually verify it, and how would you know if an unauthorized assumption had been made?

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

### Readiness Check

Before beginning the main course, confirm:

- [ ] I can state the three duties of the supervisor: delegate, verify, own
- [ ] I know the difference between a capable junior and a trustworthy one
- [ ] I have completed at least one delegate-verify-correct loop with a real task
- [ ] I am the commander, not the typist
