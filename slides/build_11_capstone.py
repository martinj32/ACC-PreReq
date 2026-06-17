"""
ACC Module 11 — The Proving Ground: Capstone Build
Deck mirrors docs/modules/11-capstone.md.
Build with the shared Army Cyber Dark theme. DO NOT run — orchestrator builds.
"""

from acc_theme import *


def build():
    prs = new_deck()

    # ---- Title -------------------------------------------------------------
    add_title_slide(
        prs,
        "The Proving\nGround:\nCapstone Build",
        "PREREQUISITE MODULE  |  INSTRUCTOR-LED  |  2-3 DAY BLOCK",
        "[IMAGE: an operator at a range qualification table — the moment "
        "training becomes proof; everything earned, now demonstrated]",
    )

    # ---- Overview ----------------------------------------------------------
    add_overview_slide(
        prs,
        "Integrate every prior module into one real build — and prove you "
        "commanded it: a constraining CLAUDE.md, a full delegate-verify-own "
        "loop, and a clean recovery from a bad agent edit.",
        "180+ minutes  |  Graded on supervision, not just the artifact",
        [
            "Scope and plan a real, demo-able project",
            "Author a CLAUDE.md that constrains a live agent run",
            "Run one full delegate-verify-own loop on the build",
            "Recover a deliberate bad agent edit with version control",
            "Document, push, and sign for a product that is yours",
        ],
    )

    # =======================================================================
    # SECTION 01 — The Mission
    # =======================================================================
    add_section_header(
        prs, "01", "The Mission",
        "Not a tutorial project — the integration of everything, graded on how you supervised it.",
        "[IMAGE: a mission planning board with one objective circled; "
        "scoped tight enough to demo in two minutes]",
    )

    add_concept_slide(
        prs, "Choose One Build Path — Keep It Two-Minute Small",
        [
            ("Path A — CLI tool: password checker, MD-to-HTML, task logger", False),
            ("Input -> logic -> output, with a basic error handled", True),
            ("Path B — Web app: note-taker, unit converter, quote generator", False),
            ("HTML/CSS/JS, takes input, does something, runs locally", True),
            ("Path C — API integration: calls a free public API, handles errors", False),
            ("Every path, same standard:", False),
            ("README, 5+ meaningful commits, no credentials in history, on GitHub", True),
        ],
        note="The two-minute test: if you can't demo it in two minutes, it's too "
             "big. A small build cleanly supervised beats an ambitious one you "
             "never finished verifying.",
    )

    add_check_on_learning(
        prs,
        "Your project has to be impressive AND leave room to verify the agent's "
        "work inside your time budget. When those conflict, which do you protect, "
        "and why is that the right call for THIS course?",
    )

    add_hands_on(
        prs, "The Mission",
        [
            "Pick a path. Write a one-paragraph description and list 3-5 features.",
            "Apply the two-minute test out loud. Cut scope until it passes.",
            "Commit the plan: git commit -m 'Initial project plan'.",
        ],
    )

    add_section_summary(
        prs, "The Mission",
        [
            "The capstone certifies command of an agent, not hand-written code",
            "Three build paths; same standard of README, commits, and a live product",
            "Two-minute test keeps scope small enough to reach the verify loop",
            "Under-scoping is recoverable; over-scoping kills the graded loop",
        ],
    )

    # =======================================================================
    # SECTION 02 — Standing Orders (CLAUDE.md)
    # =======================================================================
    add_section_header(
        prs, "02", "Set the\nStanding Orders",
        "A CLAUDE.md that actually binds the agent — real scope, real prohibitions, real read-only files.",
        "[IMAGE: a posted operations order at the CP; the agent reads it "
        "before it touches the first file]",
    )

    add_concept_slide(
        prs, "A CLAUDE.md That Constrains a Real Run",
        [
            ("Scope boundary — what the project is AND what it is NOT", False),
            ("Hard prohibitions — 2+ enforceable 'never' rules", False),
            ("Modifiable surface — which files the agent may change vs read-only", False),
            ("Done criteria — a finish line you and the agent share", False),
            ("Conflict rule — which requirement wins (e.g. security beats speed)", False),
            ("Set up the project context exactly as in Module 10:", False),
            (".claude/ folder, your CLAUDE.md, your me.md — then confirm it's read", True),
            ("NET-NEW: the build is now an agentic deliverable, not solo coding", False),
        ],
        note="A CLAUDE.md that constrains nothing is not graded as steering. "
             "Add a real read-only file and a rule that protects it.",
    )

    add_example_slide(
        prs, "A Constraint That Earns Its Place",
        "Graded evidence that your standing orders held",
        [
            "Add a read-only file to the project, e.g. config.example.json,",
            "and a CLAUDE.md rule:",
            "",
            "  'Never modify config.example.json;",
            "   it is the reference template.'",
            "",
            "Later, ask the agent to 'update the config.'",
            "",
            "  A constrained agent refuses or asks.",
            "  An ungoverned agent edits the protected file.",
            "",
            "That single interaction is graded proof the boundary held —",
            "or proof it didn't.",
        ],
    )

    add_concept_slide(
        prs, "The Context File Is Sent to the Provider",
        [
            ("CLAUDE.md and me.md ship with every request", False),
            ("Data-handling bright line (Module 1) applies in full:", False),
            ("No real names, no real units, no credentials, nothing above the ceiling", True),
            ("Not in the project, not in context files, not in your build prompts", False),
            ("This is graded — see the rubric", True),
        ],
        note="VERIFY before delivery: the scrub discipline reaches all the way "
             "into your context files and the prompts you give the agent mid-build.",
        accent=CYBER_GOLD,
    )

    add_check_on_learning(
        prs,
        "You ask the agent to 'clean up the config,' and your CLAUDE.md marks the "
        "reference config read-only. What should a correctly governed agent do — "
        "and what does it tell you if it edits the file anyway?",
    )

    add_hands_on(
        prs, "Standing Orders",
        [
            "Create the .claude/ folder; add your CLAUDE.md and me.md.",
            "Write a CLAUDE.md: scope boundary, 2+ prohibitions, a named read-only "
            "file, done criteria, a conflict rule.",
            "Add an actual read-only file the prohibition protects.",
            "Run the agent; ask it to summarize the project; confirm it cites the "
            "CLAUDE.md.",
            "Commit: git commit -m 'Project setup with constrained context files'.",
        ],
    )

    add_section_summary(
        prs, "Standing Orders",
        [
            "A capstone CLAUDE.md must constrain a live agent, not describe it warmly",
            "At least one testable prohibition and a named read-only file",
            "Context files carry the Module 1 data-handling discipline — and it's graded",
            "The build is an agentic deliverable: the context file is part of the proof",
        ],
    )

    # =======================================================================
    # SECTION 03 — The Loop
    # =======================================================================
    add_section_header(
        prs, "03", "The Loop:\nDelegate,\nVerify, Own",
        "The graded heart of the capstone — performed deliberately and documented, not by reflex.",
        "[IMAGE: a three-station cycle diagram rendered as a fire-mission "
        "loop: call, confirm, sign for the effect]",
    )

    add_concept_slide(
        prs, "One Full Turn of the Loop, Made Explicit",
        [
            ("DELEGATE — give a concrete, bounded task with the context it needs", False),
            ("Vague order, vague result — deliberate prompting still applies", True),
            ("VERIFY — do not accept 'done' on the agent's word", False),
            ("Read the code and narrate it (Module 10); run it; confirm no rule broken", True),
            ("Check the files it CLAIMS it changed are the files it ACTUALLY changed", True),
            ("This is the 'verify after acting' reflex from M5/M7 — here it's graded", True),
            ("OWN — you sign for the result; 'the agent did it' is no defense (M9)", False),
        ],
        note="This loop is the single highest-weighted rubric item — it is the "
             "skill the whole course exists to certify.",
    )

    add_example_slide(
        prs, "Verify Against the Work, Not the Summary",
        "The diff is the evidence — the agent's 'done' is not",
        [
            "The agent reports:",
            "  'Done — added the feature and updated the tests.'",
            "",
            "Trusting that sentence is not verification.",
            "",
            "Verifying means you:",
            "  - read what the code actually does and narrate it back",
            "  - run it and confirm it does the task",
            "  - confirm it broke no prohibition from your CLAUDE.md",
            "  - read the DIFF and confirm it matches the agent's claim",
            "",
            "The most expensive capstone failures come from accepting a",
            "confident 'done' without checking the artifact underneath.",
        ],
    )

    add_check_on_learning(
        prs,
        "The agent says it changed only app.js, but the diff also shows an edit to "
        "a file your CLAUDE.md marked read-only. What does a correct OWNER do — "
        "and what does this tell you about trusting the agent's summary?",
    )

    add_hands_on(
        prs, "The Loop",
        [
            "DELEGATE: give the agent one concrete build task scoped by your CLAUDE.md.",
            "VERIFY: read and narrate the code; run it; confirm no prohibition broken; "
            "check the diff matches the agent's claim.",
            "OWN: if correct, commit with a message naming what you verified "
            "(e.g. 'Add input validation — verified rejects empty input, no protected "
            "files touched').",
            "If wrong, send it back with a specific correction.",
            "Repeat for one more feature so the loop is a habit, not a one-off.",
        ],
    )

    add_section_summary(
        prs, "The Loop",
        [
            "Delegate a bounded task, verify the work, own the result",
            "Verify against the diff, never against the agent's summary",
            "An unexpected edit to a protected file is a FAILED verification",
            "This documented loop is the highest-weighted item on the rubric",
        ],
    )

    # =======================================================================
    # SECTION 04 — The Rewind
    # =======================================================================
    add_section_header(
        prs, "04", "The Rewind:\nRecover a\nBad Edit",
        "Deliberately let an agent edit go wrong — then recover cleanly with git.",
        "[IMAGE: a duty logbook open to a prior entry; a finger marking the "
        "last known-good page to return to]",
    )

    add_concept_slide(
        prs, "The Rewind, Start to Finish",
        [
            ("Commit known-good FIRST — you can only rewind to a snapshot you took", False),
            ("This is why the loop commits after every verified feature", True),
            ("Recognize the bad edit — broken function, deleted line, protected-file edit", False),
            ("Roll back — return the file or working tree to the last good commit", False),
            ("The bad edit is undone; your verified history is intact", True),
            ("Re-issue — hand the task back with a tighter instruction, run the loop again", False),
            ("NET-NEW and graded: a deliberate bad-edit-and-recover, not a hypothetical", False),
        ],
        note="Git is the duty logbook from Module 6 — a time machine. The capstone "
             "makes you use it under the exact condition it exists for.",
    )

    add_concept_slide(
        prs, "You Can Only Recover to a Commit You Made",
        [
            ("The rewind works only if you committed known-good BEFORE the bad edit", False),
            ("That is the operational reason the loop commits after every feature", False),
            ("Skip the commits and there is nothing to rewind to", True),
            ("Frequent verified commits are what make agent supervision survivable", False),
            ("Caveat: a rewind recovers tracked files — it does NOT un-leak a secret", False),
            (".env in .gitignore before the first commit still holds (Module 10)", True),
        ],
        note="VERIFY after rollback: run the project and confirm a clean working "
             "tree before you continue. Version control saves you from bad edits, "
             "not from leaked credentials.",
        accent=CYBER_GOLD,
    )

    add_check_on_learning(
        prs,
        "An agent edit just broke your build, and you committed a working version "
        "ten minutes ago. Walk through your recovery. Then answer: what would your "
        "options be if you had NOT committed?",
    )

    add_hands_on(
        prs, "The Rewind",
        [
            "Confirm you have a verified, committed known-good state from the loop.",
            "Deliberately induce a bad edit: prompt the agent into a wrong change, or "
            "break a file by hand.",
            "Confirm the damage — run the project, see it fail or misbehave.",
            "Roll back to the last good commit; confirm a clean working tree and a "
            "working project.",
            "Re-issue the task with a tighter instruction; run the loop to a correct "
            "result.",
        ],
    )

    add_section_summary(
        prs, "The Rewind",
        [
            "An agent will break something — recovery is a reflex, not a panic",
            "You can only rewind to a known-good commit you took beforehand",
            "Frequent verified commits are what make supervision survivable",
            "A rewind fixes bad edits, not leaked secrets — .gitignore still matters",
        ],
    )

    # =======================================================================
    # SECTION 05 — Ship It
    # =======================================================================
    add_section_header(
        prs, "05", "Ship It:\nDocument,\nPush, Sign",
        "Finish the way every real deliverable ends — a clean README, a clean history, an accountable sign-off.",
        "[IMAGE: a completed product tag being signed and dated; the work "
        "becomes something someone else can use and you can be held to]",
    )

    add_concept_slide(
        prs, "Deliver and Take Accountability",
        [
            ("DOCUMENT — README: what it does, how to run it, requirements", False),
            ("Comment any logic that isn't self-evident", True),
            ("PUSH — verify commits are local, push to GitHub, confirm it appears", False),
            ("FINAL SCRUB — no real names, no credentials, no .env in history", False),
            ("The bright line does not relax at the finish line", True),
            ("SIGN — you vouch for the product; the Module 9 authorship duty", False),
        ],
        note="A credential in a public repo is compromised the moment it lands. If "
             "you find one, it's already in history — rotate it and clean the repo, "
             "don't just delete the file.",
    )

    add_check_on_learning(
        prs,
        "You are about to push. What is the last check you run before the "
        "repository goes public, and why can it not wait until after the push?",
    )

    add_hands_on(
        prs, "Ship It",
        [
            "Write the README: what it does, how to run it, requirements.",
            "Comment any logic that is not self-evident.",
            "Final scrub for names, credentials, and .env in history.",
            "Push to GitHub; confirm the repo is visible with full commit history.",
            "Write a one-line sign-off: what you built, what you verified, that you "
            "stand behind it.",
        ],
    )

    add_section_summary(
        prs, "Ship It",
        [
            "README + clean pushed history makes the work a real, usable product",
            "Final scrub for secrets before the push — not after",
            "A leaked credential is compromised on landing; rotate, don't just delete",
            "Signing is the Module 9 authorship duty applied to the whole artifact",
        ],
    )

    # =======================================================================
    # The Rubric (as a summary table) + Readiness + End
    # =======================================================================
    add_summary_table(
        prs,
        "THE RUBRIC",
        "Weighted toward supervision — verified modest build beats un-supervised impressive one",
        [
            ["Delegate-verify-own loop", "30 pts",
             "One full documented loop: task, diff-check vs claim, ownership"],
            ["CLAUDE.md constrained the run", "15 pts",
             "Testable prohibition + scope boundary that steered the agent"],
            ["Git rewind of a bad edit", "15 pts",
             "Deliberate bad edit recovered to known-good; clean tree shown"],
            ["Data-handling & ethics", "15 pts",
             "No names/units/creds; no .env in history; accountable sign-off (M9)"],
            ["Working artifact", "15 pts",
             "Runs, does what it promised, basic error handling"],
            ["Docs & commits", "10 pts",
             "Clear README; 5+ meaningful commits; pushed to GitHub"],
        ],
        ["CRITERION", "WEIGHT", "EVIDENCE"],
        [Inches(0.45), Inches(4.0), Inches(5.5)],
        [Inches(3.5), Inches(1.4), Inches(6.9)],
    )

    add_readiness_check(
        prs,
        [
            "My capstone runs and does what it promised, with basic error handling",
            "My CLAUDE.md has a testable prohibition that demonstrably steered the agent",
            "I ran and documented at least one full delegate-verify-own loop",
            "I verified the diff against the agent's claim, not just its summary",
            "I deliberately recovered a bad agent edit to a known-good commit",
            "No real names, units, or credentials anywhere; no .env in history",
            "5+ meaningful commits, clear README, pushed and visible on GitHub",
            "I wrote an accountable sign-off vouching for the output",
        ],
    )

    add_end_slide(
        prs,
        "The Proving\nGround:\nCapstone Build",
        [
            "Confirm your loop, your rewind, and your sign-off are documented",
            "Submit the GitHub repo with the full commit history",
            "Proceed to Module 12 — Crossing the LD: Bridge to Advanced Agentics",
        ],
    )

    save_deck(prs, __file__, "11-capstone.pptx")


if __name__ == "__main__":
    build()
