# Know the Terrain: Filesystem & Terminal

**Who this is for:** Someone who uses computers every day but has never thought about the structure underneath the apps — and is about to supervise an agent that operates directly on that structure.

**What you will leave with:** You can navigate the filesystem by clicking and by typing, read a path as a route, tell plaintext from rich text, create and move files from the command line, find a flag you do not know, stop a command that will not quit, and verify every action you take. These are the exact moves an agent makes on your machine. You learn them so you can supervise.

---

## Files, Folders, and the Tree

**BLUF.** Everything on a computer lives in a file, files live in folders, folders nest into a tree, and the address of any file is the path you walk to reach it — the apps you use have been hiding this structure, and understanding it is the ground everything else stands on.

### Why This Matters

Every terminal command depends on being able to think about where things are. A student who cannot read a path gets lost the moment they type their first command. This section builds the map before the movement. It is also the terrain an agent walks: when an agent works on your machine, it moves through this same tree.

### Concepts

A **file** holds data: a document, an image, a script. A **folder** (also called a directory) holds files and other folders. Folders nest inside folders, forming a tree. Every file on the machine has exactly one location in that tree.

The **path** is the route through the tree to reach a file. On Windows it looks like `C:\Users\YourName\Documents\report.txt`. On a Mac or Linux machine it looks like `/home/yourname/documents/report.txt`. Read it left to right: each backslash or forward slash is one step down the tree.

Most apps hide this. When you save a file in Word, you pick a name and Word decides where it goes. The tree exists whether you see it or not.

!!! example "Finding a File You Saved Last Week"
    Open File Explorer (Windows) or Finder (Mac). Navigate to your Downloads folder. Find a file you downloaded recently.

    Look at the address bar at the top — that is the path. Read it. That string of words separated by slashes is the route through the tree to reach that exact file.

!!! tip "Turn on File Extensions Now"
    By default, Windows hides file extensions (the `.docx`, `.txt`, `.pdf` after the name). Turn them on before the next section: File Explorer → View → Show → File name extensions.

    You will need to see extensions throughout this course.

!!! warning "Do Not Assume You Have Seen This"
    Many people save files and find them through search or recent items — they have genuinely never navigated the folder tree. Test yourself: can you find a file you saved last week without using search? If not, that is what this section fixes.

??? note "Instructor Note — Extension Visibility"
    Turning extensions on here prevents confusion in the next section where the difference between `.txt` and `.docx` is the whole lesson. Do not skip this step.

### Hands-On

1. Open File Explorer (Windows) or Finder (Mac).
2. Navigate from your home folder down to Downloads by clicking — do not use search.
3. Find a file. Read its full path in the address bar.
4. Create a new folder on your Desktop. Name it `practice`.
5. Move any file into that folder by dragging.

You are walking the tree by clicking. The terminal section is the same moves, typed.

!!! question "Before You Continue"
    You just moved a file by dragging. Write out the path to where it now lives. Could you give someone else those directions and have them find it?

<div class="quiz-block">
  <p class="quiz-question">What is a file path?</p>
  <ul class="quiz-options">
    <li data-correct="false">The name of a file, including its extension</li>
    <li data-correct="false">A shortcut that opens a file faster</li>
    <li data-correct="true">The route through the folder tree that locates a specific file</li>
    <li data-correct="false">The history of changes made to a file</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can describe a file, a folder, and how they nest into a tree
- [ ] I can read a path as a route through that tree
- [ ] I have navigated to a specific file without using search
- [ ] File extensions are now visible on my machine

---

## Plaintext vs Rich Text

**BLUF.** A plaintext file is just characters — no hidden formatting, no metadata — and that is exactly what models and tools want, because what you see is literally what the machine reads.

### Why This Matters

At some point you will paste content from Word into an AI tool and wonder why things break. The answer is hidden characters. Understanding this difference diagnoses a category of problems you will hit repeatedly.

### Concepts

**Plaintext** is exactly what it says: text, nothing else. Open a `.txt` file in any program on any machine and you see every character the file contains. No hidden formatting. No metadata. What you see is what the machine reads.

**Rich text** files like `.docx` store formatting instructions alongside the text — bold, font size, margins, revision history, all packed in alongside the words. When you paste from Word into a terminal or a markdown document, those hidden characters come with it.

Common plaintext extensions: `.txt`, `.md`, `.csv`, `.json`, `.py`

Common rich text extensions: `.docx`, `.xlsx`, `.pdf`

