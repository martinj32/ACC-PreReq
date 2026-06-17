# The Duty Logbook: Version Control with Git

**Who this is for:** Someone who can navigate the terminal and is about to hand file access to an agent that works fast and never sleeps.

**What you will leave with:** You understand version control as a duty logbook of every change you can rewind, and you have done it for real — a Git repository with five or more commits, a branch you created and merged, a merge conflict you resolved by hand, and a `.gitignore` you wrote *before* the first commit so nothing sensitive ever entered the history.

---

## Why Version Control Exists

**BLUF.** When an agent can change your files, you want a logbook of every change — what changed, when, why, and who — with the ability to go back; that logbook is version control.

### Why This Matters

You just learned to create, move, and rename files from the command line. An agent will do those same operations — at speed, on multiple files, sometimes without asking. The agent is about to start making entries in your files. Without version control, one bad run can overwrite work with no way to recover it. The logbook is how you keep accountability over a teammate who works fast and never sleeps.

### Concepts

Every time a file changes, version control records a snapshot: what changed, when, and a note about why. Stored locally on your machine. Every snapshot can be rewound.

Version control is the **duty logbook**. Every change recorded: what, when, why, who. The agent is about to start making entries in your files; the logbook is how you keep accountability over a teammate who works fast and never sleeps. The same way a watch logs every event so the next shift can reconstruct what happened, Git logs every change so you can answer "who changed this, when, and why" in a two-second lookup.

**Two layers:**

- **Local logbook.** Your machine keeps the record. You can always rewind to any previous snapshot without needing the internet.
- **Remote copy.** The same history synchronized to a cloud server (GitHub). Backup — and the mechanism for teammates working on the same files.

!!! note "Why Software People Seem to Remember Everything"
    They do not. They have the log. "Who changed this and when?" is a two-second lookup. "What did this file look like last Tuesday?" is one command. The logbook is doing the remembering.

??? note "Instructor Note — Audience Framing"
    For a military audience, the duty logbook framing lands immediately. For a civilian audience, "undo button for your whole project" works better. Read the room. Either way, the concept was loaded at the end of the terminal module; this module turns the concept into commands.

### Hands-On

No commands in this section. Load the reason first:

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

- [ ] I can explain version control as a duty logbook of file changes I can rewind
- [ ] I understand why it matters once an agent has write access
- [ ] I can distinguish the local logbook from the remote copy
- [ ] I am ready to turn the concept into commands

---

## Your First Repository: Commit, Log, Diff

**BLUF.** A repository is a folder Git is watching; you stage the changes you want to record, commit them with a message, and Git keeps that snapshot forever — `git add`, `git commit`, and `git log` get you most of the way.

### Why This Matters

The concept is loaded. Now you make entries in the logbook yourself. The three-state model — working directory, staging area, committed — is the one thing that confuses beginners, and doing it by hand a few times is the fastest way past the confusion.

### Concepts

A **repository** (repo) is a folder Git is tracking. Run `git init` inside a folder and Git starts watching it.

**The three states of a change:**

- **Working directory** — your files as they are right now, edited but not yet recorded.
- **Staging area** — the changes you have selected to include in the next snapshot (`git add`).
- **Committed** — a permanent snapshot in the logbook (`git commit`).

The difference between `git add` and `git commit`: `add` selects what goes in the snapshot; `commit` takes the snapshot and writes the logbook entry. A commit is an immutable record of change.

**Commit messages are documentation.** A commit message tells the next person — including future you — what changed and why. Write in present tense, action-focused, informative.

| Command | What it does |
|---|---|
| `git init` | Start tracking the current folder |
| `git status` | Show what has changed and what is staged |
| `git add <file>` | Stage a change for the next commit |
| `git commit -m "message"` | Record a snapshot with a message |
| `git log` | Show the history of commits |
| `git diff` | Show what changed between snapshots |

!!! example "Bad vs Good Commit Messages"
    **Bad:** "fix stuff" · "update" · "work"

    **Good:** "Add authentication logic to login form" · "Fix off-by-one error in pagination"

    A good message is present tense, action-focused, and tells you what changed without opening the file.

!!! tip "Three Commands Get You 90% of the Way"
    `git add`, `git commit`, `git push`. You do not need the whole tool to start keeping a logbook. Add the rest as you need it, and look up flags with `git --help` — real developers do this constantly.

??? note "Instructor Note — The Three-State Model Is the Stumble"
    Students mix up `add` and `commit`. Run `git status` between every step so they watch a change move from working directory to staged to committed. Make the state visible.

### Hands-On — Exercise 1: Your First Repository

