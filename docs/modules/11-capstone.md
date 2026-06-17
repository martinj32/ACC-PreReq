# The Proving Ground: Capstone Build

**Who this is for:** An operator who has worked every prior module and is ready to stop practicing the pieces and prove them — under their own command, on a real artifact.

**What you will leave with:** A working project on GitHub, built and shipped through the full workflow — but more than that, evidence that you commanded an agent correctly: a `CLAUDE.md` that genuinely constrained a real run, one complete delegate-verify-own loop, and a deliberate recovery from a bad agent edit using version control. The artifact is the easy part. The proof is the loop.

---

## The Mission

**BLUF.** The capstone is not a tutorial project — it is the integration of everything: plan, command an agent, verify its work, recover from its mistakes, and ship something real to GitHub, with the grade weighted on *how you supervised the build*, not just on whether the artifact runs.

### Why This Matters

Every prior module taught one skill in isolation. The proving ground is where they combine under realistic pressure — where a vague `CLAUDE.md` lets the agent wander, where an unverified edit slips a bug into your artifact, where a bad agent change has to be rolled back without panic. Anyone can get a demo to run. The course is certifying something harder: that you can put a capable agent to work, stay the accountable supervisor, and produce a product you can sign for. That is the readiness gate to the main course.

### Concepts

Choose **one** build path. Keep it small enough to demo in two minutes — under-scoping is recoverable, over-scoping kills the loop.

- **Path A — CLI tool.** A password-strength checker, a Markdown-to-HTML converter, a task logger. Takes input, applies logic, returns output, handles a basic error.
- **Path B — Web app.** A note-taker, a unit converter, a quote generator. HTML/CSS/JS, takes user input, does something with it, runs locally.
- **Path C — API integration.** A CLI or web app that calls a free public API (weather, jokes, conversions). Authenticates or calls a real endpoint, handles errors gracefully.

**Every path, the same standard:** a README, at least five commits with meaningful messages, no credentials in history, and a working product on GitHub.

!!! tip "The Two-Minute Test"
    If you cannot demo it in two minutes, it is too big. Scope down until the loop — command, verify, ship — fits inside the time you have. A small project built with clean supervision beats an ambitious one you never finished verifying.

??? note "Instructor Note — Scope Is the Whole Game"
    Students fail this module two ways: they over-scope and never reach the verify loop, or they under-scope into something with no decisions for the agent to get wrong. Push them toward a project with at least one real constraint and at least one place the agent could plausibly make a mistake — that is where the graded loop lives.

### Hands-On

1. Pick a path. Write a one-paragraph description and list three to five features.
2. Apply the two-minute test out loud. Cut scope until it passes.
3. Commit the plan: `git commit -m "Initial project plan"`.

!!! question "Before You Continue"
    Your project has to do two things at once: be impressive *and* leave room for you to verify the agent's work inside your time budget. Which one do you protect when they conflict, and why?

<div class="quiz-block">
  <p class="quiz-question">What is the capstone primarily certifying?</p>
  <ul class="quiz-options">
    <li data-correct="false">That you can write production-grade code by hand</li>
    <li data-correct="true">That you can command an agent, verify its work, recover from its mistakes, and sign for the result</li>
    <li data-correct="false">That you can build the most ambitious project possible</li>
    <li data-correct="false">That your project has zero bugs</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## Set the Standing Orders: A CLAUDE.md That Constrains a Real Run

**BLUF.** Before the agent writes a line, you author a `CLAUDE.md` that actually binds it — real scope, real prohibitions, real read-only files — and then you watch it hold during the build, because a context file that constrains nothing is not graded as steering.

### Why This Matters

This is where the Module 10 lesson meets a live agent. A weak `CLAUDE.md` — a warm description with no boundaries — produces an agent that does whatever it wants, and you find out only when it has modified a file it should never have touched. The proving ground requires a context file that *demonstrably* changed agent behavior. That is a NET-NEW capstone requirement: the build is now an agentic deliverable, not a solo coding exercise.

### Concepts

Your capstone `CLAUDE.md` must do real work, not describe the project warmly:

- **Scope boundary.** State what the project is and, explicitly, what it is NOT.
- **Hard prohibitions.** At least two enforceable "never" rules — a file the agent may not modify, an output rule it must obey, a pattern it must not introduce.
- **Modifiable surface.** Name which files the agent may change and which are read-only.
- **Done criteria.** What "working" means, so the agent and you share a finish line.
- **Conflict rule.** When two requirements collide, say which wins (e.g., "security beats speed").

