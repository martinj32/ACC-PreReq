"""
ACC Module 06 — The Duty Logbook: Version Control with Git
Slide deck builder. Uses the shared Army Cyber Dark theme.

Run by the orchestrator (python is blocked for the authoring agent):
    python build_06_version_control.py
Output: slides/Finished/06-version-control.pptx
"""

from acc_theme import *


def build():
    prs = new_deck()

    # --- TITLE ---
    add_title_slide(prs,
        "The Duty Logbook:\nVersion Control\nwith Git",
        "PREREQUISITE MODULE  |  2-3 HOUR BLOCK",
        "[IMAGE: A watch duty logbook open on a desk, every entry timestamped and signed]")

    # --- OVERVIEW ---
    add_overview_slide(prs,
        "Version control is a duty logbook of every change you can rewind. When an agent can edit your files at "
        "speed, the logbook is how you keep accountability — and undo any change. This module turns the concept "
        "into commands you run for real.",
        "2-3 hour block (about 110 min hands-on)",
        [
            "Explain version control as a duty logbook of changes you can rewind",
            "Initialize a repo and record snapshots with add, commit, log, and diff",
            "Create a branch, merge it, and resolve a merge conflict by hand",
            "Write a .gitignore BEFORE the first commit to keep credentials out of history",
            "Push to GitHub and review a pull request diff before merging",
        ])

    # =========================================================================
    # SECTION 1 — Why Version Control Exists
    # =========================================================================
    add_section_header(prs, "01",
        "Why Version\nControl Exists",
        "When an agent can change your files, you want a logbook of every change — and the ability to go back.",
        "[IMAGE: A fast-moving teammate making entries while a supervisor reviews the running log]")

    add_concept_slide(prs, "Version Control Is the Duty Logbook", [
        ("Every file change records a snapshot: what changed, when, and a note about why.", False),
        ("Stored locally. Every snapshot can be rewound.", False),
        ("The duty logbook: every change recorded — what, when, why, who.", False),
        ("An agent does the same file operations you learned — at speed, on many files, sometimes unprompted.", False),
        ("The logbook keeps accountability over a teammate who works fast and never sleeps.", False),
        ("Local layer: your machine keeps the record — rewind any snapshot, no internet needed.", True),
        ("Remote layer: the same history synced to GitHub — backup, and the way teammates share files.", True),
    ], note="Why software people seem to remember everything: they do not — they have the log. 'Who changed this "
            "and when?' is a two-second lookup. The logbook is doing the remembering.")

    add_hands_on(prs, "Load the Reason First", [
        "Think about a file you have edited multiple times over the past month.",
        "Ask: if I needed to see what it looked like three weeks ago, could I?",
        "Ask: if something went wrong, what would I lose?",
        "That gap — between what you want to recover and what you can recover — is what version control fills.",
        "No commands yet. The commands come next, once the reason is loaded.",
    ], "[IMAGE: A soldier mentally tracing edits to a document with no record to fall back on]")

    add_check_on_learning(prs,
        "An agent just ran a batch edit on 40 files. You look at one and it is not right.\n\n"
        "Without version control, what are your options?\n\n"
        "With version control, what changes?")

    add_section_summary(prs, "Why Version Control Exists", [
        "Version control records every change as a rewindable snapshot — what, when, why, who.",
        "It is a duty logbook for a teammate who works fast and never sleeps.",
        "Local layer keeps the record offline; remote layer (GitHub) backs it up and enables sharing.",
        "It matters the moment an agent gets write access to your files.",
    ])

    # =========================================================================
    # SECTION 2 — Your First Repository
    # =========================================================================
    add_section_header(prs, "02",
        "Your First Repository:\nCommit, Log, Diff",
        "Stage the changes you want to record, commit them with a message, and Git keeps that snapshot forever.",
        "[IMAGE: A first logbook entry being written and signed at the start of a watch]")

    add_concept_slide(prs, "The Three States of a Change", [
        ("A repository is a folder Git is tracking. git init starts watching it.", False),
        ("Working directory: your files as they are now — edited, not yet recorded.", False),
        ("Staging area: the changes you selected for the next snapshot (git add).", False),
        ("Committed: a permanent snapshot in the logbook (git commit).", False),
        ("git add selects what goes in; git commit takes the snapshot and writes the entry.", False),
        ("git status shows changes; git log shows history; git diff shows what changed.", False),
        ("Commit messages are documentation: present tense, action-focused, informative.", False),
    ], note="Three commands get you 90% of the way: git add, git commit, git push. Look up flags with git --help "
            "— real developers do this constantly. Run git status between every step to watch a change move states.")

    add_example_slide(prs,
        "Bad vs Good Commit Messages",
        "A message tells future-you what changed without opening the file",
        [
            "BAD:",
            '  "fix stuff"',
            '  "update"',
            '  "work"',
            "",
            "GOOD:",
            '  "Add authentication logic to login form"',
            '  "Fix off-by-one error in pagination"',
            "",
            "Good = present tense, action-focused, tells you what changed.",
            "The logbook is only useful if the entries are readable.",
        ],
        "[IMAGE: Two logbook pages — one with illegible scrawl, one with clear timestamped entries]")

    add_hands_on(prs, "Exercise 1 — Your First Repository", [
        "Create a folder, cd into it, run git init.",
        "Create README.md with a line of content. Run git status — see it untracked.",
        "git add README.md, then git status again — watch it move to staged.",
        "git commit -m \"Add project README\". Run git log to see the entry.",
        "Edit the file, git add and git commit again. Run git diff and read the change. Save a transcript.",
    ], "[IMAGE: A change moving working dir -> staging -> committed, three clear stations]")

    add_check_on_learning(prs,
        "You edited three files but only want to record changes to one of them in this snapshot.\n\n"
        "Which command controls what goes into the commit, and how?")

    add_section_summary(prs, "Your First Repository", [
        "A repo is a folder Git tracks; git init starts it.",
        "Three states: working directory -> staged (git add) -> committed (git commit).",
        "git log reads history; git diff shows what changed between snapshots.",
        "Commit messages are documentation — write them present tense and action-focused.",
    ])

    # =========================================================================
    # SECTION 3 — Branching, Merging, and Resolving a Conflict
    # =========================================================================
    add_section_header(prs, "03",
        "Branching, Merging,\nand Conflicts",
        "A branch is parallel work you can experiment on without touching main; merging folds it back; conflicts you resolve by hand.",
        "[IMAGE: Two parallel lines of work diverging from a main line and folding back together]")

    add_concept_slide(prs, "Branches, Merges, and Conflict Markers", [
        ("A branch is a movable pointer to a line of commits. main is the default.", False),
        ("git branch <name> creates it; git switch <name> moves onto it.", True),
        ("Your commits go on the branch; main stays untouched until you merge.", False),
        ("git merge <name> folds a branch's changes into the current branch.", False),
        ("A merge conflict happens when two branches change the same line of the same file.", False),
        ("Git stops and marks the conflict: <<<<<<<  =======  >>>>>>>", True),
        ("Edit to the version you want, delete the markers, git add and git commit to finish.", True),
    ], note="Git is a time machine: every commit is a snapshot. Try an idea on a branch, merge it if it works, "
            "throw it away if it does not. Branches make experimentation free.")

    add_concept_slide(prs, "A Conflict Is Not an Emergency", [
        ("A conflict is Git telling you it needs a human decision — not that something broke.", False),
        ("Walk through one slowly the first time. After one practice conflict, it stops being scary.", False),
        ("This is the SAME review you do when an agent hands you a branch.", False),
        ("If the agent's branch touches files you also changed, you resolve it exactly this way.", False),
        ("git branch -d <name> deletes a branch once it is merged.", False),
    ])

    add_hands_on(prs, "Exercise 2 — Branching Sprint + Merge Conflict", [
        "On main, create a file and commit it.",
        "Create branch feature/add-content, switch to it, change the file, commit.",
        "Switch back to main, verify unchanged, then git merge feature/add-content. Delete the branch.",
        "Force a conflict: two branches from main each edit the SAME line of one file.",
        "Merge the first (succeeds), merge the second (conflict). Resolve markers, git add, git commit. Transcript.",
    ], "[IMAGE: A soldier reconciling two conflicting field reports into one agreed version]")

    add_check_on_learning(prs,
        "You merge a branch and Git reports a conflict in one file.\n\n"
        "What does that mean Git is asking you to do, and what are the three markers it left in the file?")

    add_section_summary(prs, "Branching, Merging, and Conflicts", [
        "A branch is isolated work; main stays intact until you merge.",
        "git branch / git switch / git merge / git branch -d cover the workflow.",
        "A merge conflict is a request for a human decision, not a failure.",
        "Resolving a conflict by hand is the same skill as reviewing an agent's branch.",
    ])

    # =========================================================================
    # SECTION 4 — .gitignore First, Then Push
    # =========================================================================
    add_section_header(prs, "04",
        ".gitignore First,\nThen Push",
        ".gitignore tells Git which files to never track — and you create it BEFORE the first commit, because too late equals never.",
        "[IMAGE: A redaction stamp applied to documents before they ever enter the official record]")

    add_concept_slide(prs, "The OPSEC Enforcement Layer", [
        (".gitignore is a plaintext file listing patterns Git should never track.", False),
        ("Anything matching a pattern is never staged, never committed, never reaches the remote.", False),
        ("Minimum entries: .env  *.key  *credentials*  .DS_Store  __pycache__/  .venv/  node_modules/", True),
        ("The remote: GitHub hosts a copy. git push sends commits up; git pull brings teammates' down.", False),
        ("A pull request (PR) proposes a merge with a reviewable diff — the quality gate for agent work.", False),
        ("When an agent changes files on a branch, the PR is how you review it line by line before main.", True),
    ], note="This is the data-handling bright line from Module 1, enforced at the tool level. Same discipline, "
            "now built into the workflow.")

    add_example_slide(prs,
        "Why Sequence Is Load-Bearing",
        "DANGER: create .gitignore BEFORE your first commit",
        [
            "If a credential file is committed first, adding it to .gitignore",
            "later does NOT remove it from history. The file stays recoverable",
            "by anyone with the repo.",
            "",
            "Deleting it in a new commit does not erase it — the earlier",
            "snapshot still holds it. Rewriting published history is painful",
            "and unreliable.",
            "",
            "The only safe move: never commit it. That is what .gitignore",
            "is for, and that is why it comes FIRST. This is not a",
            "recoverable mistake.",
        ],
        "[IMAGE: A leaked credential in an old logbook page — visible no matter what later pages say]")

    add_hands_on(prs, "Exercise 3 — .gitignore and Push", [
        "In a new repo, BEFORE any commit, create .gitignore: .env, credential patterns, .DS_Store, __pycache__/, .venv/.",
        "Create a fake .env with a dummy secret. Run git status — confirm .env does NOT appear.",
        "Make your real first commit (README and code, not the secret).",
        "Create a GitHub repo (gh repo create), then git push. Confirm commits appear on GitHub.",
        "Optional: push a branch, gh pr create, review the diff, merge. Build the repo to 5+ commits — that is the deliverable.",
    ], "[IMAGE: A pre-flight checklist completed before anything leaves the wire]")

    add_check_on_learning(prs,
        "You accidentally committed a .env file with a real credential and pushed it.\n\n"
        "Why is deleting the file in a new commit not enough, and what should you have done to prevent this?")

    add_section_summary(prs, ".gitignore First, Then Push", [
        ".gitignore lists patterns Git never tracks — keep credentials and junk out of the logbook.",
        "Create it BEFORE the first commit: once in history, .gitignore later does not remove it.",
        "git push backs the repo up to GitHub; git pull brings shared changes down.",
        "A PR diff is the review gate — the way you check an agent's changes before they touch main.",
    ])

    # =========================================================================
    # MODULE SUMMARY TABLE
    # =========================================================================
    add_summary_table(prs,
        "MODULE SUMMARY", "The Duty Logbook — Concepts and Commands",
        [
            ["The logbook", "git init, git status", "A repo records every change"],
            ["Make an entry", "git add, git commit, git log, git diff", "Stage, snapshot, read history"],
            ["Parallel work", "git branch, git switch, git merge", "Try changes in isolation"],
            ["Resolve conflict", "edit markers, git add, git commit", "A human decision, not a failure"],
            ["OPSEC layer", ".gitignore BEFORE first commit", "Keep credentials out of history"],
            ["Remote + review", "git push, gh pr create, PR diff", "Back up, share, review agent work"],
        ],
        ["CONCEPT", "COMMANDS", "THE POINT"],
        [Inches(0.45), Inches(3.2), Inches(8.2)],
        [Inches(2.7), Inches(5.0), Inches(4.1)])

    # =========================================================================
    # READINESS CHECK
    # =========================================================================
    add_readiness_check(prs, [
        "I can explain version control as a duty logbook of changes I can rewind",
        "I can init a repo and record snapshots with add, commit, log, and diff",
        "I write commit messages in present tense, action-focused",
        "I can create a branch, merge it, and resolve a conflict by hand",
        "My .gitignore exists BEFORE any commit and excludes .env and credential files",
        "I confirmed ignored files do not appear in git status before pushing",
        "I can push to GitHub and read a PR diff before merging — the review gate for agent work",
        "My repository has five or more commits and a successful push",
    ])

    # =========================================================================
    # END SLIDE
    # =========================================================================
    add_end_slide(prs,
        "The Duty Logbook:\nVersion Control\nwith Git",
        [
            "Keep using the logbook on every project — commit early, commit often, write readable messages.",
            "Always create .gitignore before the first commit. Too late is the same as never.",
            "Build your repo to five or more commits with a successful push as the module deliverable.",
            "Next module: with terrain mapped and the logbook running, move from advising a model to commanding an agent.",
        ])

    save_deck(prs, __file__, "06-version-control.pptx")


if __name__ == "__main__":
    build()
