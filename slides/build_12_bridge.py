"""
ACC Module 12 — Crossing the LD: Bridge to Advanced Agentics
Deck mirrors docs/modules/12-bridge-advanced.md.
Recognition depth, NOT build depth. Heavy verify-before-teaching flags on MCP.
Build with the shared Army Cyber Dark theme. DO NOT run — orchestrator builds.
"""

from acc_theme import *


def build():
    prs = new_deck()

    # ---- Title -------------------------------------------------------------
    add_title_slide(
        prs,
        "Crossing\nthe LD:\nBridge to\nAdvanced\nAgentics",
        "PREREQUISITE MODULE  |  SELF-PACED  |  RECOGNITION DEPTH",
        "[IMAGE: a unit crossing the line of departure at first light — "
        "terrain ahead mapped, footing sure; the bridge to what comes next]",
    )

    # ---- Overview ----------------------------------------------------------
    add_overview_slide(
        prs,
        "A recognition module: it gives you the vocabulary and the map for "
        "advanced agentics so the main course has something to build on — and "
        "deliberately stops short of teaching you to build any of it.",
        "Self-paced  |  Recognition, not mastery",
        [
            "Recognize advanced agentics as the same primitive, scaled",
            "Name RAG, MCP (Tool/Resource/Prompt), and the guardrail controls",
            "Name the four workflow patterns and the sub-agent idea",
            "Recognize agent evaluation as the verify step at scale",
            "Know exactly what is deferred to the main course",
        ],
    )

    # ---- Read This First (recognition framing) -----------------------------
    add_concept_slide(
        prs, "How to Read This Module",
        [
            ("The eleven before this taught you to DO things — this one to RECOGNIZE them", False),
            ("When the main course says 'wrap that tool in an MCP server,'", False),
            ("you'll already know what the words point at", True),
            ("Watch for the 'Deferred to the main course' markers throughout", False),
            ("They aren't gaps — they are the boundary of this course", True),
            ("Everything here is built on the one primitive you already own", False),
        ],
        note="Recognition, not build. You leave able to NAME these topics, not "
             "implement them. That is the whole job of a bridge.",
    )

    # =======================================================================
    # SEGMENT 0 — Recap the Primitive
    # =======================================================================
    add_section_header(
        prs, "00", "Recap\nthe Primitive",
        "Everything advanced is the primitive you already command — repeated, connected, scaled.",
        "[IMAGE: three nested blocks labeled engine, harness, operator, with "
        "a loop arrow around them; the foundation, unchanged]",
    )

    add_concept_slide(
        prs, "You Already Hold the Whole Foundation",
        [
            ("ENGINE — the model: predicts text, reasons in language, no body (M1)", False),
            ("HARNESS — what gives the engine a body: tools, file access, action (M7)", False),
            ("OPERATOR — you: the accountable supervisor who delegates and owns (M7/M9)", False),
            ("THE LOOP — delegate, verify, own, run on a live build (M11)", False),
            ("Every advanced topic ahead is one of these, extended:", False),
            ("more tools on the harness, a plan you approve, one agent directing many", True),
        ],
        note="Map every new term back to the primitive: is this a richer engine, a "
             "bigger harness, or a tighter operator loop? Almost everything sorts "
             "into one of those three.",
    )

    add_section_summary(
        prs, "Recap the Primitive",
        [
            "Advanced agentics is not new in kind — it's the primitive, scaled",
            "Engine, harness, operator, and the loop are the whole foundation",
            "Sort every new term into richer engine, bigger harness, or tighter loop",
            "Anchoring to what you own keeps the main course from feeling like a wall",
        ],
    )

    # =======================================================================
    # SEGMENT 1 — Grounding and Retrieval
    # =======================================================================
    add_section_header(
        prs, "01", "Grounding\nand Retrieval",
        "The 'RAG-by-hand' pattern from Module 7 — now with its name.",
        "[IMAGE: an analyst answering from an open, cited source binder "
        "rather than from memory; traceable to the page]",
    )

    add_concept_slide(
        prs, "Name the Pattern You Already Used",
        [
            ("GROUNDED vs UNGROUNDED — the operator's question: where did this come from?", False),
            ("Ungrounded: from trained weights — fluent, no source to check (all M1 risks)", True),
            ("Grounded: from real material retrieved into context — cited, traceable", True),
            ("RAG — retrieval-augmented generation:", False),
            ("retrieve real sources, put them in context, answer from them", True),
            ("You did this by hand in Module 7; the main course builds it into the harness", False),
            ("Fixes two M1 failures: knowledge cutoff AND hallucination", False),
        ],
        note="Grounding doesn't remove the verify step — you still confirm the "
             "retrieved source is real and the answer reflects it.",
    )

    add_check_on_learning(
        prs,
        "You used 'RAG by hand' in an earlier module without knowing the name. "
        "What did that actually consist of — and how do you tell a grounded answer "
        "from a generated one?",
    )

    add_section_summary(
        prs, "Grounding and Retrieval",
        [
            "RAG is the named version of the by-hand grounding you already did",
            "Grounded output is cited and verifiable; generated output is not",
            "It's the practical fix for knowledge cutoff and hallucination at once",
            "DEFERRED: building retrieval pipelines (embeddings, vector stores)",
        ],
    )

    # =======================================================================
    # SEGMENT 2 — Connecting Tools and MCP
    # =======================================================================
    add_section_header(
        prs, "02", "Connecting\nTools & MCP",
        "The harness is extensible — MCP is the emerging standard way to extend it.",
        "[IMAGE: a harness with modular ports; new capability modules "
        "snapping into a standard connector]",
    )

    add_concept_slide(
        prs, "MCP — Model Context Protocol (Conceptual)",
        [
            ("The harness is extensible — adding a tool makes a general agent useful", False),
            ("MCP: an open standard for connecting agents to external tools and data", False),
            ("Write a capability once, reuse it across agents instead of bespoke wiring", True),
            ("Three things an MCP server exposes:", False),
            ("TOOL — an action the agent can invoke (the agent DOES something)", True),
            ("RESOURCE — data the agent can read (the agent READS something)", True),
            ("PROMPT — a reusable instruction template (the agent REUSES something)", True),
            ("The sort: Tool = action, Resource = readable data, Prompt = canned instruction", False),
        ],
        note="VERIFY-BEFORE-TEACHING: this is the highest version-sensitivity risk "
             "in the course. Treat every specific here as illustrative of the "
             "CONCEPT, not as current fact.",
        accent=CYBER_GOLD,
    )

    add_concept_slide(
        prs, "MCP Is Version-Sensitive — Verify Before You Rely",
        [
            ("MCP is a fast-moving standard — details change between versions", False),
            ("Protocol details, transport, available servers, governance, semantics —", False),
            ("all shift; do NOT teach any specific MCP detail from memory", True),
            ("Before any course run or operational use:", False),
            ("verify the current state at official docs AND what your org has authorized", True),
            ("Connecting a tool expands the attack and disclosure surface", False),
            ("New tool/resource = a new path data flows out, or untrusted input flows in", True),
            ("The Module 1 data-handling bright line applies in full", False),
        ],
        note="An extensible harness is powerful — and is exactly why the guardrails "
             "in the next segment exist. Verify currency before delivery.",
        accent=CYBER_GOLD,
    )

    add_check_on_learning(
        prs,
        "In MCP terms, what is the difference between a Tool and a Resource — and "
        "why must you verify any specific MCP detail against current docs rather "
        "than teaching it from memory?",
    )

    add_section_summary(
        prs, "Connecting Tools and MCP",
        [
            "The harness is extensible; MCP standardizes how you connect new tools",
            "An MCP server exposes Tools (actions), Resources (data), Prompts (templates)",
            "MCP is version-sensitive — verify every specific before teaching or relying",
            "DEFERRED: building MCP servers and wiring real tools and data",
        ],
    )

    # =======================================================================
    # SEGMENT 3 — Permissions and Guardrails
    # =======================================================================
    add_section_header(
        prs, "03", "Permissions\nand Guardrails",
        "The technical 'how' behind staying the accountable human in the loop.",
        "[IMAGE: an access-control panel with scoped switches and an "
        "approval gate; least privilege made physical]",
    )

    add_concept_slide(
        prs, "The Supervisor Mindset, Made Enforceable",
        [
            ("SCOPED PERMISSIONS — specific read/write/execute rights, nothing more", False),
            ("Least privilege applied to agents: read-only can't modify; sandboxed can't escape", True),
            ("COMMAND ALLOWLISTS — permit a defined set; everything else blocked by default", False),
            ("APPROVAL GATES — agent pauses on a consequential action and asks a human", False),
            ("The gate is where your judgment enters the loop", True),
            ("SANDBOXES — an isolated environment where a mistake can't damage anything real", False),
            ("This is what makes the capstone bad-edit drill safe to do at scale", True),
        ],
        note="Guardrails reduce how much damage a mistake can do — they do NOT "
             "transfer accountability. You still own the output (Module 9).",
    )

    add_check_on_learning(
        prs,
        "An approval gate pauses the agent before a consequential action so a human "
        "can approve it. Why does that mechanism reduce risk WITHOUT reducing your "
        "accountability for the result?",
    )

    add_section_summary(
        prs, "Permissions and Guardrails",
        [
            "Scoped permissions, allowlists, approval gates, sandboxes",
            "These are the technical implementation of the supervisor mindset",
            "Guardrails make supervision enforceable, not unnecessary",
            "DEFERRED: configuring scopes, allowlists, gates, and sandboxes",
        ],
    )

    # =======================================================================
    # SEGMENT 4 — Planning and Decomposition
    # =======================================================================
    add_section_header(
        prs, "04", "Planning &\nDecomposition",
        "The agent's plan is a supervision artifact — steer at the plan, not the wreckage.",
        "[IMAGE: an agent presenting a step-by-step plan on a board for a "
        "commander's approval before execution]",
    )

    add_concept_slide(
        prs, "Plan-Then-Act as an Approval Checkpoint",
        [
            ("DECOMPOSITION — break a large, ambiguous task into ordered sub-steps", False),
            ("You did this with pseudocode in Module 10; an agent does it for a big job", True),
            ("PLAN-THEN-ACT — agent proposes a plan, you approve/correct, THEN it executes", False),
            ("Catching a flawed approach in the plan is far cheaper than in finished work", True),
            ("The plan as a supervision artifact:", False),
            ("the earliest, cheapest place to apply oversight — the delegate step, visible", True),
        ],
        note="Correcting a plan costs a sentence; correcting completed work costs a "
             "rebuild. The plan is your highest-leverage moment to redirect.",
    )

    add_check_on_learning(
        prs,
        "Why is an agent's proposed plan described as a 'supervision artifact,' and "
        "why is reviewing it the cheapest place to apply your judgment?",
    )

    add_section_summary(
        prs, "Planning and Decomposition",
        [
            "Agents can decompose a big task into ordered, reviewable steps",
            "Plan-then-act inserts your approval before any change is made",
            "The plan is the earliest and cheapest supervision checkpoint",
            "DEFERRED: building agents that plan and managing plan-execution",
        ],
    )

    # =======================================================================
    # SEGMENT 5 — Workflow Patterns, Named
    # =======================================================================
    add_section_header(
        prs, "05", "Workflow\nPatterns,\nNamed",
        "Recognize the four by name now — you build them in the main course.",
        "[IMAGE: four labeled flow diagrams side by side, each a different "
        "arrangement of the same primitive]",
    )

    add_concept_slide(
        prs, "Four Recognition Targets",
        [
            ("PROMPT CHAINING — a sequence where each step's output feeds the next", False),
            ("draft -> critique -> revise; order is the point", True),
            ("ROUTING — classify the request first, then send to the best handler", False),
            ("a triage step: simple to a fast path, complex to a heavier one", True),
            ("ORCHESTRATOR-WORKERS — one agent splits a job, workers do parts, it assembles", False),
            ("a team lead delegating to a section", True),
            ("EVALUATOR-OPTIMIZER — one agent produces, another critiques, the first revises", False),
            ("a generate-and-critique loop that runs until output meets the bar", True),
        ],
        note="Recognize the shape, defer the build. When the main course says "
             "'route this,' you'll know it means classify-then-dispatch.",
    )

    add_check_on_learning(
        prs,
        "A workflow classifies each incoming request and sends it to the handler "
        "best suited for it. Which named pattern is this — and which pattern instead "
        "feeds each step's output into the next?",
    )

    add_section_summary(
        prs, "Workflow Patterns, Named",
        [
            "Prompt chaining: ordered steps, each feeding the next",
            "Routing: classify-then-dispatch to the best handler",
            "Orchestrator-workers: one agent splits, delegates, assembles",
            "Evaluator-optimizer: generate, critique, revise — DEFERRED to build",
        ],
    )

    # =======================================================================
    # SEGMENT 6 — Sub-Agents / Multi-Agent
    # =======================================================================
    add_section_header(
        prs, "06", "Sub-Agents\n& Multi-Agent",
        "One commander agent directing workers — a preview, not an orchestration lesson.",
        "[IMAGE: a command-and-control chart: one commander node delegating "
        "to a row of worker nodes]",
    )

    add_concept_slide(
        prs, "One Commander, Many Workers (Preview)",
        [
            ("SUB-AGENTS — worker-agents a coordinating agent spawns and directs", False),
            ("each handles a bounded piece of a larger job", True),
            ("THE COMMANDER ANALOGY — one agent decomposes, assigns, integrates results", False),
            ("the chain-of-command structure you already understand, in agents", True),
            ("SUPERVISION GETS HARDER, NOT OPTIONAL — you're overseeing a delegation chain", False),
            ("the loop still applies; it just has more surface to cover", True),
        ],
        note="More agents multiply capability AND the places things go wrong. Don't "
             "read 'the agents handle it' as 'I can stop verifying.'",
    )

    add_check_on_learning(
        prs,
        "What does adding sub-agents change about the operator's responsibility — "
        "and what is the trap in assuming a multi-agent system supervises itself?",
    )

    add_section_summary(
        prs, "Sub-Agents and Multi-Agent",
        [
            "One commander agent can delegate to multiple worker-agents",
            "Same chain-of-command structure you already understand, in agents",
            "Multi-agent expands the surface the accountable human must supervise",
            "DEFERRED: designing and orchestrating multi-agent systems",
        ],
    )

    # =======================================================================
    # SEGMENT 7 — Evaluating an Agent
    # =======================================================================
    add_section_header(
        prs, "07", "Evaluating\nan Agent",
        "Judging the whole output, not one answer — the verify step, grown up.",
        "[IMAGE: a QA bench sampling outputs against a known-good reference "
        "set; spot-checks on a production line]",
    )

    add_concept_slide(
        prs, "Whole-Output Evaluation (Light)",
        [
            ("SPOT-CHECKS — sample a subset of outputs and verify them closely", False),
            ("you can't read everything at scale; check enough to calibrate trust", True),
            ("REGRESSION TESTING — keep known-good results; re-run after any change", False),
            ("catches when a change quietly breaks what used to work", True),
            ("EVALUATOR-OPTIMIZER, REUSED — one agent or rubric judges another's output", False),
            ("the same Segment-5 pattern, applied as a scalable verify step", True),
        ],
        note="Everything here is the capstone's verify step at scale — how you keep "
             "verifying when there's too much output to read by hand.",
    )

    add_check_on_learning(
        prs,
        "Why is whole-output evaluation necessary instead of just reading every "
        "answer — and how do spot-checks and regression tests relate to the verify "
        "step you ran in the capstone?",
    )

    add_section_summary(
        prs, "Evaluating an Agent",
        [
            "Judge the whole output, not a single answer",
            "Spot-checks, regression testing, and the evaluator-optimizer idea",
            "Evaluation is the capstone's verify step scaled up",
            "DEFERRED: building production evaluation harnesses",
        ],
    )

    # =======================================================================
    # What's Deferred summary table + Readiness + End
    # =======================================================================
    add_summary_table(
        prs,
        "WHAT'S DEFERRED",
        "You cross with the map; the main course is where you build",
        [
            ["Grounding / Retrieval", "RAG as named, traceable grounding",
             "Retrieval pipelines (embeddings, vector stores)"],
            ["Tools & MCP", "Extensible harness; Tool/Resource/Prompt",
             "MCP servers + real connections (verify details)"],
            ["Permissions & Guardrails", "Scopes, allowlists, gates, sandboxes",
             "Configuring enforceable agent permissions"],
            ["Planning", "Plan-then-act as a checkpoint",
             "Agents that decompose and plan"],
            ["Workflow Patterns", "The four patterns by name",
             "Implementing chaining/routing/orchestration/eval"],
            ["Sub-Agents", "One commander directing workers",
             "Designing multi-agent systems"],
        ],
        ["TOPIC", "YOU CAN NOW RECOGNIZE", "MAIN COURSE TEACHES YOU TO BUILD"],
        [Inches(0.45), Inches(3.7), Inches(7.4)],
        [Inches(3.2), Inches(3.7), Inches(4.9)],
    )

    add_readiness_check(
        prs,
        [
            "I can state advanced agentics is the same primitive, scaled",
            "I can name RAG as the grounding pattern I already used by hand",
            "I can describe MCP and Tool/Resource/Prompt — and know it's version-sensitive",
            "I can name the permission and guardrail controls behind supervision",
            "I can explain why an agent's plan is a supervision checkpoint",
            "I can name the four workflow patterns",
            "I recognize the sub-agent idea expands, not removes, supervision",
            "I can name spot-checks, regression, and evaluator-optimizer",
            "I know which of these is deferred to the main course",
        ],
    )

    add_end_slide(
        prs,
        "Crossing\nthe LD:\nBridge to\nAdvanced\nAgentics",
        [
            "Carry the primitive and the loop across — everything ahead is built from them",
            "Verify anything version-sensitive (above all MCP) against current docs",
            "Report to the ACC main course — this is where you build",
        ],
    )

    save_deck(prs, __file__, "12-bridge.pptx")


if __name__ == "__main__":
    build()
