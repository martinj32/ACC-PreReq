"""
ACC Module 2 — Briefing the Machine: Prompting as a Mission Order
Slide deck builder. Uses the shared Army Cyber Dark theme.

Mirrors docs/modules/02-prompting.md section-for-section.
Run by the orchestrator only — do not run python here.
"""

from acc_theme import *


def build():
    prs = new_deck()

    # --- TITLE ---
    add_title_slide(prs,
        "Module 2:\nBriefing the Machine",
        "PREREQUISITE MODULE  |  SELF-PACED",
        "[IMAGE: NCO delivering a clear five-paragraph order to a soldier — a deliberate brief, not a vague request]")

    # --- OVERVIEW ---
    add_overview_slide(prs,
        "Converting prompting-by-feel into method: tell the model who to be, give it context, "
        "show it an example, and say what good output looks like — then extend that clarity with "
        "intermediate structure. Brief it like a mission order, not a search box.",
        "Self-paced (2 sections)",
        [
            "Write a deliberate prompt using the four-element framework: Role, Context, Example, Output Spec",
            "Treat prompting as an iterative conversation, not a one-shot command",
            "Scrub real identifiers out of every prompt before sending it",
            "Use few-shot examples to pin down a pattern",
            "Use chain-of-thought to make reasoning auditable, not just to improve quality",
            "Decompose a big ask into ordered, verifiable steps",
            "Request structured output and use the schema to surface gaps; distinguish system vs. user prompt",
        ])

    # =========================================================================
    # SECTION 01 — Prompting as a Mission Order
    # =========================================================================
    add_section_header(prs, "01", "Prompting as a\nMission Order",
        "A vague prompt is a vague order — and a vague order gets a vague result from a junior "
        "who fills the gaps with assumptions.",
        "[IMAGE: Two mission briefs side by side — one a wall of text, one a clean five-paragraph OPORD]")

    add_concept_slide(prs, "The Four Elements of a Deliberate Prompt", [
        ("The model meets you halfway the moment you give it structure.", False),
        ("Without context it guesses: who you are, what you need, what 'good' looks like.", False),
        ("Role — tell the model who to be.", False),
        ("'You are a plain-language editor' produces different output than no framing at all.", True),
        ("Context — tell it what it needs to know that it cannot infer: task, audience, constraints.", False),
        ("Example — show what good output looks like; one strong example beats three paragraphs of description.", False),
        ("Output Spec — tell it the format, length, and tone you want.", False),
    ], note="The four elements are a structure, not a script to recite. The durable skill is clarity — giving the model what it needs to not guess. How you deliver that varies by task.")

    add_example_slide(prs, "Before and After: Same Model, Different Brief",
        "Scenario: Asking for a summary",
        ["WEAK PROMPT:",
         '  "Write me a summary."',
         "",
         "STRONG PROMPT:",
         '  "You are summarizing this for a senior leader who has two minutes.',
         '   Pull out the three most important points. Use bullet points.',
         '   No jargon. Max 100 words."',
         "",
         "Same model. Different brief. Different result.",
         "",
         "The iterative habit matters more than the perfect prompt:",
         "  a rough ask the model can build on beats silence.",
         "  Read the output, tighten the next ask, repeat."],
        "[IMAGE: NCO handing a soldier a clearly written OPORD — specific orders, specific results]")

    add_concept_slide(prs, "Scrub Before You Brief, and When You Are Stuck", [
        ("Module 1's data-handling rule applies to EVERY prompt you write.", False),
        ("Real names, units, locations, grids, op-dates, credentials do not go into an unauthorized tool.", True),
        ("Use bracketed placeholders: [UNIT], [LOCATION], [NCO]. A scrubbed prompt works just as well.", True),
        ("If you are stuck framing the prompt, ask the model to interview you:", False),
        ("'I need help with [task]. Ask me the questions you need answered before you start.'", True),
        ("Answer the questions, then tell it to proceed.", True),
    ], note="The template trap: the four elements are a structure, not a script. Magic phrases are not the lesson — clarity is. Students who chase tricks over structure hit a ceiling fast.", accent=CYBER_GOLD)

    add_check_on_learning(prs,
        "What specifically changed between your one-line prompt and your structured prompt?\n\n"
        "Which of the four elements made the biggest difference for your task?\n\n"
        "You ask the model to 'write a report.' It produces something generic and too long. "
        "What is the most effective fix?\n\n"
        "A) Switch to a more powerful model\n"
        "B) Ask the same question again and hope for a better result\n"
        "C) Add role, context, an example of good output, and a length/format spec to the prompt\n"
        "D) Break the report into smaller pieces and ask for each separately")

    add_hands_on(prs, "Prompting as a Mission Order", [
        "Pick a real task you need help with right now.",
        "Write a one-line version of the request. Submit it. Save the output.",
        "Add role, context, an example of what good looks like, and an output spec. Submit again.",
        "Compare the two outputs side by side.",
        "Optional: if stuck, type 'I need help with [task]. Ask me the questions you need answered before you start.'",
    ], "[IMAGE: Soldier comparing two drafts on a clipboard — vague request next to a deliberate brief]")

    add_section_summary(prs, "Prompting as a Mission Order", [
        "Four elements: Role, Context, Example, Output Spec — give the model what it needs to not guess.",
        "A vague prompt is a vague order. Structure reduces the surface area for wrong assumptions.",
        "The iterative habit matters more than the perfect prompt — read, tighten, repeat.",
        "Scrub real identifiers out of every prompt; bracketed placeholders work just as well.",
    ])

    # =========================================================================
    # SECTION 02 — Intermediate Prompting
    # =========================================================================
    add_section_header(prs, "02", "Intermediate\nPrompting",
        "Five moves — few-shot, chain-of-thought, decomposition, structured output, system-vs-user. "
        "Each extends clarity. None is a trick.",
        "[IMAGE: Commander handing off a complex multi-phase mission — structured beyond a single simple order]")

    add_concept_slide(prs, "Few-Shot: Show the Pattern", [
        ("Instead of describing what you want, SHOW it — with two, three, or more worked examples.", False),
        ("One example is 'one-shot'; several is 'few-shot.'", False),
        ("More examples pin down the pattern more tightly — the model matches the input-to-output shape.", False),
        ("Use it when the task has a consistent format and one example leaves too much room to drift.", False),
        ("Example — classify reports by urgency:", False),
        ("'Routine resupply completed.' -> LOW   'Comms link intermittent 20 min.' -> MEDIUM", True),
        ("'Unidentified vehicle breached the wire.' -> HIGH   '[new report]' -> ?", True),
    ], note="Three examples teach the pattern far more reliably than the sentence 'classify these by how urgent they are.'")

    add_concept_slide(prs, "Chain-of-Thought: Reasoning You Can Audit", [
        ("Ask the model to show its reasoning before its answer: 'Work through this step by step, then conclude.'", False),
        ("Payoff 1: on multi-step problems, visible reasoning often improves the answer.", False),
        ("Payoff 2 (the important one): the reasoning is now AUDITABLE.", False),
        ("You can see where it went wrong instead of accepting a bare answer.", True),
        ("That makes chain-of-thought a VERIFICATION aid, not just a quality aid.", True),
        ("A bare answer you cannot trace is a black box.", False),
        ("For anything consequential, ask for the reasoning so you can supervise it.", False),
    ], note="Anchor chain-of-thought to supervision, not magic: the reason an operator asks for visible reasoning is to CHECK it. That framing carries straight into the supervisor mindset in Module 7.")

    add_concept_slide(prs, "Decomposition and Structured Output", [
        ("Decomposition — when the ask is big, break it into an ordered sequence of smaller asks.", False),
        ("Drive the steps yourself, or have the model lay out a plan and proceed with your approval.", True),
        ("Keeps each step verifiable; prevents the model collapsing a complex job into a shallow pass.", True),
        ("Structured output — tell the model the exact shape: JSON object, Markdown table, fixed schema.", False),
        ("Makes output predictable AND forces the model to fill specific slots, which surfaces gaps.", True),
        ("Ask for a 'Source' column: an empty cell tells you the model has no source —", True),
        ("a gap a free-text paragraph would have hidden.", True),
    ], note="Structured output as a gap detector: a named-field schema forces missing information into the open. That connects prompting straight back to the verification reflex from Module 1.")

    add_concept_slide(prs, "System vs. User Prompt", [
        ("System prompt — standing instructions: who the model is, the rules, the constraints.", False),
        ("Loaded by the platform before the conversation begins; persists for the whole session.", True),
        ("User prompt — each turn you type; the individual task.", False),
        ("Standing order vs. task order.", False),
        ("Typing 'You are a [role]' in your message is persona injection — it works, but it lives in the visible chat.", False),
        ("That is not the same as a true platform-level system prompt.", True),
        ("Context files later in the course are durable standing orders in file form — same idea, made persistent.", False),
    ], note="Still not tricks: few-shot shows the pattern, chain-of-thought exposes reasoning, decomposition orders the work, structured output fixes the shape, system-vs-user separates standing rules from the task. If a 'technique' adds no clarity, it is folklore.")

    add_check_on_learning(prs,
        "For your own most common AI task, which intermediate technique would help most — "
        "and is the help about output QUALITY or about your ability to VERIFY the output?\n\n"
        "Why is asking the model to 'show its reasoning step by step' valuable to an operator who must defend the output?\n\n"
        "A) It guarantees the answer is correct\n"
        "B) It makes the model run faster\n"
        "C) It makes the reasoning auditable, so you can inspect where it went wrong instead of accepting a bare answer\n"
        "D) It removes the need to verify the output")

    add_hands_on(prs, "Intermediate Prompting — Build Your Five Prompts", [
        "Few-shot: write a prompt with three worked examples plus a fourth unsolved item. Run it.",
        "Chain-of-thought: ask for step-by-step reasoning then the answer. Could you catch an error in the steps?",
        "Decomposition: take one big ask and break it into an ordered sequence of smaller prompts. Run them in turn.",
        "Structured output: ask for a JSON object or table with named columns, including one the model may mark 'NONE.' See what gaps appear.",
        "System vs. user: set a standing instruction first, then send several task prompts. Watch the standing order persist.",
    ], "[IMAGE: Soldier assembling five labeled prompt cards into a field reference binder]")

    add_section_summary(prs, "Intermediate Prompting", [
        "Few-shot: show several worked examples to pin down a pattern.",
        "Chain-of-thought: 'show your reasoning' makes the output auditable — a verification aid.",
        "Decomposition: break a big ask into ordered, verifiable steps.",
        "Structured output surfaces gaps; system vs. user is standing order vs. task order.",
    ])

    # =========================================================================
    # MODULE SUMMARY TABLE
    # =========================================================================
    col_x = [L, Inches(3.5), Inches(8.1)]
    col_w = [Inches(2.9), Inches(4.4), Inches(5.0)]
    add_summary_table(prs,
        "MODULE SUMMARY",
        "Briefing the Machine — Prompting as a Mission Order",
        [
            ("Four Elements",      "Role, Context, Example, Output Spec",       "A vague prompt is a vague order. Structure stops the guessing."),
            ("Iterate",            "Read, tighten the next ask, repeat",        "The iterative habit beats hunting for one perfect prompt."),
            ("Few-Shot",           "Show several worked examples",              "Pins down a pattern one example leaves too loose."),
            ("Chain-of-Thought",   "'Show reasoning, then answer'",             "Makes reasoning auditable — verification, not just quality."),
            ("Decomposition",      "Break a big ask into ordered steps",        "Keeps each step verifiable; prevents a shallow single pass."),
            ("Structured Output",  "Ask for JSON / table / schema",            "Predictable shape, and named fields surface missing info."),
            ("System vs. User",    "Standing order vs. the task at hand",       "Sets up context files as durable standing orders later."),
        ],
        ["CONCEPT", "CORE IDEA", "WHY IT MATTERS"],
        col_x, col_w)

    # =========================================================================
    # READINESS CHECK
    # =========================================================================
    add_readiness_check(prs, [
        "I can name the four elements of a deliberate prompt and ran a before/after comparison",
        "I treat prompting as a conversation, not a one-shot command",
        "I scrub real identifiers out of every prompt before sending it",
        "I can use few-shot examples to pin down a pattern",
        "I can ask for chain-of-thought reasoning and use it to verify, not just to improve quality",
        "I can decompose a big ask into ordered, verifiable steps and request structured output to surface gaps",
        "I can explain the difference between a system prompt and a user prompt, and I built five structured prompts",
    ])

    # =========================================================================
    # END SLIDE
    # =========================================================================
    add_end_slide(prs, "Module 2:\nBriefing the Machine", [
        "Keep your five structured prompts — they are your deliverable for this module.",
        "Pick the one technique that helped most and make it a default habit on your real work.",
        "Carry the chain-of-thought / structured-output instinct forward: both set up output to be verified and supervised.",
        "Note where you used a standing instruction — that is the seed of the context files you will write in Module 10.",
    ])

    save_deck(prs, __file__, "02-prompting.pptx")


if __name__ == "__main__":
    build()