You set up the project context exactly as in Module 10: a `.claude/` folder, your `CLAUDE.md`, your `me.md`. Then you run the agent inside it and confirm it reads them.

!!! example "A Constraint That Earns Its Place"
    Add a read-only file to your project — say `config.example.json` — and a `CLAUDE.md` rule: "Never modify `config.example.json`; it is the reference template." Later, ask the agent to "update the config." A constrained agent refuses or asks; an ungoverned one edits the protected file. That single interaction is graded evidence that your standing orders held.

!!! warning "The Context File Is Sent to the Provider"
    Everything in `CLAUDE.md` and `me.md` ships with every request. The data-handling bright line from Module 1 applies: no real names, no real units, no credentials, nothing above the system's authorization ceiling — not in the project, not in the context files, not in the prompts you give the agent during the build. This is graded (see the rubric).

??? note "Instructor Note — Make the Constraint Testable"
    Require at least one prohibition the instructor can test live: a read-only file, a forbidden output. If a student's `CLAUDE.md` has no rule you can deliberately try to make the agent violate, it has no constraint worth grading. Have them demonstrate the agent honoring the boundary on camera or in a transcript.

### Hands-On

1. Create the project's `.claude/` folder; add your `CLAUDE.md` and `me.md`.
2. Write a `CLAUDE.md` with a scope boundary, at least two prohibitions, a named read-only file, done criteria, and a conflict rule.
3. Add an actual read-only file to the repo that the prohibition protects.
4. Run the agent in the folder. Ask it to summarize the project; confirm it cites your `CLAUDE.md`.
5. Commit: `git commit -m "Project setup with constrained context files"`.

!!! question "Before You Continue"
    You ask the agent to "clean up the config," and your `CLAUDE.md` marks the reference config read-only. What should a correctly governed agent do — and what does it tell you if it edits the file anyway?

<div class="quiz-block">
  <p class="quiz-question">Why must the capstone <code>CLAUDE.md</code> include at least one enforceable prohibition?</p>
  <ul class="quiz-options">
    <li data-correct="false">Because longer context files always perform better</li>
    <li data-correct="false">Because the agent will not start without one</li>
    <li data-correct="true">Because a context file that constrains nothing is not evidence of supervision, and the rubric grades whether it actually steered the agent</li>
    <li data-correct="false">Because prohibitions reduce token cost</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## The Loop: Delegate, Verify, Own

**BLUF.** The graded heart of the capstone is one complete delegate-verify-own loop — you hand the agent a real task, you check the output against the work it claims to have done, and you accept accountability for the result — performed deliberately and documented, not done by reflex.

### Why This Matters

Module 7 named the loop; Module 9 made owning the output an ethical duty. The proving ground is where you execute it on a live build and leave evidence. This is the single highest-weighted item in the rubric, because it is the skill the whole course exists to certify. A finished artifact with no visible verification is an ungoverned build — it fails the loop even if the code runs.

### Concepts

One full turn of the loop, made explicit:

1. **Delegate.** Give the agent a concrete, bounded task with the context it needs — the same deliberate prompting from earlier modules. Vague order, vague result.
2. **Verify.** Do not accept "done" on the agent's word. Read the code it wrote and narrate it back (Module 10 literacy). Run it. Confirm it does what was asked and nothing it was forbidden. Check that the files it claims to have changed are the files it actually changed. This is the "verify after acting" reflex you first met in the terminal and carried through Module 7 — here it is graded.
3. **Own.** You sign for the result. If a claim is wrong, a file is unexpectedly modified, or an edit is subtly off, that is yours to catch and yours to answer for. "The agent did it" is not a defense (Module 9).

!!! danger "Verify Against the Work, Not the Summary"
    An agent will tell you it did the thing. The summary is not the evidence — the diff is. Read what actually changed. The most expensive capstone failures come from accepting a confident "done" without checking the artifact underneath it.

!!! tip "Make the Loop Visible"
    Capture the loop so it can be graded: the task you delegated, the verification you performed (what you read, what you ran, what you checked), and your explicit acceptance. A short transcript or a few commit messages that name the check are enough.

??? note "Instructor Note — Grade the Loop, Not the Artifact"
    The temptation is to grade whether the project runs. Resist it. A working artifact with no evidence of verification scores low; a modest artifact with a clean, documented delegate-verify-own loop scores high. Look specifically for the student checking the diff against the agent's claim — that is the certifiable skill.

### Hands-On

