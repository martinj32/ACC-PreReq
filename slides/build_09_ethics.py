"""
ACC Module 09 — Rules of Engagement: Ethics & Responsible AI Use
================================================================
Builds 09-ethics.pptx on the shared Army Cyber Dark theme.

Deck flow mirrors docs/modules/09-ethics.md:
    Title -> Overview
    -> for each of 8 sections:
         Section Header -> Concept(s) -> Example (where the md has one)
         -> Check on Learning -> Hands-On -> Section Summary
    -> Module Summary Table -> Readiness Check -> End

DO NOT run this directly during the build pass other than via the orchestrator;
python is blocked for the authoring agent. The orchestrator runs build().
"""

from acc_theme import *


def build():
    prs = new_deck()

    # ------------------------------------------------------------------ TITLE
    add_title_slide(
        prs,
        "Module 09:\nRules of Engagement",
        "PREREQUISITE MODULE  |  SELF-PACED",
        "[IMAGE: An officer signing a release line on a SITREP; an AI-drafted "
        "paragraph on the screen behind, one claim circled in red — the signer "
        "owns it]",
    )

    # --------------------------------------------------------------- OVERVIEW
    add_overview_slide(
        prs,
        "Ethics is what you do with AI OUTPUT and whether the use is right, "
        "lawful, and accountable — distinct from OPSEC/data-handling, which "
        "governs what flows IN.",
        "Self-paced  |  8 sections  |  ~2-3 hours",
        [
            "Sign for every AI-assisted product — capability does not transfer accountability",
            "Treat a hallucination in a consequential product as authored harm",
            "Judge first, consult second — defeat automation bias",
            "Spot stereotype-matching and refuse to launder bias into products",
            "Disclose material AI use; know DoDI 5400.19 governs public-facing content",
            "Stay inside the lawful-use boundary: capability is not authorization",
            "Respect privacy beyond OPSEC: 'collectible' is not 'appropriate'",
            "Map it all to the five DoD AI Ethical Principles",
        ],
    )

    # Module-wide framing + verify-currency flag (concept slide w/ note)
    add_concept_slide(
        prs,
        "Ethics Is Not OPSEC",
        [
            ("Module 1 = DATA HANDLING: what flows IN — what you may paste. That is security.", False),
            ("This module = the OUTPUT side: what you do with what comes out, and whether the use is right.", False),
            ("You can be perfectly OPSEC-compliant and still commit an ethical failure:", False),
            ("sign for a fabricated claim", True),
            ("hide that AI wrote your product", True),
            ("use generation to deceive", True),
            ("Clean inputs do not make an output honest. This module owns the output side.", False),
        ],
        note="VERIFY CURRENCY: This module cites DoD AI policy (5 Principles, CDAO RAI, "
             "DoDI 5400.19, NIST AI RMF) — all in active revision. Not legal advice. "
             "Verify the current version before delivery; ask chain/legal when unsure.",
        accent=CYBER_GOLD,
    )

    # ===================================================== SECTION 1
    add_section_header(
        prs, "01", "Accountability\n& Authorship",
        "You sign for it — capability does not transfer accountability.",
        "[IMAGE: A signature block on an analytic product; the pen is the operator's, "
        "not the machine's]",
    )
    add_concept_slide(
        prs,
        "You Sign for It",
        [
            ("Authorship attaches to the SIGNER, not the drafter.", False),
            ("Forward, brief, or sign a product = you ASSERT every claim in it as your own.", True),
            ("There is no 'the model said so' defense.", False),
            ("That sentence doesn't reduce responsibility — it admits you signed unverified.", True),
            ("Vouching is PER-CLAIM, not per-document.", False),
            ("Every name, date, figure, citation, causal link — verified or you own being wrong.", True),
            ("A product is only as signed-for as its least-checked sentence.", True),
        ],
        note="Fluent is not verified. Polish is exactly what makes an unverified claim "
             "slide through review. This is the supervisor's 'OWN the outcome' duty, made literal.",
    )
    add_check_on_learning(
        prs,
        "An AI-drafted assessment you signed and forwarded contained a fabricated "
        "statistic that drove a bad decision. Who is accountable — and what "
        "specifically did you fail to do?",
    )
    add_hands_on(
        prs,
        "Sign for It — Correctly",
        [
            "Ask a model to draft a 4-6 sentence analytic paragraph on a NON-sensitive topic you know well.",
            "Find every checkable claim: each name, date, number, causal 'because'.",
            "Verify each claim against a trusted source, or mark it 'cannot verify'.",
            "Find the planted false claim that reads as plausible — if you'd signed first, you'd have asserted it.",
            "Only after every claim is verified or struck, INITIAL the paragraph: 'I vouch for every claim here.'",
        ],
        img_label="[IMAGE: A paragraph with each claim check-marked, then initialed at the bottom]",
    )
    add_section_summary(
        prs,
        "Accountability & Authorship",
        [
            "Capability does not transfer accountability — you author what you sign.",
            "'The model said so' is not a defense; it is an admission you didn't verify.",
            "Vouching is per-claim: every checkable fact, verified or owned.",
            "A product is only as signed-for as its least-checked sentence.",
        ],
    )

    # ===================================================== SECTION 2
    add_section_header(
        prs, "02", "Hallucination as\nan Ethical Failure",
        "A fabricated claim you release is authored harm — verify to the stakes.",
        "[IMAGE: A confident-looking assessment with a fabricated citation "
        "highlighted, riding up the chain]",
    )
    add_concept_slide(
        prs,
        "Authored Harm, Scaled to Stakes",
        [
            ("Same mechanism, different stakes: the model has no truth-check (Module 1).", False),
            ("The technical event is identical; the ethical weight is not.", True),
            ("Harm attaches at the point of RELEASE — when you adopt the claim as your own.", False),
            ("Your verification duty scales with consequence:", False),
            ("Low (rough draft): sanity-check obvious errors", True),
            ("Medium (internal summary): verify key claims, citations, figures", True),
            ("High (decision is made on it): verify EVERY checkable claim, independently", True),
        ],
        note="The stakes set the standard — not your schedule. A deadline raises the "
             "temptation to skip the check; it never lowers the bar.",
        accent=CYBER_GOLD,
    )
    add_example_slide(
        prs,
        "Same Fabrication, Different Worlds",
        "A model invents: 'per the 2024 regional stability report, incidents rose 40%' — no such report exists",
        [
            "IN A STUDY NOTE TO YOURSELF:",
            "  You catch it later. No harm done.",
            "",
            "IN AN ASSESSMENT YOUR COMMANDER BRIEFS UPWARD:",
            "  A 40% figure with a citation is exactly what decisions get built on.",
            "  By the time anyone finds the report doesn't exist —",
            "  the decision is already made, on YOUR authored claim.",
            "",
            "Same token-generation event.",
            "One is a curiosity. One is a failure you signed for.",
        ],
        img_label="[IMAGE: Split screen — a sticky note vs. a briefing slide on a command screen]",
    )
    add_check_on_learning(
        prs,
        "You know the model can fabricate. You're on a deadline drafting a product "
        "a commander will act on. What does KNOWING the mechanism obligate you to "
        "do that you wouldn't be obligated to if you didn't know?",
    )
    add_hands_on(
        prs,
        "Stakes-Scaled Verification",
        [
            "Take a model output with a specific factual claim + citation (reuse a Module 1 hallucination, or generate fresh on a non-sensitive topic).",
            "Write: 'If low-stakes, the consequence is ___. If high-stakes, the consequence is ___.'",
            "For the high-stakes version, write the verification you would owe before signing.",
            "Now actually do that verification on the claim. Did it survive?",
        ],
        img_label="[IMAGE: A dial labeled STAKES turning up, with the verification bar rising alongside it]",
    )
    add_section_summary(
        prs,
        "Hallucination as an Ethical Failure",
        [
            "A technical fact (hallucination) becomes an ethical event (authored harm).",
            "Harm attaches at release — when you adopt and forward the claim.",
            "Verification duty scales with stakes, not with how busy you are.",
            "Knowing the mechanism creates the duty — you can't claim you didn't know.",
        ],
    )

    # ===================================================== SECTION 3
    add_section_header(
        prs, "03", "Over-Reliance &\nAutomation Bias",
        "Judge first, consult second — or the skill quietly erodes.",
        "[IMAGE: An analyst writing an assessment by hand, the screen turned face-down "
        "until they finish]",
    )
    add_concept_slide(
        prs,
        "Judge First, Consult Second",
        [
            ("Automation bias: humans over-trust automated output — documented, not a personal weakness.", False),
            ("It's psychology, so you counter it with a PROCEDURE, not willpower.", True),
            ("Anchoring: whatever you see first sets your reference point.", False),
            ("See the model's take first and you're editing it, not assessing the problem.", True),
            ("Deskilling: a skill you stop exercising decays — you become a relay, not an analyst.", False),
            ("Countermeasure: form your own assessment and WRITE IT DOWN before you see the model's.", False),
            ("Where your read and the model's disagree is the most valuable thing on the page.", True),
        ],
        note="Speed is the trap. The faster the answer arrives, the more tempting it is "
             "to skip your own. Accept a slower start to get an owned result.",
    )
    add_check_on_learning(
        prs,
        "You've started reaching for the model BEFORE forming your own view on every "
        "problem. What skill is quietly eroding — and what is the one-step fix?",
    )
    add_hands_on(
        prs,
        "Judge-First, Consult-Second (do in order — no peeking)",
        [
            "Pick an analytic question on a non-sensitive topic you know something about.",
            "BEFORE touching any AI: write your own assessment (3-5 sentences). Commit to it.",
            "NOW ask the model the same question.",
            "Compare — where do you agree, where do you disagree?",
            "For every disagreement, decide with reasoning who is right — verify, do NOT default to the machine.",
            "Write one sentence: did the model sharpen your assessment, or nearly replace it?",
        ],
        img_label="[IMAGE: Two columns — 'MY ASSESSMENT' filled in first, 'MODEL' revealed second]",
    )
    add_section_summary(
        prs,
        "Over-Reliance, Automation Bias & Deskilling",
        [
            "Automation bias is documented human psychology — counter it with procedure.",
            "Anchoring: see the model first and your independent judgment never forms.",
            "Deskilling: stop exercising the skill and it decays — you become a relay.",
            "Judge first, write it down, THEN consult — disagreements are the gold.",
        ],
    )

    # ===================================================== SECTION 4
    add_section_header(
        prs, "04", "Bias & Fairness in\nAI-Assisted Analysis",
        "Spot stereotype-matching vs. evidence — and refuse to launder it.",
        "[IMAGE: A model output where stereotype-based claims are struck through, "
        "evidence-based claims kept]",
    )
    add_concept_slide(
        prs,
        "Don't Launder Bias Into the Product",
        [
            ("Trained, not programmed (Module 1): the model inherited human bias from its training text.", False),
            ("Not malicious — a mirror of data that was never neutral. No rulebook to audit.", True),
            ("Stereotype-matching vs. evidence-based output — same confident voice:", False),
            ("Stereotype-matching: fills a gap with the common assumption, dressed as analysis", True),
            ("Evidence-based: anchored to the specific facts YOU provided", True),
            ("The laundering risk: adopt a biased output and a stereotype wears your signature.", False),
            ("Module 1 = SPOT it (literacy). Module 9 = the DUTY not to pass it on.", True),
        ],
        note="Bias isn't only demographic. Any confident conclusion the specific evidence "
             "doesn't support — which actor is 'probably' responsible — check it against the facts.",
        accent=CYBER_GOLD,
    )
    add_example_slide(
        prs,
        "Spotting Stereotype-Matching",
        "A model profiles a group's likely behavior from a thin description — confident, detailed",
        [
            "THE TEST:",
            "  Strip out the group label.",
            "  Ask what SPECIFIC evidence in your input supports each claim.",
            "",
            "IF the claims survive only because of the label —",
            "  not the facts —",
            "  the model is matching a stereotype, not analyzing evidence.",
            "",
            "That assessment does NOT go in your product.",
        ],
        img_label="[IMAGE: A profile with the demographic label peeled off, half the claims collapsing]",
    )
    add_check_on_learning(
        prs,
        "A model hands you a confident profile of a group. How do you tell whether it's "
        "reading the evidence you gave it or replaying a training-data stereotype — and "
        "what do you OWE once you can tell?",
    )
    add_hands_on(
        prs,
        "Strip the Assumption",
        [
            "Ask a model to assess a group/actor from a deliberately thin, non-sensitive (fictional/historical) description.",
            "Underline every confident conclusion in the output.",
            "For each: what specific fact in MY input supports this? Mark the ones surviving only on assumption.",
            "Rewrite using only evidence-supported claims. Note how much shorter — and more honest — it gets.",
            "Write one sentence: what would you have laundered into a product if you'd accepted the first output?",
        ],
        img_label="[IMAGE: A long assessment shrinking to a short evidence-only version]",
    )
    add_section_summary(
        prs,
        "Bias & Fairness in AI-Assisted Analysis",
        [
            "The model inherited human bias from training data — it is a mirror, not malicious.",
            "Stereotype-matching fills gaps with assumption; evidence-based tracks your facts.",
            "Fluency hides bias — you are the filter or the conduit.",
            "Spotting bias without correcting it is itself a failure.",
        ],
    )

    # ===================================================== SECTION 5
    add_section_header(
        prs, "05", "Disclosure &\nAttribution",
        "Provenance of your product — default to traceability.",
        "[IMAGE: A product footer reading 'Drafted with AI assistance; all claims "
        "verified' next to an analyst's initials]",
    )
    add_concept_slide(
        prs,
        "Provenance: Where Did This Come From?",
        [
            ("Provenance: where a product came from and what touched it — the basis of traceability.", False),
            ("Disclose when AI assistance is MATERIAL — it shaped substance, not just polish.", False),
            ("Test: would a consumer weight it differently knowing how much the model produced?", True),
            ("Public affairs is a HARD line, governed by policy not personal judgment:", False),
            ("DoDI 5400.19 — notice when generative AI creates public-facing content", True),
            ("AI-generated/modified visual info cites the technology; humans approve before release", True),
            ("No policy stated? Default to TRACEABILITY — note that AI assisted, and how.", False),
        ],
        note="VERIFY CURRENCY: DoDI 5400.19 and DoD disclosure guidance are in active "
             "revision. Confirm the current version + unit policy before relying on it. "
             "Not legal advice — ask your PAO/chain/legal when unsure.",
        accent=CYBER_GOLD,
    )
    add_check_on_learning(
        prs,
        "You used a model to draft most of an assessment, then verified and lightly "
        "edited it. Your unit has no explicit disclosure policy for internal products. "
        "What is your default — and why is it the safer call?",
    )
    add_hands_on(
        prs,
        "Write the Provenance Note",
        [
            "Take a recent non-sensitive AI-assisted product, or build a short one now.",
            "Apply the materiality test: did AI shape SUBSTANCE or just polish? Write the one-sentence answer.",
            "Draft a one-line provenance note appropriate to the product.",
            "Decide destination — internal or public-facing? If public, write what DoDI 5400.19's principles require (verify current policy first).",
            "Identify who in your chain you'd ask if unsure whether disclosure was required.",
        ],
        img_label="[IMAGE: A one-line provenance footer being stamped onto a finished product]",
    )
    add_section_summary(
        prs,
        "Disclosure & Attribution",
        [
            "Provenance = where it came from and what touched it; it enables traceability.",
            "Disclose when AI is material (shaped substance), via the materiality test.",
            "Public-facing content is governed by DoDI 5400.19 — verify its current form.",
            "No policy stated? Default to traceability — disclose and move on.",
        ],
    )

    # ===================================================== SECTION 6
    add_section_header(
        prs, "06", "Dual-Use &\nMisuse Awareness",
        "Capability is not authorization — recognize the boundary, not a how-to.",
        "[IMAGE: A single generative tool with two arrows out — one to a legitimate "
        "report, one to fabricated media, a STOP gate on the second]",
    )
    add_concept_slide(
        prs,
        "The Lawful-Use Boundary",
        [
            ("Dual-use: a capability with both legitimate and harmful applications — the same features.", False),
            ("Synthetic media (fake text/image/audio/video) matters two directions:", False),
            ("As a TARGET: adversaries use it against you — calibrate trust in unverified media", True),
            ("As an OPERATOR: generating deception is governed by law, authorities, policy — not freelanced", True),
            ("The lawful-use boundary is set by law/authorities/policy — NOT by what the tool can do.", False),
            ("Near the line (deception, impersonation, fabricated media, influence)? STOP and route up.", True),
        ],
        note="Capability is not authorization. The tool being able to do something tells "
             "you NOTHING about whether you're allowed to. This is awareness, not instruction.",
        accent=CYBER_GOLD,
    )
    add_check_on_learning(
        prs,
        "A tasking could be done by generating a convincing piece of fabricated media, "
        "and the model would do it without complaint. What does the model's WILLINGNESS "
        "tell you about whether you're authorized — and what is your next move?",
    )
    add_hands_on(
        prs,
        "Recognize the Boundary (no generation today)",
        [
            "List three legitimate uses of generative AI in your work and three ways the SAME capabilities could be misused.",
            "Notice: they are the same features.",
            "For each misuse, write one sentence on who sets the boundary (law, authorities, policy, chain).",
            "Write the reflex: 'When a task approaches deception/impersonation/fabricated media, I STOP and route it to ___.'",
            "Reflect: how would you verify a piece of media before trusting it, knowing how easily it's synthesized?",
        ],
        img_label="[IMAGE: A checklist of features each labeled both USE and MISUSE, with a routing arrow up the chain]",
    )
    add_section_summary(
        prs,
        "Dual-Use & Misuse Awareness",
        [
            "Dual-use: the feature that helps you also enables harm — the use is what's governed.",
            "Synthetic media is both a threat to you and a boundary on you.",
            "Capability is not authorization — set by law/authorities/policy, not the tool.",
            "Near the line? Stop and route up — recognition, not a how-to.",
        ],
    )

    # ===================================================== SECTION 7
    add_section_header(
        prs, "07", "Privacy &\nCollection Ethics",
        "Beyond OPSEC: 'collectible' is not 'appropriate'.",
        "[IMAGE: Individually-harmless data points (a name, a location, a post) snapping "
        "together into an intrusive profile]",
    )
    add_concept_slide(
        prs,
        "Technically Collectible Is Not Appropriate",
        [
            ("Module 1 (connect, don't re-teach): data handling = what sensitive material flows IN.", False),
            ("This section = the OTHER side: ethics of data you collect/use about OTHER people.", True),
            ("Third-party/incidental data: collection sweeps in non-targets — obligations remain.", False),
            ("Consent & expectation: data offered for one purpose isn't fair game for any purpose.", False),
            ("Aggregation: harmless points combine into an intrusive profile — AI excels at this.", False),
            ("The whole is far more sensitive than the parts; you can profile without touching 'sensitive' data.", True),
            ("Technically collectible != lawfully/ethically appropriate — the boundary is law/authorities/policy.", False),
        ],
        note="VERIFY / ASK: Rules on collection, retention, dissemination — especially "
             "U.S. persons information — are strict and not yours to interpret on the fly. "
             "Not legal advice. Route hard cases to chain + legal/oversight before acting.",
        accent=CYBER_GOLD,
    )
    add_check_on_learning(
        prs,
        "Every data point about a person is publicly available and individually "
        "harmless. An AI tool correlates them into a detailed profile in seconds. Why "
        "might that AGGREGATION still cross an ethical or legal line — and what do you "
        "do when you sense it might?",
    )
    add_hands_on(
        prs,
        "Watch the Aggregate (a reasoning exercise)",
        [
            "Imagine a fictional task to profile a person from open sources. List five individually-harmless data points.",
            "Combine them. Write down what the AGGREGATE reveals that no single point did.",
            "Identify where in that aggregation you'd want to stop and ask — and who you'd ask.",
            "Write one sentence distinguishing this duty from the Module 1 data-handling rule, in your own words.",
        ],
        img_label="[IMAGE: Five small data cards merging into one detailed dossier, a STOP line drawn partway]",
    )
    add_section_summary(
        prs,
        "Privacy & Collection Ethics Beyond OPSEC",
        [
            "OPSEC protects OUR information; this protects OTHER people's.",
            "Third-party/incidental data carries privacy obligations you didn't seek.",
            "Aggregation is the AI-amplified risk — harmless parts, intrusive whole.",
            "'Technically collectible' is not 'lawfully/ethically appropriate' — ask on hard cases.",
        ],
    )

    # ===================================================== SECTION 8
    add_section_header(
        prs, "08", "DoD AI Principles\n& Lawful-Use Close",
        "Responsible, Equitable, Traceable, Reliable, Governable — mapped back.",
        "[IMAGE: Five pillars labeled with the principles, each tied by a line back to a "
        "habit from Sections 1-7]",
    )
    add_concept_slide(
        prs,
        "The Five Principles, Mapped to Your Habits",
        [
            ("DoD adopted five AI Ethical Principles — every one has an operator-level expression:", False),
            ("RESPONSIBLE — humans keep judgment & accountability  ->  §1 sign for it; §3 judge first", True),
            ("EQUITABLE — minimize unintended bias  ->  §4 don't launder stereotype-matching", True),
            ("TRACEABLE — transparent, auditable methods & sources  ->  §5 disclosure; §2 verify to sources", True),
            ("RELIABLE — explicit, tested, well-defined uses  ->  §2 hallucination; §6 lawful-use boundary", True),
            ("GOVERNABLE — detect/avoid harm, ability to disengage  ->  §6 dual-use; §7 privacy; stop & route up", True),
            ("Supporting (cite + verify): CDAO Responsible AI guidance; DoDI 5400.19; NIST AI RMF (Govern/Map/Measure/Manage).", False),
        ],
        note="VERIFY CURRENCY: the 5 Principles, CDAO RAI guidance, DoDI 5400.19, and NIST "
             "AI RMF are all in active revision. Not legal advice — a literacy map, not a "
             "compliance checklist. Confirm current versions + unit policy before relying on them.",
        accent=CYBER_GOLD,
    )
    add_example_slide(
        prs,
        "The Standing Order — How This Module Closes",
        "Three sentences carry the whole module forward",
        [
            "(1)  You SIGN for every AI-assisted product —",
            "       capability never transfers accountability.",
            "",
            "(2)  VERIFY before you act —",
            "       and your duty scales with the stakes.",
            "",
            "(3)  When the right call is unclear — disclosure, dual-use,",
            "       privacy, lawfulness — STOP and ASK your chain of",
            "       command or legal/ethics advisor.",
            "",
            "Not legal advice. Does not replace unit policy.",
            "The operator who asks is never the one who fails the ethics check.",
        ],
        img_label="[IMAGE: A 'WHEN UNCLEAR, ASK' placard above a clear path to the chain of command]",
    )
    add_check_on_learning(
        prs,
        "Map one real, non-sensitive AI-assisted task you expect to do this month onto "
        "the five principles. Which principle is most at risk in that task — and what "
        "will you do to honor it?",
    )
    add_hands_on(
        prs,
        "Map It Back",
        [
            "Without looking, name the five DoD AI Ethical Principles. Check yourself against the table.",
            "For each principle, write the one habit from Sections 1-7 that expresses it.",
            "Pick the principle you're personally weakest on and write one concrete workflow change.",
            "Write the standing-order sentence in your own words: 'When ethics is unclear, I ___.'",
        ],
        img_label="[IMAGE: A worksheet linking each of the five principles to a personal habit]",
    )
    add_section_summary(
        prs,
        "DoD AI Ethical Principles & Lawful-Use Close",
        [
            "Five principles: Responsible, Equitable, Traceable, Reliable, Governable.",
            "Each maps to a habit you practiced — the seven habits were one framework.",
            "CDAO RAI guidance, DoDI 5400.19, NIST AI RMF — cite by name, verify currency.",
            "Standing order: verify, sign, and when unclear, ask the chain or legal.",
        ],
    )

    # ----------------------------------------------------- MODULE SUMMARY TABLE
    add_summary_table(
        prs,
        "MODULE SUMMARY",
        "Rules of Engagement — the eight duties",
        [
            ["1. Accountability", "You sign for it", "Capability doesn't transfer accountability"],
            ["2. Hallucination", "Verify to the stakes", "A released fabrication is authored harm"],
            ["3. Automation Bias", "Judge first, consult second", "Write your own assessment before the model's"],
            ["4. Bias & Fairness", "Don't launder bias", "Stereotype-matching vs. evidence — refuse it"],
            ["5. Disclosure", "Default to traceability", "Material AI use; public = DoDI 5400.19"],
            ["6. Dual-Use", "Capability != authorization", "Stay in the lawful-use boundary; route up"],
            ["7. Privacy", "Respect others' data", "'Collectible' != 'appropriate'; watch aggregation"],
            ["8. DoD Principles", "Map it all back", "Responsible/Equitable/Traceable/Reliable/Governable"],
        ],
        ["Section", "The Duty", "One-Line Takeaway"],
        [Inches(0.45), Inches(3.1), Inches(6.4)],
        [Inches(2.55), Inches(3.2), Inches(5.9)],
    )

    # ----------------------------------------------------- READINESS CHECK
    add_readiness_check(
        prs,
        [
            "I can explain why capability does not transfer accountability — I sign for it",
            "I treat a hallucination in a consequential product as authored harm, scaled to stakes",
            "I judge first and consult second — own assessment written before the model's",
            "I can spot stereotype-matching vs. evidence and refuse to launder bias into a product",
            "I disclose material AI use and know DoDI 5400.19 governs public-facing content",
            "I know capability is not authorization and stay inside the lawful-use boundary",
            "I respect privacy beyond OPSEC: 'collectible' is not 'appropriate' — I watch aggregation",
            "I can name the five DoD AI Ethical Principles and map each to a habit",
            "I know the standing order: verify, sign, and when unclear, ask the chain or legal",
        ],
    )

    # ----------------------------------------------------- END
    add_end_slide(
        prs,
        "Module 09:\nRules of Engagement",
        [
            "You sign for every AI-assisted product — capability never transfers accountability",
            "Your verification duty scales with the stakes",
            "When the ethical call is unclear, stop and ask your chain or legal",
            "Verify policy currency before you rely on it — none of this is legal advice",
            "Next: Module 10 — Field Craft: Markdown, Code, Tools & Context Files",
        ],
    )

    save_deck(prs, __file__, "09-ethics.pptx")


if __name__ == "__main__":
    build()
