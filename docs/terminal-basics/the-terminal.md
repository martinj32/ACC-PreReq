# Terminal Basics — The Terminal

**Who this is for:** Someone who has completed The Machine module and is ready to stop clicking and start typing.

**What you will leave with:** You can navigate the filesystem from the command line, create and move files, use paths and tab-completion, read command help, and stop anything that will not quit. These are the exact moves an agent makes on your machine — you are learning them so you can supervise.

---

## What the Terminal Is (and Why It Is Safe)

**BLUF.** The terminal is a typed way to give the computer the same instructions you used to give by clicking — it is not hacking, it is not dangerous by default, and it feels alien for about an hour before it feels normal.

### Why This Matters

This is where the course gets uncomfortable for some people. If you are wondering why an AI course includes a unit on typing Unix commands — the answer is in the Agentic AI section. The short version: the agent acts through the terminal. You need to understand the terrain it operates on.

### Concepts

A command is a typed instruction. It is the same as a click — it tells the computer to do something. The difference is precision: a click is constrained by what a menu shows you; a command can express anything the machine understands.

The **prompt line** is where your typing goes. It usually ends with a `$` (Mac/Linux) or `>` (Windows PowerShell). When you see that character, the terminal is ready for input.

!!! example "Your First Command"
    Open the terminal. On Windows: search for "PowerShell" or "Terminal" in the Start menu. On Mac: search for "Terminal" in Spotlight.

    Type `date` (Mac/Linux) or `Get-Date` (Windows PowerShell) and press Enter.

    The terminal printed the current date and returned the prompt. That is a command.

!!! warning "Nothing Today Can Hurt the Machine"
    The commands in this module and the next two are read-only and harmless. You are looking at the filesystem, not modifying it. Anything that can cause real damage comes much later, behind heavy framing.

??? note "Instructor Note — Address the Bait-and-Switch Out Loud"
    Name the frustration before a student says it: "Some of you are wondering why an AI course spent two weeks on the command line." Then make the connection explicit: the agent acts through the terminal. The student who does not understand the terminal cannot supervise an agent using it.

### Hands-On

1. Open the terminal on your machine.
2. Sit with the blinking cursor for ten seconds. Name the feeling. Then continue.
3. Type the command to print the current date. Press Enter.
4. Close the terminal and open it again.

That is it. You opened it, ran something, and closed it. The anxiety has a smaller surface area now.

!!! question "Before You Continue"
    You typed a command and saw a response. What is the difference between that and clicking a button in an app? What stayed the same?

<div class="quiz-block">
  <p class="quiz-question">What does a terminal actually do?</p>
  <ul class="quiz-options">
    <li data-correct="false">It connects you to the internet through a secure tunnel</li>
    <li data-correct="false">It runs programs faster than clicking does</li>
    <li data-correct="true">It accepts typed instructions and passes them to the operating system — the same as clicking, without the menu</li>
    <li data-correct="false">It is a special tool only developers have access to</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can open the terminal on my machine
- [ ] I ran one command and read its output
- [ ] I can find the prompt line and know where my typing goes
- [ ] The anxiety is smaller than it was at the start of this module

---

## Navigating: Where Am I, What Is Here

**BLUF.** Three commands cover most of navigation — where am I, what is here, move — and mastering them by typing replaces every click from The Machine module.

### Why This Matters

Getting "lost" in the filesystem is the number-one beginner panic in the terminal. These three commands are the reset button. Know them cold and you can always find your way back to a known position.

### Concepts

| Command | Job | Works on |
|---|---|---|
| `pwd` | Print current location | Mac, Linux, WSL, PowerShell |
| `ls` | List folder contents | Mac, Linux, WSL, PowerShell |
| `cd foldername` | Move into a folder | All |
| `cd ..` | Move up one level | All |

`pwd` — **P**rint **W**orking **D**irectory. Your current location in the tree.

`ls` — **L**i**s**t. Everything in the current folder. Add `-la` (Mac/WSL) for details including hidden files.

`cd` — **C**hange **D**irectory. `cd foldername` moves down; `cd ..` moves up.