1. **Delegate:** give the agent one concrete build task scoped by your `CLAUDE.md`.
2. **Verify:** read the produced code and narrate it; run it; confirm it does the task and violates no prohibition; check the diff matches the agent's claim.
3. **Own:** if it is correct, commit it with a message that names what you verified (e.g., `Add input validation — verified rejects empty input, no protected files touched`). If it is wrong, send it back with specific correction.
4. Repeat for at least one more feature so the loop becomes a habit, not a one-off.

!!! question "Before You Continue"
    The agent reports "Done — added the feature and updated the tests." What is the difference between trusting that sentence and verifying it, and what exactly do you look at?

<div class="quiz-block">
  <p class="quiz-question">During the verify step, the agent says it changed only <code>app.js</code>, but the diff also shows an edit to a file your <code>CLAUDE.md</code> marked read-only. What does a correct owner do?</p>
  <ul class="quiz-options">
    <li data-correct="false">Accept it — the feature works, so the extra edit is fine</li>
    <li data-correct="false">Commit it and note the discrepancy for later</li>
    <li data-correct="true">Treat it as a failed verification: reject the change, restore the protected file, and re-issue the task with the boundary restated</li>
    <li data-correct="false">Ask the agent whether the edit was necessary and trust its answer</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## The Rewind: Recovering a Bad Agent Edit With Version Control

**BLUF.** You will deliberately let (or cause) the agent to make a bad edit, then recover from it cleanly using git — because the operator who can roll back a mistake works without fear, and the one who cannot is one bad edit from losing the build.

### Why This Matters

Module 6 framed git as the duty logbook — a time machine where every commit is a recoverable snapshot. The capstone makes you use it under the exact condition it exists for: an agent edit went wrong and you need to get back to known-good. This is a NET-NEW capstone requirement and a graded one. It converts git from a concept you practiced into a reflex you can reach for when an agent breaks something mid-build.

### Concepts

The rewind, start to finish:

- **Commit known-good first.** You can only rewind to a snapshot you took. This is why the loop commits after each verified feature — every clean commit is a recovery point. The discipline pays off precisely here.
- **Recognize the bad edit.** During a verify step, the agent introduces something wrong — a broken function, a deleted line you needed, an edit to a protected file.
- **Roll back.** Use version control to return the file (or the working tree) to the last good commit. The bad edit is undone; your verified history is intact.
- **Re-issue.** Hand the task back with a tighter instruction, and run the loop again.

!!! danger "You Can Only Recover to a Commit You Made"
    The rewind only works if you committed known-good state *before* the bad edit. This is the operational reason the delegate-verify-own loop commits after every verified feature. Skip the commits and there is nothing to rewind to. Frequent, verified commits are what make agent supervision survivable.

!!! tip "The .gitignore Caveat Still Applies"
    A rewind recovers tracked files. It does not protect a credential you committed by mistake — that is already in history. The Module 10 rule holds: `.env` in `.gitignore` before the first commit. Version control saves you from bad edits, not from leaked secrets.

??? note "Instructor Note — Make Them Cause the Failure"
    Require a deliberate bad-edit-and-recover, not a hypothetical. Have the student either prompt the agent into a clearly wrong change or hand-break a file, then recover to the last good commit and show the clean working tree. The learning is in feeling that a mistake is reversible — fear of breaking things is what makes junior operators over-cautious or, worse, reckless without a safety net.

### Hands-On

1. Confirm you have a verified, committed known-good state (from the loop).
2. Deliberately induce a bad edit: prompt the agent into a change you know is wrong, or break a file by hand.
3. Confirm the damage — run the project, see it fail or misbehave.
4. Roll back to the last good commit using version control; confirm the working tree is clean and the project works again.
5. Re-issue the task with a tighter instruction and run the loop to a correct result.

!!! question "Before You Continue"
    An agent edit just broke your build, and the last thing you did was commit a working version ten minutes ago. Walk through your recovery. Now answer: what would your options be if you had *not* committed?

<div class="quiz-block">
  <p class="quiz-question">An agent makes a bad edit that breaks your project. What single prior habit determines whether you can cleanly recover?</p>
  <ul class="quiz-options">
    <li data-correct="false">Having used the most powerful model available</li>
    <li data-correct="true">Having committed a verified known-good snapshot before the bad edit</li>
    <li data-correct="false">Having a very detailed README</li>
    <li data-correct="false">Having asked the agent to be careful</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## Ship It: Document, Push, and Sign

**BLUF.** You finish the build the way every real deliverable ends — a clear README, a clean commit history pushed to GitHub, and a final accountable sign-off that the product is yours and verified.