!!! example "The Word-to-Markdown Trap"
    Type a bullet point in Word using a hyphen. Word automatically converts your straight quote to a "smart quote" and your double hyphen to an em-dash.

    Paste that into a Markdown file. The Markdown parser reads the curly apostrophe as a plain character. The em-dash breaks the bullet. What looked fine in Word is broken in plaintext.

    The fix: write Markdown in a code editor, not Word.

!!! warning "Pasting from Word Silently Breaks Things"
    Smart quotes, em-dashes, non-breaking spaces, and invisible formatting characters all travel with Word content. When you paste into a terminal, a chat interface, or a Markdown file, those characters come along. If something looks correct but behaves wrong, hidden characters are the first thing to check.

??? note "Instructor Note — Encodings"
    Do not go into encodings (UTF-8, ASCII, etc.) at this level. "Plaintext is honest, rich text hides things" is the entire lesson.

### Hands-On

1. Open Notepad (Windows) and type a few sentences. Save as `test.txt`.
2. Open the same file in VS Code. Compare how it looks.
3. Now open any `.docx` file in VS Code (not Word). Look at what is actually inside it.

You are seeing the difference between "what a human reads" and "what a machine reads."

!!! question "Before You Continue"
    You paste a block of text from a Word document into your AI chatbot and the formatting looks off. What is the most likely cause, and what would you do instead?

<div class="quiz-block">
  <p class="quiz-question">Why do models and command-line tools prefer plaintext over rich-text formats like .docx?</p>
  <ul class="quiz-options">
    <li data-correct="false">Plaintext files are smaller and load faster</li>
    <li data-correct="true">What you see in a plaintext file is exactly what the machine reads — no hidden characters or formatting</li>
    <li data-correct="false">Rich text files require a license to open</li>
    <li data-correct="false">Models cannot open .docx files at all</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can distinguish plaintext from rich text and give an example of each
- [ ] I understand why pasting from Word can silently break things
- [ ] I know the common plaintext extensions
- [ ] I have seen what a .docx file actually looks like underneath

---

## Looking at Files in a Real Editor

**BLUF.** A code editor is a better text viewer — install one, open a folder, read a file, close it without fear; that is the whole job in this section.

### Why This Matters

The terminal work ahead requires reading files from the command line. The editor gives you a visual companion to that work — the same files, different view. Installing it now removes the install step as a distraction when the lesson is about something else.

### Concepts

A code editor is not an IDE (a full programming environment). It is a text viewer with good defaults: syntax highlighting, a visible file tree, and a preview mode for formatted files.

VS Code is the standard choice here. Free, runs on Windows and Mac, handles every file type in this course.

**Three things to know:**

- The **file tree panel** (left side) shows the folder structure — the same tree, now labeled.
- The **editor panel** (right side) shows file content.
- **Markdown preview:** click the split-square icon to render a `.md` file's formatting.

!!! example "Rendering a Markdown File"
    Open a `.md` file in VS Code. In the top-right corner, click the preview icon (or press `Ctrl+Shift+V`). The left pane shows raw Markdown; the right pane shows it rendered.

    You are seeing plaintext and its rendered output side by side.

!!! warning "Scope Discipline"
    Scope for now: open, view, close. Do not install extensions, change settings, or start editing files. The goal is comfort at the front door, not a full tour.

??? note "Instructor Note — Install Problems"
    A broken install on one machine should not stall the room. Have a backup viewer (Notepad++ is a lighter alternative) and move on. The lesson is "open and view a file," not "install VS Code perfectly."

### Hands-On

1. Download and install VS Code if you have not already.
2. Go to File → Open Folder. Open the `practice` folder from the first section.
3. Click the `.txt` file you created. Read it in the editor panel.
4. Find a `.md` file anywhere on your machine. Open it. Toggle the preview.

!!! question "Before You Continue"
    You are looking at the same Markdown file in two panes — raw on the left, rendered on the right. Which version does the machine work with? Which version does the human read?

<div class="quiz-block">
  <p class="quiz-question">What is the main reason to use a code editor instead of Word for working with plaintext files?</p>
  <ul class="quiz-options">
    <li data-correct="false">Code editors have more fonts and formatting options</li>
    <li data-correct="false">Code editors are faster to open</li>
    <li data-correct="true">Code editors work in plaintext — no hidden characters, no automatic formatting changes</li>
    <li data-correct="false">Word cannot open .txt files</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] VS Code (or equivalent) is installed and opens without errors
- [ ] I can open a folder and navigate its tree in the editor
- [ ] I have opened a Markdown file and toggled the rendered preview
- [ ] I did not change any settings or install any extensions

