"""
ACC Module 10 — Field Craft: Markdown, Code, Tools & Context Files
Deck mirrors docs/modules/10-field-craft.md.
Build with the shared Army Cyber Dark theme. DO NOT run — orchestrator builds.
"""

from acc_theme import *


def build():
    prs = new_deck()

    # ---- Title -------------------------------------------------------------
    add_title_slide(
        prs,
        "Field Craft:\nMarkdown, Code,\nTools & Context",
        "PREREQUISITE MODULE  |  SELF-PACED",
        "[IMAGE: an operator's field kit laid out on a poncho — notebook, "
        "multitool, radio — each item labeled; the craft behind the mission]",
    )

    # ---- Overview ----------------------------------------------------------
    add_overview_slide(
        prs,
        "Four pieces of field craft — clean documents, code-literacy, a verified "
        "toolbox, and context files — turn a commander of agents into one whose "
        "work holds up.",
        "Self-paced  |  Consolidates four foundational skill blocks",
        [
            "Write structured Markdown and avoid the errors that break it",
            "Read and reason about basic code well enough to verify it",
            "Install, authenticate, and verify the developer toolbox",
            "Author a CLAUDE.md and me.md that steer a real agent",
        ],
    )

    # =======================================================================
    # SECTION 01 — Markdown
    # =======================================================================
    add_section_header(
        prs, "01", "Markdown:\nThe Lingua Franca",
        "Your READMEs, prompts, and context files are all Markdown — write it right.",
        "[IMAGE: a typed field message on the left rendering into a clean "
        "formatted brief on the right; plain marks becoming structure]",
    )

    add_concept_slide(
        prs, "Markdown — A Few Marks, Used Everywhere",
        [
            ("Plain text plus formatting marks a renderer turns into clean output", False),
            ("Headers: # through ###### — a SPACE is required after the #", False),
            ("Emphasis: **bold**, *italic*, `inline code`", False),
            ("Lists: - or 1. — a BLANK LINE is required before the list", False),
            ("Code blocks: triple backticks, optional language hint (```python)", False),
            ("Tables: header row + separator row |---|---| (separator mandatory)", False),
            ("Links: [text](url); task lists: - [ ] and - [x]", False),
            ("Course standard: GitHub Flavored Markdown (GFM)", True),
        ],
        note="The formatting IS the structure. Break it and the model reads a wall "
             "of text instead of structured instruction.",
    )

    add_concept_slide(
        prs, "The Four Rules That Cause Most Errors",
        [
            ("Space required between # and heading text", False),
            ("Blank line required before any list", False),
            ("Blank line required before a fenced code block", False),
            ("Tables require a header row AND a separator row", False),
            ("Smart-quote trap: never draft Markdown in Word or Google Docs —", False),
            ("curly quotes silently break code blocks; write in VS Code", True),
        ],
        note="VERIFY: use the VS Code preview pane (Ctrl+Shift+V) to confirm a "
             "document renders before you hand it to an agent.",
        accent=CYBER_GOLD,
    )

    add_example_slide(
        prs, "Same Content, Two Renders",
        "The blank line and the space after ## are load-bearing",
        [
            "WITH correct spacing:",
            "",
            "  ## Rules",
            "  (blank line)",
            "  - Never include real names",
            "  - Flag incomplete entries",
            "",
            "  -> a heading and two discrete rules the model obeys",
            "",
            "WITHOUT the blank line / the space:",
            "",
            "  ##Rules",
            "  - Never include real names- Flag incomplete entries",
            "",
            "  -> one run-on paragraph parsed as a single instruction",
        ],
    )

    add_check_on_learning(
        prs,
        "You write '#Mission Brief' at the top of a file and it renders as plain "
        "text instead of a large heading. What is the single fix — and what habit "
        "would have caught it before you handed the file off?",
    )

    add_hands_on(
        prs, "Markdown",
        [
            "Open VS Code; create README.md and open the preview (Ctrl+Shift+V).",
            "Write a personal README: h1 name, 3-item bullet list, one bold term, "
            "one inline-code term, one fenced code block.",
            "Add a 2-tool comparison table with a header and separator row; confirm "
            "it renders.",
            "Deliberately break one rule, watch the preview break, then fix it.",
            "Save the file — you reuse it later.",
        ],
    )

    add_section_summary(
        prs, "Markdown",
        [
            "Markdown is plain text plus a small set of formatting marks",
            "Four spacing rules cause the overwhelming majority of errors",
            "Smart quotes from Word/Docs silently break code — write in VS Code",
            "Your authority travels in Markdown; correct formatting is field craft",
        ],
    )

    # =======================================================================
    # SECTION 02 — Programming Concepts
    # =======================================================================
    add_section_header(
        prs, "02", "Programming:\nReading the Output",
        "You don't need to write production code — you need to read what the agent writes.",
        "[IMAGE: an operator tracing a printed script line by line with a "
        "red pen, the way you'd check a fire-mission worksheet]",
    )

    add_concept_slide(
        prs, "A Small Vocabulary Covers Most of It",
        [
            ("Variables — a named container for a value (count = 0)", False),
            ("Types: strings, numbers, booleans, arrays/lists, objects", True),
            ("Operators — arithmetic, comparison (==, <, >), logical (and/or/not)", False),
            ("Conditionals — if / else: branch on whether something is true", False),
            ("Loops — for / while: repeat a block", False),
            ("Watch for off-by-one errors and infinite loops", True),
            ("Functions — a named, reusable block with inputs and an output", False),
            ("Pseudocode first: write the steps in plain English, then translate", False),
        ],
        note="To verify agent code, narrate each block back into plain English. "
             "If you can't narrate it, you can't verify it.",
    )

    add_example_slide(
        prs, "Read This Function",
        "Verify the logic without writing a line",
        [
            "function isStrongPassword(pw) {",
            "  if (pw.length < 8) {",
            "    return false;",
            "  }",
            "  return true;",
            "}",
            "",
            "Narrate it:",
            "  'Take a password. If shorter than 8 characters, fail.",
            "   Otherwise, pass.'",
            "",
            "You just verified the logic. Now the operator's question:",
            "  is 'length 8+' actually a STRONG rule?",
            "  Reading is step one. Judging correctness is your job.",
        ],
    )

    add_check_on_learning(
        prs,
        "An agent hands you a 30-line script. Before you run it or sign for it, "
        "what is the first thing you do — and which rule from Module 9 does skipping "
        "that step violate?",
    )

    add_hands_on(
        prs, "Programming Concepts",
        [
            "Write pseudocode for a grade calculator (scores in -> average + letter "
            "grade out). Steps only, no syntax.",
            "Predict the output of a for-loop printing 1 through 5; then say what "
            "changes if the bound is off by one.",
            "Given a while-loop whose condition never changes, identify why it runs "
            "forever and the one line that fixes it.",
            "Take a function an AI wrote for you earlier; narrate each block in plain "
            "English. Flag any block you can't narrate — that's your verify gap.",
        ],
    )

    add_section_summary(
        prs, "Programming Concepts",
        [
            "The bar is reading literacy, not authorship",
            "Variables, conditionals, loops, functions cover most of what you read",
            "Pseudocode first; narrate agent code back into plain English to verify",
            "You cannot responsibly sign for output you cannot read",
        ],
    )

    # =======================================================================
    # SECTION 03 — Developer Tools
    # =======================================================================
    add_section_header(
        prs, "03", "Developer Tools:\nThe Toolbox",
        "Install, authenticate, and verify the kit before you need it — not when it fails.",
        "[IMAGE: a pre-mission equipment layout, each tool checked off on a "
        "clipboard; green ticks down the column]",
    )

    add_concept_slide(
        prs, "The Core Toolbox — Each Tool, One Role",
        [
            ("Claude Code — the agentic harness; verify: claude --version", False),
            ("gh (GitHub CLI) — auth + pull requests; gh auth login (HTTPS), gh auth status", False),
            ("git — the version-control engine (Module 6 duty logbook); git --version", False),
            ("VS Code — the editor; add WSL + Markdown Preview; code --version", False),
            ("Node.js or Python — the runtime; node --version / python --version", False),
            ("PATH & 'command not found' — usually means restart the terminal", False),
            ("Find a command with which (or where on native Windows)", True),
            (".env files hold secrets per project — never commit them", False),
        ],
        note="Run every --version check in one pass BEFORE a project. A green "
             "checklist up front saves the session that dies on a missing tool.",
    )

    add_concept_slide(
        prs, ".env Goes in .gitignore BEFORE the First Commit",
        [
            ("A credential committed even once stays in git history forever", False),
            ("Adding it to .gitignore afterward does NOT remove it", True),
            ("Create .gitignore with .env in it before the first commit", False),
            ("Same OPSEC-enforcement rule as Module 6 — not recoverable", True),
            ("The data-handling bright line from Module 1 reaches your config files", False),
        ],
        note="VERIFY: after creating .env, run git status and confirm it does NOT "
             "appear before you ever commit.",
        accent=CYBER_GOLD,
    )

    add_check_on_learning(
        prs,
        "You install a new CLI tool, then immediately get 'command not found.' "
        "Before assuming the install failed, what is the first thing to try, and "
        "what concept explains why it works?",
    )

    add_hands_on(
        prs, "Developer Tools",
        [
            "Run the full sweep: claude / git / gh / code --version and node (or "
            "python) --version. Record each result.",
            "For any failure, diagnose with which/where; if it's right after an "
            "install, restart the terminal and retry.",
            "Authenticate GitHub: gh auth login (HTTPS), then confirm gh auth status.",
            "In a practice folder, create .gitignore with .env in it FIRST, then a "
            ".env with a dummy key; confirm git status hides it.",
        ],
    )

    add_section_summary(
        prs, "Developer Tools",
        [
            "Each tool has one role: model writes, git tracks, GitHub stores, editor edits",
            "Verify the whole toolbox with --version checks up front",
            "'Command not found' usually means PATH — restart the terminal first",
            ".env in .gitignore before the first commit; a leaked credential is not recoverable",
        ],
    )

    # =======================================================================
    # SECTION 04 — Context Files
    # =======================================================================
    add_section_header(
        prs, "04", "Context Files:\nStanding Orders",
        "CLAUDE.md = what to build. me.md = how you work. Constraints are the deliverable.",
        "[IMAGE: a posted standing-orders board at a unit CP; every shift "
        "reads it on relief without a re-brief]",
    )

    add_concept_slide(
        prs, "Two Files Steer the Agent Before You Type",
        [
            ("CLAUDE.md — WHAT to build: scope, hard rules, modifiable files, 'done'", False),
            ("Crucially: what the project is NOT (the scope boundary)", True),
            ("me.md — HOW you work: role, comms preference, decision style", False),
            ("Both are Markdown — ## headers become distinct instruction blocks", False),
            ("Constraints are the deliverable: the strongest line is a prohibition", False),
            ("'Never modify schema.sql.' 'Use the template; invent no sections.'", True),
            ("Ask of every draft: what should the agent NOT do? What's out of scope?", False),
            ("Same idea as Module 4 personalizing — now at version-controlled file scale", False),
        ],
        note="A CLAUDE.md that constrains nothing steers nothing. If it has no "
             "prohibition, it's documentation, not steering.",
    )

    add_example_slide(
        prs, "A CLAUDE.md That Actually Constrains",
        "Every rule enforceable, every boundary explicit",
        [
            "# Project: Daily Brief Generator",
            "",
            "## What this does",
            "Pulls the unit's daily log and produces a formatted brief.",
            "",
            "## Rules",
            "- Never include real names in output — use [NAME]",
            "- Use the provided template; do not invent new sections",
            "- Flag any entry with incomplete location or time data",
            "",
            "## Files",
            "- brief-template.md — output template (read-only, never modify)",
            "- input-log.txt — the daily log to process",
            "",
            "Compare to 'build me a nice brief tool' — nothing to obey.",
        ],
    )

    add_concept_slide(
        prs, "Context Files Are Sent to the Provider",
        [
            ("A CLAUDE.md / me.md ships with every request, like Module 4 custom instructions", False),
            ("Data-handling bright line (Module 1): nothing sensitive or above the ceiling", False),
            ("Ammunition discipline (Module 8): every line spends context budget — keep tight", False),
            ("Make it conflict-aware: state which wins when requirements collide", False),
            ("e.g. 'when speed and security conflict, security wins'", True),
        ],
        note="VERIFY: this is the SAME discipline from Modules 1, 4, and 8 at file "
             "scale — not a new rule and not a re-teach.",
        accent=CYBER_GOLD,
    )

    add_check_on_learning(
        prs,
        "Two operators write a CLAUDE.md for the same project. One is a warm "
        "paragraph describing the goal; the other names three things the agent must "
        "never do. Which one actually changes the agent's behavior, and why?",
    )

    add_hands_on(
        prs, "Context Files",
        [
            "Write a me.md (5-10 lines): role, comms preference, decision style, one "
            "always-do and one never-do.",
            "Write a CLAUDE.md for a unit task manager: what it is, what it is NOT, "
            "2+ hard rules, modifiable files, 1+ read-only file, success criteria.",
            "Add a one-line conflict-resolution rule (e.g. security beats speed).",
            "Place both in a project folder, run the agent, ask it to summarize the "
            "project — confirm it references your CLAUDE.md.",
            "Re-read and underline every genuine prohibition; if none, rewrite until "
            "there is at least one.",
        ],
    )

    add_section_summary(
        prs, "Context Files",
        [
            "CLAUDE.md tells the agent what to build; me.md tells it how you work",
            "Constraints and scope boundaries are what actually steer behavior",
            "Markdown formatting determines whether the model reads structure or mush",
            "Same data-handling and context-cost discipline as Modules 1, 4, and 8",
        ],
    )

    # =======================================================================
    # Module Summary Table + Readiness + End
    # =======================================================================
    add_summary_table(
        prs,
        "MODULE SUMMARY",
        "Field Craft — the four skills behind the mission",
        [
            ["Markdown", "Plain text + a few marks; 4 spacing rules cause most errors",
             "Your authority travels in Markdown — write it right"],
            ["Programming", "Variables, conditionals, loops, functions; pseudocode first",
             "Read what the machine writes well enough to verify it"],
            ["Dev Tools", "Install, authenticate, verify the whole toolbox up front",
             "Green checklist before the build, not a failure mid-build"],
            ["Context Files", "CLAUDE.md = what to build; me.md = how you work",
             "Constraints steer the agent; none means it steers nothing"],
        ],
        ["AREA", "WHAT IT IS", "OPERATOR TAKEAWAY"],
        [Inches(0.45), Inches(2.7), Inches(7.4)],
        [Inches(2.2), Inches(4.6), Inches(4.9)],
    )

    add_readiness_check(
        prs,
        [
            "I can write Markdown with 5+ syntax elements and spot a spacing violation",
            "I can read a short function and narrate its logic in plain English",
            "Every tool passes its --version check and GitHub is authenticated",
            "My .gitignore excludes .env and was created before the first commit",
            "My CLAUDE.md names what the project is NOT and has a genuine prohibition",
            "The agent reads my context files and references them when asked",
        ],
    )

    add_end_slide(
        prs,
        "Field Craft:\nMarkdown, Code,\nTools & Context",
        [
            "Stage your README, me.md, and CLAUDE.md for the capstone",
            "Confirm your full toolbox is green before you build",
            "Proceed to Module 11 — The Proving Ground: Capstone Build",
        ],
    )

    save_deck(prs, __file__, "10-field-craft.pptx")


if __name__ == "__main__":
    build()