!!! example "Walking the Tree"
    ```bash
    pwd              # See where you are
    ls               # See what is here
    cd Documents     # Move into Documents
    pwd              # Confirm you moved
    ls               # See what is in Documents
    cd ..            # Move back up one level
    pwd              # Confirm you are back
    ```

    Walk this sequence on your own machine. These are the exact same moves you did by clicking in The Machine module — same tree, typed instead.

!!! tip "pwd Is Your Reset Button"
    Any time you feel lost in the terminal, type `pwd`. It tells you exactly where you are. You can never be permanently lost if you can always ask "where am I."

??? note "Instructor Note — Reps Over Coverage"
    Same three commands, many short repetitions, spread across several days. Do not introduce file creation yet. One capability at a time. Reps build muscle memory; coverage builds confusion.

### Hands-On

1. Open the terminal. Run `pwd`. Read the path. Find that same location in File Explorer.
2. Run `ls`. Identify three items by name.
3. Run `cd` to move into one of them.
4. Run `pwd` and `ls` again.
5. Run `cd ..` to go back up.

Repeat this cycle until it feels routine.

!!! question "Before You Continue"
    You typed `cd Documents` and then `pwd`. What does `pwd` tell you, and how does it prove you moved?

<div class="quiz-block">
  <p class="quiz-question">You are in the terminal and have no idea where you are in the filesystem. What is the first command you run?</p>
  <ul class="quiz-options">
    <li data-correct="false">`ls` to see what files are nearby</li>
    <li data-correct="true">`pwd` to print your current location</li>
    <li data-correct="false">`cd` to move to a known folder</li>
    <li data-correct="false">Close and reopen the terminal to reset</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can print my current location with `pwd`
- [ ] I can list folder contents with `ls`
- [ ] I can move into and back out of folders with `cd` and `cd ..`
- [ ] I have walked the same tree by clicking (The Machine) and by typing (this module)

---

## Acting: Make, Move, Copy

**BLUF.** Four commands cover most day-to-day file work — make a folder, make a file, copy, move — the same actions from The Machine module, now typed.

### Why This Matters

Navigation got you to the position; now you act on it. This is where the terminal goes from "I can look around" to "I can do things." These four commands are the ones an agent uses most when it works in your filesystem.

### Concepts

Every action you take, you confirm. You do not assume the round landed — you check the target. The habit starts here.

=== "Mac / WSL / Linux"
    | Command | What it does |
    |---|---|
    | `mkdir foldername` | Make a new folder |
    | `touch filename.txt` | Make a new empty file |
    | `cp source destination` | Copy a file |
    | `mv source destination` | Move or rename a file |

=== "Windows (PowerShell)"
    | Command | What it does |
    |---|---|
    | `mkdir foldername` | Make a new folder |
    | `New-Item filename.txt` | Make a new empty file |
    | `cp source destination` | Copy a file |
    | `mv source destination` | Move or rename a file |

!!! example "Build Something From Scratch"
    ```bash
    mkdir project
    cd project
    touch notes.txt
    ls                              # Verify notes.txt is there
    mkdir drafts
    cp notes.txt drafts/notes-copy.txt
    ls drafts                       # Verify the copy landed
    mv notes.txt notes-v1.txt
    ls                              # Verify the rename happened
    ```

    After each command, run `ls` to confirm the change happened. That is the verify-after-acting habit — build it now.

!!! warning "No Deletion Yet"
    Deletion is irreversible at the command line. There is no Recycle Bin. It comes later, behind heavy framing. For now: make, copy, and move only.

!!! warning "Typos Create New Files"
    If you mistype a filename, the command does not error — it creates a second file with the wrong name. Run `ls` after every action and read the output.

??? note "Instructor Note — The Verify Habit"
    "Trust the action, not the narration" runs through all agentic work. Build it here. A student who verifies every terminal action will verify every agent action later.

### Hands-On

1. Make a folder called `terminal-practice`.
2. Navigate into it.
3. Create a file called `day1.txt`.
4. Copy it to `day1-backup.txt`.
5. Rename `day1.txt` to `day1-v1.txt`.
6. Run `ls` after each step to verify the change.

