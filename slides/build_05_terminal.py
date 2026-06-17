"""
ACC Module 05 — Know the Terrain: Filesystem & Terminal
Slide deck builder. Uses the shared Army Cyber Dark theme.

Run by the orchestrator (python is blocked for the authoring agent):
    python build_05_terminal.py
Output: slides/Finished/05-terminal.pptx
"""

from acc_theme import *


def build():
    prs = new_deck()

    # --- TITLE ---
    add_title_slide(prs,
        "Know the Terrain:\nFilesystem &\nTerminal",
        "PREREQUISITE MODULE  |  2-3 HOUR BLOCK",
        "[IMAGE: Soldier studying a terrain map before movement — the filesystem is the ground]")

    # --- OVERVIEW ---
    add_overview_slide(prs,
        "Learn to read and walk the filesystem by clicking and by typing, tell plaintext from rich text, and run, "
        "control, and verify terminal commands. These are the exact moves an agent makes on your machine — you "
        "learn them so you can supervise.",
        "2-3 hour block (about 110 min hands-on)",
        [
            "Read a file path as a route through the folder tree",
            "Distinguish plaintext from rich text and know why tools want plaintext",
            "Navigate, create, copy, and move files from the command line",
            "Use paths, tab-completion, flags, help, piping, redirection, and Ctrl+C",
            "Build the verify-after-acting habit — trust the disk, not the narration",
        ])

    # =========================================================================
    # SECTION 1 — Files, Folders, and the Tree
    # =========================================================================
    add_section_header(prs, "01",
        "Files, Folders,\nand the Tree",
        "Everything lives in a file; files live in folders; folders nest into a tree; the path is the route you walk.",
        "[IMAGE: A nested folder tree rendered as a terrain map with grid lines]")

    add_concept_slide(prs, "The Tree and the Path", [
        ("A file holds data. A folder holds files and other folders. Folders nest into a tree.", False),
        ("Every file has exactly one location in that tree.", False),
        ("The PATH is the route through the tree to reach a file.", False),
        ("Windows: C:\\Users\\YourName\\Documents\\report.txt", True),
        ("Mac / Linux: /home/yourname/documents/report.txt", True),
        ("Read it left to right — each slash is one step down the tree.", False),
        ("Most apps hide this. The tree exists whether you see it or not.", False),
    ], note="Turn on file extensions now: File Explorer -> View -> Show -> File name extensions. You will need to "
            "see .txt vs .docx in the next section.")

    add_hands_on(prs, "Walk the Tree by Clicking", [
        "Open File Explorer (Windows) or Finder (Mac).",
        "Navigate from your home folder down to Downloads by clicking — do not use search.",
        "Find a file. Read its full path in the address bar.",
        "Create a new folder on your Desktop. Name it 'practice'.",
        "Move any file into that folder by dragging.",
    ], "[IMAGE: A hand dragging a file along a marked route through a folder tree]")

    add_check_on_learning(prs,
        "You just moved a file by dragging.\n\n"
        "Write out the path to where it now lives.\n\n"
        "Could you give someone else those directions and have them find it?")

    add_section_summary(prs, "Files, Folders, and the Tree", [
        "Files live in folders; folders nest into a tree; every file has one location.",
        "A path is the route through the tree — read left to right, each slash is one step.",
        "Apps hide the tree, but it is always there.",
        "Turn on file extensions before continuing.",
    ])

    # =========================================================================
    # SECTION 2 — Plaintext vs Rich Text
    # =========================================================================
    add_section_header(prs, "02",
        "Plaintext vs\nRich Text",
        "Plaintext is just characters — no hidden formatting — and that is exactly what models and tools want.",
        "[IMAGE: Two documents side by side — one clean text, one stuffed with hidden formatting marks]")

    add_concept_slide(prs, "What You See Is What the Machine Reads", [
        ("Plaintext: text, nothing else. What you see is what the machine reads.", False),
        ("No hidden formatting, no metadata — opens the same everywhere.", True),
        ("Rich text (.docx): stores formatting, fonts, margins, revision history alongside the words.", False),
        ("Those hidden characters travel when you paste into a terminal, chat, or Markdown file.", True),
        ("Plaintext extensions: .txt  .md  .csv  .json  .py", False),
        ("Rich text extensions: .docx  .xlsx  .pdf", False),
    ], note="The Word-to-Markdown trap: Word turns straight quotes into smart quotes and double hyphens into "
            "em-dashes. Pasted into plaintext, they break things silently. Fix: write Markdown in a code editor.")

    add_check_on_learning(prs,
        "You paste a block of text from a Word document into your AI chatbot and the formatting looks off.\n\n"
        "What is the most likely cause, and what would you do instead?")

    add_section_summary(prs, "Plaintext vs Rich Text", [
        "Plaintext is honest: what you see is what the machine reads.",
        "Rich text hides formatting, smart quotes, and invisible characters.",
        "Pasting from Word silently breaks terminals, chats, and Markdown.",
        "When something looks right but behaves wrong, check for hidden characters first.",
    ])

    # =========================================================================
    # SECTION 3 — Looking at Files in a Real Editor
    # =========================================================================
    add_section_header(prs, "03",
        "Looking at Files\nin a Real Editor",
        "A code editor is a better text viewer — install one, open a folder, read a file, close it without fear.",
        "[IMAGE: A code editor with a file tree on the left and a rendered Markdown preview on the right]")

    add_concept_slide(prs, "VS Code: Three Things to Know", [
        ("A code editor is not an IDE — it is a text viewer with good defaults.", False),
        ("VS Code is the standard here: free, Windows and Mac, handles every file type in this course.", False),
        ("File tree panel (left): the folder structure, now labeled.", True),
        ("Editor panel (right): file content.", True),
        ("Markdown preview: click the split-square icon (Ctrl+Shift+V) to render a .md file.", True),
        ("Scope for now: open, view, close. No extensions, no settings changes, no editing.", False),
    ])

    add_hands_on(prs, "Open and View a File", [
        "Download and install VS Code if you have not already.",
        "File -> Open Folder. Open the 'practice' folder from Section 1.",
        "Click the .txt file you created. Read it in the editor panel.",
        "Find a .md file anywhere on your machine. Open it. Toggle the rendered preview.",
    ], "[IMAGE: Raw Markdown and rendered Markdown shown side by side in an editor]")

    add_section_summary(prs, "Looking at Files in a Real Editor", [
        "A code editor works in plaintext — no hidden characters, no auto-formatting.",
        "The file tree is the same tree from Section 1, now labeled.",
        "Markdown preview shows raw plaintext and rendered output side by side.",
        "Scope: open, view, close. Comfort at the front door, not a full tour.",
    ])

    # =========================================================================
    # SECTION 4 — What the Terminal Is (and Why It Is Safe)
    # =========================================================================
    add_section_header(prs, "04",
        "What the Terminal Is\n(and Why It Is Safe)",
        "A typed way to give the same instructions you used to give by clicking — not hacking, not dangerous by default.",
        "[IMAGE: A terminal window with a blinking prompt — calm, not threatening]")

    add_concept_slide(prs, "A Command Is a Typed Click", [
        ("A command is a typed instruction — the same as a click, with more precision.", False),
        ("A click is limited to what a menu shows. A command can express anything the machine understands.", False),
        ("The prompt line is where your typing goes — it ends with $ (Mac/Linux) or > (PowerShell).", False),
        ("First command: 'date' (Mac/Linux) or 'Get-Date' (PowerShell). The date prints; the prompt returns.", False),
        ("Everything in this section and the next two is read-only and harmless.", False),
    ], note="Environment note: course transcripts assume a Linux/Unix shell. On Windows, WSL gives that "
            "('wsl --install', no admin on Win 11). Windows files live at /mnt/c/Users/YourName/. The per-tab "
            "tables in the markdown give PowerShell equivalents for students who stay on it.")

    add_hands_on(prs, "Your First Five Commands", [
        "Open the terminal. Sit with the blinking cursor for ten seconds. Name the feeling.",
        "Mac/WSL: run date, whoami, pwd, ls, echo \"hello\" — read each output.",
        "PowerShell: run Get-Date, $env:USERNAME, Get-Location, Get-ChildItem, Write-Output \"hello\".",
        "Close the terminal and open it again.",
        "Re-run one command from memory without looking at the table.",
    ], "[IMAGE: A soldier running a quick comms check — short, routine, builds confidence]")

    add_check_on_learning(prs,
        "You typed a command and saw a response.\n\n"
        "What is the difference between that and clicking a button in an app?\n\n"
        "What stayed the same?")

    add_section_summary(prs, "What the Terminal Is", [
        "A command is a typed click — same action, more precision, no menu.",
        "The prompt line ends with $ or > and signals the terminal is ready.",
        "Nothing in the read-only sections can hurt the machine.",
        "On Windows, WSL provides the Linux/Unix shell the course assumes.",
    ])

    # =========================================================================
    # SECTION 5 — Navigating
    # =========================================================================
    add_section_header(prs, "05",
        "Navigating: Where\nAm I, What Is Here",
        "Three commands cover navigation — where am I, what is here, move — and pwd is the reset button.",
        "[IMAGE: A soldier checking a grid reference to confirm position before moving]")

    add_concept_slide(prs, "pwd, ls, cd", [
        ("pwd — Print Working Directory: your current location in the tree.", False),
        ("ls — List: everything in the current folder. Add -la (Mac/WSL) for hidden files.", False),
        ("cd foldername — Change Directory: move down into a folder.", False),
        ("cd .. — move up one level.", False),
        ("Walk the tree: pwd -> ls -> cd Documents -> pwd -> ls -> cd .. -> pwd.", False),
    ], note="pwd is your reset button. Any time you feel lost, type pwd — it tells you exactly where you are. "
            "You can never be permanently lost if you can always ask 'where am I.'")

    add_hands_on(prs, "Exercise 1 — Orientation Walk", [
        "Run pwd. Read the path. Find that same location in File Explorer / Finder.",
        "From your home directory, navigate to five different locations.",
        "Run pwd after EACH move to confirm where you landed.",
        "Run ls in each; identify three items by name in one of them.",
        "Move back up with cd .. and confirm with pwd. Save a transcript (1 of 6).",
    ], "[IMAGE: A route traced across a map with checkpoints at each stop]")

    add_check_on_learning(prs,
        "You typed 'cd Documents' and then 'pwd'.\n\n"
        "What does pwd tell you, and how does it prove you moved?")

    add_section_summary(prs, "Navigating", [
        "pwd prints your location; ls lists contents; cd moves; cd .. moves up.",
        "pwd is the reset button — you can never be permanently lost.",
        "These are the same moves you did by clicking, now typed.",
        "Reps over coverage: one capability at a time builds muscle memory.",
    ])

    # =========================================================================
    # SECTION 6 — Acting: Make, Move, Copy — and Verify
    # =========================================================================
    add_section_header(prs, "06",
        "Acting: Make,\nMove, Copy —\nand Verify",
        "Four commands cover daily file work — and every one of them you confirm before you trust it.",
        "[IMAGE: A soldier confirming a round landed on target before calling the next — check, do not assume]")

    add_concept_slide(prs, "Make, Copy, Move — Then Verify", [
        ("mkdir foldername — make a new folder.", False),
        ("touch filename.txt (Mac/WSL) / New-Item filename.txt (PowerShell) — make an empty file.", False),
        ("cp source destination — copy a file.", False),
        ("mv source destination — move or rename a file.", False),
        ("After EVERY action, run ls to confirm the change landed.", False),
        ("Typos do not error — they create a second file with the wrong name. Read the ls output.", False),
        ("No deletion yet: irreversible at the command line, behind heavy framing later.", False),
    ], note="THIS IS THE VERIFY-AFTER-ACTING HABIT, AND IT STARTS HERE. Trust the result on disk, not the "
            "narration that an action happened. You will use this same reflex to supervise an agent (Module 7) "
            "and it is graded at the capstone (Module 11). Build it now while the stakes are a practice file.")

    add_example_slide(prs,
        "Build Something From Scratch",
        "Every action confirmed with ls — the verify habit in motion",
        [
            "mkdir project",
            "cd project",
            "touch notes.txt",
            "ls                      # Verify notes.txt is there",
            "mkdir drafts",
            "cp notes.txt drafts/notes-copy.txt",
            "ls drafts               # Verify the copy landed",
            "mv notes.txt notes-v1.txt",
            "ls                      # Verify the rename happened",
            "",
            "After each command, ls confirms reality. Do not trust the silence.",
        ],
        "[IMAGE: A checklist where each built item is verified before the next begins]")

    add_hands_on(prs, "Exercise 2 — File Manipulation Sprint", [
        "Make a folder structure: projects/acc-prep/module-5/  then cd into module-5.",
        "Create three text files (touch, or echo a line into one).",
        "Copy one file into a 'backup' subfolder.",
        "Rename one file (e.g. day1.txt -> day1-v1.txt).",
        "Run ls after EVERY step and read the output. Save a transcript (2 of 6).",
    ], "[IMAGE: A staged build area with each item checked off as it is placed]")

    add_check_on_learning(prs,
        "You ran 'mv notes.txt notes-final.txt'.\n\n"
        "What does ls show you, and what would it look like if you had made a typo in the destination name?")

    add_section_summary(prs, "Acting — Make, Move, Copy, Verify", [
        "mkdir, touch/New-Item, cp, mv cover most daily file work.",
        "Verify after acting: run ls after every change and read the output.",
        "Typos create new files silently — the ls check is how you catch them.",
        "No deletion yet. The verify habit is the through-line of agentic supervision.",
    ])

    # =========================================================================
    # SECTION 7 — Paths, Tab-Completion, and the Up-Arrow
    # =========================================================================
    add_section_header(prs, "07",
        "Paths, Tab-Completion,\nand the Up-Arrow",
        "A path is a grid coordinate; tab-completion makes the completed portion typo-proof; the up-arrow recalls commands.",
        "[IMAGE: A precise grid coordinate plotted on a map — a single wrong digit misses the target]")

    add_concept_slide(prs, "Aim Precisely", [
        ("Absolute path: starts from the root — works from anywhere. /home/you/docs/report.txt", False),
        ("Relative path: starts from where you are — breaks if you move. docs/report.txt", False),
        ("A path is a grid coordinate: a wrong space or capital fails or hits the wrong target. The space is load-bearing.", False),
        ("Tab-completion: start a name, press Tab, the terminal finishes it. Tab twice for multiple matches.", False),
        ("Tab-completion makes typos structurally impossible for the completed portion. Use it every time.", False),
        ("Up-arrow: cycle previous commands, edit one, re-run — instead of retyping.", False),
    ])

    add_hands_on(prs, "Exercise 3 — Path Puzzle", [
        "Target file: /home/user/projects/claude/config.txt",
        "Write the absolute path to it.",
        "Write the relative path from /home/user/  and from /home/user/projects/.",
        "Navigate using each path to confirm it reaches the file.",
        "Redo with tab-completion (Tab after each segment). Use up-arrow to re-run an edited command. Notes (3 of 6).",
    ], "[IMAGE: The same target plotted three ways — one absolute fix, two relative bearings]")

    add_check_on_learning(prs,
        "You are deep in a nested folder and need to copy a file to a location three levels up.\n\n"
        "Would you use an absolute or a relative path? Why?")

    add_section_summary(prs, "Paths, Tab-Completion, Up-Arrow", [
        "Absolute paths work anywhere; relative paths depend on where you are.",
        "A path is unforgiving of a wrong character — exactness matters.",
        "Tab-completion is the biggest accuracy win — use it on every path.",
        "The up-arrow turns one good command into a reusable tool.",
    ])

    # =========================================================================
    # SECTION 8 — Commands, Flags, Help, and Knowing When to Stop
    # =========================================================================
    add_section_header(prs, "08",
        "Flags, Help, Piping,\nand When to Stop",
        "Flags change behavior; --help finds them without memorizing; pipe and redirect chain commands; Ctrl+C stops anything.",
        "[IMAGE: A control panel with options, a manual, and a clearly marked stop button]")

    add_concept_slide(prs, "Flags, Help, Glue, and the Stop Button", [
        ("Flags change a command's behavior: ls vs ls -l vs ls -la. Same command, different output.", False),
        ("Do not memorize flags — look them up: ls --help, or man ls (Mac/Linux/WSL).", False),
        ("Pipe | sends one command's output into another: ls | wc -l counts items.", False),
        ("Redirect > writes output to a file (replaces); >> appends to a file.", False),
        ("The prompt returning means the command finished. A blinking cursor with no prompt means it is still running.", False),
        ("Ctrl+C stops a running command and returns the prompt. It deletes nothing.", False),
    ], note="Ctrl+C is the most important shortcut: it sends an interrupt and stops the current process. Drill it "
            "until it is a reflex — you need this before anything else can go wrong.")

    add_hands_on(prs, "Exercises 4-6 — Help, Pipes, and a Real Scenario", [
        "Ex 4 (Help): run ls --help / Get-Help; find the hidden-files flag; build a help card for ls cd mkdir cp mv (4 of 6).",
        "Ex 5 (Piping): use >, >>, and ls | wc -l; verify with ls and by opening the file (5 of 6).",
        "Ex 6 (Scenario): make a mixed folder, list the .txt files, mkdir archive, move them in.",
        "Run ls on BOTH folders to verify the move — confirm arrivals, confirm nothing left behind.",
        "Press Ctrl+C during a long command to prove you can stop it. Transcript (6 of 6).",
    ], "[IMAGE: A short workflow chained together, ending with a verification step]")

    add_check_on_learning(prs,
        "You run a command and nothing happens for thirty seconds — the cursor just blinks.\n\n"
        "What are the two possibilities, and how do you handle each one?")

    add_section_summary(prs, "Flags, Help, Piping, and Stopping", [
        "Flags change behavior; --help and man let you find a flag without memorizing it.",
        "Pipe (|) chains commands; redirect (>, >>) captures output to a file.",
        "The prompt returning means finished; a blinking cursor means still running.",
        "Ctrl+C stops anything you start and deletes nothing — drill it to reflex.",
    ])

    # =========================================================================
    # MODULE SUMMARY TABLE
    # =========================================================================
    add_summary_table(prs,
        "MODULE SUMMARY", "Know the Terrain — Capabilities and Habits",
        [
            ["Read the terrain", "path, file tree, plaintext vs rich", "Know where things live first"],
            ["Navigate", "pwd, ls, cd, cd ..", "Never be lost; pwd resets you"],
            ["Act", "mkdir, touch/New-Item, cp, mv", "Make, copy, move — no deletion"],
            ["Aim precisely", "abs/rel paths, Tab, up-arrow", "Let the machine complete names"],
            ["Control", "flags, --help, |, >, >>, Ctrl+C", "Look it up; chain; stop anything"],
            ["Verify", "ls after every action", "Trust the disk, not the narration"],
        ],
        ["CAPABILITY", "COMMANDS / TOOLS", "THE HABIT IT BUILDS"],
        [Inches(0.45), Inches(3.3), Inches(7.7)],
        [Inches(2.8), Inches(4.4), Inches(4.6)])

    # =========================================================================
    # READINESS CHECK
    # =========================================================================
    add_readiness_check(prs, [
        "I can read a file path as a route through the folder tree",
        "I can distinguish plaintext from rich text and know why tools prefer plaintext",
        "I can navigate with pwd, ls, cd, and cd ..",
        "I can make, copy, and move files — and I have not deleted anything",
        "I use absolute and relative paths, tab-completion, and the up-arrow",
        "I can find a flag with --help, chain commands with pipes, and stop anything with Ctrl+C",
        "I verify after acting on every file operation — I trust the disk, not the narration",
    ])

    # =========================================================================
    # END SLIDE
    # =========================================================================
    add_end_slide(prs,
        "Know the Terrain:\nFilesystem &\nTerminal",
        [
            "Keep running short pwd/ls/cd reps until navigation is reflex.",
            "Carry the verify-after-acting habit forward — it is graded at the capstone.",
            "Complete all six hands-on transcripts as your module deliverable.",
            "Next module: when an agent can change files at speed, you want a logbook you can rewind — version control.",
        ])

    save_deck(prs, __file__, "05-terminal.pptx")


if __name__ == "__main__":
    build()
