"""
ACC Module 07 — From Advisor to Operator: Commanding an Agent
Slide deck builder. Mirrors docs/modules/07-commanding-an-agent.md.

Sources folded in: agent-concepts.md (Chatbot vs Agent, Supervisor Mindset) and
mental-models core-content.md (harness, tool calls, operator posture, worked
examples, identify-the-models exercise). The harness and operator treatments are
de-duplicated into ONE clean treatment each.
"""

from acc_theme import *
from pptx.util import Inches


def build():
    prs = new_deck()

    # ---------------------------------------------------------------- TITLE
    add_title_slide(prs,
        "From Advisor\nto Operator:\nCommanding\nan Agent",
        "PREREQUISITE MODULE  |  SELF-PACED",
        "[IMAGE: Soldier at a command post terminal in a supervisory posture, "
        "overseeing an automated system working on screen]")

    # ------------------------------------------------------------- OVERVIEW
    add_overview_slide(prs,
        "A chatbot gives advice; an agent takes action. This module gives you the "
        "harness (what turns an engine into an agent), the operator posture agentic "
        "work depends on, and the delegate-verify-own loop you will run on every task.",
        "Self-paced module (prerequisites: Terminal, Version Control)",
        [
            "Explain the harness and name the engine-harness-operator stack",
            "State the one-line difference between a chatbot and an agent",
            "Describe what read, write, and execute access means in practice",
            "Explain how tool calls let you verify instead of trust",
            "State the three duties of the operator: delegate, verify, own",
            "Run the delegate-verify-own loop on a real task",
        ])

    # ======================================================================
    # SECTION 1 — The Harness
    # ======================================================================
    add_section_header(prs, "01", "The Harness",
        "A chatbot gives advice. An agent takes action. The harness is the tool layer "
        "that gives a text-only engine eyes, hands, and a body on your real machine.",
        "[IMAGE: Soldier asking for directions versus a soldier leading the patrol — "
        "advisor vs. actor]")

    add_concept_slide(prs, "What Turns an Engine Into an Agent", [
        ("Ask a chatbot to rename a folder — it tells you the command.", False),
        ("Ask an agent — it renames the folder. That is the entire difference.", False),
        ("The engine (Module 1) is a brain in a jar: it reads text and writes text.", False),
        ("The harness gives that engine three things:", False),
        ("Eyes — tools to read files, list directories, check git, fetch URLs", True),
        ("Hands — tools to write files, create directories, modify code", True),
        ("A body — tools to execute commands, run tests, move files", True),
        ("Engine + Harness (sensors and actuators) = Agency.", False),
    ], note="The three levels of access you grant: READ (look at files), WRITE "
            "(create and modify files), EXECUTE (run commands in your terminal).")

    add_concept_slide(prs, "The Engine-Harness-Operator Stack", [
        ("Engine — the LLM: reasons, generates, plans.", False),
        ("Harness — the tool layer: gives the engine reach into files, "
         "commands, and external systems.", False),
        ("Operator — you: direct the mission, approve consequential actions, "
         "own the result.", False),
        ("The engine cannot act without a harness.", True),
        ("The harness cannot direct without an operator.", True),
        ("All three are required. Everything in advanced agentic work "
         "stacks on this primitive.", True),
    ], note="This is the payoff for Terminal Basics. Every command students learned — "
            "pwd, ls, cd, mkdir, mv — is what the agent runs in their filesystem. "
            "Vocabulary drifts in the wild (Anthropic says 'model + tools + orchestration "
            "layer'); same concepts.")

    add_check_on_learning(prs,
        "You give the engine a mission: search 200 field reports for grid 38SMB4521 "
        "and return every matching excerpt.\n\n"
        "Without a harness, it can only generate plausible-sounding excerpts from "
        "memory — and you cannot tell which it did.\n\n"
        "With a harness, it calls tools against the actual files and returns real, "
        "traceable results.\n\n"
        "What does that difference mean for how you verify the output?")

    add_hands_on(prs, "Chatbot vs Agent (do this ONCE)", [
        "Open your AI chatbot (Claude web, ChatGPT, or equivalent).",
        "Ask it: 'Rename the folder project to project-v1.' Read the response — did it "
        "rename anything or tell you how?",
        "If Claude Code is available, open it in a project folder and ask the same thing.",
        "Watch: does it call a tool? Ask for confirmation? Does the folder change on disk?",
        "Write one sentence: what was different? Which response DID the work?",
    ], "[IMAGE: Soldier comparing two radio responses — one with instructions, "
       "one with a completed action report]")

    add_section_summary(prs, "The Harness", [
        "A chatbot gives advice. An agent takes action — that is the entire difference.",
        "The harness gives a text-only engine eyes, hands, and a body: read, write, execute.",
        "Engine + harness + operator = the complete agentic system; all three required.",
        "You are extending real trust. The operator posture is what keeps it responsible.",
    ])

    # ======================================================================
    # SECTION 2 — Tool Calls
    # ======================================================================
    add_section_header(prs, "02", "Tool Calls:\nVerify, Don't\nTrust",
        "A tool call is a structured request to an external system. It turns "
        "'trust me' into 'here is the file I read and the test I ran.'",
        "[IMAGE: Soldier verifying a report against the actual source documents on a "
        "command-post desk]")

    add_concept_slide(prs, "What a Tool Call Is", [
        ("'Execute this specific action and return the result.'", False),
        ("The engine does not run the action — it requests it, then reasons "
         "about what comes back.", False),
        ("Four families of tool calls:", False),
        ("Reading (eyes) — read files, list dirs, check git, fetch URLs", True),
        ("Writing (hands) — create, edit, move, copy files", True),
        ("Executing (body) — run commands, run tests, call APIs", True),
        ("Thinking — extended reasoning and multi-step planning", True),
        ("The loop: reason, act, observe, adjust, repeat.", False),
    ], note="Example tool calls: read('/project/app.js') returns file contents; "
            "run('npm test') returns test output; write('/project/config.json', ...) "
            "confirms the write. Each produces a real artifact, not a guess.")

    add_concept_slide(prs, "Why Tool Calls Enable Verification", [
        ("Without tools, the engine generates text — you cannot tell if it is "
         "hallucinating, using stale data, or reasoning from bad assumptions.", False),
        ("With tools, it reads the actual file, makes the change, runs the actual "
         "test, and reports a result you can trace.", False),
        ("Every failure mode from Module 1 still applies to ACTIONS:", True),
        ("It can hallucinate a file path, confidently run the wrong command, "
         "produce a different plan on a second run.", True),
        ("Tool calls are how the operator catches all three before damage.", True),
    ], note="Tools are your audit trail. The agent read THAT file, ran THAT test, "
            "wrote THAT content. You can trace every step — impossible with pure text "
            "generation. That is what makes an agent's product defensible.")

    add_check_on_learning(prs,
        "An agent tells you it verified that your export script produces correctly "
        "formatted output.\n\n"
        "Scenario one: it reviewed a description you pasted and said it looks correct.\n\n"
        "Scenario two: it called a read tool on the actual output file and checked it "
        "against the template.\n\n"
        "Which scenario gives you a defensible product? Why?")

    add_hands_on(prs, "Trace the Tool-Call Loop", [
        "In Claude Code, ask: 'What is in my current directory?' Watch it call the "
        "list tool and return real results — not a guess.",
        "Ask: 'Read [a specific file in your project].' Watch it read the actual file.",
        "Ask it to make a small edit. Before it writes, ask: 'What exactly are you "
        "going to change, and why?'",
        "Verify before you approve. Every action is visible — that is the audit trail.",
    ], "[IMAGE: Soldier tracing each line of a completed action report against a live "
       "system readout]")

    add_section_summary(prs, "Tool Calls", [
        "A tool call is a structured request: execute this action, return the result.",
        "Four families: reading, writing, executing, thinking.",
        "Tools let the agent verify against reality instead of generating from memory.",
        "Every tool call is a traceable action — your audit trail and your defense.",
    ])

    # ======================================================================
    # SECTION 3 — The Operator Posture
    # ======================================================================
    add_section_header(prs, "03", "The Operator\nPosture",
        "Delegate clearly, verify the work, own the outcome. The agent is a motivated "
        "junior who will confidently fill any gap you leave.",
        "[IMAGE: NCO supervising a junior soldier completing a task — reviewing the "
        "work before signing off]")

    add_concept_slide(prs, "The Motivated-Junior Model", [
        ("The agent is a junior teammate with filesystem access — a motivated PFC "
         "handed a mission.", False),
        ("Capable. Fast. Eager. Executes confidently on an ambiguous brief rather "
         "than stopping to ask.", False),
        ("It executes your intent — including the parts you left implicit.", False),
        ("Three duties of the operator:", False),
        ("Delegate clearly — vague intent produces confident but wrong execution", True),
        ("Verify the work — check what it DID, not what it SAID it did", True),
        ("Own the outcome — capability does not transfer accountability", True),
    ], note="Human in the loop means you are positioned to review and approve "
            "consequential actions BEFORE they execute. You are the decision point, "
            "not a passive observer. Active supervision is the correct posture.")

    add_concept_slide(prs, "How Supervision Breaks Down", [
        ("Blind trust — 'It sounds right.' Confident output is not verified output.", False),
        ("Learned helplessness — 'I can't check this, it's too technical.' "
         "You don't replicate the work; you check whether it makes sense.", False),
        ("Three recognizable failure modes:", False),
        ("Over-trust — sweeping change, no review for hours, 20 surprises", True),
        ("Under-involvement — vague ask, agent guesses, 10 wasted iterations", True),
        ("Automation fallacy — chained steps, one fails silently, broken code ships", True),
    ], note="DANGER — If you don't understand it, don't approve it. If the agent says "
            "'I'll refactor the schema' and you don't understand the change, ask it to "
            "explain first. You are the operator. You are responsible.")

    add_concept_slide(prs, "The Delegate-Verify-Own Loop", [
        ("Delegate — write a clear brief: who you are, what you need, what good "
         "looks like, what is off-limits.", False),
        ("Verify — check the actual output, not the narration.", False),
        ("Own — if something is wrong, catch it, fix it, note what to specify "
         "more precisely next time.", False),
        ("The primary lever for steering an agent is a context file:", True),
        ("CLAUDE.md / me.md bake in 'do not delete anything', 'show the plan first', "
         "and your unit's conventions — full treatment in Module 10.", True),
    ], note="The 'verify after acting' reflex is the one habit allowed to spiral: "
            "introduced in Terminal, reinforced here, graded in the capstone. "
            "Optimize for the loop, not the polish.")

    add_check_on_learning(prs,
        "An agent has been running a long session and proposes to 'clean up the "
        "database by removing duplicate records.' It sounds reasonable.\n\n"
        "What do you ask before approving?\n\n"
        "What could go wrong if you approve without reviewing?")

    add_hands_on(prs, "Run the Loop Once", [
        "Give the agent (or chatbot) a small, real task.",
        "Delegate: write a clear brief — who you are, what you need, what good output "
        "looks like, what is off-limits.",
        "Submit it. Read the output.",
        "Verify: does it do what you asked? Any assumption you didn't authorize? "
        "Anything wrong?",
        "Own: correct it, and identify what you should have specified more precisely.",
        "Label your first brief: over-trust, under-involvement, or automation fallacy?",
    ], "[IMAGE: NCO with a clipboard reviewing a junior soldier's completed work before "
       "signing off at a command post]")

    add_section_summary(prs, "The Operator Posture", [
        "The agent is a motivated junior — capable, fast, and assumption-prone.",
        "Three duties: delegate clearly, verify the work, own the outcome.",
        "Blind trust and learned helplessness are both failure modes — check the work.",
        "Context files (CLAUDE.md / me.md) are your primary steering lever — see Module 10.",
    ])

    # ======================================================================
    # SECTION 4 — Worked Examples
    # ======================================================================
    add_section_header(prs, "04", "Worked\nExamples",
        "Harness, tool calls, and operator posture fire together on every real task. "
        "These intel-shop scenarios show defensible vs. pulled products.",
        "[IMAGE: After-action review board with soldiers analyzing an operation log at "
        "a conference table]")

    add_example_slide(prs, "Example 1 — The Harness Makes Output Traceable",
        "Scenario: Build an intelligence summary from a folder of raw sources",
        [
            "WITHOUT THE HARNESS:",
            "  'Write a summary of adversary logistics activity.'",
            "  Engine generates from training data. A reviewer flags two claims",
            "  not in your sources. You cannot trace them. The brief is pulled.",
            "",
            "WITH THE HARNESS:",
            "  'Read /reports/AO-North/ and base the summary only on those files.'",
            "  Agent lists 14 files, reads each, excludes 3 with no logistics",
            "  content, returns a summary with source citations by filename.",
            "",
            "WHY IT MATTERS:",
            "  First output may be accurate or hallucinated — you can't tell.",
            "  Second is traceable to actual sources. Every claim defensible.",
        ],
        "[IMAGE: Analyst cross-checking a finished summary against a stack of "
        "source documents, each claim tagged to a filename]")

    add_example_slide(prs, "Example 2 — Smart Sampling Beats a Data Dump",
        "Scenario: 500 field reports; find every mention of grid 38SMB4521",
        [
            "BAD APPROACH:",
            "  Paste all 500 reports (100,000 tokens) and ask it to find every mention.",
            "  Agent is overwhelmed, loses track, returns incomplete, unverifiable results.",
            "",
            "GOOD APPROACH:",
            "  'Search /reports/field/ and return every mention with source filenames.'",
            "  Agent runs find, then grep (7 matching files), reads only those:",
            "  '9 mentions across 7 reports. Three are the same 72-hour window from",
            "   different collection sources.'",
            "",
            "WHY IT MATTERS:",
            "  Bad: 100,000 tokens, unverifiable coverage.",
            "  Good: ~10,000 tokens, complete and traceable coverage.",
        ],
        "[IMAGE: Soldier running a targeted search across a digital report archive, "
        "seven files highlighted out of hundreds]")

    add_example_slide(prs, "Example 3 — Supervision Prevents a Bad Product",
        "Scenario: Draft and format a SITREP from unstructured notes",
        [
            "WITHOUT SUPERVISION (over-trust):",
            "  'Draft a SITREP from my notes.'",
            "  Agent infers details not in the notes. You submit. It includes a",
            "  casualty figure it inferred — not in your notes, not accurate.",
            "",
            "WITH SUPERVISION:",
            "  'Draft from /notes/0600-update.txt. Use only that file. Flag any",
            "   required field you cannot fill from the source.'",
            "  Agent: 'Could not fill friendly count (Sect 3), next report period",
            "  (Sect 6) — flagged [REQUIRED - NOT IN SOURCE]. Do not submit yet.'",
            "",
            "WHY IT MATTERS:",
            "  Supervision keeps YOU in control of what enters the product.",
            "  The agent flags gaps instead of inventing answers.",
        ],
        "[IMAGE: NCO reviewing a draft SITREP with two fields visibly flagged "
        "'REQUIRED - NOT IN SOURCE' before release]")

    add_check_on_learning(prs,
        "You receive an intelligence summary from an agent with three confident "
        "claims about adversary activity. You cannot tell whether they came from "
        "source documents it read or from training-data pattern-matching.\n\n"
        "What do you do before including the summary in a product — and which of the "
        "three examples is the template for doing it right?")

    add_section_summary(prs, "Worked Examples", [
        "A tool-grounded summary is defensible; a generated one is not.",
        "Searching beats pasting for a large collection of files.",
        "Supervision stops an agent from inventing content in a product.",
        "Shared pattern: ground in real files, verify with tools, keep the operator deciding.",
    ])

    # ======================================================================
    # SECTION 5 — Capstone Exercise
    # ======================================================================
    add_section_header(prs, "05", "Identify the\nMental Models",
        "Read a real transcript and name which models are in play — harness, tool "
        "calls, operator posture. That proves the concepts are habits, not vocabulary.",
        "[IMAGE: Instructor and students reviewing a printed terminal transcript, "
        "annotating it section by section]")

    add_example_slide(prs, "The Transcript",
        "Identify the model(s) in play in each section before checking answers",
        [
            "[SECTION A]",
            "  Dev pastes 2,000 tokens of payment code: 'What's wrong?'",
            "  Agent proposes a try-catch fix. Dev: 'Thanks, I'll test it later.'",
            "  [Leaves. The fix doesn't handle all edge cases.]",
            "",
            "[SECTION B]",
            "  Dev: 'Read /src/payment.js and identify the silent-timeout bug.'",
            "  Agent reads the file, writes the fix, runs npm test: all pass.",
            "  Dev: 'Great. Merge it.'",
            "",
            "[SECTION C]",
            "  Dev shares schema + slow query. Agent finds a missing index,",
            "  writes a migration, runs it, benchmarks: 5000ms -> 200ms.",
            "  Dev asks production impact first, THEN: 'Approved. Ship it.'",
        ],
        "[IMAGE: Three-panel terminal transcript pinned to a board, each panel "
        "tagged A, B, and C]")

    add_concept_slide(prs, "Model Answers", [
        ("Section A — VIOLATIONS:", False),
        ("Harness unused; no tool calls means no verification (a guess); "
         "operator under-involved; pasting beats reading the file", True),
        ("Section B — CORRECT USE:", False),
        ("Harness works (read, write, test); tool calls verify; operator "
         "supervised and approved after a real result", True),
        ("Section C — FULL STACK:", False),
        ("Smart sampling (schema + query, not whole DB); supervision (asks "
         "before approving); tool-call verification; cost-conscious iteration", True),
    ], note="The win is naming the models on demand — the bridge from 'I read about "
            "this' to 'I do this.' Get comfortable saying them out loud in a session.")

    add_check_on_learning(prs,
        "In Section A, the agent proposes a fix without reading the file or running "
        "tests.\n\n"
        "Which model is most directly violated — and in one sentence, what single "
        "change in Section B turned the outcome around?")

    add_hands_on(prs, "Name the Models", [
        "Re-read Sections A, B, and C in the markdown.",
        "For each, write down which model(s) are in play and what was done right or wrong.",
        "Open the model answers and compare against your own.",
        "In your next real session, name a model out loud as you use it: "
        "'I'm using the harness now'; 'I'm supervising now.'",
    ], "[IMAGE: Soldier annotating a transcript with model names in the margin]")

    add_section_summary(prs, "Identify the Mental Models", [
        "You can read a transcript and name which models are in play.",
        "You can spot a violated model and state the fix.",
        "The harness changes an outcome from 'guess' to 'verified.'",
        "Naming the models out loud is the bridge from concept to habit.",
    ])

    # ======================================================================
    # MODULE SUMMARY TABLE
    # ======================================================================
    add_summary_table(prs,
        "MODULE SUMMARY",
        "Commanding an Agent",
        [
            ("The Harness", "Engine + tools = agency",
             "Without tools the engine is a brain in a jar; with them it acts."),
            ("Engine-Harness-Operator", "Three required parts",
             "Engine reasons, harness reaches, operator owns. All three or it breaks."),
            ("Tool Calls", "Requests that execute outside the engine",
             "Verification and an audit trail — hallucinations get caught."),
            ("Operator Posture", "Delegate, verify, own",
             "You sign for the result. Review before consequential actions."),
            ("Delegate-Verify-Own", "Brief, check, fix and learn",
             "The whole skill of commanding an agent, run on every task."),
        ],
        ["CONCEPT", "CORE IDEA", "WHY IT MATTERS"],
        [L, Inches(3.5), Inches(8.1)],
        [Inches(2.9), Inches(4.4), Inches(5.0)])

    # ======================================================================
    # READINESS CHECK
    # ======================================================================
    add_readiness_check(prs, [
        "I can state the one-line difference between a chatbot and an agent",
        "I can name all three parts of the engine-harness-operator model",
        "I can explain what read, write, and execute access means in practice",
        "I can explain what a tool call is and why it enables verification",
        "I know that an action narrated is not the same as an action verified",
        "I can state the three duties of the operator: delegate, verify, own",
        "I can name the three ways supervision breaks down and the fix for each",
        "I know context files are the primary lever for steering an agent (Module 10)",
        "I can read a transcript and name which models are in play",
        "I am the commander, not the typist",
    ])

    # ======================================================================
    # END SLIDE
    # ======================================================================
    add_end_slide(prs, "Commanding\nan Agent", [
        "Complete all five hands-on exercises before continuing.",
        "In your first Claude Code session, name out loud which access level you grant: "
        "read, write, or execute.",
        "Before any agentic task: write the brief, verify the real output, own the result.",
        "Next — Module 8: tokens, context, and cost (how to spend the agent's ammunition).",
    ])

    save_deck(prs, __file__, "07-commanding-agent.pptx")


if __name__ == "__main__":
    build()
