"""
ACC Module 3 — Feeding the Machine: Grounding & Multimodality
Slide deck builder. Uses the shared Army Cyber Dark theme.

Mirrors docs/modules/03-grounding-multimodality.md section-for-section.
Run by the orchestrator only — do not run python here.
"""

from acc_theme import *


def build():
    prs = new_deck()

    # --- TITLE ---
    add_title_slide(prs,
        "Module 3:\nFeeding the Machine",
        "PREREQUISITE MODULE  |  SELF-PACED",
        "[IMAGE: Soldier handing real source documents through a slot to an isolated analyst — feeding the brain in a jar]")

    # --- OVERVIEW ---
    add_overview_slide(prs,
        "A bare LLM is a brain in a jar with a knowledge cutoff and no live access. Grounding "
        "(web search, file upload, connectors) feeds it real, current source material — the "
        "practical fix for cutoff and hallucination. Multimodality opens new input channels, "
        "each with its own failure mode.",
        "Self-paced (3 sections)",
        [
            "Explain grounding as feeding real source material into the model at request time",
            "Name three grounding paths: web search, file upload, connectors",
            "Tell a grounded answer from a generated one — confirm grounding fired, trace claims",
            "Treat a citation as a starting point for verification, not as proof",
            "Name the input modes: images, screenshots, PDFs, charts, voice",
            "Name the characteristic failure mode of each input mode",
            "Apply the Module 1 data-handling rule to images, PDFs, and voice — not just text",
        ])

    # =========================================================================
    # SECTION 01 — Grounding: Punching a Hole in the Jar
    # =========================================================================
    add_section_header(prs, "01", "Grounding:\nPunching a Hole\nin the Jar",
        "The engine is still a brain in a jar — but grounding feeds it real, current, specific "
        "source material through a slot. That is the fix for cutoff and hallucination.",
        "[IMAGE: A sealed jar with a delivery slot — real documents being passed in from outside]")

    add_concept_slide(prs, "What Grounding Actually Does", [
        ("Module 1 baseline (still true of the ENGINE): no body, no memory, no live access, a knowledge cutoff.", False),
        ("Grounding means giving the model real source material to work from, at request time.", False),
        ("Instead of predicting from training alone, it answers FROM actual text put in its context.", False),
        ("The prediction engine is unchanged — what changed is the material you hand it for this request.", False),
        ("This corrects and extends the mental model: the jar is still a jar; grounding hands material through a slot.", False),
    ], note="Do not let students conclude Module 1 was wrong. The engine is still a brain in a jar. Grounding is an external tool layer feeding it — 'extend the model,' not 'replace it.'")

    add_concept_slide(prs, "Three Grounding Paths — and Why They Fix the Two Big Problems", [
        ("Web search — live search, current pages, answers from the results.", False),
        ("The direct fix for the knowledge cutoff: no longer limited to training data.", True),
        ("File / document upload — attach a PDF, spreadsheet, or text file; the model reads its actual contents.", False),
        ("Connectors — wired into an external system (doc store, wiki, database, drive) to retrieve records on demand.", False),
        ("Connecting tools in depth, and the protocols that standardize it, is Module 12.", True),
        ("Cutoff fix: search/connectors bring in post-training info. Hallucination fix: claims trace to a real source.", False),
        ("Grounding does not guarantee correctness — it makes output TRACEABLE, which makes verification possible.", False),
    ], note="VERIFY BEFORE TEACHING: which tools have web search, how upload works, what connectors exist, and how each is enabled change frequently. Treat every feature claim as a snapshot; confirm the actual tool before relying on it.")

    add_check_on_learning(prs,
        "Module 1 told you the model is a brain in a jar with no live access. "
        "You just watched it answer a question about a recent event.\n\n"
        "Did the engine change — or did something feed the jar? What is the difference, and why does it matter for trust?\n\n"
        "What does 'grounding' actually do to an LLM's behavior?\n\n"
        "A) It retrains the model on new data in real time\n"
        "B) It removes the knowledge cutoff permanently\n"
        "C) It feeds real source material into the model's context at request time so it answers from that, not just training\n"
        "D) It makes the model stop hallucinating entirely")

    add_hands_on(prs, "Grounding", [
        "Ask your tool a question about something that clearly happened AFTER its training cutoff. Note: refuse, guess, or search?",
        "If it has web search, require it to search and ask the same question again. Compare the two answers.",
        "Upload a short document and ask a question whose answer is ONLY in that document. Confirm the answer came from your file.",
        "Ask: 'Which parts of that answer came from the document, and which from your own knowledge?' Can it separate them?",
    ], "[IMAGE: Analyst comparing a from-memory answer against one drawn from a freshly retrieved source]")

    add_section_summary(prs, "Grounding: Punching a Hole in the Jar", [
        "Grounding feeds real source material into the model's context at request time.",
        "Three paths: web search, file upload, connectors.",
        "It is the practical fix for knowledge cutoff and hallucination — output becomes traceable.",
        "The engine is unchanged; grounding is an external tool layer feeding the jar.",
    ])

    # =========================================================================
    # SECTION 02 — Grounded vs. Generated
    # =========================================================================
    add_section_header(prs, "02", "Grounded vs.\nGenerated:\nTell Them Apart",
        "A grounded answer and a generated answer look identical on screen — confident either way. "
        "Confirm grounding fired and trace the claim before you trust it.",
        "[IMAGE: Two identical-looking reports — one sourced and footnoted, one written from memory]")

    add_concept_slide(prs, "Confirm It Fired, Then Trace the Claim", [
        ("Capability is not use — a tool WITH web search may answer a question straight from training, no search.", False),
        ("Look for the signal that grounding happened: a search step, cited sources, 'based on the file', retrieved snippets.", False),
        ("No signal? Assume it answered from training until you check.", True),
        ("Trace claims to sources — a grounded answer should let you ask 'where did this exact claim come from?'", False),
        ("If a claim cannot be traced to the provided source, treat it as generated.", True),
        ("The dangerous case — the MIXED answer: part faithfully from your source, part plausible completion bolted on.", False),
        ("Tone is uniform, so the seam is invisible. Ask directly: 'which parts came from the source?'", True),
    ], note="This is the Module 1 reflex applied. Grounding does not let you stop verifying — it gives you something checkable to verify against. The five verification techniques are exactly the drills you run here.")

    add_example_slide(prs, "A Citation Is Not Proof",
        "Scenario: The tool cites a source — now what?",
        ["WHAT GROUNDING GIVES YOU:",
         "  Trace-ability. You can follow a claim back to a source and check it.",
         "",
         "WHAT GROUNDING DOES NOT GIVE YOU:",
         "  Certainty. The tool can still:",
         "    - retrieve the WRONG document",
         "    - quote a real source INACCURATELY",
         "    - cite a page that does NOT support the claim",
         "",
         "THE MOVE:",
         "  Make it cite, THEN open the citation and confirm it says what the model says it says.",
         "  A cited source the model invented or misread is still a hallucination.",
         "  Trace-ability lowers risk; it does not remove the operator. You still own the output."],
        "[IMAGE: Analyst opening a cited reference to confirm it actually supports the claim above it]")

    add_check_on_learning(prs,
        "Your tool gives you a confident, well-written answer with no visible sources, "
        "even though it has web search available.\n\n"
        "What is your safest assumption about where that answer came from — and what do you do next?\n\n"
        "A tool that has web search gives you a confident answer with no citations and no visible search step. "
        "What should you assume?\n\n"
        "A) It must have searched, because it has the capability\n"
        "B) Assume it answered from training data until you confirm grounding actually fired\n"
        "C) The answer is verified because it sounds confident\n"
        "D) Citations are unnecessary when a tool has search enabled")

    add_hands_on(prs, "Grounded vs. Generated", [
        "Ask a grounded question and look for the signal that grounding fired (search step, citations, file reference). Is it there?",
        "Pick one specific claim and ask the tool: 'What is your source for that exact claim?'",
        "Open that source and confirm it actually supports the claim. Did it?",
        "Find one claim you CANNOT trace to a provided source. Treat it as generated — would you have caught it without checking?",
    ], "[IMAGE: Soldier running a checklist over an answer — marking each claim sourced, traced, or unverified]")

    add_section_summary(prs, "Grounded vs. Generated", [
        "Confirm grounding actually fired before trusting a 'grounded' answer — capability is not use.",
        "Trace a grounded claim to its source and verify the source supports it.",
        "The mixed answer (part grounded, part generated) is the dangerous case — the seam is invisible.",
        "A citation is a starting point for verification, not proof. You still own the output.",
    ])

    # =========================================================================
    # SECTION 03 — Multimodality
    # =========================================================================
    add_section_header(prs, "03", "Multimodality:\nMore Ways In,\nMore Ways to Misread",
        "Images, screenshots, PDFs, charts, and voice — not just typed text. Powerful for real "
        "work, and each input mode carries its own failure mode.",
        "[IMAGE: A workstation taking in a photo, a scanned PDF, a chart, and a voice waveform at once]")

    add_concept_slide(prs, "The Input Modes You Will Actually Use", [
        ("Images and screenshots — photos of documents, whiteboards, equipment; screenshots of errors or interfaces.", False),
        ("PDFs and documents — multi-page files read directly, including scanned ones.", False),
        ("A PDF is both a grounding source and a visual input — the categories overlap.", True),
        ("Charts and tables in images — graphs, data tables, diagrams embedded in a picture, not clean data.", False),
        ("Voice input — you speak; the tool transcribes to text, then the model answers from the transcript.", False),
        ("You will not always have clean text to paste — these channels let the model take what you actually have.", False),
    ], note="Every new input channel is a new place for the model to go confidently wrong — and the failures are easy to miss because you assume 'it can see the image, so it read it correctly.' It often did not.")

    add_concept_slide(prs, "Each Mode's Own Failure Mode", [
        ("Blurry / low-quality images — the model fills unreadable text with plausible guesses; a smudged digit becomes a confident wrong number.", False),
        ("Tables and charts — misreads which value is in which cell, swaps rows and columns, misjudges a value off an axis.", False),
        ("Dense or handwritten docs — transcription errors and skipped lines; may silently drop content it could not parse.", False),
        ("Voice — mishears words, especially names, jargon, callsigns, and numbers; then answers a subtly different question.", False),
        ("Across all modes — the model rarely says 'I couldn't read this.' It answers confidently over a partial read.", False),
    ], note="Misreads inherit the confident tone — the Module 1 confident-wrong failure mode riding in on a new channel. Verify the READ before you trust the REASONING. Good reasoning over a misread table is still wrong.", accent=CYBER_GOLD)

    add_concept_slide(prs, "OPSEC Crosses Modes", [
        ("A screenshot, a photo of a document, or a scanned PDF can carry exactly the sensitive content you would never paste as text.", False),
        ("Names, grids, unit designations, markings, faces.", True),
        ("Uploading an image is a disclosure decision — identical to pasting text.", False),
        ("Everything in Module 1's data-handling rule applies to every image, PDF, and voice clip.", False),
        ("The bright line does not change because the input is a picture instead of words.", False),
    ], note="Separate two questions when the model extracts data: did it READ the input correctly, and did it REASON correctly from what it read? Check the read first.", accent=CYBER_GOLD)

    add_check_on_learning(prs,
        "You upload a screenshot of a data table and the model gives you a clean analysis.\n\n"
        "Two different things could be wrong: how it READ the table, and how it REASONED from it. "
        "Which do you check first, and why?\n\n"
        "You give the model a photo of a slightly blurry data table and it returns specific numbers with full confidence. "
        "What is the right posture?\n\n"
        "A) Trust the numbers — the model can see the image clearly\n"
        "B) Assume it flagged anything it could not read\n"
        "C) Verify the extracted values against the original; misreads come out with the same confident tone\n"
        "D) Re-upload the image until the answer changes")

    add_hands_on(prs, "Multimodality", [
        "Screenshot a small fabricated, non-sensitive table and ask the model to read specific cells back. Check every value.",
        "Give it a chart image and ask for a specific value off the graph. Right, or confidently close-but-wrong?",
        "If your tool supports voice, speak a sentence with a name, a callsign, and a number. Check the transcription first.",
        "Upload a multi-page PDF and ask about content on a later page. Confirm it actually read that far.",
        "For each test: did the model flag any uncertainty about what it read? (It probably did not.)",
    ], "[IMAGE: Soldier cross-checking a model's extracted table values against the original printed document]")

    add_section_summary(prs, "Multimodality: More Ways In, More Ways to Misread", [
        "Input modes: images/screenshots, PDFs, charts/tables, voice.",
        "Each has a characteristic failure: blurry-text guesses, swapped cells, dropped lines, misheard names/numbers.",
        "Misreads inherit the confident tone — check the model's read separately from its reasoning.",
        "OPSEC crosses modes: an image, PDF, or voice clip is a disclosure decision, same as pasting text.",
    ])

    # =========================================================================
    # MODULE SUMMARY TABLE
    # =========================================================================
    col_x = [L, Inches(3.5), Inches(8.1)]
    col_w = [Inches(2.9), Inches(4.4), Inches(5.0)]
    add_summary_table(prs,
        "MODULE SUMMARY",
        "Feeding the Machine — Grounding & Multimodality",
        [
            ("Grounding",          "Feed real source material at request time",  "The practical fix for knowledge cutoff and hallucination."),
            ("Three Paths",        "Web search, file upload, connectors",         "Three ways to hand the jar real, current, specific info."),
            ("Grounded vs. Gen",   "Confirm it fired; trace claims to sources",   "Capability is not use. The mixed answer is the dangerous case."),
            ("Citation != Proof",  "Trace-ability lowers risk, not the operator", "Run the Module 1 verification drills on the cited source."),
            ("Multimodality",      "Images, screenshots, PDFs, charts, voice",    "More ways in for real work — and more ways to misread."),
            ("Per-Mode Failures",  "Blurry text, swapped cells, misheard input",  "Misreads inherit the confident tone. Verify the read first."),
            ("OPSEC Crosses Modes","An image/PDF/voice clip is a disclosure",     "The Module 1 data-handling rule applies to every channel."),
        ],
        ["CONCEPT", "CORE IDEA", "WHY IT MATTERS"],
        col_x, col_w)

    # =========================================================================
    # READINESS CHECK
    # =========================================================================
    add_readiness_check(prs, [
        "I can explain grounding as feeding real source material into the model at request time",
        "I can name three grounding paths: web search, file upload, connectors",
        "I confirm grounding actually fired before trusting a 'grounded' answer",
        "I can trace a grounded claim to its source and treat a citation as a starting point, not proof",
        "I can name the input modes and the characteristic failure mode of each",
        "I check the model's read of an input separately from its reasoning",
        "I apply the Module 1 data-handling rule to images, PDFs, and voice — not just typed text",
    ])

    # =========================================================================
    # END SLIDE
    # =========================================================================
    add_end_slide(prs, "Module 3:\nFeeding the Machine", [
        "On your next real task, deliberately ground the model (search or upload) and trace one claim to its source.",
        "Run a 'verify the read' check on an image or chart before trusting any number it extracts.",
        "Carry grounding forward: in Module 7 it is a tool call; in Module 12 it gets a name — retrieval.",
        "Apply your Module 1 bright line to images, PDFs, and voice, not just text. The disclosure decision is the same.",
    ])

    save_deck(prs, __file__, "03-grounding.pptx")


if __name__ == "__main__":
    build()