!!! question "Before You Continue"
    You ran `mv notes.txt notes-final.txt`. What does `ls` show you, and what would it look like if you had made a typo in the destination name?

<div class="quiz-block">
  <p class="quiz-question">You run `mv report.txt final-report.txt` and then `ls`. What are you checking for?</p>
  <ul class="quiz-options">
    <li data-correct="false">Whether the file's contents changed</li>
    <li data-correct="false">Whether the command is still running</li>
    <li data-correct="true">Whether `final-report.txt` exists and `report.txt` is gone — confirming the rename happened correctly</li>
    <li data-correct="false">Whether the file is now read-only</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can create a folder and a file from the command line
- [ ] I can copy and move/rename files
- [ ] I run `ls` after every action to verify it happened
- [ ] I have not attempted to delete anything yet

---

## Paths, Tab-Completion, and the Up-Arrow

**BLUF.** A path is the full address of a file; tab-completion finishes names so you stop fat-fingering them; the up-arrow recalls your last command — three tools that separate fighting the terminal from flowing in it.

### Why This Matters

Typos in paths fail silently or hit the wrong target. Tab-completion is the single biggest accuracy and morale win in the terminal. The up-arrow turns one good command into a reusable tool. These are not tricks; they are standard operating procedure.

### Concepts

**Absolute vs. relative paths.**

An **absolute path** starts from the root of the filesystem: `C:\Users\YourName\Documents\report.txt` (Windows) or `/home/yourname/documents/report.txt` (Mac/Linux). It works from anywhere.

A **relative path** starts from wherever you currently are: `Documents/report.txt` or `../otherfolder/file.txt`. It only works if you are in the right starting position.

A path is a grid coordinate: precise, unambiguous, and unforgiving of a wrong character. A space or a capital letter in the wrong place either fails or hits the wrong target. The space is load-bearing.

!!! example "Absolute vs. Relative in Practice"
    You are in `/home/yourname/`. Both of these reach the same file:

    - Absolute: `/home/yourname/documents/report.txt`
    - Relative: `documents/report.txt`

    Move to a different folder and the relative path breaks. The absolute path still works.

**Tab-completion.** Start typing a folder or file name and press Tab. The terminal finishes it. If there is more than one match, press Tab twice to see the options. Use it on every path, every time.

**The up-arrow.** Press the up-arrow to cycle through previous commands. Edit a recalled command and re-run it instead of retyping from scratch.

!!! tip "The Most Important Habit in This Module"
    Never finish typing a long path by hand if tab-completion can do it. Tab-completion makes typos structurally impossible for the completed portion.

??? note "Instructor Note — Exactness as Frustration"
    A student annoyed that a capital letter breaks a path is learning the right thing. Name it: "Yes, the space matters. The capital letter matters. That is why tab-completion exists."

### Hands-On

1. Navigate to a folder using the full absolute path — type it by hand once to feel the length.
2. Navigate to the same folder using tab-completion. Press Tab after each segment.
3. Run `ls` in a folder with several items. Start typing one item's name, press Tab, watch it complete.
4. Run a command. Press the up-arrow. Edit one character and re-run it.

!!! question "Before You Continue"
    You are deep in a nested folder and need to copy a file to a location three levels up. Would you use an absolute or a relative path? Why?

<div class="quiz-block">
  <p class="quiz-question">Why does tab-completion reduce errors in terminal commands?</p>
  <ul class="quiz-options">
    <li data-correct="false">It suggests the most recently used command</li>
    <li data-correct="false">It checks whether the path is valid before you submit</li>
    <li data-correct="true">It completes names from what actually exists on disk, so the completed portion cannot contain a typo</li>
    <li data-correct="false">It speeds up the terminal by caching common paths</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can write both an absolute and a relative path to the same file
- [ ] I use tab-completion on every path — it is now a habit, not an option
- [ ] I can recall and edit previous commands with the up-arrow
- [ ] I understand why exactness (spaces, capitalization) matters in a path

---

## Commands, Flags, and Knowing When to Stop