1. Create a new folder and `cd` into it. Run `git init`.
2. Create a file (for example `README.md`) with a line of content.
3. Run `git status` — see the file listed as untracked.
4. `git add README.md`, then `git status` again — watch it move to staged.
5. `git commit -m "Add project README"`. Run `git log` to see the entry.
6. Edit the file, then `git add` and `git commit` again. Run `git diff` between commits and read the change.

**Deliverable:** a transcript showing init → commit → log with your annotations.

!!! question "Before You Continue"
    You edited three files but only want to record changes to one of them in this snapshot. Which command controls what goes into the commit, and how?

<div class="quiz-block">
  <p class="quiz-question">What is the difference between `git add` and `git commit`?</p>
  <ul class="quiz-options">
    <li data-correct="false">`git add` saves to GitHub; `git commit` saves locally</li>
    <li data-correct="true">`git add` stages which changes go into the next snapshot; `git commit` records that snapshot in the logbook</li>
    <li data-correct="false">They do the same thing; `commit` is just the newer command</li>
    <li data-correct="false">`git add` creates the repository; `git commit` adds files to it</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can initialize a repo with `git init`
- [ ] I can stage a change with `git add` and record it with `git commit`
- [ ] I can read history with `git log` and changes with `git diff`
- [ ] I write commit messages in present tense, action-focused

---

## Branching, Merging, and Resolving a Conflict

**BLUF.** A branch is a parallel line of work you can experiment on without touching the main version; merging folds it back in; and when two branches change the same line, you resolve the conflict by hand — the exact situation you hit reviewing an agent's work.

### Why This Matters

Branches are how you try something — including something an agent produced — without risking the working version. Merging is how good work comes back in. Merge conflicts are where students panic; walking through one slowly removes the fear, and it is the same skill you use when an agent's branch collides with yours.

### Concepts

**A branch** is a movable pointer to a line of commits. `main` is the default. Create a new branch and your commits go there, leaving `main` untouched until you merge.

| Command | What it does |
|---|---|
| `git branch <name>` | Create a branch |
| `git switch <name>` (or `git checkout <name>`) | Move onto a branch |
| `git merge <name>` | Fold a branch's changes into the current branch |
| `git branch -d <name>` | Delete a merged branch |

**A merge conflict** happens when two branches change the same line of the same file. Git cannot decide which version wins, so it stops and asks you. It marks the conflict in the file with `<<<<<<<`, `=======`, and `>>>>>>>`. You edit the file to the version you want, delete the markers, then `git add` and `git commit` to complete the merge.

!!! tip "Git Is a Time Machine"
    Every commit is a snapshot. You can jump back, try a new idea on a branch, and merge it in when it works — or throw the branch away if it does not. Branches make experimentation free.

!!! warning "Merge Conflicts Are Not an Emergency"
    A conflict is Git telling you it needs a human decision, not that something broke. Walk through one slowly the first time. After one practice conflict, it stops being scary. This is the same review you do when an agent hands you a branch that touches files you also changed.

??? note "Instructor Note — Walk One Conflict Live"
    Students panic at conflict markers. Create the conflict on purpose, project it, and resolve it once slowly. Then have each student create and resolve their own. It gets comfortable fast.

### Hands-On — Exercise 2: Branching Sprint and a Merge Conflict

1. On `main`, create a file and commit it.
2. Create a branch `feature/add-content`, switch to it, make a change, and commit.
3. Switch back to `main`, verify the file is unchanged, then `git merge feature/add-content`. Delete the branch.
4. Now force a conflict: create two branches from `main`, each editing the **same line** of one file.
5. Merge the first branch (succeeds). Merge the second (conflict).
6. Open the file, resolve the conflict markers by hand, `git add` and `git commit` to finish.

**Deliverable:** a transcript showing branch creation, switching, merging, and a resolved conflict, annotated.

!!! question "Before You Continue"
    You merge a branch and Git reports a conflict in one file. What does that mean Git is asking you to do, and what are the three markers it left in the file?

<div class="quiz-block">
  <p class="quiz-question">Why would you do experimental work on a branch instead of directly on `main`?</p>
  <ul class="quiz-options">
    <li data-correct="false">Branches run faster than the main line</li>
    <li data-correct="false">Git requires every change to be on a branch</li>
    <li data-correct="true">A branch lets you try a change in isolation; `main` stays intact until you decide to merge, and you can discard the branch if it does not work</li>
    <li data-correct="false">Branches are the only place merge conflicts cannot happen</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can create a branch, switch to it, and commit on it
- [ ] I can merge a branch back into `main` and delete it
- [ ] I have created and resolved at least one merge conflict by hand
- [ ] I understand a conflict is a request for a human decision, not a failure

---

## .gitignore First, Then Push: The OPSEC Layer

**BLUF.** `.gitignore` tells Git which files to never track — credentials, secrets, junk — and you create it *before* your first commit, because once a sensitive file enters the history, adding it to `.gitignore` later does not remove it.