---

## What the Terminal Is (and Why It Is Safe)

**BLUF.** The terminal is a typed way to give the computer the same instructions you used to give by clicking — it is not hacking, it is not dangerous by default, and it feels alien for about an hour before it feels normal.

### Why This Matters

This is where the course gets uncomfortable for some people. If you are wondering why an AI course includes a unit on typing commands, the short version is: the agent acts through the terminal. You need to understand the terrain it operates on so you can supervise it.

### Concepts

A command is a typed instruction. It is the same as a click — it tells the computer to do something. The difference is precision: a click is constrained by what a menu shows you; a command can express anything the machine understands.

The **prompt line** is where your typing goes. It usually ends with a `$` (Mac/Linux) or `>` (Windows PowerShell). When you see that character, the terminal is ready for input.

!!! example "Your First Command"
    Open the terminal. On Windows: search for "PowerShell" or "Terminal" in the Start menu. On Mac: search for "Terminal" in Spotlight.

    Type `date` (Mac/Linux) or `Get-Date` (Windows PowerShell) and press Enter.

    The terminal printed the current date and returned the prompt. That is a command.

!!! warning "Nothing in This Section Can Hurt the Machine"
    The commands in this section and the next two are read-only and harmless. You are looking at the filesystem, not modifying it. Anything that can cause real damage comes much later, behind heavy framing.

??? note "Instructor Note — Environment Choice (WSL vs PowerShell)"
    The course's hands-on transcripts assume a Linux/Unix shell (`touch`, `ls`, `mkdir`). On Windows, the recommended environment is WSL (Windows Subsystem for Linux): `wsl --install`, no admin required on Windows 11. Windows files appear at `/mnt/c/Users/YourName/`, so `C:\Users\Jake\Documents` becomes `/mnt/c/Users/Jake/Documents` — backslashes to forward slashes, drive letter lowercased. Native PowerShell uses different commands (`New-Item` instead of `touch`); the each-tab tables below give the PowerShell equivalents for students who stay on it.

??? note "Instructor Note — Address the Bait-and-Switch Out Loud"
    Name the frustration before a student says it: "Some of you are wondering why an AI course spent time on the command line." Then make the connection explicit: the agent acts through the terminal. The student who does not understand the terminal cannot supervise an agent using it.

### Hands-On

1. Open the terminal on your machine. Sit with the blinking cursor for ten seconds. Name the feeling.
2. Run each command below for your platform. Read the output before moving to the next one.

=== "Mac / WSL (Linux)"
    | Command | What it does |
    |---|---|
    | `date` | Print the current date and time |
    | `whoami` | Print your username |
    | `pwd` | Print your current location in the filesystem |
    | `ls` | List the files in the current folder |
    | `echo "hello"` | Print text to the terminal |

=== "Windows PowerShell"
    | Command | What it does |
    |---|---|
    | `Get-Date` | Print the current date and time |
    | `$env:USERNAME` | Print your username |
    | `Get-Location` | Print your current location in the filesystem |
    | `Get-ChildItem` | List the files in the current folder |
    | `Write-Output "hello"` | Print text to the terminal |

3. Close the terminal and open it again. Re-run one command from memory without looking at the table.

You opened it, ran five things, and closed it. The anxiety has a smaller surface area now.

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
- [ ] The anxiety is smaller than it was at the start of this section

---

## Navigating: Where Am I, What Is Here

**BLUF.** Three commands cover most of navigation — where am I, what is here, move — and mastering them by typing replaces every click from the first section.

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

    Walk this sequence on your own machine. These are the exact same moves you did by clicking in the first section — same tree, typed instead.

!!! tip "pwd Is Your Reset Button"
    Any time you feel lost in the terminal, type `pwd`. It tells you exactly where you are. You can never be permanently lost if you can always ask "where am I."

??? note "Instructor Note — Reps Over Coverage"
    Same three commands, many short repetitions, spread across several days. Do not introduce file creation yet. One capability at a time. Reps build muscle memory; coverage builds confusion.

### Hands-On — Exercise 1: Orientation Walk

1. Open the terminal. Run `pwd`. Read the path. Find that same location in File Explorer / Finder.
2. Starting from your home directory, navigate to five different locations. Run `pwd` after each move to confirm where you landed.
3. Run `ls` in each to see what is there. Identify three items by name in one of them.
4. Move back up with `cd ..` and confirm with `pwd`.