### Why This Matters

Shipping is where the work becomes a product someone else can use and you can be held to. The README is how the next person runs it; the commit history is the record of how you supervised the build; the push makes it real and visible. This is the same data-handling and accountability discipline you have carried since Module 1, applied at the moment of delivery.

### Concepts

- **Document.** A README that states what the project does, how to run it, and any requirements. Comments on any non-obvious logic.
- **Push.** Verify all commits are local, then push to GitHub. Confirm it appears on GitHub.com.
- **Final scrub.** Before the push goes public, re-check: no real names, no credentials, no `.env` in history. The bright line does not relax at the finish line.
- **Sign.** You are vouching for the product. You have read what it does and verified it works — the Module 9 authorship duty, applied to the whole artifact.

!!! warning "No Credentials in History — Final Check"
    Run a last pass for secrets before you push. A credential in a public repository is compromised the moment it lands. If you find one, it is already in history — rotate it and clean the repo; do not just delete the file.

### Hands-On

1. Write the README: what it does, how to run it, requirements.
2. Add comments to any logic that is not self-evident.
3. Final scrub for names, credentials, and `.env` in history.
4. Push to GitHub; confirm the repo is visible with your full commit history.
5. Write a one-line sign-off: what you built, what you verified, and that you stand behind it.

!!! question "Before You Continue"
    You are about to push. What is the last check you run before the repository goes public, and why can it not wait until after?

<div class="quiz-block">
  <p class="quiz-question">You discover an old commit in your history contains a real API key. The file is already deleted in the latest commit. What is the correct response?</p>
  <ul class="quiz-options">
    <li data-correct="false">Nothing — the key is gone from the current version</li>
    <li data-correct="false">Add the file to <code>.gitignore</code> and push</li>
    <li data-correct="true">Treat the key as compromised: rotate it immediately and clean it from history before publishing</li>
    <li data-correct="false">Make the repository private and leave the key in history</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## The Rubric

**BLUF.** The grade is weighted toward supervision — the delegate-verify-own loop and data-handling/ethics discipline carry real points, so a verified modest build outscores an impressive un-supervised one.

This rubric grades *how you commanded the build*, not only whether the artifact runs.

| Criterion | Points | Evidence |
|---|---|---|
| **Delegate-verify-own loop** | 30 | At least one full, documented loop: a delegated task, a real verification of the diff against the agent's claim, and explicit ownership. The certifiable skill. |
| **CLAUDE.md actually constrained the run** | 15 | A context file with a testable prohibition and scope boundary that demonstrably steered (or correctly stopped) the agent. |
| **Git rewind of a bad agent edit** | 15 | A deliberate bad edit recovered to a known-good commit, with a clean working tree shown afterward. |
| **Data-handling & ethics discipline** | 15 | No real names, units, or credentials anywhere; no `.env` in history; an accountable sign-off vouching for the output (Module 9). |
| **Working artifact** | 15 | The project runs and does what it promised, with basic error handling. |
| **Documentation & commits** | 10 | Clear README; 5+ meaningful commit messages; pushed to GitHub. |

**Passing:** 70+ points. **Honors:** 90+ with a clean loop and a recovered rewind.

!!! note "Why the Loop Outweighs the Artifact"
    A flawless artifact built by an unsupervised agent is exactly the failure mode this course exists to prevent. The points follow the supervision because that is the skill that transfers to the main course.

??? note "Instructor Note — Weighting Is Deliberate"
    If a student protests that their app runs perfectly but scored mid-range, the answer is in the weighting: the loop, the constraint, the rewind, and the ethics discipline are 75 of the 100 points. Working code is table stakes, not the certification. Hold the line.

---

## Summary

| Phase | What You Prove | Graded Evidence |
|---|---|---|
| The Mission | Scoped a real, demo-able project | One-paragraph plan, two-minute test passed |
| Standing Orders | A CLAUDE.md that constrains a live agent | Testable prohibition + scope boundary that held |
| The Loop | Delegate, verify, own — on a real build | Documented loop: task, diff-check, ownership |
| The Rewind | Recover a bad agent edit with git | Deliberate bad edit rolled back to known-good |
| Ship It | Deliver and sign for the product | README, clean history pushed, no secrets, sign-off |

!!! note "End of Module"
    You have proven it — not the artifact, the command. You set standing orders an agent obeyed, ran the loop and caught what needed catching, recovered cleanly from a bad edit, and signed for a product that is yours. That is the readiness gate. One module remains: the bridge that names what comes next on the far side of the line of departure.