### Why This Matters

This is the load-bearing OPSEC step of the entire git workflow. The remote copy on GitHub is a backup and a way to collaborate — but it also means anything you commit can leave your machine. The `.gitignore` file is the enforcement layer that keeps credentials and controlled material out of the logbook in the first place. Sequence matters: too late is the same as never.

### Concepts

**`.gitignore`** is a plaintext file listing patterns Git should ignore. Anything matching a pattern never gets staged, never gets committed, never reaches the remote.

Minimum entries for any project:

```
.env
*.key
*credentials*
.DS_Store
__pycache__/
.venv/
node_modules/
```

**The remote.** GitHub hosts a copy of your repo. You `git push` to send commits up and `git pull` to bring teammates' commits down. A **pull request (PR)** is a proposal to merge one branch into another, with a diff you review before the merge — the quality gate for agentic work. When an agent produces changes on a branch, the PR is how you review exactly what it did, line by line, before it touches `main`.

!!! danger "Create .gitignore Before Your First Commit"
    If a credential file is committed first, adding it to `.gitignore` later does **not** remove it from history. The file remains recoverable by anyone with the repo. Create `.gitignore` before the first commit — it is the OPSEC enforcement layer for git, and this is not a recoverable mistake. This is the data-handling bright line from Module 1, enforced at the tool level.

!!! warning "Once It Is in History, It Is in History"
    Deleting the file in a later commit does not erase it — the earlier snapshot still holds it. Rewriting published history is painful and unreliable. The only safe move is to never commit it. That is what `.gitignore` is for, and that is why it comes first.

??? note "Instructor Note — The Two OPSEC Stumbles That Matter Most"
    The `.gitignore`-timing mistake is one of the two highest-consequence stumbles in the course (the other is pasting sensitive data into an unauthorized tool, from Module 1). Run the `.gitignore` step before students make any commit they intend to push. Verify the ignored files do not appear in `git status` before anyone runs `git push`.

### Hands-On — Exercise 3: .gitignore and Push

1. In a new repo, **before any commit**, create `.gitignore` and add `.env`, credential patterns, `.DS_Store`, `__pycache__/`, `.venv/`.
2. Create a fake `.env` file with a dummy secret. Run `git status` — confirm `.env` does **not** appear.
3. Make your real first commit (the README and code, not the secret).
4. Create a GitHub repo (the `gh` CLI: `gh repo create`), then `git push` your commits up. Confirm they appear on GitHub.
5. Optional: create a branch, push it, open a PR with `gh pr create`, review the diff, and merge it. The diff is the agent-review gate.

Across all exercises, build a repository with **five or more commits** and a successful push. That repo is your Module 6 deliverable.

!!! question "Before You Continue"
    You accidentally committed a `.env` file with a real credential and pushed it. Why is deleting the file in a new commit not enough, and what should you have done to prevent this?

<div class="quiz-block">
  <p class="quiz-question">When must you create a `.gitignore` for a credential file to actually be protected?</p>
  <ul class="quiz-options">
    <li data-correct="false">Any time before you push to GitHub</li>
    <li data-correct="false">Right after the first commit, so Git knows the file exists</li>
    <li data-correct="true">Before the first commit — once a sensitive file is in history, adding it to `.gitignore` later does not remove it</li>
    <li data-correct="false">It does not matter; `.gitignore` removes files from history retroactively</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] My `.gitignore` exists before any commit and excludes `.env` and credential files
- [ ] I confirmed ignored files do not appear in `git status` before pushing
- [ ] I can push commits to a GitHub repo and see them online
- [ ] I can open a PR and read the diff before merging — the review gate for agent work
- [ ] My repository has five or more commits and a successful push

---

## Summary

| Concept | Commands | The point |
|---|---|---|
| The logbook | `git init`, `git status` | A repo records every change: what, when, why, who |
| Make an entry | `git add`, `git commit -m`, `git log`, `git diff` | Stage, snapshot, read the history |
| Parallel work | `git branch`, `git switch`, `git merge` | Try changes in isolation; fold the good ones back |
| Resolve conflict | edit markers, `git add`, `git commit` | A conflict is a request for a human decision |
| OPSEC layer | `.gitignore` **before** first commit | Keep credentials out of history — not recoverable if late |
| Remote + review | `git push`, `gh pr create`, the PR diff | Backup, collaborate, and review agent changes before merge |

## End of Module

You have a duty logbook now, and you have used it for real: commits, branches, a resolved conflict, and a `.gitignore` that kept secrets out of the history from the first entry. This is the safety net that makes agentic work survivable — when an agent edits your files at speed, every change is recorded and any change is reversible. With the terrain mapped (Module 5) and the logbook running, you are ready to hand the agent the keys: next, you move from advising a model to commanding one that acts.