Repeat this cycle until it feels routine. **Deliverable:** a terminal transcript of the walk (the first of six that build your Module 5 transcript).

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
- [ ] I have walked the same tree by clicking (first section) and by typing (this one)

---

## Acting: Make, Move, Copy — and Verify

**BLUF.** Four commands cover most day-to-day file work — make a folder, make a file, copy, move — the same actions from the first section, now typed; and every one of them you confirm before you trust it.

### Why This Matters

Navigation got you to the position; now you act on it. This is where the terminal goes from "I can look around" to "I can do things." These four commands are the ones an agent uses most when it works in your filesystem — which is exactly why the verify habit you build here is the one you will use to supervise an agent later.

### Concepts

Every action you take, you confirm. You do not assume the round landed — you check the target. **This is the "verify after acting" habit, and it starts here.** It is the single most important reflex in this course: trust the result on the disk, not the narration that an action happened. You will see this habit again when you command an agent, and again at the capstone, where it is graded. Build it now while the stakes are a practice file.

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

??? note "Instructor Note — The Verify Habit Is the Through-Line"
    "Trust the action, not the narration" runs through all agentic work. Build it here deliberately and name it. A student who verifies every terminal action will verify every agent action later. This habit is introduced here on purpose and reinforced in the commanding-an-agent module and graded at the capstone — do not let it stay implicit.

### Hands-On — Exercise 2: File Manipulation Sprint

1. Make a folder structure: `projects/acc-prep/module-5/`.
2. Navigate into `module-5`.
3. Create three text files (use `touch`, or `echo` to add a line of content to one).
4. Copy one file to a `backup` subfolder.
5. Rename one file (for example `day1.txt` to `day1-v1.txt`).
6. Run `ls` after **every** step to verify the change landed. Read the output — do not assume.

**Deliverable:** a terminal transcript showing each step and its verification (transcript 2 of 6).

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
- [ ] I run `ls` after every action to verify it happened — this is the verify-after-acting habit
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

!!! tip "The Most Important Habit in This Section"
    Never finish typing a long path by hand if tab-completion can do it. Tab-completion makes typos structurally impossible for the completed portion.

??? note "Instructor Note — Exactness as Frustration"
    A student annoyed that a capital letter breaks a path is learning the right thing. Name it: "Yes, the space matters. The capital letter matters. That is why tab-completion exists." On Windows/WSL, also drill the `/mnt/c/...` path translation here — it is the number-one path stumble.

### Hands-On — Exercise 3: Path Puzzle

Given a file at `/home/user/projects/claude/config.txt`, write each of these and verify it works:

1. The absolute path to the file.
2. The relative path from `/home/user/` to the file.
3. The relative path from `/home/user/projects/` to the file.
4. Navigate using each path to confirm it reaches the file. Then re-do step 1 using tab-completion — press Tab after each segment and watch it complete.
5. Run a command, press the up-arrow, edit one character, and re-run it.

**Deliverable:** a short Markdown document listing each path and proof it works (transcript/notes 3 of 6).

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

## Commands, Flags, Help, and Knowing When to Stop

**BLUF.** Most commands take flags that change what they do; `--help` shows you all available flags without memorization; piping and redirection chain commands together; and `Ctrl+C` stops anything that will not quit.

### Why This Matters

