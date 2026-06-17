"""
ACC Module 08 — Ammunition Discipline: Tokens, Context & Cost
Slide deck builder. Mirrors docs/modules/08-tokens-context-cost.md.

Written as a SPIRAL on Module 1: the token is NOT re-defined here — we open by
asserting prior knowledge and move straight to spending tokens well. Sources
folded in: mental-models core-content.md (model tiers, context operational depth,
tokens as currency, cost-consciousness) and ai-literacy.md (How AI Is Delivered
and Paid For). Verify-before-teaching flags ride every model name/tier/price/
context-window size.
"""

from acc_theme import *
from pptx.util import Inches


def build():
    prs = new_deck()

    # ---------------------------------------------------------------- TITLE
    add_title_slide(prs,
        "Ammunition\nDiscipline:\nTokens, Context\n& Cost",
        "PREREQUISITE MODULE  |  SELF-PACED",
        "[IMAGE: Soldier checking a basic load of ammunition before a mission — "
        "deliberate accounting of a finite resource]")

    # ------------------------------------------------------------- OVERVIEW
    add_overview_slide(prs,
        "You already know what a token IS (Module 1). This module is how to SPEND "
        "tokens like a pro: pick the right model with a simple heuristic, manage a "
        "context window that fills silently, and keep cost under control on real work.",
        "Self-paced module (spirals on Module 1 — AI Foundations)",
        [
            "Treat tokens as ammunition: cost, speed, and accuracy scale with them",
            "Apply a model-selection heuristic: fast vs. reasoning vs. big-context",
            "Manage a context window that fills silently as tool results accumulate",
            "Run the four habits that keep token cost down",
            "Identify how AI is delivered and paid for: app, API, or managed key",
            "Connect cloud delivery back to the Module 1 data-handling boundary",
        ])

    # ======================================================================
    # SECTION 1 — Spend, Don't Just Count
    # ======================================================================
    add_section_header(prs, "01", "Spend,\nDon't Just\nCount",
        "You know what a token IS from Module 1. Here is how to spend one like a pro — "
        "every token costs money and time.",
        "[IMAGE: Soldier budgeting a limited supply of rounds across a long operation]")

    add_concept_slide(prs, "From Knowing a Token to Using One", [
        ("You already own one fact from Module 1, so we do not re-teach it:", False),
        ("A token is the unit of text the model processes — roughly 0.75 of an "
         "English word; code is denser, so more tokens per line.", True),
        ("That is the last time we define it. From here, it is all about spending.", False),
        ("Three things scale with the tokens you spend:", False),
        ("Cost — every input token and every output token costs; output costs more", True),
        ("Speed — more tokens means a slower response", True),
        ("Accuracy — longer is not better; verbose prompts add noise", True),
    ], note="The mental shift: Module 1 taught you to RECOGNIZE a token. Here you learn "
            "to BUDGET it. Treat tokens as free and you blow through context, overpay, "
            "and iterate ten times. Treat them as ammunition and one disciplined pass "
            "does the job.")

    add_check_on_learning(prs,
        "In Module 1 you watched a context window fill and degrade.\n\n"
        "Knowing now that a token costs money and time, what does a sprawling 80-turn "
        "conversation cost you that a tight one does not?")

    add_hands_on(prs, "Feel the Weight of a Token", [
        "Take a prompt you would normally send. Optionally paste it into a tokenizer "
        "(platform.openai.com/tokenizer) and note the token count next to the word count.",
        "Rewrite the same request as a structured prompt: task, context, constraint, "
        "output format. Count again.",
        "Notice which version is longer in the RIGHT way — more structure, not more noise.",
        "You are not learning what a token is. You are learning to feel its weight.",
    ], "[IMAGE: Side-by-side prompt cards, one rambling and one tight, with token "
       "counts marked on each]")

    add_section_summary(prs, "Spend, Don't Just Count", [
        "A token was defined in Module 1 — here it is about spending, not defining.",
        "Cost, speed, and accuracy all scale with the tokens you spend.",
        "Output tokens cost more than input tokens.",
        "Treat tokens as ammunition, not as free.",
    ])

    # ======================================================================
    # SECTION 2 — The Model Landscape
    # ======================================================================
    add_section_header(prs, "02", "Families,\nTiers & the\nSelection Rule",
        "Each model family offers a fast, a balanced, and a powerful tier. The top "
        "cost skill a junior can learn: match the tier to the task.",
        "[IMAGE: Three vehicles staged for different missions — a fast scout, a "
        "balanced workhorse, and a heavy hauler]")

    add_concept_slide(prs, "The Tiers — and Why Biggest Is the Wrong Default", [
        ("Three families dominate: Claude (Anthropic), GPT (OpenAI), Gemini (Google).", False),
        ("Each offers a fast/cheap, a balanced, and a powerful/expensive tier.", False),
        ("Claude's tiers — the standard working toolchain:", False),
        ("Haiku — fast and cheap: eval loops, formatting, high-volume tasks", True),
        ("Sonnet — balanced: the standard working model for most tasks", True),
        ("Opus — powerful and expensive: reserve for the hardest reasoning", True),
        ("Reaching for the biggest model every time is a diesel generator "
         "charging a phone.", False),
    ], note="VERIFY BEFORE YOU RUN — model names, tiers, pricing, and context-window "
            "sizes change with every release. The tier CONCEPT is durable; the names "
            "and numbers are not. Verify current IDs and prices at anthropic.com/pricing "
            "and docs.anthropic.com before any course run.",
        accent=CYBER_GOLD)

    add_concept_slide(prs, "The Model-Selection Heuristic", [
        ("Sort the task into one of three buckets and pick on the spot:", False),
        ("Fast / cheap tier — mechanical, low-judgment work: summarize, reformat, "
         "classify, extract, tight eval loops. Smallest tier that meets the bar.", True),
        ("Reasoning tier — real analysis, planning, multi-step logic: assess options, "
         "write or refactor non-trivial code. Balanced or powerful tier.", True),
        ("Big-context tier — a large body of material at once: a long document, a "
         "sprawling codebase, a multi-source comparison. Fit the window, then verify "
         "its size.", True),
        ("Match the model to the task. 'Always use the biggest' is expensive, slower, "
         "and usually unnecessary.", False),
    ], note="Name drift is real — Haiku/Sonnet/Opus and competitor names will change. "
            "Teach the SHAPE (fast, balanced, powerful) and make bookmarking the "
            "provider docs part of the job.",
        accent=CYBER_GOLD)

    add_check_on_learning(prs,
        "You have a high-volume task: classify 2,000 short messages as urgent or "
        "routine. The work is simple but there is a lot of it.\n\n"
        "Which tier — and why is reaching for the most powerful model the wrong call "
        "here?")

    add_hands_on(prs, "Pick the Tier", [
        "Go to the provider's model page (e.g., anthropic.com/claude) and find the "
        "current tiers. Do the names match what this section lists?",
        "Pick three tasks you might actually do: a format conversion, a complex "
        "analysis, and a long-document read.",
        "Assign each to a tier using the heuristic, and write one sentence per task "
        "explaining why.",
        "Name drift is real. Bookmarking the docs is part of the discipline.",
    ], "[IMAGE: Soldier matching three tools to three jobs on a planning board]")

    add_section_summary(prs, "Families, Tiers & the Selection Rule", [
        "Every family offers three tiers: fast, balanced, powerful.",
        "Matching the tier to the task is the biggest lever on cost.",
        "Heuristic: fast for mechanical, reasoning for hard thinking, big-context for bulk.",
        "VERIFY all model names, tiers, prices, and context sizes before use.",
    ])

    # ======================================================================
    # SECTION 3 — Context Windows, Operationally
    # ======================================================================
    add_section_header(prs, "03", "The Window\nThat Fills\nSilently",
        "You know a context window is finite working memory (Module 1). In agentic "
        "work it fills silently — every tool result accumulates.",
        "[IMAGE: A whiteboard quietly filling with notes until the earliest ones are "
        "crowded off the edge]")

    add_concept_slide(prs, "The Three Operational Rules", [
        ("You know the shape from Module 1: a finite whiteboard; once full, old "
         "content gets crowded out. Here is what changes with an agent working.", False),
        ("Context is not infinite — multi-day chats, long docs, and verbose "
         "reasoning add up fast.", True),
        ("Tool results accumulate — the filesystem op doesn't cost context, but every "
         "RESULT returns into the window and stays.", True),
        ("You control what's in context — which docs, how verbose, how much history. "
         "Strategic use is a skill.", True),
        ("A long session that reads many files can fill the window through tool-result "
         "accumulation, not just conversation.", False),
    ], note="CONTEXT FILLS SILENTLY — most operators don't notice until the model "
            "contradicts itself, misses instructions, or degrades. By then you're deep "
            "in. Watch for the signals and start fresh PROACTIVELY.")

    add_concept_slide(prs, "Smart Sampling Beats Cramming", [
        ("The fix for nearly every context problem: don't pour everything in — let "
         "the agent SAMPLE what it needs.", False),
        ("Single conversation getting long? Start fresh; paste only relevant context; "
         "or have the agent read from files instead of carrying history.", True),
        ("System prompt bloated? Keep it concise; rely on files (CLAUDE.md, me.md) the "
         "agent reads on demand, not stuffed into every request.", True),
        ("File-heavy work? Don't 'read the whole codebase' — use find/grep to locate "
         "the relevant 10-20 files, then read only those.", True),
        ("An agent samples fresh at each tool call — that's why it can work on large "
         "projects without drowning.", False),
    ], note="BIGGER IS NOT ALWAYS BETTER — a very large window still attends better to "
            "the beginning and end than the middle. Buried instructions get partially "
            "ignored. (Context-window sizes are version-sensitive — verify current "
            "numbers before teaching.)",
        accent=CYBER_GOLD)

    add_check_on_learning(prs,
        "You are two hours into an agent session: 30 files read, 15 commands run, a "
        "long back-and-forth. The agent starts contradicting what it said an hour "
        "ago.\n\n"
        "What filled the window — and what do you do?")

    add_hands_on(prs, "Watch the Window Under Pressure", [
        "In an agent, ask it to find and read only the files relevant to a specific "
        "question, using search rather than reading everything. Watch it sample.",
        "Run a longer session with several file reads and commands, then ask it to "
        "summarize what it has done so far. Check the accuracy.",
        "Notice the first sign of drift — a contradiction, a forgotten constraint.",
        "That drift is your cue to start a fresh session.",
    ], "[IMAGE: Soldier monitoring a gauge creeping toward full while a task runs long]")

    add_section_summary(prs, "The Window That Fills Silently", [
        "Three rules: context is finite, tool results accumulate, you control what's in it.",
        "The window fills silently — drift is your cue to start fresh.",
        "Smart sampling (search, then read what's needed) beats cramming everything in.",
        "Bigger windows still attend worst to the middle.",
    ])

    # ======================================================================
    # SECTION 4 — Ammunition Discipline (Cost)
    # ======================================================================
    add_section_header(prs, "04", "Habits That\nKeep Cost\nDown",
        "Cost-consciousness is not penny-pinching — it is getting the result in one "
        "disciplined pass instead of ten loose ones.",
        "[IMAGE: An NCO running a tight, rehearsed drill — one clean repetition instead "
        "of ten sloppy ones]")

    add_concept_slide(prs, "Three Dimensions, Four Principles", [
        ("Three cost dimensions:", False),
        ("Token — every input token costs, every output token costs more", True),
        ("Time — longer chats and more tool calls take longer; waiting is dead time", True),
        ("Iteration — ten passes is 10x the tokens; clear the first time is 1x", True),
        ("Four principles:", False),
        ("Concision is a feature; repetition is waste", True),
        ("Cheap vs. expensive ops matter — a tool read returns a small result; "
         "pasting a 30k-token file costs 30k input tokens plus reasoning", True),
        ("Plan before you prompt — then prompt once, strategically", True),
    ], note="USE TOOLS INSTEAD OF PASTING — bad: paste a 50,000-token codebase for a "
            "refactor. Good: 'Read /src/auth/login.js and identify the bug' — the agent "
            "reads only what it needs (~5,000 tokens) and answers focused.")

    add_concept_slide(prs, "Where Cost Hides: Iteration", [
        ("A vague 80-token prompt that needs five clarifying rounds costs far more "
         "than a structured 120-token prompt that lands first try.", False),
        ("Longer in the RIGHT way is cheaper than short and vague.", False),
        ("More cost-conscious behaviors:", False),
        ("Iterate tightly — review immediately, correct in the same session, keep "
         "context warm, avoid re-reads", True),
        ("Know when to ask the agent vs. solve it yourself — agent for architecture "
         "and unfamiliar code; quick search for syntax lookups", True),
        ("Plan before you build — five minutes of 'here's my plan, any red flags?' "
         "saves fifty minutes of iteration", True),
    ], note="Frame it as DISCIPLINE, not stinginess — the goal is a defensible result "
            "efficiently. A clear brief is cost-conscious AND good supervision (Module 7). "
            "The two habits reinforce each other.")

    add_check_on_learning(prs,
        "You need to debug a slow API endpoint. You have the source file, the database "
        "schema, and the server logs.\n\n"
        "What is the most cost-efficient way to give the agent what it needs — and what "
        "would the expensive version look like?")

    add_hands_on(prs, "Cut the Waste", [
        "Take a prompt you would normally send. Apply the four principles: cut "
        "repetition, add structure, narrow scope, specify output format.",
        "Count words before and after. Is the revised version clearer AND tighter?",
        "Submit the revised prompt. Usable first response, or still need follow-ups?",
        "For one task this week, decide up front: what should the agent read via tools "
        "instead of you pasting?",
    ], "[IMAGE: Two prompt drafts side by side — one marked up and trimmed, the other "
       "bloated with repetition]")

    add_section_summary(prs, "Habits That Keep Cost Down", [
        "Three cost dimensions: token, time, iteration.",
        "Four principles: concision, no repetition, cheap-vs-expensive ops, plan first.",
        "Tools beat pasting for large material.",
        "Iteration is where most cost hides — one clear pass beats ten loose ones.",
    ])

    # ======================================================================
    # SECTION 5 — How AI Is Delivered and Paid For
    # ======================================================================
    add_section_header(prs, "05", "Delivered\n& Paid For",
        "The same model reaches you through different doors — a flat-rate app, a "
        "pay-per-token API, or your org's managed key — and cloud vs. local matters.",
        "[IMAGE: Three doorways into the same operations center — one flat-fee, one "
        "metered, one unit-issued]")

    add_concept_slide(prs, "Three Doors and the Cloud-vs-Local Trade-Off", [
        ("Three ways AI is paid for:", False),
        ("Subscription app — flat monthly fee, access included (ChatGPT Plus, "
         "Claude.ai Pro)", True),
        ("Pay-per-token API — you pay per token sent and received (Anthropic, "
         "OpenAI API)", True),
        ("Bring-your-own-key — your org's API key foots the bill (enterprise, "
         "Claude Code)", True),
        ("Cloud vs. local — most models run remote (input leaves your machine); some "
         "small models run on-device (no connectivity, data stays local, less capable).", False),
        ("The cost ladder: small/fast tiers cost less per token than large frontier "
         "tiers — the same ladder the selection heuristic walks.", False),
    ], note="COST IS REAL on pay-per-token — a long conversation with a large model "
            "costs more than a short one. Know your billing model BEFORE a long task. "
            "Flat-rate hides the marginal cost; API and managed keys accrue it. "
            "(Specific prices and tiers are version-sensitive — verify before teaching.)",
        accent=CYBER_GOLD)

    add_concept_slide(prs, "Delivery Connects to Data Handling", [
        ("Cloud delivery means your input LEAVES your machine.", False),
        ("That is exactly why the Module 1 data-handling rule exists:", False),
        ("Authorization is a property of the SYSTEM, not the impressiveness of "
         "the model.", True),
        ("A capable model on an unauthorized cloud system does not become authorized "
         "because it is capable.", True),
        ("This is a one-line reminder, not a re-teach — the full rule lives in "
         "Module 1; the ethics treatment is Module 9.", False),
    ], note="Skip the pricing tables — specific prices change every quarter. Teach the "
            "structure: tokens cost money, bigger models cost more, cloud sends your "
            "data off-machine, match the model and delivery to the job.")

    add_check_on_learning(prs,
        "You need to run an analysis on a very long document with several back-and-forth "
        "exchanges, on a pay-per-token plan.\n\n"
        "What factors determine the cost of that task, and how would you reduce it?")

    add_hands_on(prs, "Find Your Door", [
        "Open your chatbot's settings or account page. Find which model you are "
        "currently using and note the name.",
        "Open the provider's pricing page. Find one fast/small and one large/powerful "
        "model and read the price difference. Notice the STRUCTURE, don't memorize.",
        "Identify your delivery model: subscription app, pay-per-token API, or "
        "organization-managed key.",
        "Pick one task this week. Decide which tier AND which delivery model fit, and "
        "write one sentence explaining why.",
    ], "[IMAGE: Soldier checking which access credential and billing line their unit "
       "issued for an AI tool]")

    add_section_summary(prs, "Delivered & Paid For", [
        "Three doors: subscription app, pay-per-token API, bring-your-own-key.",
        "Cloud vs. local trades capability against keeping data on your machine.",
        "Billing model affects cost — know it before a long task.",
        "Cloud delivery is why the Module 1 data-handling boundary matters.",
    ])

    # ======================================================================
    # MODULE SUMMARY TABLE
    # ======================================================================
    add_summary_table(prs,
        "MODULE SUMMARY",
        "Tokens, Context & Cost",
        [
            ("Spending Tokens", "Know what a token is — now budget it",
             "Cost, speed, and accuracy all scale with tokens spent."),
            ("Model Tiers", "Fast, balanced, powerful in every family",
             "Matching tier to task is the biggest lever on cost."),
            ("Selection Heuristic", "Fast / reasoning / big-context buckets",
             "A junior can pick the right model on the spot."),
            ("Context, Operationally", "The window fills silently",
             "Smart sampling beats cramming; start fresh proactively."),
            ("Cost Discipline", "Four principles, tight iteration",
             "Iteration is where cost hides — one clear pass beats ten."),
            ("Delivery & Payment", "App, API, or managed key; cloud vs. local",
             "Billing affects cost; cloud governs what you may send."),
        ],
        ["CONCEPT", "CORE IDEA", "WHY IT MATTERS"],
        [L, Inches(3.5), Inches(8.1)],
        [Inches(2.9), Inches(4.4), Inches(5.0)])

    # ======================================================================
    # READINESS CHECK
    # ======================================================================
    add_readiness_check(prs, [
        "I can state, from Module 1, what a token is without re-reading it",
        "I understand that cost, speed, and accuracy all scale with tokens spent",
        "I can name the three model tiers: fast, balanced, powerful",
        "I can apply the fast / reasoning / big-context heuristic to a real task",
        "I know model names, tiers, pricing, and context sizes must be verified before use",
        "I can state the three operational context rules",
        "I can name the smart-sampling fix for long chats and file-heavy work",
        "I can name the three cost dimensions and four cost principles",
        "I can name the three ways AI is paid for and the cloud-vs-local trade-off",
        "I understand cloud delivery is why the data-handling boundary matters (Module 1)",
    ])

    # ======================================================================
    # END SLIDE
    # ======================================================================
    add_end_slide(prs, "Tokens,\nContext & Cost", [
        "Complete all five hands-on exercises before continuing.",
        "VERIFY every model name, tier, price, and context size at the provider's docs "
        "before any real run — the numbers drift, the concepts don't.",
        "On your next task, pick the tier with the heuristic and decide what the agent "
        "should read via tools instead of you pasting.",
        "Next — Module 9: Rules of Engagement (ethics and responsible AI use).",
    ])

    save_deck(prs, __file__, "08-tokens-cost.pptx")


if __name__ == "__main__":
    build()
