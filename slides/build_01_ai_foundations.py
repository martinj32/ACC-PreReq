"""
ACC Module 1 — Know Your Weapon: How AI Actually Works
Slide deck builder. Uses the shared Army Cyber Dark theme.

Mirrors docs/modules/01-ai-foundations.md section-for-section, plus an enrichment
layer: speaker notes on every teaching/check/hands-on/framing slide, and one
deep-dive concept slide after each core concept (intro depth — later modules go
deeper). Run by the orchestrator only — do not run python here.
"""

from acc_theme import *


def build():
    prs = new_deck()

    # --- TITLE ---
    set_notes(add_title_slide(prs,
        "Module 1:\nKnow Your Weapon",
        "PREREQUISITE MODULE  |  SELF-PACED",
        "[IMAGE: Soldier at a command-post terminal studying how an AI tool works before relying on it — knowing the weapon before carrying it]"),
        "Orientation: This is a prerequisite, self-paced module. The framing is deliberate — you learn the weapon system before you are trusted to employ it. By the end you should be able to: say in one sentence what an LLM does (verb: 'predicts'), recognize its predictable failure modes, verify its output as a drill, decide when it is the wrong tool, and apply a hard rule about what never gets pasted into an unauthorized system. Work the hands-on drills with a real tool open — reading alone will not build the reflexes.")

    # --- OVERVIEW ---
    set_notes(add_overview_slide(prs,
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
        ]),
        "The BLUF is the whole module in one breath: an LLM predicts text from learned patterns — not rules, not memory, not live data. Seven sections build on each other: what it is, how tokens/context work, why it's stateless, how it fails, how to verify, when to use it, and what never to paste. Set expectations: tokens/context is intro-depth here (Module 8 goes deep); grounding and tools are Module 3; the ethics of bias and of output use are Module 9. The two non-negotiables to leave with: verify what matters, and never paste sensitive content into an unauthorized system.")

    # =========================================================================
    # SECTION 01 — What an LLM Actually Is
    # =========================================================================
    add_section_header(prs, "01", "What an LLM\nActually Is",
        "The model predicts what comes next — not rules, not memory, not a lookup table. "
        "Fluent output is not the same as correct output.",
        "[IMAGE: Soldier reading a training manual — learning patterns, not memorizing a rulebook]")

    set_notes(add_concept_slide(prs, "Prediction, Not Lookup", [
        ("The model reads a sequence of text and predicts what comes next — one chunk at a time.", False),
        ("No lookup table. No truth check. No rules written by a programmer.", False),
        ("Given everything written so far: what is the statistically most likely next piece?", False),
        ("Trained, not programmed.", False),
        ("No one wrote 'Paris is the capital of France.' The model trained on enough text that it became the likely completion.", True),
        ("Upside: it generalizes across almost any domain.", True),
        ("Failure mode: if training data was wrong or thin, the model learned those patterns too.", True),
    ], note="The only accurate verb is 'predicts.' The model does not know, want, think, or lie. Catch yourself using those words and swap in 'predicts.'"),
        "A large language model does one thing: it reads the sequence of text in front of it and predicts the next chunk. That is the whole job. There is no lookup table it consults, no fact-checking step, no library of hand-written rules a programmer typed in. The single question it answers, over and over, is: \"Given everything so far, what is the most likely next piece?\" Picture a colleague who has read an enormous amount and learned which words tend to follow which — when you say \"the capital of France is,\" the strongest continuation is \"Paris.\" Nobody ever wrote a rule that says \"Paris is the capital of France.\" That sentence simply became the most likely completion during training, because the model was trained, not programmed. The common misconception this corrects: people assume the model is \"looking up an answer\" in a database. It is not. It is predicting. The upside is that prediction generalizes — it can complete sentences it has never seen exactly. The matching failure: if the patterns it learned were wrong or thin, it predicts confidently anyway. Capable and predictably fallible, both at once. The only accurate verb here is \"predicts.\"")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "Trained, Not Programmed: Where the Patterns Come From", [
        ("A programmer writes explicit rules; this model has none of that.", False),
        ("Training = showing it enormous amounts of text and nudging it to predict the next chunk better.", False),
        ("It learns statistical patterns, not stored facts.", False),
        ("'Paris' follows 'the capital of France is' because that pattern dominated the text.", True),
        ("One mechanism, both traits:", False),
        ("Strength: it generalizes to sentences it never saw exactly.", True),
        ("Weakness: thin or wrong patterns get predicted just as confidently.", True),
    ], note="Intro framing only — how training actually adjusts the model is beyond this module."),
        "This slide closes a gap the prior slide leaves: learners hear \"trained, not programmed\" but often picture training as someone loading facts into a database. That is the wrong mental model. Programming means a human writes explicit instructions: if the user asks X, return Y. This model has none of those. Training is different in kind — the model is shown a vast amount of text and repeatedly nudged to get better at one task: predicting the next chunk. Over time it absorbs which patterns of words tend to follow which. It never files away \"Paris is the capital of France\" as a fact; that string just becomes the most likely completion of \"the capital of France is.\" This single mechanism is why the model is both impressive and unreliable. Because it learned patterns rather than memorized entries, it can handle phrasings it never encountered — real capability. But the very same process means a pattern that was rare, outdated, or simply wrong in the training text gets predicted just as smoothly as a correct one. Capable and predictably fallible, from one cause. Keep the verb straight: it predicts.\n\nSuggested visual: split panel — left 'PROGRAMMED: human types if/then rules'; right 'TRAINED: model reads text, learns next-chunk patterns'.")

    set_notes(add_concept_slide(prs, "The LLM Is the Engine", [
        ("By itself, the LLM is a brain in a jar.", False),
        ("Capable of reasoning in text — incapable of acting on its own.", False),
        ("No body. No memory between chats. No live connection to the world unless something gives it one.", False),
        ("Fluent, confident output is not the same as correct output.", False),
        ("Both are true simultaneously — that is the working mental model.", False),
    ], note="VERIFY BEFORE TEACHING: model names, tiers, context-window sizes, and pricing change every release. Any specific number in this course is a snapshot — confirm at the provider's docs before a course run."),
        "By itself, the model is a brain in a jar. It reasons in text — extraordinarily well — but it cannot act on its own. It has no body, so it cannot click, send, or run anything. It has no memory between chats, so it starts every conversation blank. It has no live connection to the world unless something hands it one. Everything you have seen an AI product \"do\" — search the web, read a file, send an email — is wiring bolted on around the engine, not the engine itself. We cover that wiring (tools and grounding) in Module 3. The point to lock in now is the gap between fluent and correct. The model produces smooth, confident output by design, because fluency is exactly what next-token prediction optimizes. Confidence is not evidence of accuracy. A wrong answer arrives in the same calm, well-formed prose as a right one. Hold both truths at once: the engine is genuinely capable, and it fails in predictable ways. That is calibrated trust.")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "Fluent Is Not Correct: Calibrated Trust", [
        ("Fluency is what next-chunk prediction optimizes — smooth text is the product, not proof.", False),
        ("A confident tone carries no information about accuracy.", False),
        ("A wrong answer arrives in the same calm prose as a right one.", False),
        ("Calibrated trust = hold both at once:", False),
        ("Genuinely capable across a huge range of tasks.", True),
        ("Fails in predictable ways — and looks just as confident when it does.", True),
        ("Practical posture: verify load-bearing claims; never read confidence as evidence.", False),
    ], note="Why and when it fails most predictably is built out in later modules; here, just separate fluent from correct."),
        "This slide gives learners a posture to carry, not just a fact. The deck's whole theme is calibrated trust, and this is where it gets concrete. Start from why the model sounds so sure: it was optimized to produce likely, well-formed text. Confident, fluent prose is literally the output it is best at generating. That means the smoothness of an answer tells you nothing about whether the answer is true. Picture two responses side by side — one accurate, one wrong. They look identical: same calm tone, same clean grammar, same air of authority. There is no built-in tell. So the working posture is calibrated trust, which is two things held together and never collapsed into one. Do not slide into hype (\"it's basically always right\") and do not slide into cynicism (\"it's just fancy autocomplete, ignore it\"). Both are wrong. The honest position: it is extraordinarily capable and it fails in predictable ways, simultaneously. The operational consequence is simple — when a claim is load-bearing, verify it from a real source. Treat confidence as style, not evidence.\n\nSuggested visual: two identical-looking speech bubbles, one labeled CORRECT, one WRONG — same confident style.")

    set_notes(add_check_on_learning(prs,
        "The model just gave you a confident-sounding answer.\n\n"
        "What would it take to verify it? Where would you check?\n\n"
        "A language model was never given a rule that says 'Paris is the capital of France.' "
        "How does it produce that answer?\n\n"
        "Think it through: trained on patterns vs. looked up vs. hard-coded — which is it, and what does that mean for accuracy?"),
        "ANSWER KEY. The model produces \"Paris\" because it was TRAINED on patterns, not because it looked the fact up or because a programmer hard-coded a rule. During training it saw \"the capital of France is Paris\" (and the surrounding pattern) enough times that \"Paris\" became the most likely completion. Implication for accuracy: there is no database row guaranteeing correctness — only a strong statistical pattern. Where that pattern in the training text was thin or wrong, the same mechanism produces a confident wrong answer. To verify an output you cannot rely on the model itself; you go to an independent source (Section 05).")

    set_notes(add_hands_on(prs, "What an LLM Actually Is", [
        "Type an incomplete sentence on a topic you know well and submit it. Read what the model predicts.",
        "Add the word 'definitely' or 'obviously' to the same sentence and submit again. Does the completion change?",
        "Ask the model a factual question you already know the answer to. Check the output for accuracy.",
        "Ask the exact same question in a new chat. Is the answer identical, or slightly different?",
        "Ask yourself: 'How would I verify any of these outputs if I did not already know the answer?'",
    ], "[IMAGE: Soldier testing radio frequencies — observing how small input changes shift the output]"),
        "FACILITATION: the point is to FEEL prediction, not to get a \"right\" answer. In step 2, adding \"definitely/obviously\" often shifts the completion — proof the model steers on surrounding tokens, not facts. In step 4, the same question in a new chat often returns a slightly different answer — nondeterminism, previewed. The real deliverable is step 5: if you cannot say how you would verify an output, you do not yet trust it appropriately.")

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

    set_notes(add_concept_slide(prs, "What Is a Token?", [
        ("The model does not read words — it reads chunks of text called tokens.", False),
        ("In English prose, one token is roughly three-quarters of a word.", False),
        ("Code and non-English text tokenize less efficiently — more tokens per word.", False),
        ("You do not need to count tokens precisely.", False),
        ("The instinct to keep input focused is the deliverable from this section.", False),
    ], note="This is INTRO depth only. Spending tokens deliberately and managing context as a resource is Module 8 (Ammunition Discipline). Learn the 'what' here; learn the 'how to spend' there."),
        "The model does not read words. It reads tokens — chunks of text the tokenizer carves your input into. A token is often a whole short word, but longer or rarer words split into pieces, and punctuation and spaces count too. A useful rule of thumb for ordinary English: about 1 token per 4 characters, or roughly 0.75 of a word per token, which is the same as saying 100 tokens is about 75 words. (Verify before a course run — figures are model/tokenizer dependent.) Two things tokenize less efficiently than plain prose: source code, with all its symbols and indentation, and non-English text, especially languages that do not use the Latin alphabet — both burn more tokens for the same apparent length. You will never need to count tokens by hand, and you should not try. The deliverable from this slide is an instinct, not arithmetic: everything you send costs tokens, so keep your input focused and free of dead weight. How you actually budget and spend tokens across a long task — \"ammunition discipline\" — is the subject of Module 8.")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "A Token, Worked: One Sentence Split", [
        ("Take a plain sentence: 'The radio operator re-read the log.'", False),
        ("The tokenizer carves it into chunks — not one word, one token.", False),
        ("Common short words ('The', ' log') are often a single token; spaces ride with the next word.", True),
        ("A less common or hyphenated stretch ('re-read') can split into pieces.", True),
        ("Rule of thumb (English): ~4 chars per token, ~0.75 word per token, 100 tokens ≈ 75 words.", False),
        ("Code and non-English text split into MORE tokens for the same length.", False),
        ("You never count by hand — the instinct is 'keep input lean.'", False),
    ], note="Intro only; budgeting tokens across a task is Module 8 (Ammunition Discipline). Figures are model/tokenizer dependent — verify before a run."),
        "The prior slide tells learners the model reads tokens, but \"token\" stays abstract until they watch one sentence get cut up. So we work an example. Take \"The radio operator re-read the log.\" A tokenizer does not split on words; it splits on learned chunks. Very common words like \"The\" or \"log\" usually come through as a single token, and the leading space is bundled with the word after it — that is why spacing counts toward your total. A less common or hyphenated stretch like \"re-read\" can break into two or three pieces. Out of this comes the practical rule of thumb for everyday English: roughly one token per four characters, or about three-quarters of a word per token, which is the same as saying 100 tokens lands near 75 words. Two warnings on that rule. Source code tokenizes far less efficiently — every bracket, dot, and indent eats tokens — and non-English text, especially non-Latin scripts, runs higher too. None of this is something you compute manually. The takeaway is an instinct: text becomes tokens, tokens are finite, so send focused input and cut dead weight. How you actively manage that budget is Module 8.\n\nSuggested visual: the sentence with vertical bars showing token boundaries, e.g. The | radio | operator | re | -read | the | log | .")

    set_notes(add_concept_slide(prs, "The Context Window", [
        ("Every model has a hard ceiling on tokens it can hold in a single conversation.", False),
        ("That ceiling is the context window — a whiteboard with finite space.", False),
        ("New writing crowds out old writing once it fills.", False),
        ("A full window: the model hedges, contradicts what it said ten turns ago, forgets a constraint.", False),
        ("That is not a bug — it is the whiteboard running out of space.", False),
        ("Models attend better to the beginning and end of the window than to the middle.", True),
        ("Start a fresh chat when the task changes OR when the model starts drifting.", True),
    ], note="VERIFY BEFORE TEACHING: approximate sizes change with releases — Claude ~200k, GPT-4o ~128k, Gemini 1M+ tokens. Bigger is not always better; quality degrades in the middle of a huge window."),
        "Every conversation has a hard ceiling on how many tokens it can hold at once. That ceiling is the context window. Think of it as a whiteboard of fixed size: your messages, the model's replies, and any files or instructions all get written on the same board. When the board fills, new writing crowds out the old — there is no overflow bin. Approximate sizes at the time of writing: Claude models around 200K tokens (larger on some tiers), GPT-4o around 128K, and Gemini 2.5 Pro at 1M or more. These change constantly — verify before a course run and treat them as ballpark. When a window gets full or cluttered, you see real symptoms: the model starts hedging, contradicts something it said earlier, or quietly drops a constraint you set at the top. That is not a bug — it is the whiteboard running out of room. There is a second wrinkle: models attend more reliably to the beginning and the end of the window than to the middle, so material buried in a long middle is the easiest to lose. The practical move is simple — start a fresh chat when the task changes or when the model begins to drift.")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "Lost in the Middle: Where Attention Goes", [
        ("Models attend more reliably to the start and end of the window than the middle.", False),
        ("Performance follows a U-shape: strong at the edges, weak in the center.", False),
        ("Holds even for models built for long context.", True),
        ("In a long chat: a top constraint can fade; a detail in the middle is easiest to drop.", False),
        ("Defensive moves:", False),
        ("Put the key instruction near the top, or restate it near your latest message.", True),
        ("Start fresh when the thread is long and the middle is bloated.", True),
    ], note="This is an intro to position effects; deeper context management is Module 8."),
        "The prior slide mentions in passing that models attend better to the beginning and end than the middle. This slide makes that concrete because it changes how you write prompts. Researchers tested where, inside a long input, a model can actually find a piece of information. The result was a U-shaped curve: accuracy is highest when the needed information sits at the very start or the very end, and it sags noticeably when that information is parked in the middle. This held even for models specifically marketed as long-context — a bigger window does not flatten the dip. So what does this mean at the keyboard? Two things go wrong in long chats. A rule you set in your opening message can quietly lose force as the conversation grows and that opener drifts toward the buried middle. And a detail mentioned once, deep in a long exchange, is the single most likely thing to get dropped. The defense is positional. Put your most important constraint near the top, and if the chat has gotten long, restate it close to your newest message so it sits at the high-attention end. When the middle is bloated, start fresh. Deeper management techniques come in Module 8.\n\nSuggested visual: U-shaped curve, x-axis 'position in context (start → middle → end)', y-axis 'recall accuracy', with a dip in the middle.")

    set_notes(add_check_on_learning(prs,
        "You set an important constraint at the start of a long conversation. "
        "Ten exchanges later, the model seems to have forgotten it.\n\n"
        "What happened, and what would you do differently next time?\n\n"
        "You are in a long chat and the model starts contradicting instructions you gave at the start. "
        "What is the most likely cause?\n\n"
        "A) The model changed its mind\n"
        "B) You used the wrong model for this task\n"
        "C) Earlier content has been crowded out of the context window\n"
        "D) The model is testing whether you notice"),
        "ANSWER KEY: C — earlier content has been crowded out of the context window. The model did not \"change its mind\" (A) and is not \"testing\" you (D); using a different model (B) is unrelated. The whiteboard filled, and your early constraint scrolled off or sank into the low-attention middle. Fixes: restate the constraint near your latest message, or start a fresh chat and lead with the constraint. Ties to the \"lost in the middle\" effect.")

    set_notes(add_hands_on(prs, "Tokens and Context", [
        "Open a fresh chat and paste several paragraphs of dense text.",
        "Ask the model to summarize just the first paragraph.",
        "In the same chat, ask it about something from the end of what you pasted.",
        "Start a new chat and ask the same question. Compare the quality.",
        "Notice: does the model attend differently to the top vs. the buried middle?",
    ], "[IMAGE: Soldier reviewing a long operation log — noting what dropped off the bottom]"),
        "FACILITATION: learners should notice the model handles the FIRST paragraph (top of window) more reliably than something buried in the middle of a long paste — the \"lost in the middle\" effect made real. The fresh-chat comparison should feel cleaner. Takeaway to name aloud: keep input focused; put the most important instruction near the top or restate it near your latest message.")

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

    set_notes(add_concept_slide(prs, "The Model Is Stateless", [
        ("The engine remembers nothing between calls. It does not 'stay logged in' to your chat.", False),
        ("Each time you send a message, the platform feeds the ENTIRE thread back as one block of text.", False),
        ("The model reads all of it fresh, predicts the next turn — then forgets again.", False),
        ("'Memory' is the transcript, not recall.", False),
        ("When it refers back to message ten, it is re-reading it — because the platform put it back in front of it.", True),
        ("This is why the window matters: the conversation grows every turn, and the oldest turns drop off the top.", True),
    ], note="Kill the 'helpful person reading along' picture. Replace it with: a stateless engine handed a fresh transcript every turn. That one fact explains statelessness, context limits, and cross-chat memory all at once."),
        "There is no one on the other end keeping track of you. The model is stateless: it remembers nothing between calls. It does not \"stay logged in\" to your conversation. Here is what actually happens each time you hit send. The platform takes the entire thread so far — your first message, every reply, everything — bundles it into one big block of text, and feeds that whole block to the engine. The engine reads it fresh, predicts the next response, and then forgets all of it. The next turn, the platform does it again with the now-longer transcript. So the \"memory\" you experience is not the model recalling anything. It is the transcript being re-presented every single turn — like a radio operator who is handed the full log to re-read before every transmission, because he was never holding it in the first place. When the model \"refers back\" to something you said earlier, it is not remembering; it is re-reading text the platform just put in front of it again. This is exactly why the context window matters so much: that re-fed transcript has to fit inside the window, every turn.")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "What Statelessness Looks Like: A Three-Turn Walkthrough", [
        ("Turn 1 — you send 'My callsign is Bravo.' The engine reads it, replies, then forgets.", False),
        ("Turn 2 — you ask 'What's my callsign?' The platform re-feeds the WHOLE thread.", False),
        ("The engine reads it fresh, finds 'Bravo' in the text, answers — then forgets again.", True),
        ("It never 'kept' the callsign; it re-read what the platform re-pasted.", False),
        ("Every turn the re-fed transcript grows — and it must fit in the window.", False),
        ("If 'Bravo' scrolls out of the window, the engine can't see it — and the answer changes.", False),
    ], note="The 'memory' you feel is the transcript being re-presented, not the engine recalling anything."),
        "The prior slide states the principle; learners absorb it better by watching it run. Walk through three turns. On Turn 1 you tell the assistant your callsign is Bravo. Behind the scenes the platform packages that message, hands the whole thing to the engine, the engine predicts a reply, and then it discards everything — it holds nothing. On Turn 2 you ask, \"What's my callsign?\" The engine did not remember Bravo, because it remembers nothing. What lets it answer is that the platform re-feeds the entire thread so far — your first message, its reply, and your new question — as one block of text. The engine reads that block fresh, finds the word Bravo sitting right there in the transcript, and answers from it. Then it forgets again. Turn 3 repeats the pattern with an even longer transcript. Two consequences fall out. First, what feels like memory is just re-presentation — the radio operator handed the full log every transmission. Second, the punchline that ties back to Section 2: the re-fed transcript keeps growing and must fit in the context window. If Bravo ever scrolls out of that window, the engine literally cannot see it anymore, and the next answer will be wrong.\n\nSuggested visual: three stacked panels showing the transcript blob growing each turn, with an arrow re-feeding the whole blob into a 'stateless engine' box.")

    set_notes(add_concept_slide(prs, "No Cross-Chat Memory — and Your Three Moves", [
        ("A fresh chat starts with a blank transcript. It knows nothing about your other conversations.", False),
        ("Some products bolt on a 'memory' or 'projects' feature — that is an added layer, not the model remembering you.", False),
        ("Continue — add a turn; everything before stays in context. Use when the thread is helping.", False),
        ("Edit — rewrite an earlier message; most tools discard everything after and re-run. Fix bad instructions at the source.", False),
        ("New chat — start with an empty transcript. Use when old context is dead weight or dragging the model off course.", False),
    ], note="Edit at the source, do not pile on. If your third message had a bad instruction, edit it — do not send a fourth saying 'ignore that.' A clean transcript produces cleaner output."),
        "Open a fresh chat and the transcript is blank. The model knows nothing about your other conversations — not yesterday's, not the one in the next tab. Product features labeled \"memory\" or \"projects\" can make it feel like the model knows you, but those are an added layer: the platform quietly inserts saved notes into the transcript. The model is not remembering you; it is reading what was pasted in. Because every turn is just the platform re-feeding a transcript, you have exactly three moves to control what the engine sees. First, Continue: add a turn, and all prior context stays on the board. Second, Edit: rewrite an earlier message — and note that most tools then discard everything after that point and re-run from there, so editing is how you fix a problem at its source instead of stacking corrections on top of it. Third, New chat: start with an empty transcript to clear out dead weight when the old thread is cluttered or off-track. The discipline to carry away: when something went wrong upstream, edit at the source. Do not pile on more \"no, I meant\" messages — that just fills the window with noise.")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "Three Moves in Practice: Continue, Edit, New Chat", [
        ("Continue — add a turn; the full prior transcript rides along (use when on track).", False),
        ("Edit — rewrite an earlier message; most tools discard everything after and re-run.", False),
        ("This is how you fix a problem at its source instead of stacking corrections.", True),
        ("New chat — empty transcript; the model knows nothing of the old one.", False),
        ("Use when the thread is cluttered, off-track, or the task changed.", True),
        ("'Memory'/'projects' features just paste saved notes in — not the model recalling you.", False),
        ("Rule: fix upstream. Piled-on corrections only fill the window with noise.", False),
    ], note="Edit at the source; don't pile on corrections."),
        "The prior slide lists the three moves; this slide turns them into a decision habit. Everything you do to a chat is really an action on the transcript the platform re-feeds the engine, so think in terms of what each move does to that transcript. Continue simply appends your new turn while keeping all prior context — the right move when the conversation is healthy and you are building forward. Edit rewrites a message you already sent, and here is the part people miss: most tools then throw away everything after that message and re-run from the edit point. That is a feature, not a loss. It means editing is how you correct a mistake at its source rather than stacking \"no, I actually meant\" replies on top of a bad turn — those stacked corrections just clutter the window and can drift into the low-attention middle. New chat hands the engine a blank transcript; it knows nothing of the previous thread, which is exactly what you want when the old one is bloated or the task has changed. One myth to puncture: \"memory\" and \"projects\" features do not mean the model remembers you. They paste saved notes into the transcript for you. The model still just reads text. The discipline: fix upstream.\n\nSuggested visual: three labeled buttons — Continue (append), Edit (rewrite + truncate after), New chat (blank) — over a transcript strip.")

    set_notes(add_check_on_learning(prs,
        "You spent an hour in one chat building useful context. You close it and open a fresh one tomorrow.\n\n"
        "What does the new chat know about yesterday's work, and what would you do to get that context back?\n\n"
        "When the model refers back to something you said earlier in the SAME conversation, what is actually happening?\n\n"
        "A) The model stored your message in long-term memory\n"
        "B) The platform re-fed the whole transcript to the stateless model, so it re-read your earlier message\n"
        "C) The model has a running memory of you across all chats\n"
        "D) The model guessed what you probably said"),
        "ANSWER KEY: B — the platform re-fed the whole transcript to the stateless model, so it re-read your earlier message. It did not store anything in long-term memory (A), it has no running cross-chat memory of you by default (C), and it did not guess (D). \"Memory\" inside a conversation is re-reading the re-presented transcript, every turn. This is why a brand-new chat knows nothing of yesterday — and why a long chat eventually drops its own early turns.")

    set_notes(add_hands_on(prs, "Conversation Mechanics & Statelessness", [
        "Tell the model a specific fact ('My callsign is Raptor-6'). Continue a few turns, then ask it to repeat the fact.",
        "Open a brand-new chat and ask it for your callsign. Watch it have no idea — that is statelessness.",
        "Go back to the first chat, edit an early message to change the fact, and re-run. Watch the later turns regenerate.",
        "Reflect: when in your own work would 'edit the source message' beat 'send a correction'?",
    ], "[IMAGE: Two operation logs side by side — one continued, one started blank — showing what carries over and what does not]"),
        "FACILITATION: the callsign drill makes statelessness physical. Step 2 (new chat has no idea) is the \"aha\" — no cross-chat memory by default. Step 3 (edit the early message, watch later turns regenerate) shows \"fix at the source\" beats stacking corrections. If a tool has a \"memory/projects\" feature on, point out that is an added layer pasting notes in — not the model recalling you.")

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

    set_notes(add_concept_slide(prs, "Failure Mode 1: Hallucination", [
        ("The model has no truth-checking step.", False),
        ("It generates tokens that are statistically likely to follow prior context.", False),
        ("It cannot distinguish accurate training data from plausible completion.", False),
        ("Confident output and correct output are entirely unrelated.", False),
        ("This is expected behavior of the system — not a rare bug.", False),
        ("Doctrinal frame: the sharp junior analyst who never says 'I don't know.'", True),
    ], note="The goal is calibrated trust, not distrust. The model is extraordinarily capable AND it hallucinates. Both are true simultaneously."),
        "Start with the central tension. The model is extraordinarily capable AND it will state false things with total confidence. Both are true at once. A \"hallucination\" is not a glitch and not a rare bug — it is the system working exactly as built. The model predicts the next token that is statistically likely to follow the ones before it. There is no separate truth-checking step inside it. It cannot distinguish accurate training data from a plausible-sounding completion, because to the model those are the same kind of thing: likely text. That is why confident output and correct output are simply unrelated. The doctrinal frame: treat it as the sharp junior analyst who never says \"I don't know\" — brilliant, fast, and constitutionally unable to admit a gap, so it fills the gap with something that sounds right. Concrete case: in 2023 a New York attorney filed a brief citing six court decisions that did not exist; he had used ChatGPT, which fabricated case names, citations, and full opinions, then confirmed they were real when he asked. A judge sanctioned the attorneys $5,000 (Mata v. Avianca). Correct the misconception now: the goal is calibrated trust, not distrust. We do not stop using the analyst. We verify before we act.")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "Why Hallucination Is Structural, Not a Bug", [
        ("The model predicts the next likely token — no built-in step asks 'is this true?'", False),
        ("Right answers and invented ones come from the same process: likely-sounding text.", True),
        ("Training rewards a confident guess over 'I don't know.'", False),
        ("A guess can score points; 'I don't know' scores zero — so it learns to guess.", True),
        ("A 2025 OpenAI analysis argues this is baked into training and grading, not a patchable defect.", False),
        ("You can't wait for a version that 'stops hallucinating' — build verification in now.", False),
    ], note="Hallucination is the system working as designed, not breaking — so the fix is your process, not a patch. (2025 framing is version-dependent — verify before a run.)"),
        "People assume hallucination is a temporary defect that the next model release will fix. That assumption is dangerous because it tells you to wait instead of to verify. Walk through why it is structural. The model's whole job is to predict likely text. \"Likely\" and \"true\" overlap a lot — but they are not the same thing, and nothing inside the model separates them. On top of that, the way models are trained and tested rewards confident answers. If a test gives a point for a right guess and zero for \"I don't know,\" then over millions of examples the system learns that guessing beats admitting a gap — exactly like a student who answers every multiple-choice question because blanks are guaranteed zeros. A 2025 OpenAI paper, \"Why Language Models Hallucinate,\" makes this case directly: hallucinations trace back to pretraining and to evaluation methods that reward confident fabrication. Treat this framing as version-dependent and confirm the current state before teaching it. The takeaway is doctrinal: stop waiting for a perfect tool. The tool is genuinely powerful and it will keep doing this. Calibrated trust means you design the check into the work.\n\nSuggested visual: side-by-side — the same confident sentence, one labeled TRUE, one labeled FABRICATED, identical styling. Caption: 'From the outside, right and wrong look identical.'")

    set_notes(add_concept_slide(prs, "Failure Modes 2, 3, and 4", [
        ("Confident-Wrong — hallucination is not always dramatic.", False),
        ("Subtly wrong dates, statistics, or plausible citations that do not exist; tone stays equally confident.", True),
        ("Nondeterminism — temperature introduces variation by design.", False),
        ("Same prompt, different run, different result. Do not treat one output as 'the answer.'", True),
        ("Knowledge Cutoff — three behaviors that look identical from the outside:", False),
        ("(a) flags the gap honestly  (b) answers confidently from stale data  (c) searches the web — confirm it fired.", True),
        ("You cannot tell which one you got without checking. Grounding tools are Module 3.", True),
    ], note="All three knowledge-cutoff cases look the same on screen. Never let confidence stand in for a check on anything that could have changed since training."),
        "Three more predictable failure shapes. None is a malfunction. Confident-Wrong: the output is mostly right but a date, a statistic, or a citation is subtly off, and the tone is exactly as confident on the wrong part as on the right part. A plausible-but-fake citation is the classic tell — it looks formatted and real because the model predicts what a real citation looks like, not whether this one exists. Nondeterminism: same prompt, run twice, different answers — by design. A setting called temperature introduces variation so output is not robotic, so do not treat any single output as \"the answer\"; it is one sample from a range. (Even at temperature zero, modern systems can still vary run to run because of how requests are batched on hardware — a deeper topic, but the practical lesson holds.) Knowledge Cutoff: training stops at a date, and three behaviors look identical on screen — (a) it honestly flags the gap, (b) it answers confidently from stale data, (c) it searches the web for current info. You cannot tell which happened by reading the answer; you must confirm a search actually fired. Tools that fetch live data are grounding — that is Module 3. Today's literacy point: all three cases look the same, so check.")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "Anatomy of a Fabricated Citation", [
        ("A fake citation looks real because the model predicts the SHAPE of a citation, not a record.", False),
        ("Plausible name, court, year, perfect formatting — all invented.", True),
        ("Documented case: Mata v. Avianca (2023) — a lawyer filed six nonexistent ChatGPT-generated cases.", False),
        ("Asked to confirm they were real, the tool confirmed the fabrications; the attorneys were sanctioned $5,000.", True),
        ("The only catch: open the primary source and confirm the citation resolves.", False),
        ("Asking the same AI 'are you sure?' is not a check — it predicts reassurance.", False),
    ], note="A confident 'yes, it's real' from the same model is worthless; only the primary record settles it."),
        "This slide turns confident-wrong into something you can feel. A fabricated citation is the purest example, because a citation is pure format — and format is exactly what the model is best at predicting. It produces a name, a court, a volume, a year, all in correct style, because it has seen thousands of real ones. None of that machinery checks whether this specific case exists. Mata v. Avianca is the canonical real-world case, and it is worth telling in full because of the second mistake: when opposing counsel could not find the cases, the attorney did not go to a law database — he asked ChatGPT whether the cases were real, and it said yes. That is the trap to burn into memory. Asking a model to verify itself is not verification; it just predicts the reassuring answer. The judge sanctioned both attorneys $5,000 in June 2023 and required them to notify the real judges falsely named as authors. The discipline: a citation is verified only when you open the primary source and the cite resolves. This connects straight to cite-and-check and \"go to the primary document.\"\n\nSuggested visual: a clean, official-looking but fake case citation with a red 'DOES NOT EXIST' stamp. Caption: 'Formatted perfectly. Entirely invented.'")

    set_notes(add_concept_slide(prs, "Failure Mode 5: Bias-Spotting (Literacy)", [
        ("The model learned from human text, and human text carries skewed patterns and stereotypes.", False),
        ("The model reproduces those patterns.", False),
        ("Ask it to 'describe a nurse' or 'describe a hacker' — notice the defaults it reaches for.", True),
        ("Ask about a thinly-represented group or region — watch the output get generic or lean on cliche.", True),
        ("Your job HERE is literacy: simply notice when output is skewed or stereotype-shaped.", False),
        ("The ethical duty — what you owe affected people, and unit policy — is Module 9.", False),
    ], note="Same rule as hallucination: name the skew, do not conclude the tool is useless. Calibrated trust, not cynicism."),
        "This is a literacy skill, not the ethics lecture — the ethical and policy duty around bias is Module 9. Today you just learn to notice skew. Why skew exists: the model learned from enormous amounts of human text and human-made images. That material carries human patterns, including stereotypes, and the model predicts what is statistically common in that material, so it reproduces those patterns. Ask it to \"describe a nurse\" or \"a hacker\" and watch the defaults it reaches for. Ask about a thinly represented group or region and the output often flattens into something generic or cliche — because the model has less varied material to predict from, so it falls back to the dominant pattern. Concrete, documented case: Bloomberg generated over 5,000 images with a popular text-to-image model and found it pushed gender and racial disparities to extremes worse than the real world — high-paying jobs skewed toward lighter-skinned men; \"nurse\" and \"fast-food worker\" skewed the other way (\"Humans Are Biased. Generative AI Is Even Worse,\" 2023). Name the skew when you see it. That is the whole job here. Do not over-correct into \"the tool is useless\" — it is capable and it is skewed, both true. Naming it is what lets you use it well.")

    set_notes(add_check_on_learning(prs,
        "You just watched the model invent a source.\n\n"
        "What does that mean for the next time it gives you a fact you have not heard before?\n\n"
        "You run the same prompt twice in two separate chats and get different answers. "
        "What is the most accurate explanation?\n\n"
        "A) One of the chats had a longer context window\n"
        "B) The model updated itself between the two runs\n"
        "C) The model uses randomness by design — the same input does not guarantee the same output\n"
        "D) You phrased the prompt slightly differently without noticing"),
        "ANSWER KEY: C — the model uses randomness by design, so the same input does not guarantee the same output. It did not update itself between runs (B), context-window length is irrelevant here (A), and the variation is real even if your wording was identical (D). The setting is called temperature. Practical lesson: never treat a single output as \"the answer\" — it is one sample. Run-to-run wobble on a fact is a signal to verify.")

    set_notes(add_hands_on(prs, "How LLMs Fail", [
        "Ask for 5 peer-reviewed sources on a narrow topic — with author names, journals, and years.",
        "Pick one citation and try to verify it exists. Search the journal's site or a database.",
        "Ask the same question in a new chat. Compare the two citation lists — identical?",
        "Ask about something you know happened recently. Watch it handle events past its cutoff.",
        "Ask it to 'describe a typical [role]' for two stereotype-prone roles. Note the defaults — that is bias you can see.",
    ], "[IMAGE: Analyst comparing two documents side by side — verifying source against model output]"),
        "FACILITATION: this drill is designed to PRODUCE failures on purpose. The fabricated citations (steps 1-2) are the headline — most will not survive a real check; tie back to Mata v. Avianca. Step 3 shows the citation list changes run-to-run (nondeterminism). Step 5's \"describe a typical [role]\" surfaces visible bias. Frame every failure as expected behavior, not a broken tool — calibrated trust.")

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

    set_notes(add_concept_slide(prs, "Five Verification Techniques", [
        ("Cite-and-check — ask for the source, then confirm the source actually says it.", False),
        ("A model that invents the claim often invents the source too — check it, do not just request it.", True),
        ("Cross-source — confirm against an independent authoritative source you trust.", False),
        ("Not another AI: two pattern-matchers trained on the same internet is not corroboration.", True),
        ("Re-run for consistency — run it 2-3 times in fresh chats; wobble run-to-run is a red flag.", False),
        ("Second-tool check — take the same question to a genuinely different tool.", False),
        ("Lateral reading — leave the answer; read ABOUT the claim and its sources from the outside.", False),
    ], note="Match the technique to the stakes: a throwaway brainstorm needs none; a number going into a product gets at least one; a claim informing a decision gets cross-source plus a second-tool check."),
        "\"Verify it\" is not a vibe. It is a set of drills, from light to heavy. Cite-and-check: ask the model for its source, then go confirm the source actually says the thing — this catches the most common failure, because an invented claim usually rides in on an invented source, and asking then checking is two steps, not one. Cross-source: find an independent authoritative source you already trust — and it must NOT be another AI, because two pattern-matchers trained on the same internet agreeing is not corroboration; it is the same guess twice. Re-run for consistency: ask the same question in two or three fresh chats — because output is nondeterministic, run-to-run wobble on a fact is a red flag that the model is unsure and filling the gap. Second-tool check: run it through a genuinely different tool or system, one unlikely to fail in the same place. Lateral reading: leave the answer entirely, open new tabs, and read ABOUT the claim and its sources from the outside — this is how professional fact-checkers work; a Stanford study found they out-verified PhD historians, fast, precisely because they read laterally instead of staying on the page. Match the technique to the stakes — that is the next slide and the whole discipline.")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "Scale Your Verification to the Stakes", [
        ("Match the size of the check to the size of the risk — not every claim needs every technique.", False),
        ("Throwaway / brainstorm (no one acts on it): no verification needed.", False),
        ("A fact going into a product (brief, email, report): at least one independent check.", False),
        ("Cite-and-check, or one cross-source you trust.", True),
        ("An input to a real decision (resources, people): cross-source PLUS a second, different tool.", False),
        ("Independent authoritative source AND a genuinely different system — never two similar AIs.", True),
    ], note="Verify-before-you-call-the-grid — match the rigor to the consequence, every time."),
        "This is the slide that makes \"verify it\" practical instead of exhausting. Total verification on everything is unrealistic and people will just stop doing it. Zero verification on things that matter is how you end up in a Mata v. Avianca situation. The answer is calibration, in three concrete tiers. Tier one, throwaway: you are brainstorming and no one will act on the raw output, so no check is needed — speed is the point. Tier two, goes-into-a-product: the moment a specific fact, number, or quote will appear in something another person reads, you owe at least one independent check — cite-and-check the source, or pull one cross-source you already trust. Tier three, decision input: when output will shape a real decision about resources or people, you stack techniques — an independent authoritative source AND a genuinely different tool, because the cost of being confidently wrong is now high. The military frame lands here: verify-before-you-call-the-grid. You would not call a fire mission off an unconfirmed coordinate; apply the same instinct to AI output, sized to what it will move. Calibrated trust is exactly this judgment.\n\nSuggested visual: a three-tier ladder mapping low/medium/high stakes to none / one check / cross-source + second-tool. Caption: 'Right-size the check.'")

    set_notes(add_example_slide(prs, "Two AIs Agreeing Is Not Verification",
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
        "[IMAGE: Two screens showing matching AI answers next to a single authoritative source document]"),
        "This is the single most common false-confidence trap, so slow down here. The WRONG move: ask Claude, ask ChatGPT, see that they match, and conclude \"verified.\" You verified nothing. Both are pattern-matchers trained on heavily overlapping data from the same internet. When they agree, the most likely reason is that they both absorbed the same common pattern — including the same common mistake. Agreement between two similar systems measures similarity, not truth. It is two witnesses who read the same wrong newspaper. The RIGHT move: go to a genuinely different kind of source — the primary document, the official record, a human subject-matter expert. A system that does not share the same training and the same blind spots is unlikely to make the same mistake in the same place, so when it agrees, that actually means something. And scale the rigor to the consequence — a throwaway brainstorm needs nothing; a number going into a product needs at least one independent check; an input to a real decision needs cross-source plus a second, different tool.")

    set_notes(add_check_on_learning(prs,
        "The model gives you a specific statistic that will go into a brief your commander reads.\n\n"
        "Which of the five techniques do you run before that number leaves your hands — and why that one?\n\n"
        "You want to verify a factual claim a model gave you. Which approach is genuinely independent corroboration?\n\n"
        "A) Ask a second AI chatbot the same question and see if it agrees\n"
        "B) Ask the same model to confirm it is sure\n"
        "C) Check the claim against an authoritative primary source you trust\n"
        "D) Re-read the model's answer more carefully"),
        "ANSWER KEY: C — check the claim against an authoritative primary source you trust. Asking a second chatbot (A) is false corroboration: two pattern-matchers on overlapping training data share the same blind spots. Asking the same model if it's sure (B) just predicts reassurance. Re-reading more carefully (D) adds no independent evidence. For a statistic going into a commander's brief, cite-and-check against the primary source — and given the stakes, add a second-tool/cross-source check.")

    set_notes(add_hands_on(prs, "Verifying AI Output", [
        "Ask the model a factual question whose answer you do NOT already know. Save the answer.",
        "Cite-and-check: ask for the source. Confirm it exists and says what was claimed.",
        "Re-run: ask the identical question in two fresh chats. Did the answer hold or drift?",
        "Second-tool / cross-source: take the claim to a search engine or the primary document. Does it hold?",
        "Write one sentence: which technique would you reach for first for the work you actually do, and why?",
    ], "[IMAGE: Soldier running a checklist — each line a separate verification step against a real claim]"),
        "FACILITATION: this turns \"verify it\" into reps. Insist they pick a question whose answer they do NOT already know (step 1) — verifying a known answer teaches nothing. The cite-and-check (step 2) is the highest-yield habit. Step 5 (which technique fits my real work, and why) is what should transfer to the job. Reinforce: matching another AI is not a check.")

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

    set_notes(add_concept_slide(prs, "Right Tool / Wrong Tool", [
        ("Good at: drafting, rewriting, summarizing, brainstorming, explaining, reformatting, translating, first passes.", False),
        ("Anything where the value is the language and you remain the check on the facts.", True),
        ("Wrong tool — reach for something else:", False),
        ("Precise math or calculation — it predicts plausible numbers, it does not compute reliably.", True),
        ("Real-time or post-cutoff facts — guessing from stale data without verified grounding (Module 3).", True),
        ("Authoritative citation or the official record — go to the source; the model is not the source.", True),
        ("Anything sensitive or above the system's ceiling — a HARD STOP, not a judgment call.", True),
    ], note="The wrong-tool tell: if you are about to trust the model on a number, a date, a citation, or a live fact — stop. Those are exactly the four cases it is built to get confidently wrong."),
        "Think of the model as one tool in a kit, not the whole kit. It predicts the next likely words, which makes it strong wherever the value IS the language: drafting, rewriting, summarizing, brainstorming, explaining, reformatting, translating, first passes — and in all of those, you stay the check on the facts. It is the wrong tool the moment correctness depends on something other than fluent language. Precise math: it predicts plausible-looking numbers; it does not compute reliably. Real-time or post-cutoff facts: it guesses from stale data unless it is grounded against a verified source (Module 3). Authoritative citation or official record: go to the source — the model is not the source. And anything sensitive or above your system's authorization ceiling is a hard stop, not a judgment call (Section 7). The misconception this slide corrects: \"it sounds confident and detailed, so it must be right.\" Confidence is a property of the output style, not of the accuracy. Concrete example: ask it to total a column of figures in a report and it returns a clean, confident sum that is simply wrong. The tell — anytime you are about to trust the model on a number, date, citation, or live fact, stop. That is the wrong tool reaching for the wrong job.")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "Right Tool vs Wrong Tool: A Side-by-Side", [
        ("Same task, two outcomes — does correctness ride on language, or on facts?", False),
        ("RIGHT: 'Rewrite this releasable announcement' → value is the language; you check it.", False),
        ("RIGHT: 'Brainstorm 10 names for an event' → open-ended; no fact to be wrong about.", False),
        ("WRONG: 'What's 17.5% of this budget line?' → predicts a plausible number, doesn't compute.", False),
        ("WRONG: 'Give the current reg number and cite it' → authoritative record; not the source.", False),
        ("WRONG: 'Summarize this personnel file' → sensitive; hard stop before right/wrong applies.", False),
    ], note="If correctness depends on a number, a live fact, or an official record, it is the wrong tool — verify at the source."),
        "This slide turns the abstract rule into a pattern you can recognize fast. Notice the RIGHT cases are always a job where the language itself is the deliverable and you remain the check. The WRONG cases are always a job where the answer must match an external truth — a computed value, a live fact, an official citation — or where the content should never have been pasted at all. The personnel-file row is deliberate: with sensitive content, the right/wrong-tool question never even opens, because the data-handling gate from Section 7 fires first. The misconception corrected: that whether AI is appropriate depends on how hard the task is. It does not. A model can produce a flawless rewrite and a confidently wrong percentage in the same breath, because both are just predicted text — only one of them is checkable against the words on the page. Train your eye on the column the task belongs in before you type. When a task straddles both — \"rewrite this and add the current figures\" — split it: let the model do the language, and you supply and verify the facts.\n\nSuggested visual: two-column table, green 'RIGHT TOOL' left / red 'WRONG TOOL' right, with paired example rows.")

    set_notes(add_concept_slide(prs, "The Decision Checklist — Run It Before You Type", [
        ("1. Open-ended language work, or a precise/authoritative answer? (Precise -> wrong tool.)", False),
        ("2. Does the answer depend on current or post-cutoff information? (Yes -> wrong tool without verified grounding.)", False),
        ("3. Can I verify the output before anyone relies on it? (No -> do not use it for this.)", False),
        ("4. Is the content sensitive, controlled, or above this system's ceiling? (Yes -> hard stop, do not paste.)", False),
        ("Clears all four? AI is a good fit — and you still verify what matters.", False),
    ], note="Question 4 is a hard stop, not a tradeoff. If the content is sensitive or above the ceiling, the answer is no regardless of how useful the tool would be. Full treatment in Section 07.", accent=CYBER_GOLD),
        "Run this before you type, not after you are attached to the answer. Four questions. One: is this open-ended language work, or do I need a precise, authoritative answer? Precise means wrong tool. Two: does the answer depend on current or post-cutoff information? If yes, it is the wrong tool without verified grounding. Three: can I verify the output before anyone relies on it? If no, do not use it — an unverifiable answer you cannot check is worse than no answer, because it looks finished. Four: is the content sensitive, controlled, or above the system's ceiling? If yes, hard stop, do not paste. Clear all four and you have a good fit — and you still verify what matters. The misconception corrected: that judgment about AI is a vibe or a gut call. It is a short, repeatable checklist. Note that Question 4 is not a tradeoff you balance against deadline pressure. It is a gate. Section 7 gives it full treatment.")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "When the Checklist Says Yes — Then What", [
        ("Passing the checklist means 'good fit,' NOT 'skip verification.'", False),
        ("Good fit + verify is the whole posture; a good fit you never check is still a risk.", False),
        ("Verify what MATTERS: any number, date, name, or citation someone will rely on.", False),
        ("You own the output the moment you pass it on — the tool does not share that.", False),
        ("Polished, confident answers are the easiest to wave through — slow down there.", False),
        ("Task changes mid-stream? Re-run the gate (new content pasted = re-classify).", False),
    ], note="'Good fit' is permission to start, not permission to stop checking."),
        "People hear \"good fit\" and relax. This slide closes that gap. Clearing all four questions only tells you the task is appropriate for the tool. It says nothing about whether this particular output is correct. The most dangerous outputs are the ones that pass the checklist cleanly and come back polished — a clean memo with one wrong date, a tidy summary that quietly drops a key condition. Polish lowers your guard; that is exactly when to raise it. The rule of thumb: verify anything a person will act on. If a number, date, name, or citation in the output will drive a decision, check it against the source before it leaves your hands. The misconception corrected: that the checklist is a finish line. It is a starting gate. And it is not a one-time gate — if the task shifts while you work (you paste new content, you ask for live figures), run the four questions again, because the answer can flip. You remain the responsible check on facts from the first prompt to the moment you hand the result on.\n\nSuggested visual: a funnel — four checklist gates at the top narrowing to a single 'VERIFY WHAT MATTERS' step before 'USE'.")

    set_notes(add_check_on_learning(prs,
        "A teammate is about to ask a chatbot to compute exact payroll figures from a personnel roster.\n\n"
        "Two separate things are wrong with that. Name both.\n\n"
        "Which task is the LLM the WRONG tool for?\n\n"
        "A) Drafting a first version of a memo you will edit and verify\n"
        "B) Rewriting a dense paragraph in plainer language\n"
        "C) Producing the exact current price of a commodity and treating it as authoritative\n"
        "D) Brainstorming a list of possible approaches to a problem"),
        "ANSWER KEY: C — producing the exact current price of a commodity and treating it as authoritative is the wrong-tool case (a live/precise fact the model predicts rather than knows). A, B, and D are all good fits: drafting a memo you'll edit, rewriting for clarity, and brainstorming are open-ended language work where you remain the check. The payroll scenario is doubly wrong: precise calculation (wrong tool) AND a personnel roster is sensitive content (hard stop, Section 07).")

    set_notes(add_hands_on(prs, "When to Use AI", [
        "List the last five things you used (or wanted to use) an AI tool for.",
        "Run each one through the four-question checklist.",
        "Flag any that were actually wrong-tool cases — precise math, live facts, authoritative citation, sensitive content.",
        "For one flagged case, write down what the RIGHT tool would have been.",
    ], "[IMAGE: Decision flowchart pinned to a planning board — four checks before committing to a course of action]"),
        "FACILITATION: this audits their actual habits, not a hypothetical. Most learners will find at least one wrong-tool case among their last five uses — usually precise math, a live fact, an authoritative citation, or sensitive content. The value is step 4: naming what the RIGHT tool would have been builds the redirect reflex, so the checklist runs automatically next time.")

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

    set_notes(add_concept_slide(prs, "Authorization Is a Property of the System", [
        ("Authorization is a property of the system — not the impressiveness of the tool.", False),
        ("A highly capable model on an unauthorized system does not become authorized because it is impressive.", False),
        ("The boundary is set by policy, not capability.", False),
        ("What must never go into an unauthorized system:", False),
        ("PII: names combined with identifiers, SSNs, DOBs, home addresses", True),
        ("Sensitive, controlled, or classified material of any kind", True),
        ("Anything above the system's authorization ceiling", True),
    ], note="Most AI delivery is cloud-based: your input leaves your machine. This is the security spine — what flows IN. What you do with the output, and whether a use is ethical/lawful, is Module 9."),
        "Authorization is a property of the SYSTEM, not the tool's impressiveness. A highly capable model running on an unauthorized system is still unauthorized. Read that again: capability does not grant permission. The boundary is policy, not how good the output looks. Why does this matter so much here? Because most AI is delivered from the cloud. When you paste, your input leaves your machine and travels to the provider's servers to be processed. Depending on the provider, tier, and settings, that input may be retained, logged, or even used to train future models (provider/tier/settings-dependent — verify, and never state one provider's policy as fact). You cannot pull it back. This is the security spine of the module: it is about what flows IN. What you do with the output, and the ethics of that, is Module 9. So the bright line is simple. NEVER into an unauthorized system: PII (names paired with identifiers, SSNs, dates of birth, home addresses); sensitive, controlled, or classified material of any kind; and anything above the system's authorization ceiling. The misconception corrected: \"this model is so advanced it must be safe to use for anything.\" Advanced is not authorized. The control point is the system, and only an authorizing authority sets it.")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "What Actually Happens to Your Input", [
        ("Most consumer AI is cloud-based: your input does not stay on your device.", False),
        ("You paste → the text travels over the network to the provider's servers.", False),
        ("It is processed remotely to predict a response.", False),
        ("Depending on provider, tier, and settings, it may be logged, retained, or used to train.", False),
        ("You cannot recall it; 'delete' on your side does not guarantee deletion on theirs.", False),
        ("This round-trip is WHY the control point is the system, not the model's skill.", False),
    ], note="Once it leaves your machine you have lost positive control of it — that is the whole reason the bright line exists. Retention/training behavior is provider/tier/settings-dependent — verify."),
        "This explains the mechanism behind the rule so it sticks. When you use a typical cloud AI tool, pasting is not a local action — your words are transmitted off your device to servers you do not control. There they are processed to generate the reply. What happens next varies. Many providers retain conversation data, and several consumer tiers use inputs to train future models by default unless the user opts out, with retention windows ranging from weeks to years depending on the provider and settings. Do not state any one provider's policy as fact — it changes, and it differs by plan and account setting. The doctrinal point is provider-independent: once your input leaves the machine, you have lost positive control. There is no reliable undo, and deleting your local copy does not reach into their systems. The misconception corrected: \"it's just a chat box on my screen, it stays with me.\" It does not — it is a round-trip to someone else's infrastructure. That is precisely why authorization attaches to the system, not the model: the system determines where your input goes and what is done with it. Capability cannot protect data it has already shipped.\n\nSuggested visual: flow diagram — your device → network → provider servers (process / possible retain / possible train) → response back; a one-way 'no undo' arrow on the upload leg.")

    set_notes(add_concept_slide(prs, "The Default Posture and the Classify-Before-You-Paste Habit", [
        ("Default posture: when in doubt, do not paste. Ask someone who can authorize it first.", False),
        ("Classify before you paste — take two seconds before pasting anything:", False),
        ("What is this content?", True),
        ("Is this system authorized for it?", True),
        ("Build that pause until it is automatic.", True),
        ("The 'paraphrase and summarize it first' loophole does not exist.", False),
        ("This bright line does not expire — not at the end of this course, not under time pressure.", False),
    ], note="One careless paste in an unauthorized system is the kind of mistake with real and lasting consequences. Default to no until you hear yes from someone who can authorize it. Do not soften this.", accent=CYBER_GOLD),
        "The default posture is no. When in doubt, do not paste — ask someone who can authorize first. Build one habit until it is automatic: classify before you paste. It takes two seconds and two questions. What is this content? Is this system authorized for it? If you cannot answer both with confidence, you have your answer — stop. Two traps to name out loud. First, the loophole that does not exist: \"I'll just paraphrase or summarize it first, so it's not really the sensitive thing.\" It is. Summarizing controlled content does not declassify it; the protected information still flows into an unauthorized system. Second, the expiration myth: the bright line does not expire — not when the course ends, not when you are slammed and the deadline is now. Time pressure is exactly when the careless paste happens. Concrete example: a busy shift, an unauthorized public chatbot, and a real personnel record pasted in to \"speed up a summary\" — that input may now be retained outside any authorized boundary, with no undo. One careless paste has real, lasting consequences. Default to no until you hear yes.")

    # DEEP DIVE (new)
    set_notes(add_concept_slide(prs, "The 2-Second Pause, Worked", [
        ("Before any paste, run two questions — it fits in the time it takes to hit paste.", False),
        ("Q1 — What is this content? (releasable / PII / controlled / sensitive / unsure)", False),
        ("Q2 — Is THIS system authorized for THAT content? (yes / no / unsure)", False),
        ("'Unsure' on either routes to STOP and ask — unsure is not yes.", False),
        ("Releasable text + authorized system = proceed (still verify facts).", False),
        ("A real record, or anything 'unsure' = do not paste; paraphrasing doesn't change it.", False),
    ], note="Two seconds now beats a consequence that does not expire — when in doubt, do not paste."),
        "This makes the habit concrete enough to actually perform under pressure. The pause is two questions and it fits in the time it takes to move your hand to the paste shortcut. First, classify the content: say what it is. If you cannot name it cleanly, that itself is a signal. Second, ask whether this specific system is authorized for that specific content — not whether the tool is good, whether it is permitted. Three lanes come out. Yes and yes: proceed, and remember you still owe verification of any facts. Any no: stop. Any unsure, on either question: stop and ask someone who can authorize — unsure routes to no, never to yes. Walk the two examples. A plainly releasable announcement into an approved system — clear to go. An actual personnel record, or content you cannot confidently classify — do not paste, and note that summarizing or rewording it first does not create an exception; the protected information still flows in. The misconception corrected: that the pause is too slow to bother with when you are busy. The pause is two seconds; the careless paste has consequences that do not expire. Build the pause until it is automatic. Default to no until you hear yes.\n\nSuggested visual: a simple decision flow — Q1 classify → Q2 authorized? → three lanes: YES/YES proceed, any NO stop, any UNSURE stop-and-ask.")

    set_notes(add_check_on_learning(prs,
        "You are under a deadline and want to paste a document into your AI tool to summarize it quickly. "
        "You are not sure whether the system is authorized for that content.\n\n"
        "What do you do?\n\n"
        "You have a borderline-sensitive document and an unauthorized but highly capable AI tool that would save hours. "
        "What is the correct call?\n\n"
        "A) Paste it — the efficiency gain justifies a judgment call\n"
        "B) Summarize the key points in your head first, then paste the summary\n"
        "C) Do not paste. Authorization does not change based on capability or time pressure. Ask first.\n"
        "D) Paste it, but delete the conversation immediately after"),
        "ANSWER KEY: C — do not paste; authorization does not change based on capability or time pressure, so ask first. A rationalizes a judgment call that isn't yours to make. B is the paraphrase/summarize loophole, which does not exist — protected information still flows into an unauthorized system. D (\"delete it after\") does not help: once it leaves your machine you've lost positive control. Default to no until an authorizing authority says yes.")

    set_notes(add_hands_on(prs, "Data Handling: What Never to Paste", [
        "No prompting today. Think about the last three things you pasted into an AI tool.",
        "For each one: was the system authorized for that type of content?",
        "Identify one category of content you work with regularly that you will never paste into an unauthorized tool.",
        "Write that category down. It is your personal bright line.",
        "Keep it. It does not expire.",
    ], "[IMAGE: Soldier reviewing a checklist before touching a terminal — a deliberate pause before action]"),
        "FACILITATION: deliberately no prompting today — this is a discipline drill, not a tool drill. The output is a written personal bright line: one category of content the learner will never paste into an unauthorized tool. Have them keep it somewhere they will see it. Reinforce the two-second classify-before-you-paste pause until it is automatic. The bright line does not expire.")

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
    set_notes(add_summary_table(prs,
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
        col_x, col_w),
        "RECAP. The seven rows are the whole module: prediction, finite context, statelessness, predictable failure, verification, tool-fit, and data handling. If a learner can give the \"core idea\" and \"why it matters\" for each row from memory, they are ready. Two rows are load-bearing above the rest: \"How LLMs Fail\" (it justifies verification) and \"Data Handling\" (a hard line with real consequences).")

    # =========================================================================
    # READINESS CHECK
    # =========================================================================
    set_notes(add_readiness_check(prs, [
        "I can state in one sentence what an LLM does — using only the verb 'predicts'",
        "I can explain tokens and the context window, and why long chats degrade",
        "I can explain why the model is stateless and what conversation 'memory' really is",
        "I can name the five failure modes and have produced a hallucination with my own hands",
        "I can run the five verification techniques as drills, not as a vibe",
        "I can run the four-question 'when to use AI' checklist before I type",
        "I know what must never go into an unauthorized system and have written my personal bright line",
    ]),
        "SELF-ASSESSMENT. These map one-to-one to the learning objectives. The honest bar is \"can do unaided,\" not \"have seen.\" Two are performance items, not knowledge items: having actually produced a hallucination with your own hands, and having written your personal data-handling bright line. If any box is unchecked, send the learner back to that section's hands-on before advancing.")

    # =========================================================================
    # END SLIDE
    # =========================================================================
    set_notes(add_end_slide(prs, "Module 1:\nKnow Your Weapon", [
        "Produce a hallucination with your own hands before moving on — if you have not yet, do it now.",
        "Run all five verification techniques against one planted false claim in a single session.",
        "Run your last five AI uses through the four-question 'when to use it' checklist.",
        "Write down your personal bright line for content you handle — and keep it. It does not expire.",
    ]),
        "CLOSEOUT. The four next steps are deliberately hands-on, not reading: produce a hallucination, run all five verification techniques on one planted false claim, audit your last five AI uses against the checklist, and write your bright line. These convert the module from knowledge into reflexes. This is a prerequisite — the rest of the course assumes these habits are already in place.")

    save_deck(prs, __file__, "01-ai-foundations.pptx")


if __name__ == "__main__":
    build()