You are about to encounter tools that require flags to run correctly. You will also encounter commands that hang. Both situations create confusion and abandonment if you do not know what to do. This section removes both as blockers and adds the two glue operators — pipe and redirect — that turn single commands into small workflows.

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
man ls        # Full manual page (Mac/Linux/WSL)
```

Read the output top to bottom. It looks overwhelming the first time. Find the flag you need; ignore the rest.

**Piping and redirection.** Two operators chain commands and capture output:

- `|` (pipe) sends the output of one command into another: `ls | wc -l` counts the items in a folder.
- `>` writes output to a file, replacing it: `ls > files.txt`.
- `>>` appends output to a file: `echo "another line" >> files.txt`.

**The prompt is the signal.** When a command finishes, the prompt returns. If the cursor blinks with no prompt and nothing is happening, the command is still running.

**Ctrl+C** stops a running command and returns the prompt. It does not delete anything; it stops execution and hands control back to you.

!!! example "Stopping a Running Command"
    Run `ping google.com` (or `ping -t google.com` on Windows). Watch it run indefinitely. Press `Ctrl+C`. The command stops and the prompt returns.

    You just demonstrated that you can stop anything you start.

!!! tip "Ctrl+C: The Most Important Shortcut"
    Ctrl+C sends an interrupt and stops the current process. Use it whenever a command hangs, runs too long, or you need to abort. Drill it until it is a reflex — you need this before anything else can go wrong.

!!! warning "Do Not Memorize Flags"
    The concept of a flag and how to look one up is the lesson. The skill is knowing flags exist and knowing how to find the one you need.

### Hands-On — Exercise 4: The Help System

1. Run `ls --help` (Mac/Linux/WSL) or `Get-Help Get-ChildItem` (PowerShell). Read the first ten lines without panic.
2. Find the flag that shows hidden files. Run `ls` with that flag.
3. Answer three questions from the help output: what does `-l` do? What about `-a`? How do you list by size?
4. Build a one-page help reference card for `ls`, `cd`, `mkdir`, `cp`, `mv`.

**Deliverable:** the help reference card (deliverable 4 of 6).

### Hands-On — Exercise 5: Piping and Redirection

1. Create a text file with several lines (paste content or use `echo` repeatedly with `>>`).
2. Run `ls` and save the output to a file with `>`.
3. Count the number of items in a directory using a pipe (`ls | wc -l`).
4. Append a line to your file with `>>` and verify with `ls` and by opening the file.

**Deliverable:** a transcript showing two redirection examples and one pipe example (transcript 5 of 6).

### Hands-On — Exercise 6: Real-World Scenario

Scenario: "You have a folder of files. You need to find the `.txt` files, list them, and move them into an `archive` folder."

1. Create the scenario: make a folder, populate it with a mix of files (some `.txt`).
2. List just the `.txt` files.
3. Make an `archive` folder.
4. Move the `.txt` files into it. **Run `ls` on both folders to verify** — confirm the files arrived and nothing was left behind.
5. Press `Ctrl+C` at least once during a long-running command to prove you can stop it.

**Deliverable:** an annotated terminal transcript explaining each step (transcript 6 of 6). The six transcripts together are your **Module 5 deliverable**.

!!! question "Before You Continue"
    You run a command and nothing happens for thirty seconds — the cursor just blinks. What are the two possibilities, and how do you handle each one?

<div class="quiz-block">
  <p class="quiz-question">You need to run `ls` but want to see hidden files. You do not know the flag. What do you do?</p>
  <ul class="quiz-options">
    <li data-correct="false">Search online and copy the first answer you find</li>
    <li data-correct="false">Try adding flags at random until one works</li>
    <li data-correct="true">Run `ls --help` and find the flag in the output</li>
    <li data-correct="false">Assume the terminal cannot show hidden files</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-block">
  <p class="quiz-question">You moved a batch of files with `mv` and the command returned no error. What confirms the move actually did what you intended?</p>
  <ul class="quiz-options">
    <li data-correct="false">No error message means it worked — nothing else to check</li>
    <li data-correct="false">The command printed a success summary</li>
    <li data-correct="true">Running `ls` on the source and destination and reading the output — verify after acting, do not trust the silence</li>
    <li data-correct="false">Re-running the same command a second time</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can add a flag to a command and observe the difference in output
- [ ] I can use `--help` or `man` to find a flag I do not know
- [ ] I can pipe output between commands and redirect output to a file
- [ ] I know the prompt returning means a command finished
- [ ] I can stop a running command with `Ctrl+C` without fear
- [ ] I verify after acting on every file operation — I trust the disk, not the narration

---

## Summary

| Capability | Commands / tools | The habit it builds |
|---|---|---|
| Read the terrain | path, file tree, plaintext vs rich text | Know where things live before you act |
| Navigate | `pwd`, `ls`, `cd`, `cd ..` | Never be permanently lost; `pwd` is the reset button |
| Act | `mkdir`, `touch`/`New-Item`, `cp`, `mv` | Make, copy, move — no deletion yet |
| Aim precisely | absolute vs relative paths, tab-completion, up-arrow | Exactness; let the machine complete names |
| Control | flags, `--help`/`man`, `|`, `>`, `>>`, `Ctrl+C` | Look it up; chain commands; stop anything you start |
| Verify | `ls` after every action | Trust the result on disk, not the narration — the through-line of agentic work |

## End of Module

You now know the terrain an agent operates on, and you have started the one habit that matters most when you hand that terrain to an agent: verify after acting. Every command in this module — `pwd`, `ls`, `cd`, `mkdir`, `mv` — is a command an agent runs on your machine. You learned to navigate it so you can supervise someone else navigating it. Next, you close the loop on safety: when an agent can change your files at speed, you want a logbook of every change you can rewind. That logbook is version control.
