"""
ACC Module 1 — Know Your Weapon: How AI Actually Works
Slide deck builder. Uses the shared Army Cyber Dark theme.

Mirrors docs/modules/01-ai-foundations.md section-for-section.
Run by the orchestrator only — do not run python here.
"""

from acc_theme import *


def build():
    prs = new_deck()

    # --- TITLE ---
    add_title_slide(prs,
        "Module 1:\nKnow Your Weapon",
        "PREREQUISITE MODULE  |  SELF-PACED",
        "[IMAGE: Soldier at a command-post terminal studying how an AI tool works before relying on it — knowing the weapon before carrying it]")

    # --- OVERVIEW ---
    add_overview_slide(prs,
        "An LLM predicts text from learned patterns — not rules, not memory, not live data. "
        "Know what it is, how a conversation actually works, where it fails, how to verify it, "
        "when to use it, and what never goes in.",
        "Self-paced (7 sections)",
        [
            "State what an LLM actually does — and why that is not the same as knowing",
            "Explain tokens and context windows in plain terms (intro depth)",
            "Explain why the model is stateless and what conversation 'memory' really is",
            "Name the five failure modes and produce a hallucination on demand",
            "Run five verification techniques as drills, not as a vibe",
            "Decide when AI is the right tool and when it is the wrong one",
            "Apply the classify-before-you-paste rule to content you handle every day",
        ])

    # =========================================================================
    # SECTION 01 — What an LLM Actually Is
    # =========================================================================
    add_section_header(prs, "01", "What an LLM\nActually Is",
        "The model predicts what comes next — not rules, not memory, not a lookup table. "
        "Fluent output is not the same as correct output.",
        "[IMAGE: Soldier reading a training manual — learning patterns, not memorizing a rulebook]")

    add_concept_slide(prs, "Prediction, Not Lookup", [
        ("The model reads a sequence of text and predicts what comes next — one chunk at a time.", False),
        ("No lookup table. No truth check. No rules written by a programmer.", False),
        ("Given everything written so far: what is the statistically most likely next piece?", False),
        ("Trained, not programmed.", False),
        ("No one wrote 'Paris is the capital of France.' The model trained on enough text that it became the likely completion.", True),
        ("Upside: it generalizes across almost any domain.", True),
        ("Failure mode: if training data was wrong or thin, the model learned those patterns too.", True),
    ], note="The only accurate verb is 'predicts.' The model does not know, want, think, or lie. Catch yourself using those words and swap in 'predicts.'")

    add_concept_slide(prs, "The LLM Is the Engine", [
        ("By itself, the LLM is a brain in a jar.", False),
        ("Capable of reasoning in text — incapable of acting on its own.", False),
        ("No body. No memory between chats. No live connection to the world unless something gives it one.", False),
        ("Fluent, confident output is not the same as correct output.", False),
        ("Both are true simultaneously — that is the working mental model.", False),
    ], note="VERIFY BEFORE TEACHING: model names, tiers, context-window sizes, and pricing change every release. Any specific number in this course is a snapshot — confirm at the provider's docs before a course run.")

    add_check_on_learning(prs,
        "The model just gave you a confident-sounding answer.\n\n"
        "What would it take to verify it? Where would you check?\n\n"
        "A language model was never given a rule that says 'Paris is the capital of France.' "
        "How does it produce that answer?\n\n"
        "Think it through: trained on patterns vs. looked up vs. hard-coded — which is it, and what does that mean for accuracy?")

    add_hands_on(prs, "What an LLM Actually Is", [
        "Type an incomplete sentence on a topic you know well and submit it. Read what the model predicts.",
        "Add the word 'definitely' or 'obviously' to the same sentence and submit again. Does the completion change?",
        "Ask the model a factual question you already know the answer to. Check the output for accuracy.",
        "Ask the exact same question in a new chat. Is the answer identical, or slightly different?",
        "Ask yourself: 'How would I verify any of these outputs if I did not already know the answer?'",
    ], "[IMAGE: Soldier testing radio frequencies — observing how small input changes shift the output]")

    add_section_summary(prs, "What an LLM Actually Is", [
        "The model predicts what comes next — statistically likely, not looked up or rule-based.",
        "Trained, not programmed: it learned patterns from text, including the wrong ones.",
        "Fluent, confident output is not the same as correct output.",
        "The only accurate verb is 'predicts' — not knows, thinks, or remembers.",
    ])

    # =========================================================================
    # SECTION 02 — Tokens and Context (Introduction)
    # =========================================================================
    add_section_header(prs, "02", "Tokens and\nContext (Intro)",
        "The model reads in tokens and can only hold a fixed number at once. "
        "Fill that limit and earlier content falls out. Deep management is Module 8.",
        "[IMAGE: Tactical whiteboard filling with overlapping mission graphics — running out of space]")

    add_concept_slide(prs, "What Is a Token?", [
        ("The model does not read words — it reads chunks of text called tokens.", False),
        ("In English prose, one token is roughly three-quarters of a word.", False),
        ("Code and non-English text tokenize less efficiently — more tokens per word.", False),
        ("You do not need to count tokens precisely.", False),
        ("The instinct to keep input focused is the deliverable from this section.", False),
    ], note="This is INTRO depth only. Spending tokens deliberately and managing context as a resource is Module 8 (Ammunition Discipline). Learn the 'what' here; learn the 'how to spend' there.")

    add_concept_slide(prs, "The Context Window", [
        ("Every model has a hard ceiling on tokens it can hold in a single conversation.", False),
        ("That ceiling is the context window — a whiteboard with finite space.", False),
        ("New writing crowds out old writing once it fills.", False),
        ("A full window: the model hedges, contradicts what it said ten turns ago, forgets a constraint.", False),
        ("That is not a bug — it is the whiteboard running out of space.", False),
        ("Models attend better to the beginning and end of the window than to the middle.", True),
        ("Start a fresh chat when the task changes OR when the model starts drifting.", True),
    ], note="VERIFY BEFORE TEACHING: approximate sizes change with releases — Claude ~200k, GPT-4o ~128k, Gemini 1M+ tokens. Bigger is not always better; quality degrades in the middle of a huge window.")

    add_check_on_learning(prs,
        "You set an important constraint at the start of a long conversation. "
        "Ten exchanges later, the model seems to have forgotten it.\n\n"
        "What happened, and what would you do differently next time?\n\n"
        "You are in a long chat and the model starts contradicting instructions you gave at the start. "
        "What is the most likely cause?\n\n"
        "A) The model changed its mind\n"
        "B) You used the wrong model for this task\n"
        "C) Earlier content has been crowded out of the context window\n"
        "D) The model is testing whether you notice")

    add_hands_on(prs, "Tokens and Context", [
        "Open a fresh chat and paste several paragraphs of dense text.",
        "Ask the model to summarize just the first paragraph.",
        "In the same chat, ask it about something from the end of what you pasted.",
        "Start a new chat and ask the same question. Compare the quality.",
        "Notice: does the model attend differently to the top vs. the buried middle?",
    ], "[IMAGE: Soldier reviewing a long operation log — noting what dropped off the bottom]")

    add_section_summary(prs, "Tokens and Context (Intro)", [
        "The model reads in tokens — roughly 0.75 of an English word each.",
        "Every model has a context window — a finite whiteboard that fills up.",
        "When the window fills, earlier content falls out silently and instructions drift.",
        "Start fresh when the task changes or the model begins to hedge. Deep management is Module 8.",
    ])

    # =========================================================================
    # SECTION 03 — Conversation Mechanics & Statelessness
    # =========================================================================
    add_section_header(prs, "03", "Conversation\nMechanics &\nStatelessness",
        "There is no one on the other end between messages. Every turn, the platform re-feeds "
        "the whole transcript to a stateless engine.",
        "[IMAGE: Radio operator handed the full message log fresh each transmission — no memory of its own]")

    add_concept_slide(prs, "The Model Is Stateless", [
        ("The engine remembers nothing between calls. It does not 'stay logged in' to your chat.", False),
        ("Each time you send a message, the platform feeds the ENTIRE thread back as one block of text.", False),
        ("The model reads all of it fresh, predicts the next turn — then forgets again.", False),
        ("'Memory' is the transcript, not recall.", False),
        ("When it refers back to message ten, it is re-reading it — because the platform put it back in front of it.", True),
        ("This is why the window matters: the conversation grows every turn, and the oldest turns drop off the top.", True),
    ], note="Kill the 'helpful person reading along' picture. Replace it with: a stateless engine handed a fresh transcript every turn. That one fact explains statelessness, context limits, and cross-chat memory all at once.")

    add_concept_slide(prs, "No Cross-Chat Memory — and Your Three Moves", [
        ("A fresh chat starts with a blank transcript. It knows nothing about your other conversations.", False),
        ("Some products bolt on a 'memory' or 'projects' feature — that is an added layer, not the model remembering you.", False),
        ("Continue — add a turn; everything before stays in context. Use when the thread is helping.", False),
        ("Edit — rewrite an earlier message; most tools discard everything after and re-run. Fix bad instructions at the source.", False),
        ("New chat — start with an empty transcript. Use when old context is dead weight or dragging the model off course.", False),
    ], note="Edit at the source, do not pile on. If your third message had a bad instruction, edit it — do not send a fourth saying 'ignore that.' A clean transcript produces cleaner output.")

    add_check_on_learning(prs,
        "You spent an hour in one chat building useful context. You close it and open a fresh one tomorrow.\n\n"
        "What does the new chat know about yesterday's work, and what would you do to get that context back?\n\n"
        "When the model refers back to something you said earlier in the SAME conversation, what is actually happening?\n\n"
        "A) The model stored your message in long-term memory\n"
        "B) The platform re-fed the whole transcript to the stateless model, so it re-read your earlier message\n"
        "C) The model has a running memory of you across all chats\n"
        "D) The model guessed what you probably said")

    add_hands_on(prs, "Conversation Mechanics & Statelessness", [
        "Tell the model a specific fact ('My callsign is Raptor-6'). Continue a few turns, then ask it to repeat the fact.",
        "Open a brand-new chat and ask it for your callsign. Watch it have no idea — that is statelessness.",
        "Go back to the first chat, edit an early message to change the fact, and re-run. Watch the later turns regenerate.",
        "Reflect: when in your own work would 'edit the source message' beat 'send a correction'?",
    ], "[IMAGE: Two operation logs side by side — one continued, one started blank — showing what carries over and what does not]")

    add_section_summary(prs, "Conversation Mechanics & Statelessness", [
        "The engine is stateless — it remembers nothing between calls.",
        "Conversation 'memory' is the re-fed transcript, not recall.",
        "A new chat knows nothing about your other chats by default.",
        "Three moves: continue, edit (fix at the source), or new chat (clear dead weight).",
    ])

    # =========================================================================
    # SECTION 04 — How LLMs Fail
    # =========================================================================
    add_section_header(prs, "04", "How LLMs\nFail",
        "False things stated with total confidence, different answers to the same question, "
        "nothing past the cutoff, and quietly skewed output. None of it is a malfunction.",
        "[IMAGE: Soldier double-checking map coordinates before calling in a grid — verification before action]")

    add_concept_slide(prs, "Failure Mode 1: Hallucination", [
        ("The model has no truth-checking step.", False),
        ("It generates tokens that are statistically likely to follow prior context.", False),
        ("It cannot distinguish accurate training data from plausible completion.", False),
        ("Confident output and correct output are entirely unrelated.", False),
        ("This is expected behavior of the system — not a rare bug.", False),
        ("Doctrinal frame: the sharp junior analyst who never says 'I don't know.'", True),
    ], note="The goal is calibrated trust, not distrust. The model is extraordinarily capable AND it hallucinates. Both are true simultaneously.")

    add_concept_slide(prs, "Failure Modes 2, 3, and 4", [
        ("Confident-Wrong — hallucination is not always dramatic.", False),
        ("Subtly wrong dates, statistics, or plausible citations that do not exist; tone stays equally confident.", True),
        ("Nondeterminism — temperature introduces variation by design.", False),
        ("Same prompt, different run, different result. Do not treat one output as 'the answer.'", True),
        ("Knowledge Cutoff — three behaviors that look identical from the outside:", False),
        ("(a) flags the gap honestly  (b) answers confidently from stale data  (c) searches the web — confirm it fired.", True),
        ("You cannot tell which one you got without checking. Grounding tools are Module 3.", True),
    ], note="All three knowledge-cutoff cases look the same on screen. Never let confidence stand in for a check on anything that could have changed since training.")

    add_concept_slide(prs, "Failure Mode 5: Bias-Spotting (Literacy)", [
        ("The model learned from human text, and human text carries skewed patterns and stereotypes.", False),
        ("The model reproduces those patterns.", False),
        ("Ask it to 'describe a nurse' or 'describe a hacker' — notice the defaults it reaches for.", True),
        ("Ask about a thinly-represented group or region — watch the output get generic or lean on cliche.", True),
        ("Your job HERE is literacy: simply notice when output is skewed or stereotype-shaped.", False),
        ("The ethical duty — what you owe affected people, and unit policy — is Module 9.", False),
    ], note="Same rule as hallucination: name the skew, do not conclude the tool is useless. Calibrated trust, not cynicism.")

    add_check_on_learning(prs,
        "You just watched the model invent a source.\n\n"
        "What does that mean for the next time it gives you a fact you have not heard before?\n\n"
        "You run the same prompt twice in two separate chats and get different answers. "
        "What is the most accurate explanation?\n\n"
        "A) One of the chats had a longer context window\n"
        "B) The model updated itself between the two runs\n"
        "C) The model uses randomness by design — the same input does not guarantee the same output\n"
        "D) You phrased the prompt slightly differently without noticing")

    add_hands_on(prs, "How LLMs Fail", [
        "Ask for 5 peer-reviewed sources on a narrow topic — with author names, journals, and years.",
        "Pick one citation and try to verify it exists. Search the journal's site or a database.",
        "Ask the same question in a new chat. Compare the two citation lists — identical?",
        "Ask about something you know happened recently. Watch it handle events past its cutoff.",
        "Ask it to 'describe a typical [role]' for two stereotype-prone roles. Note the defaults — that is bias you can see.",
    ], "[IMAGE: Analyst comparing two documents side by side — verifying source against model output]")

    add_section_summary(prs, "How LLMs Fail", [
        "Hallucination: completes plausibly, not accurately — no truth-checking step.",
        "Confident-Wrong: tone is equally confident for right and wrong claims — never read confidence as accuracy.",
        "Nondeterminism: same prompt, different run, different result — by design.",
        "Knowledge cutoff: confident answers past training may be wrong. Bias: spot skewed/stereotype output.",
    ])

    # =========================================================================
    # SECTION 05 — Verifying AI Output as a Method
    # =========================================================================
    add_section_header(prs, "05", "Verifying AI\nOutput as a\nMethod",
        "'Verify it' is not a vibe — it is five concrete techniques. Drill them and the mandated "
        "reflex becomes a skill you can execute under time pressure.",
        "[IMAGE: Intelligence analyst cross-referencing a claim against primary source documents]")

    add_concept_slide(prs, "Five Verification Techniques", [
        ("Cite-and-check — ask for the source, then confirm the source actually says it.", False),
        ("A model that invents the claim often invents the source too — check it, do not just request it.", True),
        ("Cross-source — confirm against an independent authoritative source you trust.", False),
        ("Not another AI: two pattern-matchers trained on the same internet is not corroboration.", True),
        ("Re-run for consistency — run it 2-3 times in fresh chats; wobble run-to-run is a red flag.", False),
        ("Second-tool check — take the same question to a genuinely different tool.", False),
        ("Lateral reading — leave the answer; read ABOUT the claim and its sources from the outside.", False),
    ], note="Match the technique to the stakes: a throwaway brainstorm needs none; a number going into a product gets at least one; a claim informing a decision gets cross-source plus a second-tool check.")

    add_example_slide(prs, "Two AIs Agreeing Is Not Verification",
        "Scenario: Checking a model's factual claim",
        ["WRONG — false corroboration:",
         "  Ask Claude a question. Get an answer.",
         "  Ask ChatGPT the same question. They match.",
         "  Conclude it is verified.",
         "  Reality: two pattern-matchers read overlapping training data. You verified nothing.",
         "",
         "RIGHT — independent corroboration:",
         "  Take the claim to the PRIMARY document, an official record, or a subject-matter expert.",
         "  A genuinely different system is unlikely to make the same mistake in the same place.",
         "",
         "Scale the rigor to the consequence — not every claim needs all five techniques."],
        "[IMAGE: Two screens showing matching AI answers next to a single authoritative source document]")

    add_check_on_learning(prs,
        "The model gives you a specific statistic that will go into a brief your commander reads.\n\n"
        "Which of the five techniques do you run before that number leaves your hands — and why that one?\n\n"
        "You want to verify a factual claim a model gave you. Which approach is genuinely independent corroboration?\n\n"
        "A) Ask a second AI chatbot the same question and see if it agrees\n"
        "B) Ask the same model to confirm it is sure\n"
        "C) Check the claim against an authoritative primary source you trust\n"
        "D) Re-read the model's answer more carefully")

    add_hands_on(prs, "Verifying AI Output", [
        "Ask the model a factual question whose answer you do NOT already know. Save the answer.",
        "Cite-and-check: ask for the source. Confirm it exists and says what was claimed.",
        "Re-run: ask the identical question in two fresh chats. Did the answer hold or drift?",
        "Second-tool / cross-source: take the claim to a search engine or the primary document. Does it hold?",
        "Write one sentence: which technique would you reach for first for the work you actually do, and why?",
    ], "[IMAGE: Soldier running a checklist — each line a separate verification step against a real claim]")

    add_section_summary(prs, "Verifying AI Output as a Method", [
        "Five techniques: cite-and-check, cross-source, re-run, second-tool, lateral reading.",
        "Two AIs agreeing is not corroboration — independence is the whole point.",
        "Scale verification rigor to the stakes of the output.",
        "The mandated 'verify it' reflex is now five drills you can actually execute.",
    ])

    # =========================================================================
    # SECTION 06 — When to Use AI, and When Not To
    # =========================================================================
    add_section_header(prs, "06", "When to Use\nAI — and\nWhen Not To",
        "Right tool for open-ended language work. Wrong tool for precise facts, live data, "
        "authoritative citation, and anything sensitive.",
        "[IMAGE: Soldier choosing the right tool from a kit — matching the instrument to the job]")

    add_concept_slide(prs, "Right Tool / Wrong Tool", [
        ("Good at: drafting, rewriting, summarizing, brainstorming, explaining, reformatting, translating, first passes.", False),
        ("Anything where the value is the language and you remain the check on the facts.", True),
        ("Wrong tool — reach for something else:", False),
        ("Precise math or calculation — it predicts plausible numbers, it does not compute reliably.", True),
        ("Real-time or post-cutoff facts — guessing from stale data without verified grounding (Module 3).", True),
        ("Authoritative citation or the official record — go to the source; the model is not the source.", True),
        ("Anything sensitive or above the system's ceiling — a HARD STOP, not a judgment call.", True),
    ], note="The wrong-tool tell: if you are about to trust the model on a number, a date, a citation, or a live fact — stop. Those are exactly the four cases it is built to get confidently wrong.")

    add_concept_slide(prs, "The Decision Checklist — Run It Before You Type", [
        ("1. Open-ended language work, or a precise/authoritative answer? (Precise -> wrong tool.)", False),
        ("2. Does the answer depend on current or post-cutoff information? (Yes -> wrong tool without verified grounding.)", False),
        ("3. Can I verify the output before anyone relies on it? (No -> do not use it for this.)", False),
        ("4. Is the content sensitive, controlled, or above this system's ceiling? (Yes -> hard stop, do not paste.)", False),
        ("Clears all four? AI is a good fit — and you still verify what matters.", False),
    ], note="Question 4 is a hard stop, not a tradeoff. If the content is sensitive or above the ceiling, the answer is no regardless of how useful the tool would be. Full treatment in Section 07.", accent=CYBER_GOLD)

    add_check_on_learning(prs,
        "A teammate is about to ask a chatbot to compute exact payroll figures from a personnel roster.\n\n"
        "Two separate things are wrong with that. Name both.\n\n"
        "Which task is the LLM the WRONG tool for?\n\n"
        "A) Drafting a first version of a memo you will edit and verify\n"
        "B) Rewriting a dense paragraph in plainer language\n"
        "C) Producing the exact current price of a commodity and treating it as authoritative\n"
        "D) Brainstorming a list of possible approaches to a problem")

    add_hands_on(prs, "When to Use AI", [
        "List the last five things you used (or wanted to use) an AI tool for.",
        "Run each one through the four-question checklist.",
        "Flag any that were actually wrong-tool cases — precise math, live facts, authoritative citation, sensitive content.",
        "For one flagged case, write down what the RIGHT tool would have been.",
    ], "[IMAGE: Decision flowchart pinned to a planning board — four checks before committing to a course of action]")

    add_section_summary(prs, "When to Use AI — and When Not To", [
        "AI fits open-ended language work where you remain the check on the facts.",
        "Four wrong-tool cases: precise math, live/post-cutoff facts, authoritative citation, sensitive content.",
        "Run the four-question checklist BEFORE you type, not after the output disappoints.",
        "The authorization question is a hard stop, not a tradeoff.",
    ])

    # =========================================================================
    # SECTION 07 — Data Handling: What Never to Paste
    # =========================================================================
    add_section_header(prs, "07", "Data Handling:\nWhat Never to\nPaste",
        "Once you are pasting real work into a cloud-connected tool, what you paste matters. "
        "This rule does not expire under time pressure.",
        "[IMAGE: Soldier securing a classified document safe before turning to a civilian terminal]")

    add_concept_slide(prs, "Authorization Is a Property of the System", [
        ("Authorization is a property of the system — not the impressiveness of the tool.", False),
        ("A highly capable model on an unauthorized system does not become authorized because it is impressive.", False),
        ("The boundary is set by policy, not capability.", False),
        ("What must never go into an unauthorized system:", False),
        ("PII: names combined with identifiers, SSNs, DOBs, home addresses", True),
        ("Sensitive, controlled, or classified material of any kind", True),
        ("Anything above the system's authorization ceiling", True),
    ], note="Most AI delivery is cloud-based: your input leaves your machine. This is the security spine — what flows IN. What you do with the output, and whether a use is ethical/lawful, is Module 9.")

    add_concept_slide(prs, "The Default Posture and the Classify-Before-You-Paste Habit", [
        ("Default posture: when in doubt, do not paste. Ask someone who can authorize it first.", False),
        ("Classify before you paste — take two seconds before pasting anything:", False),
        ("What is this content?", True),
        ("Is this system authorized for it?", True),
        ("Build that pause until it is automatic.", True),
        ("The 'paraphrase and summarize it first' loophole does not exist.", False),
        ("This bright line does not expire — not at the end of this course, not under time pressure.", False),
    ], note="One careless paste in an unauthorized system is the kind of mistake with real and lasting consequences. Default to no until you hear yes from someone who can authorize it. Do not soften this.", accent=CYBER_GOLD)

    add_check_on_learning(prs,
        "You are under a deadline and want to paste a document into your AI tool to summarize it quickly. "
        "You are not sure whether the system is authorized for that content.\n\n"
        "What do you do?\n\n"
        "You have a borderline-sensitive document and an unauthorized but highly capable AI tool that would save hours. "
        "What is the correct call?\n\n"
        "A) Paste it — the efficiency gain justifies a judgment call\n"
        "B) Summarize the key points in your head first, then paste the summary\n"
        "C) Do not paste. Authorization does not change based on capability or time pressure. Ask first.\n"
        "D) Paste it, but delete the conversation immediately after")

    add_hands_on(prs, "Data Handling: What Never to Paste", [
        "No prompting today. Think about the last three things you pasted into an AI tool.",
        "For each one: was the system authorized for that type of content?",
        "Identify one category of content you work with regularly that you will never paste into an unauthorized tool.",
        "Write that category down. It is your personal bright line.",
        "Keep it. It does not expire.",
    ], "[IMAGE: Soldier reviewing a checklist before touching a terminal — a deliberate pause before action]")

    add_section_summary(prs, "Data Handling: What Never to Paste", [
        "Authorization is a property of the system — not the tool's capability or your time pressure.",
        "PII, sensitive, controlled, and classified material must never go into an unauthorized system.",
        "Default posture: when in doubt, do not paste. Ask first.",
        "Classify before you paste — build the two-second pause until it is automatic.",
    ])

    # =========================================================================
    # MODULE SUMMARY TABLE
    # =========================================================================
    col_x = [L, Inches(3.5), Inches(8.1)]
    col_w = [Inches(2.9), Inches(4.4), Inches(5.0)]
    add_summary_table(prs,
        "MODULE SUMMARY",
        "Know Your Weapon — Seven Core Concepts",
        [
            ("What an LLM Is",       "Prediction from learned patterns",            "Fluent output is not correct output. The only verb is 'predicts.'"),
            ("Tokens & Context",     "Finite working memory (intro depth)",         "Long chats degrade as the window fills. Deep mgmt is Module 8."),
            ("Conversation Mechanics","Stateless engine, re-fed the transcript",     "'Memory' is re-reading. No cross-chat recall by default."),
            ("How LLMs Fail",        "Five modes — all expected behavior",           "Verify anything that matters. Spot the skew. Confidence is not accuracy."),
            ("Verifying Output",     "Five techniques as drills",                    "Cite-and-check, cross-source, re-run, second-tool, lateral reading."),
            ("When to Use AI",       "Right for language, wrong for precise/live",   "Run the four-question checklist before you type."),
            ("Data Handling",        "Authorization is a property of the system",    "When in doubt, do not paste. The bright line does not expire."),
        ],
        ["CONCEPT", "CORE IDEA", "WHY IT MATTERS"],
        col_x, col_w)

    # =========================================================================
    # READINESS CHECK
    # =========================================================================
    add_readiness_check(prs, [
        "I can state in one sentence what an LLM does — using only the verb 'predicts'",
        "I can explain tokens and the context window, and why long chats degrade",
        "I can explain why the model is stateless and what conversation 'memory' really is",
        "I can name the five failure modes and have produced a hallucination with my own hands",
        "I can run the five verification techniques as drills, not as a vibe",
        "I can run the four-question 'when to use AI' checklist before I type",
        "I know what must never go into an unauthorized system and have written my personal bright line",
    ])

    # =========================================================================
    # END SLIDE
    # =========================================================================
    add_end_slide(prs, "Module 1:\nKnow Your Weapon", [
        "Produce a hallucination with your own hands before moving on — if you have not yet, do it now.",
        "Run all five verification techniques against one planted false claim in a single session.",
        "Run your last five AI uses through the four-question 'when to use it' checklist.",
        "Write down your personal bright line for content you handle — and keep it. It does not expire.",
    ])

    save_deck(prs, __file__, "01-ai-foundations.pptx")


if __name__ == "__main__":
    build()