**BLUF.** Most commands take flags that change what they do; `--help` shows you all available flags without memorization; and `Ctrl+C` stops anything that will not quit.

### Why This Matters

You are about to encounter tools that require flags to run correctly. You will also encounter commands that hang. Both situations create confusion and abandonment if you do not know what to do. This module removes both as blockers.

### Concepts

**Flags** are options you add to a command to change its behavior. They usually start with `-` (short form) or `--` (long form).

```bash
ls          # List files, default view
ls -l       # List files, detailed view
ls -la      # List files, detailed view, including hidden files
```

Same command. Different flags. Different output.

**Finding flags.** You do not memorize flags. You look them up.

```bash
ls --help     # Shows all flags and what they do
```

Read the `--help` output top to bottom. It looks overwhelming the first time. Find the flag you need; ignore the rest.

**The prompt is the signal.** When a command finishes, the prompt returns. If the cursor blinks with no prompt and nothing is happening, the command is still running.

**Ctrl+C** stops a running command and returns the prompt. It does not delete anything; it stops execution and hands control back to you.

!!! example "Stopping a Running Command"
    Run `ping google.com` (or `ping -t google.com` on Windows). Watch it run indefinitely. Press `Ctrl+C`. The command stops and the prompt returns.

    You just demonstrated that you can stop anything you start.

!!! warning "Do Not Memorize Flags"
    The concept of a flag and how to look one up is the lesson. The skill is knowing flags exist and knowing how to find the one you need.

### Hands-On

1. Run `ls --help` (Mac/Linux) or `Get-Help ls` (PowerShell). Read the first ten lines without panic.
2. Find the flag that shows hidden files. Run `ls` with that flag.
3. Run `ping google.com` (`ping -t google.com` on Windows). Let it run for five seconds.
4. Press `Ctrl+C`. Confirm the prompt returned.

!!! question "Before You Continue"
    You run a command and nothing happens for thirty seconds — the cursor just blinks. What are the two possibilities, and how do you handle each one?

<div class="quiz-block">
  <p class="quiz-question">You need to run `ls` but want to see hidden files. You do not know the flag. What do you do?</p>
  <ul class="quiz-options">
    <li data-correct="false">Google "ls hidden files" and copy the answer</li>
    <li data-correct="false">Try adding flags at random until one works</li>
    <li data-correct="true">Run `ls --help` and find the flag in the output</li>
    <li data-correct="false">Ask the AI chatbot — the terminal cannot tell you its own flags</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can add a flag to a command and observe the difference in output
- [ ] I can use `--help` to find a flag I do not know
- [ ] I know the prompt returning means a command finished
- [ ] I can stop a running command with `Ctrl+C` without fear

---

## Why Version Control Exists

**BLUF.** When an agent can change your files, you want a logbook of every change — what changed, when, and why, with the ability to go back — and that logbook is version control.

### Why This Matters

You just learned to create, move, and rename files from the command line. An agent will do those same operations — at speed, on multiple files, sometimes without asking. Version control is what lets you see every change and undo any of them.

### Concepts

Every time a file changes, version control records a snapshot: what changed, when, and a note about why. Stored locally on your machine. Every snapshot can be rewound.

**Two layers:**

- **Local logbook.** Your machine keeps the record. You can always rewind to any previous snapshot without needing the internet.
- **Remote copy.** The same history synchronized to a cloud server. Backup — and the mechanism for teammates working on the same files.

No commands today. You are loading the reason. The commands come when you work with git directly.

!!! note "Why Software People Seem to Remember Everything"
    They do not. They have the log. "Who changed this and when?" is a two-second lookup. "What did this file look like last Tuesday?" is one command.

??? note "Instructor Note — Resist Teaching Git Commands Here"
    The concept is the prerequisite; hands-on git work teaches the commands. If a student asks "how do I actually do this," tell them: "You will do it in the next session. Today you need to know why."

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

Before moving to Agentic AI, confirm:

- [ ] I can explain version control as a logbook of file changes I can rewind
- [ ] I understand why it matters once an agent has write access
- [ ] I can distinguish the local logbook from the remote copy
- [ ] I am not yet expected to know any git commands
