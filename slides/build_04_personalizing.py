"""
ACC Module 04 — Standing Orders: Making the AI Know You
Slide deck builder. Uses the shared Army Cyber Dark theme.

Run by the orchestrator (python is blocked for the authoring agent):
    python build_04_personalizing.py
Output: slides/Finished/04-personalizing.pptx
"""

from acc_theme import *


def build():
    prs = new_deck()

    # --- TITLE ---
    add_title_slide(prs,
        "Standing Orders:\nMaking the AI\nKnow You",
        "PREREQUISITE MODULE  |  SELF-PACED",
        "[IMAGE: Soldier posting standing orders on a unit board before a shift change]")

    # --- OVERVIEW ---
    add_overview_slide(prs,
        "Most AI tools let you set persistent instructions that shape every conversation — your role, your "
        "preferences, what to always and never do — so you stop re-briefing the model from scratch each session.",
        "Self-paced (about 20 minutes)",
        [
            "Locate the custom instruction or project settings in your AI tool of choice",
            "Write at least three persistent instructions covering identity, format, and prohibited behaviors",
            "Apply the Module 1 data-handling bright line to persistent instruction fields",
            "Distinguish custom instructions, memory, projects, and personas as persistent-context mechanisms",
            "Recognize the context-window cost of custom instructions and how to manage it",
        ])

    # =========================================================================
    # SECTION 1 — Default Settings Are a Starting Point, Not a Destination
    # =========================================================================
    add_section_header(prs, "01",
        "Default Settings Are\na Starting Point",
        "Without customization, every chat starts cold. A one-time setup pays back on every conversation after.",
        "[IMAGE: A relief arriving on watch with no posted orders — starting from zero every shift]")

    add_concept_slide(prs, "Why Personalization Matters", [
        ("Without customization, every new chat starts cold.", False),
        ("The model does not know who you are, how you communicate, or what context is always relevant.", False),
        ("Every session you either re-explain yourself or accept generic output.", False),
        ("Personalization is a one-time investment that pays back on every single conversation after.", False),
        ("Persistent instructions load at the start of every conversation — before you type anything.", False),
    ], note="Think of it as the standing orders a unit posts so every shift runs the same way without a re-brief. "
            "You write them once. The watch reads them on every relief.")

    add_concept_slide(prs, "Where to Find It: ChatGPT and Claude", [
        ("ChatGPT — Custom Instructions", False),
        ("Settings -> Personalization -> Custom Instructions", True),
        ("Two fields: 'What should ChatGPT know about you?' and 'How should it respond?'", True),
        ("Applied automatically to every new conversation.", True),
        ("Claude — Projects", False),
        ("Claude.ai -> Projects -> Create a Project -> Set Instructions", True),
        ("One system prompt field — use it the same way.", True),
        ("Upload documents the model references across all conversations in that project.", True),
    ], note="Instructor Note: Custom-instruction UI locations change frequently. Verify the menu path before "
            "teaching — the concept is stable, the UI is not.")

    add_concept_slide(prs, "What to Put In — and What to Keep Out", [
        ("PUT IN: your role and what you do day to day", False),
        ("PUT IN: how you prefer responses (length, format, tone)", False),
        ("PUT IN: things to always do — 'Lead with a one-sentence summary. Use bullet points.'", False),
        ("PUT IN: things to never do — 'No emojis. No padding. Do not apologize.'", False),
        ("PUT IN: recurring context — your tools, team terminology, domain", False),
        ("KEEP OUT: anything the Module 1 data-handling line covers — the bright line still applies here.", False),
    ], note="Back-reference, not a re-teach: custom instructions go to the platform's servers on every request. "
            "Nothing sensitive, nothing controlled, nothing above the authorization ceiling. The Module 1 rule "
            "has no exception for a settings field.")

    add_example_slide(prs,
        "Before and After Custom Instructions",
        "Scenario: Analyst asking for a document summary",
        [
            "WITHOUT CUSTOM INSTRUCTIONS:",
            '  You ask: "Summarize this document."',
            "  Five-paragraph response — neutral tone, hedging, introduction,",
            "  conclusion, multiple caveats. Generic.",
            "",
            "WITH CUSTOM INSTRUCTIONS:",
            '  Instructions set: "I am an analyst. Lead with BLUF. Use bullets.',
            '  No padding. Max 150 words."',
            '  You ask: "Summarize this document."',
            "  Same document. Same model. Direct, structured output that matches",
            "  how you actually communicate.",
        ],
        "[IMAGE: Two summaries side by side — one verbose and generic, one clean and direct]")

    add_concept_slide(prs, "Two Cautions Before You Build", [
        ("Caution 1: Start with one thing.", False),
        ("Tell it one thing it gets wrong every time. Fix that first. Build from there.", True),
        ("A tight 50-word instruction that sticks beats a 1,000-word template the model ignores after three turns.", True),
        ("Caution 2: Custom instructions count against your context window.", False),
        ("They are loaded on every message — a long instruction shrinks the effective window for your conversation.", True),
        ("Keep instructions under 500 words. Need more? Use a Project document instead.", True),
    ])

    add_check_on_learning(prs,
        "You wrote a custom instruction that says 'always lead with a one-sentence summary.'\n\n"
        "On one response, the model ignores it.\n\n"
        "What are the two most likely causes?")

    add_hands_on(prs, "Setting Up Custom Instructions", [
        "Open your AI tool of choice. Find the custom instructions or project settings.",
        "Write at least three instructions:",
        "    — One about who you are and what you do",
        "    — One about how you like responses formatted",
        "    — One about something to never do",
        "Start a new chat. Ask a question you have asked before without custom instructions.",
        "Compare the two outputs. Did the model follow your instructions?",
    ], "[IMAGE: Soldier filling out a standard form at a workstation — a reusable configuration]")

    add_section_summary(prs, "Default Settings Are a Starting Point", [
        "Every session starts cold without customization — the model knows nothing about you.",
        "Custom instructions load before every conversation. Write them once; pay back on every session.",
        "Include role, format preferences, always-do and never-do behaviors.",
        "Keep sensitive and controlled material out — the Module 1 bright line still applies.",
        "Keep instructions under 500 words to protect your effective context window.",
    ])

    # =========================================================================
    # SECTION 2 — Going Further: Projects, Memory, and Personas
    # =========================================================================
    add_section_header(prs, "02",
        "Projects, Memory,\nand Personas",
        "Beyond custom instructions: structured persistent context that turns a generic tool into one that already knows your work.",
        "[IMAGE: A dedicated operations cell, pre-configured for one specific mission type]")

    add_concept_slide(prs, "Claude Projects: A Dedicated Workspace", [
        ("A Project is a workspace with its own system prompt and document library.", False),
        ("Use a Project when:", False),
        ("You have a recurring task with the same context requirements every time", True),
        ("You want to upload reference documents the model can consult in every conversation", True),
        ("You need different configurations for different types of work", True),
        ("Create one project for analysis, one for writing, one for research.", False),
        ("Each has its own instructions and document set. Context never bleeds between project types.", False),
    ])

    add_concept_slide(prs, "ChatGPT Memory: Reactive Persistence", [
        ("Memory records facts from your conversations and surfaces them in future sessions.", False),
        ("The model notes your name, role, preferences, and past decisions as they come up.", False),
        ("View, edit, and delete entries: Settings -> Personalization -> Memory.", False),
        ("Memory is reactive — it records what comes up in conversation.", False),
        ("Custom instructions are proactive — you set them deliberately.", False),
        ("Use both: custom instructions for stable preferences, memory for things that evolve.", False),
    ], note="Instructor Note: Memory availability varies by subscription tier and rollout region. Verify current "
            "availability before teaching — the concept is stable, feature gating changes.")

    add_concept_slide(prs, "Personas: Named Configurations", [
        ("A persona is a named role, tone, and constraint set you can switch to by name.", False),
        ("Supported on some platforms and all agentic harnesses.", False),
        ("A well-defined persona means you do not re-explain the agent's role every session.", False),
        ("The persona carries the configuration — you start working immediately.", False),
        ("Forward pointer: context files become the primary way to brief an agent (field-craft module).", False),
    ])

    add_example_slide(prs,
        "A Working Project Setup",
        "Scenario: Analyst who does recurring document analysis",
        [
            "PROJECT INSTRUCTIONS:",
            '  "You are a plain-language editor supporting an analyst.',
            "  Lead with the main finding. No jargon.",
            "  Flag anything that requires verification before acting on it.",
            '  Max 200 words per response unless asked for more."',
            "",
            "PROJECT DOCUMENTS:",
            "  — Organization's style guide",
            "  — Glossary of domain terms",
            "  — One-page brief on the current project",
            "",
            "Every analysis conversation starts with that context already loaded.",
            "Open the project. Start working.",
        ],
        "[IMAGE: A pre-configured workstation — everything staged before the mission begins]")

    add_check_on_learning(prs,
        "You create a Project for analysis work with detailed instructions.\n\n"
        "Three months later, your role changes.\n\n"
        "What do you need to update, and where? What happens if you do not update it?")

    add_hands_on(prs, "Projects, Memory, and Personas", [
        "If you use Claude: create a Project for one type of work you do repeatedly.",
        "    — Add instructions and at least one reference document to the Project.",
        "If you use ChatGPT: go to Settings -> Personalization -> Memory.",
        "    — Delete outdated or wrong entries. Add a manual entry the model should always know.",
        "Start a new conversation inside the Project or with memory active.",
        "Compare how quickly the model orients to your work versus a cold-start session.",
    ], "[IMAGE: Soldier comparing two briefings — one from scratch, one pre-staged and ready]")

    add_section_summary(prs, "Projects, Memory, and Personas", [
        "Claude Projects: a dedicated workspace with instructions and uploaded documents for recurring work.",
        "ChatGPT Memory: reactive — records facts from conversations. Supplements custom instructions, not a replacement.",
        "Personas: named configurations that carry role and constraints without re-briefing each session.",
        "Use Projects for structured, recurring work. Use memory for evolving preferences.",
        "Keep project documents free of sensitive or controlled material — same rule as custom instructions.",
    ])

    # =========================================================================
    # MODULE SUMMARY TABLE
    # =========================================================================
    add_summary_table(prs,
        "MODULE SUMMARY", "Standing Orders — Persistent Context at a Glance",
        [
            ["Custom instructions", "Standing orders read before every chat", "Stable role, format, never-do rules"],
            ["Projects (Claude)", "Workspace with its own instructions + docs", "Recurring work, same context each time"],
            ["Memory (ChatGPT)", "Reactive record of surfaced facts", "Things that evolve over time"],
            ["Personas", "Named role / tone / constraint set", "Agentic work without re-briefing"],
            ["Data-handling line", "The Module 1 bright line, applied here", "Always — instructions reach the servers"],
        ],
        ["MECHANISM", "WHAT IT IS", "WHEN TO USE IT"],
        [Inches(0.45), Inches(3.3), Inches(7.4)],
        [Inches(2.8), Inches(4.1), Inches(4.9)])

    # =========================================================================
    # READINESS CHECK
    # =========================================================================
    add_readiness_check(prs, [
        "I have found the custom instruction or project settings in my AI tool",
        "I have written at least three instructions: who I am, how I want responses, what to never do",
        "I ran a before/after comparison and noticed a measurable difference in output",
        "I did not include any sensitive or controlled information — the Module 1 line still holds",
        "I understand why custom instructions count against the context window and how to manage that",
        "I know the difference between custom instructions (proactive) and memory (reactive)",
        "I have set up or can describe how to set up a Project or named configuration for recurring work",
    ])

    # =========================================================================
    # END SLIDE
    # =========================================================================
    add_end_slide(prs,
        "Standing Orders:\nMaking the AI\nKnow You",
        [
            "Revisit your custom instructions after your first 10 sessions — trim what is not working.",
            "Create at least one Project or named configuration for your most common AI use case.",
            "Apply the same security discipline here as everywhere: no sensitive data in persistent instructions.",
            "Next module: leave the chat window and learn the terrain — the filesystem and the terminal.",
        ])

    save_deck(prs, __file__, "04-personalizing.pptx")


if __name__ == "__main__":
    build()
