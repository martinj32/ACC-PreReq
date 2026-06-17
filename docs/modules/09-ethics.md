# Rules of Engagement: Ethics & Responsible AI Use

**Who this is for:** An analyst or operator who can already prompt, ground, command an agent, and handle data correctly — and now needs the rulebook for *what you do with the output and whether the use is right, lawful, and accountable.*

**What you will leave with:** A working ethic for AI-assisted work: you sign for every product, you treat a hallucination in a consequential deliverable as authored harm, you judge before you consult, you spot biased output and own the duty to correct it, you disclose AI assistance when policy or honesty requires it, you stay inside the lawful-use boundary, you respect privacy beyond OPSEC, and you can map all of it back to the DoD AI Ethical Principles.

---

!!! danger "Ethics Is Not OPSEC — Do Not Confuse the Two"
    Module 1 taught **data handling**: what flows *in* — what you are allowed to paste into a system. That is security. **This module is the opposite direction.** Ethics is what you do with what comes *out*, and whether the use itself is right, lawful, and accountable. You can be perfectly OPSEC-compliant — paste nothing sensitive, use only an authorized system — and still commit an ethical failure by signing for a fabricated claim, hiding that AI wrote your product, or using generation to deceive. Clean inputs do not make an output honest. This module owns the output side.

!!! warning "Verify Currency Before Delivery — This Is Not Legal Advice"
    This module references DoD AI policy by name (the five AI Ethical Principles, CDAO Responsible AI guidance, DoDI 5400.19, NIST AI RMF). **All of it is in active revision.** Names, numbers, and requirements change. Nothing here is legal advice or a substitute for your unit's policy. Before any course run — and before you act on any framework cited here — verify the current version against the authoritative source, and when a real situation is unclear, **ask your chain of command or your legal/ethics advisor.** Treat every framework reference below as "confirm before you rely on it."

---

## 1. Accountability & Authorship: You Sign for It

**BLUF.** Capability does not transfer accountability — the moment your name, your unit, or your judgment rides on a product, you are its author no matter how much of it a model drafted, and "the model said so" is not a defense that exists.

### Why This Matters

You already met the supervisor's third duty in the agent module: *delegate, verify, **own.*** This section is where "own" stops being a slogan and becomes a signature. In analysis and operations, products carry weight: a SITREP a commander acts on, an assessment that shapes a decision, a paragraph that ends up in a higher-echelon product. When that product is wrong, no one upstream cares which tool drafted it. They care whose name is on it. That name is yours.

### Concepts

**Authorship attaches to the signer, not the drafter.** A model can draft a paragraph faster than you can type it. That speed is real and useful. What it does not do is move the accountability onto the model. The instant you forward, brief, or sign a product, you have adopted every claim in it as your own assertion. You are not "passing along what the AI produced." You are *asserting it.*

**There is no "the model said so" defense.** Imagine explaining a bad call to your commander: "The assessment was wrong because the AI hallucinated it." That sentence does not reduce your responsibility — it *adds* to it, because it admits you signed for a claim you never verified. The model is a tool, like a calculator or a junior analyst. You do not get to blame the calculator. You ran it; you signed for the answer.

**Vouching is per-claim, not per-document.** Signing for a product does not mean "it reads well" or "it sounds right." It means: for *every* checkable claim in it — every name, date, figure, citation, causal link — you have either verified it or you are personally willing to be accountable for it being wrong. A product is only as signed-for as its least-checked sentence.

!!! warning "Fluent Is Not Verified"
    A model produces confident, polished prose whether the underlying claim is true or fabricated (you saw this in Module 1's failure modes). Polish is not a signal of accuracy. The better the writing, the *more* careful you must be — good prose is exactly what makes an unverified claim slide through review.

!!! tip "The Signature Test"
    Before you forward any AI-assisted product, ask one question: *"If every claim in this turned out to be something I have to personally defend in front of my commander, am I ready to defend it?"* If the answer is no, you have not finished — you have a draft, not a product.

??? note "Instructor Note — Make the Signature Literal"
    Have students physically initial the AI-drafted paragraph in the hands-on before they "release" it, and tell them the initials mean *I vouch for every claim here.* The physical act of signing makes the abstract accountability concrete. Several students will sign, then catch themselves and pull it back to check — that hesitation is the lesson landing.

??? note "Instructor Note — Connect Back, Don't Re-Teach"
    This is the supervisor mindset's "own the outcome" duty, now made specific to authored products. Name the link out loud so students see the spiral, but do not re-teach delegate-verify-own from scratch — they have it.

### Hands-On

You will sign for a product — correctly.

1. Ask a model to draft a short analytic paragraph (4–6 sentences) on a **non-sensitive, unclassified topic you know well** — a historical event, a piece of doctrine, a technical process. Do not use operational content.
2. Read the paragraph and find **every checkable claim**: every name, date, number, and causal "because."
3. For each claim, verify it against a source you trust, or mark it "cannot verify."
4. The instructor (or a partner) has planted — or you now deliberately introduce — **one false claim** that reads as plausible. Find it. If you signed before checking, you would have asserted it.
5. Only after every claim is verified or struck, **initial the paragraph.** Those initials mean: *I vouch for every claim here.*

You just experienced the difference between *receiving* output and *authoring* a product.

!!! question "Before You Continue"
    A model drafted a flawless-sounding assessment and you forwarded it under your name. One figure in it was fabricated and a decision was made on it. Who is accountable, and what specifically did you fail to do?

<div class="quiz-block">
  <p class="quiz-question">An AI-drafted assessment you signed and forwarded contained a fabricated statistic that led to a bad decision. What is the correct accounting of responsibility?</p>
  <ul class="quiz-options">
    <li data-correct="false">The model is responsible — it generated the false statistic</li>
    <li data-correct="false">Responsibility is shared equally between you and the AI vendor</li>
    <li data-correct="true">You are accountable — signing and forwarding the product made you its author, and the duty to verify every claim was yours</li>
    <li data-correct="false">No one is at fault because hallucination is a known limitation of the technology</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can explain why capability does not transfer accountability
- [ ] I understand that "the model said so" is not a defense — it is an admission
- [ ] I know that vouching is per-claim, not "it reads well"
- [ ] I have signed for a product only after verifying every checkable claim in it

---

## 2. Hallucination as an Ethical Failure

**BLUF.** Module 1 taught hallucination as a technical fact about how the engine works; this section reframes it as an *ethical event* — when a fabricated claim rides into a consequential product under your name, the harm is authored, and your duty to verify scales with the stakes.

### Why This Matters

You already know *that* models hallucinate — you produced one with your own hands in Module 1. What you have not yet been asked is the ethical question that follows: *so what do you owe because of it?* A hallucination in a sandbox is a curiosity. The same hallucination in an intelligence assessment, a target package, or a product a commander acts on is not a curiosity — it is harm with a person's name attached. This section is about that obligation.

### Concepts

**The same mechanism, two completely different stakes.** The model has no truth-checking step — it generates statistically likely tokens regardless of whether they are true (Module 1's lesson, not re-taught here). The *technical* event is identical whether you are asking about trivia or drafting a SITREP. The *ethical* weight is not. The fabrication that is harmless in one context is consequential in the other. Knowing the mechanism does not discharge the duty — it *creates* it, because now you cannot claim you didn't know.

**Hallucination becomes authored harm at the point of release.** A false claim sitting in a chat window has harmed no one. The moment you adopt it into a product and release it, you have converted a model's statistical artifact into *your assertion*, and any harm that follows is harm you authored. The model generated the tokens; you authored the claim by signing for it (Section 1).

**Your verification duty scales with the stakes.** Not every output needs the same scrutiny — that would be paralysis. The principle is proportional: the more consequential the product, the higher the bar before you sign.

| Stakes | Example | Verification owed |
|---|---|---|
| Low | Brainstorming, rough draft you will rewrite | Sanity-check; obvious errors |
| Medium | Internal summary others will read | Verify key claims, citations, figures |
| High | Product a decision is made on | Verify *every* checkable claim against trusted sources, independently |

!!! danger "The Stakes Set the Standard — Not Your Schedule"
    The duty to verify scales with consequence, not with how busy you are. A deadline does not lower the bar on a high-stakes product; it only raises the temptation to skip the check. The fabricated citation that gets a deadline-pressured analyst is exactly the one that ends up in the brief.

!!! example "Same Fabrication, Different Worlds"
    A model invents a plausible source: *"per the 2024 regional stability report, cross-border incidents rose 40%."* There was no such report; the figure is fabricated.

    - **In a study note to yourself:** you catch it later, no harm done.
    - **In an assessment your commander briefs upward:** a 40% figure with a citation is the kind of concrete claim decisions get built on. By the time anyone discovers the report does not exist, the decision has already been made — on your authored claim.

    Same token-generation event. One is a curiosity. One is a failure you signed for.

??? note "Instructor Note — Don't Let This Become Cynicism"
    The point is calibrated duty, not distrust. The model is extraordinarily useful *and* a hallucination in a consequential product is an ethical failure. Both are true. A student who walks away refusing to use the tool has missed the lesson as badly as one who signs without checking.

### Hands-On

1. Take a model output that contains a specific factual claim with a citation (reuse one from Module 1's hallucination exercise, or generate a fresh one on a non-sensitive topic).
2. Write two sentences: *"If this rode into a low-stakes product, the consequence would be ___. If it rode into a high-stakes product, the consequence would be ___."*
3. For the high-stakes version, write the verification you would owe before signing.
4. Now actually do that verification on the claim. Did it survive?

!!! question "Before You Continue"
    You know the model can fabricate. You are on a deadline drafting a product a commander will act on. What does knowing the mechanism *obligate* you to do that you would not be obligated to do if you didn't know?

<div class="quiz-block">
  <p class="quiz-question">Why is a hallucination in a consequential product framed as an *ethical* failure and not just a technical limitation?</p>
  <ul class="quiz-options">
    <li data-correct="false">Because the model should have known the claim was false and chose to generate it anyway</li>
    <li data-correct="false">Because hallucination can always be eliminated with a better prompt</li>
    <li data-correct="true">Because once you adopt and release a fabricated claim, you have authored the harm — and knowing the mechanism creates a duty to verify that scales with the stakes</li>
    <li data-correct="false">Because using AI for consequential products is itself prohibited</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can explain how a technical fact (hallucination) becomes an ethical event (authored harm)
- [ ] I know the harm attaches at the point of release, when I adopt the claim
- [ ] I can state how verification duty scales with stakes
- [ ] I understand that a deadline raises the temptation, not lowers the standard

---

## 3. Over-Reliance, Automation Bias & Deskilling

**BLUF.** Judge first, consult second — automation bias is the documented human tendency to defer to a machine's output over your own assessment, and the antidote is to form and record your own judgment *before* you see the model's, so the AI sharpens your thinking instead of replacing it.

### Why This Matters

The most dangerous failure in AI-assisted analysis is not the model being wrong. It is *you* going quiet. When a confident output arrives before you have formed your own view, it anchors you — and your independent judgment, the thing the military actually needs from you, never gets exercised. Do that for months and the skill atrophies. The analyst who can no longer assess without the tool has become a relay, not an analyst.

### Concepts

**Automation bias.** Humans systematically over-trust automated output, especially when it is fluent and fast. You defer to the machine even when your own knowledge should override it. This is well-documented across aviation, medicine, and intelligence — it is a property of human psychology, not a personal weakness, which is exactly why you have to counter it with a *procedure* rather than willpower.

**Anchoring.** Whatever you see first sets your reference point. If the model's assessment arrives before your own, every subsequent thought is a reaction to it. You are no longer assessing the problem — you are editing the machine's take. Your independent read is gone before it ever existed.

**Deskilling.** A skill you stop exercising decays. If the model forms every assessment and you only approve them, your own analytic muscle weakens over time. The tool was supposed to be a force multiplier; used this way it becomes a substitute, and the day it is unavailable — or wrong in a way only your judgment would catch — you have nothing to fall back on.

**The countermeasure: judge first, consult second.** Form your own assessment and *write it down* before you see the model's. This single ordering change defeats anchoring (you have a reference point of your own), exercises your skill (you did the analysis), and turns the model into what it should be — a second opinion you compare against, reconcile with, or reject.

!!! tip "Where the Disagreements Live the Real Learning"
    When your written assessment and the model's disagree, that gap is the most valuable thing on the page. Either the model caught something you missed, or you caught something it fabricated. Investigate every disagreement — do not just default to the machine. Defaulting to the machine *is* automation bias.

!!! warning "Speed Is the Trap"
    The model's biggest selling point — instant output — is exactly what triggers automation bias. The faster the answer arrives, the more tempting it is to skip your own. Discipline means accepting a slower start (your own assessment first) to get a better, owned result.

??? note "Instructor Note — Make the Ordering Non-Negotiable"
    The whole lesson lives in the *sequence.* If students peek at the model first, the exercise is worthless and automation bias wins silently. Enforce it: own assessment written and visible *before* the model's is revealed. Have them keep both so they can compare.

### Hands-On

This exercise only works if you do the steps in order. Do not peek ahead.

1. Pick an analytic question on a non-sensitive topic you have some knowledge of (e.g., "what were the main drivers of [historical event]?").
2. **Before touching any AI:** write your own assessment. Three to five sentences. Commit to it.
3. *Now* ask the model the same question.
4. Compare. Where do you agree? Where do you disagree?
5. For every disagreement, decide *with reasoning* who is right — and verify, do not default to the machine.
6. Write one sentence: did the model sharpen your assessment, or were you about to let it replace it?

!!! question "Before You Continue"
    You have started reaching for the model *before* forming your own view on every problem. What skill is quietly eroding, and what is the one-step fix?

<div class="quiz-block">
  <p class="quiz-question">What is the single most effective discipline against automation bias in AI-assisted analysis?</p>
  <ul class="quiz-options">
    <li data-correct="false">Always run the prompt twice and average the two answers</li>
    <li data-correct="false">Use the most powerful model so its output is more trustworthy</li>
    <li data-correct="true">Form and write down your own assessment before you see the model's, then compare</li>
    <li data-correct="false">Accept the model's output whenever it sounds more confident than you feel</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can define automation bias and explain why it is psychology, not weakness
- [ ] I understand how anchoring erases my independent judgment
- [ ] I can explain deskilling and why it is a long-term operational risk
- [ ] I have run a judge-first, consult-second loop and compared the two

---

## 4. Bias & Fairness in AI-Assisted Analysis

**BLUF.** A model learned its patterns from human-produced text, so it inherited human biases — and in analysis that surfaces as output that matches a stereotype instead of the evidence, which you have an ethical duty to recognize and refuse to launder into your product.

### Why This Matters

Module 1 taught you the *literacy* — outputs can be skewed by training data, and you learned to *spot* it. This section is the *duty.* Spotting a biased output and shrugging is not neutral; if you pass it into an assessment, you have laundered a stereotype into an official product and given it the credibility of your signature. In intelligence work, that can mean assessing a person, group, or population based on what the training data assumed rather than what the evidence shows — which is both an analytic failure and an ethical one.

### Concepts

**Where the bias comes from.** The model was *trained, not programmed* (Module 1). It learned statistical patterns from a vast body of human text — and that text carries human assumptions, stereotypes, and skews. There is no rulebook to audit; the bias is baked into the weights. The model is not malicious. It is a mirror of its training data, and that data was not neutral.

**Stereotype-matching vs. evidence-based output.** This is the distinction to internalize. A *stereotype-matching* output fills a gap with the statistically common assumption — it tells you what the training data expected, dressed up as analysis. An *evidence-based* output is anchored to the specific facts you provided. The danger is that both arrive in the same confident voice. Your job is to ask: *is this conclusion coming from the evidence in front of us, or from a pattern the model absorbed about people like this?*

**The laundering risk.** Bias is most dangerous when it is invisible. The model produces a fluent assessment; you adopt it; now a stereotype wears the authority of an official product and a human signature. The fluency is exactly what hides the bias. You are the filter that stops it — or the conduit that passes it on.

!!! example "Spotting Stereotype-Matching"
    You ask a model to profile the likely behavior of a group based on a thin description. It returns a confident, detailed assessment.

    - **Test:** strip out the group label and ask what *specific evidence* in your input supports each claim.
    - If the claims survive only because of the label — not the facts — the model is matching a stereotype, not analyzing evidence. That assessment does not go in your product.

!!! warning "Bias Is Not Always About Demographics"
    Stereotype-matching shows up anywhere the training data had a strong prior: which actor is "probably" responsible, what a situation "usually" means, what a pattern "typically" indicates. Anytime the model reaches a confident conclusion that the specific evidence does not support, treat it as a possible inherited bias and check it against the facts.

??? note "Instructor Note — Hold the Line Between M1 and M9"
    Module 1 owns *spotting* skewed output (literacy). This module owns the *ethical duty* not to launder it (policy/conduct). Do not re-teach the mechanism of bias here — students have it. Teach the obligation: spotting without correcting is a choice, and it is the wrong one.

### Hands-On

1. Ask a model to make an assessment or prediction about a group or actor from a deliberately thin, non-sensitive description (use a fictional or historical scenario — never real operational subjects).
2. Read the output and underline every confident conclusion.
3. For each one, ask: *what specific fact in my input supports this?* Mark the ones that survive only on assumption.
4. Rewrite the assessment using only evidence-supported claims. Note how much shorter — and more honest — it gets.
5. Write one sentence on what you would have laundered into a product if you had accepted the first output.

!!! question "Before You Continue"
    A model hands you a confident profile of a group. How do you tell whether it is reading the evidence you gave it or replaying a stereotype from its training data — and what do you owe once you can tell?

<div class="quiz-block">
  <p class="quiz-question">A model produces a confident assessment of a group that goes beyond the evidence you provided. What is the ethical duty?</p>
  <ul class="quiz-options">
    <li data-correct="false">Use it — the model processed more data than any human could, so its priors are probably right</li>
    <li data-correct="false">Spotting the bias is enough; recognizing it discharges the responsibility</li>
    <li data-correct="true">Test each claim against the specific evidence, strip out anything supported only by assumption, and refuse to pass a stereotype into the product</li>
    <li data-correct="false">Soften the wording so the bias is less obvious, then include it</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can explain why a model inherits human bias from its training data
- [ ] I can distinguish stereotype-matching from evidence-based output
- [ ] I understand the laundering risk — passing bias into a signed product
- [ ] I know that spotting bias without correcting it is itself a failure

---

## 5. Disclosure & Attribution: Provenance of Your Product

**BLUF.** Provenance is the answer to "where did this come from" — and when AI assistance is material to a product, honesty and policy can require you to disclose it; absent explicit guidance, default to traceability so the chain knows what touched your work.

### Why This Matters

A product's credibility depends on knowing how it was made. If a reviewer, a commander, or a downstream consumer assumes a human analyst hand-built an assessment that was in fact largely model-generated, they are calibrating their trust on a false premise. Disclosure is not an admission of weakness — it is what lets the people relying on your product weight it correctly. In public-facing work, it can also be a hard policy requirement.

### Concepts

**Provenance.** Where a product came from and what touched it along the way — sources, tools, and the role AI played. Provenance is what makes a product *traceable*, and traceability is one of the DoD AI Ethical Principles you will map in Section 8.

**When disclosure matters most.** Not every use of a spell-checker needs a footnote. Disclosure matters when AI assistance is *material* — when it shaped the substance, structure, or conclusions of the product, not just the polish. The test: *would a reasonable consumer of this product weight it differently if they knew how much of it the model produced?* If yes, the AI role is material.

**Public affairs is a hard line.** Content released to the public is governed by policy, not personal judgment. **DoDI 5400.19 (Public Affairs Use of Artificial Intelligence)** establishes that DoD personnel provide notice when generative AI is used to create public-facing content, that AI-generated or AI-modified visual information cites the technology's use, and that components exercise human oversight and approval of generative AI outputs before public release. If your product is going outside the wire to the public, AI involvement is not a judgment call — it is a labeling requirement.

**Default to traceability when no policy is stated.** Internal products often have no explicit AI-disclosure rule yet. The safe default is *traceability*: note that AI assisted, and how, so the chain can account for it. It is far easier to defend "I disclosed and it wasn't required" than "I didn't disclose and it was."

!!! warning "Verify Currency — DoDI 5400.19 Is in Active Revision"
    DoDI 5400.19 and the broader DoD public-affairs and disclosure guidance change. Confirm the current version and your unit's implementing policy before you rely on any specific requirement stated here. This is not legal advice — when a disclosure question is real and unclear, ask your PAO, chain of command, or legal advisor.

!!! tip "The One-Line Provenance Note"
    When in doubt and no policy says otherwise, attach a one-line note to the product: *"Drafted with AI assistance; all claims verified by [you]."* It costs nothing, it preserves traceability, and it makes your verification explicit — which is also your Section 1 signature.

??? note "Instructor Note — Disclosure ≠ Confession"
    Students often hear "disclose AI use" as "admit you cheated." Reframe it: disclosure is a *quality and trust* practice, the same as citing a source. The dishonest move is letting a consumer believe a product was built a way it wasn't. Pair this with the public-affairs requirement so they see it is also policy, not just etiquette.

### Hands-On

1. Take a recent (non-sensitive) product you built with AI assistance, or build a short one now.
2. Apply the materiality test: did AI shape the *substance* or just the polish? Write the one-sentence answer.
3. Draft a one-line provenance note appropriate to the product.
4. Decide its destination: internal-only, or public-facing? If public-facing, write what DoDI 5400.19's principles would require — and note that you would verify the current policy first.
5. Identify who in your chain you would ask if you were unsure whether disclosure was required.

!!! question "Before You Continue"
    You used a model to draft most of an assessment, then verified and lightly edited it. There is no explicit disclosure policy for internal products in your unit. What is your default, and why is it the safer call?

<div class="quiz-block">
  <p class="quiz-question">You are preparing AI-assisted content for public release. What does the existence of DoDI 5400.19 mean for you?</p>
  <ul class="quiz-options">
    <li data-correct="false">Nothing — disclosure of AI use is always a personal judgment call</li>
    <li data-correct="false">You may disclose if you want, but public release is exempt from labeling</li>
    <li data-correct="true">Public-facing AI-generated or AI-modified content carries notice/labeling and human-oversight requirements — verify the current policy and follow it, it is not optional</li>
    <li data-correct="false">You only need to disclose if someone specifically asks how the product was made</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can define provenance and connect it to traceability
- [ ] I can apply the materiality test for when AI use must be disclosed
- [ ] I know DoDI 5400.19 governs AI use in public-facing content (and that I must verify its current form)
- [ ] I default to traceability when no policy is stated

---

## 6. Dual-Use & Misuse Awareness

**BLUF.** The same generative capability that drafts your assessment can fabricate convincing deception and synthetic media — this section is awareness of that dual-use reality and the lawful-use boundary, not a how-to, so you recognize misuse and stay on the right side of the line.

### Why This Matters

Generative AI is a dual-use capability: the feature that helps you also enables harm. You do not need to know *how* to misuse it — and this course will not teach that. You do need to recognize that the capability exists, that it has a lawful-use boundary, and that your job is to stay inside that boundary and recognize when something has crossed it. An operator who does not know synthetic media is trivially generated is an operator who can be deceived by it.

### Concepts

**Dual-use.** A capability with both legitimate and harmful applications. A model that can write a fluent report can also write fluent disinformation. A model that can edit an image to clarify it can also fabricate one that never happened. The capability is neutral; the *use* is what is governed.

**Synthetic media and fabricated deception.** Generative tools can produce convincing fake text, images, audio, and video. This matters to you in two directions:
- **As a potential target:** adversaries can use it against you and your sources. Calibrate your trust in unverified media accordingly.
- **As an operator:** generating deceptive content is governed by law, authorities, and policy — it is not something an individual freelances. "I could make this" is never the same as "I am authorized to make this."

**The lawful-use boundary.** This is the line. Whether a given use of generative capability is permitted depends on law, on your unit's authorities, and on policy — not on whether the tool *can* do it. Technical capability is not authorization. When you are near the line — anything involving deception, impersonation, fabricated media, or influence — stop and route it through your chain and legal, not your own judgment.

!!! danger "Capability Is Not Authorization"
    The single most important idea in this section: *the tool being able to do something tells you nothing about whether you are allowed to.* Authorization comes from law and policy and your chain — never from the model's willingness to comply. This mirrors the data-handling lesson (capability ≠ authorization) but points the other direction: there, the question was what you can put in; here, it is what you are permitted to produce.

!!! warning "Awareness, Not Instruction"
    This section deliberately does not teach techniques for generating deceptive content. The objective is recognition and the boundary, full stop. If a task seems to call for fabricated or deceptive media, that is your cue to *stop and ask*, not to figure out how.

??? note "Instructor Note — Keep It on the Boundary"
    Resist the pull toward either a how-to or a fearmongering session. The deliverable is a calibrated operator: knows the capability exists, knows it is dual-use, knows the boundary is set by law/policy/authorities, and knows the reflex is to route near-the-line questions upward. Do not let the discussion drift into specific generation methods.

### Hands-On

No generation today — this is a recognition exercise.

1. List three legitimate uses of generative AI in your work and three ways the *same* capabilities could be misused. Notice they are the same features.
2. For each misuse, write one sentence on who sets the boundary (law, authorities, policy, chain).
3. Write down the reflex: when a task approaches deception, impersonation, or fabricated media, *I stop and route it to ___.*
4. Reflect: how would you verify a piece of media before trusting it, knowing how easily it can be synthesized?

!!! question "Before You Continue"
    A tasking could be accomplished by generating a convincing piece of fabricated media, and the model would do it without complaint. What does the model's willingness tell you about whether you are authorized — and what is your next move?

<div class="quiz-block">
  <p class="quiz-question">A generative tool will readily produce a piece of fabricated media that would help with a tasking. What does that tell you about whether the use is permitted?</p>
  <ul class="quiz-options">
    <li data-correct="false">It is permitted — if the tool allows it, the use is within bounds</li>
    <li data-correct="false">It is permitted as long as no sensitive data went into the prompt</li>
    <li data-correct="true">Nothing — technical capability is not authorization; permissibility is set by law, authorities, and policy, and near-the-line tasks get routed up the chain</li>
    <li data-correct="false">It is prohibited only if the output will be released to the public</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can define dual-use and give an example from my own work
- [ ] I understand synthetic media as both a threat to me and a boundary on me
- [ ] I can state the lawful-use boundary: capability is not authorization
- [ ] I know my reflex is to stop and route near-the-line tasks up the chain

---

## 7. Privacy & Collection Ethics Beyond OPSEC

**BLUF.** OPSEC and data handling protect *your* sensitive information; privacy and collection ethics govern *other people's* — and "technically collectible" is not the same as "ethically and lawfully appropriate to collect, retain, or aggregate."

### Why This Matters

Module 1's data-handling rule was about protecting what flows in — keeping sensitive material out of unauthorized systems. This is the adjacent but distinct duty: respecting the privacy of third parties whose data you *could* gather. AI makes collection and aggregation dramatically easier, which means the ethical and legal questions arrive faster and at larger scale. The fact that a tool can vacuum up and cross-reference data about people does not mean you should — and in many cases, law and policy say you must not.

### Concepts

!!! note "Connecting to Module 1 — Once"
    Module 1 owns *data handling*: what sensitive material you may put **into** a system (the inbound, OPSEC/classification question). This section is the other side: the ethics of the data you **collect and use** about other people. Same care for information, opposite direction. We connect here and do not re-teach the inbound rule — you have it.

**Third-party and incidental data.** Collection and analysis frequently sweep in people who are not the target — bystanders, contacts, family members, whole populations. That incidental data carries privacy obligations even though you were not seeking it. "It was already in the dataset" does not dissolve the obligation.

**Consent and expectation.** People have reasonable expectations about how their information is used. Data offered for one purpose does not become fair game for any purpose. AI tools that re-purpose, infer, and cross-reference can quietly blow past the original expectation — and that gap is an ethical (and often legal) problem.

**Aggregation.** This is the multiplier AI makes dangerous. Individually harmless data points — a location here, a name there, a public post — combine into a detailed picture of a person that none of the pieces revealed alone. The whole is far more sensitive than the parts. AI is exceptionally good at exactly this kind of correlation, which means you can build an intrusive profile without ever touching anything that looked sensitive on its own.

**Technically collectible ≠ ethically/lawfully appropriate.** This is the section's spine. That data *can* be gathered, correlated, or retained says nothing about whether you are *permitted* to. The boundary is set by law, authorities, and policy — including the rules governing U.S. persons information — not by what the tool makes easy.

!!! danger "Aggregation Is the Quiet Line-Crosser"
    The most common way to cross a privacy line with AI is not one dramatic collection — it is assembling many innocuous pieces into something intrusive, fast, at scale, without noticing you crossed a threshold. Watch the *aggregate*, not just each input. When the picture you are building gets more detailed than the task requires, stop.

!!! warning "U.S. Persons and Legal Boundaries — Ask, Don't Guess"
    Rules governing the collection, retention, and dissemination of information — especially U.S. persons information — are strict, specific, and not yours to interpret on the fly. This is not legal advice. When a privacy or collection question touches these boundaries, route it to your chain of command and legal/oversight advisor *before* you act.

??? note "Instructor Note — Distinguish Cleanly from OPSEC"
    Students conflate this with data handling constantly. Hold the distinction hard: OPSEC/data-handling = protecting *our* sensitive information (inbound). Privacy/collection ethics = respecting *others'* information and the limits on gathering it (outbound/about-others). The aggregation point is the one most students have never considered — spend time there.

### Hands-On

No collection today — a reasoning exercise.

1. Imagine a (fictional) task to build a profile of a person from open sources. List five individually-harmless data points.
2. Combine them. Write down what the *aggregate* reveals that no single point did.
3. Identify where in that aggregation you would want to stop and ask — and who you would ask.
4. Write one sentence distinguishing this duty from the Module 1 data-handling rule, in your own words.

!!! question "Before You Continue"
    Every individual data point about a person is publicly available and individually harmless. An AI tool can correlate them into a detailed profile in seconds. Why might that aggregation still cross an ethical or legal line — and what do you do when you sense it might?

<div class="quiz-block">
  <p class="quiz-question">Why is "this data is technically collectible" not sufficient justification to collect and aggregate it?</p>
  <ul class="quiz-options">
    <li data-correct="false">Because collectible data is usually inaccurate</li>
    <li data-correct="false">Because it always violates OPSEC to collect third-party data</li>
    <li data-correct="true">Because ethical and lawful appropriateness — including consent, expectation, and the rules on U.S. persons information — is a separate question from technical capability, and aggregation can cross a line no single piece did</li>
    <li data-correct="false">Because the AI tool might hallucinate parts of the profile</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can distinguish privacy/collection ethics from Module 1 data handling
- [ ] I understand third-party/incidental data carries obligations
- [ ] I can explain why aggregation is the AI-amplified privacy risk
- [ ] I know "technically collectible" is not "lawfully/ethically appropriate" — and to route hard cases up

---

## 8. DoD AI Ethical Principles & Lawful-Use Close

**BLUF.** Everything in this module rolls up into five words the DoD adopted as its AI Ethical Principles — **Responsible, Equitable, Traceable, Reliable, Governable** — and this section maps each one back to the duties you just practiced, then closes with the standing order: this is not legal advice, follow unit policy, and ask the chain or legal when unsure.

### Why This Matters

You did not just learn seven disconnected habits. You practiced the operator-level expression of a coherent ethical framework the DoD has already adopted. Seeing the map does two things: it gives your habits an authoritative spine you can cite, and it gives you the vocabulary to recognize the same principles when they appear in policy, in guidance, and in the main course ahead.

### Concepts

**The DoD AI Ethical Principles.** The Department of Defense adopted five principles for the ethical use of AI: **Responsible, Equitable, Traceable, Reliable, Governable.** They were written for how the Department develops and fields AI capabilities — but every one of them has a direct, individual-operator expression, which is exactly what Sections 1–7 trained.

**The map — your habits back to the principles:**

| DoD Principle | Plain meaning | Where you practiced it |
|---|---|---|
| **Responsible** | Humans exercise appropriate judgment and remain accountable for AI use and outcomes | §1 You sign for it; §3 judge first, consult second |
| **Equitable** | Deliberate steps to minimize unintended bias | §4 Bias & fairness — don't launder stereotype-matching into products |
| **Traceable** | Transparent, auditable methods, sources, and provenance | §5 Disclosure & provenance; §2 verifying claims to trusted sources |
| **Reliable** | Explicit, well-defined uses; safety and effectiveness tested within them | §2 Hallucination as failure; §6 staying inside the lawful-use boundary |
| **Governable** | Detect and avoid unintended consequences; ability to disengage | §6 dual-use boundary; §7 privacy/aggregation limits; the reflex to stop and route up |

**The supporting frameworks (cite by name, verify currency).** Beyond the five principles, three reference points anchor responsible use — all in active revision, none legal advice:

- **DoD CDAO Responsible AI guidance** — the Chief Digital and Artificial Intelligence Office operationalizes the principles through Responsible AI guidance and generative-AI guardrails for DoD components. This is the "how we actually do it" layer under the five principles.
- **DoDI 5400.19** — public-affairs disclosure/labeling for AI in public-facing content (Section 5).
- **NIST AI RMF** — a light secondary reference: the AI Risk Management Framework's four core functions — **Govern, Map, Measure, Manage** — give a common vocabulary for managing AI risk across its lifecycle. You don't implement it as an individual; you recognize the language when it appears in policy.

!!! warning "Verify Currency Before Delivery — All Five Frameworks"
    The DoD AI Ethical Principles, CDAO Responsible AI guidance, DoDI 5400.19, and the NIST AI RMF are all subject to revision. Confirm the current version and your unit's implementing policy before you rely on any specific wording here. **None of this is legal advice.** It is a literacy map, not a compliance checklist.

!!! danger "The Standing Order — How This Module Closes"
    Three sentences carry the whole module forward:
    **(1)** You sign for every AI-assisted product, and capability never transfers accountability.
    **(2)** Verify before you act, and your duty scales with the stakes.
    **(3)** When the right call is unclear — disclosure, dual-use, privacy, lawfulness — **stop and ask your chain of command or legal/ethics advisor.** This is not legal advice and does not replace unit policy. The operator who asks is never the one who fails the ethics check.

??? note "Instructor Note — Land the Coherence"
    The payoff of this section is recognition: students realize the seven habits were one framework all along. Walk the map row by row so the principles stop being abstract words and become things they already did. Reinforce that "ask the chain/legal" is a *strength*, not an admission of incompetence — the whole module is permission to escalate.

### Hands-On

1. Without looking back, try to name the five DoD AI Ethical Principles. Check yourself against the table.
2. For each principle, write the one habit from Sections 1–7 that expresses it.
3. Pick the principle you are personally weakest on and write one concrete change to your workflow.
4. Write the standing-order sentence in your own words: *when ethics is unclear, I ___.*

!!! question "Before You Continue"
    Map one real (non-sensitive) AI-assisted task you expect to do this month onto the five principles. Which principle is most at risk in that task, and what will you do to honor it?

<div class="quiz-block">
  <p class="quiz-question">Which set correctly names the five DoD AI Ethical Principles?</p>
  <ul class="quiz-options">
    <li data-correct="false">Accurate, Fast, Secure, Auditable, Approved</li>
    <li data-correct="true">Responsible, Equitable, Traceable, Reliable, Governable</li>
    <li data-correct="false">Legal, Ethical, Transparent, Tested, Supervised</li>
    <li data-correct="false">Govern, Map, Measure, Manage, Monitor</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-block">
  <p class="quiz-question">You face an AI-use decision where disclosure and lawfulness are genuinely unclear and no policy squarely covers it. What is the correct move?</p>
  <ul class="quiz-options">
    <li data-correct="false">Make your best personal judgment and proceed — escalating wastes time</li>
    <li data-correct="false">Default to whatever the model recommends when asked about the policy</li>
    <li data-correct="true">Stop and ask your chain of command or legal/ethics advisor — this is not legal advice and does not replace unit policy</li>
    <li data-correct="false">Proceed as long as no sensitive data was entered into the tool</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can name the five DoD AI Ethical Principles from memory
- [ ] I can map each principle to a habit I practiced in this module
- [ ] I know CDAO RAI guidance, DoDI 5400.19, and NIST AI RMF by name — and that I must verify their currency
- [ ] I know the standing order: verify, sign, and when unclear, ask the chain or legal

---

## Summary

| Section | The duty | The one-line takeaway |
|---|---|---|
| 1. Accountability & Authorship | You sign for it | Capability does not transfer accountability; "the model said so" is no defense |
| 2. Hallucination as Ethical Failure | Verify to the stakes | A fabricated claim you release is authored harm; duty scales with consequence |
| 3. Over-Reliance & Automation Bias | Judge first, consult second | Form and write your own assessment before you see the model's |
| 4. Bias & Fairness | Don't launder bias | Spot stereotype-matching vs. evidence; refuse to pass it into a product |
| 5. Disclosure & Attribution | Default to traceability | Disclose material AI use; public-facing content is governed by DoDI 5400.19 |
| 6. Dual-Use & Misuse | Capability ≠ authorization | Recognize misuse; stay inside the lawful-use boundary; route near-line tasks up |
| 7. Privacy & Collection Ethics | Respect others' data | "Technically collectible" ≠ "lawfully/ethically appropriate"; watch aggregation |
| 8. DoD Principles & Lawful-Use Close | Map it all back | Responsible, Equitable, Traceable, Reliable, Governable — verify currency; ask when unsure |

---

## End of Module

You now hold the rulebook for *what you do with AI output and whether the use is right.* This is distinct from — and stacks on top of — the data-handling discipline from Module 1. Carry three things forward: **you sign for every product, your verification duty scales with the stakes, and when the ethical call is unclear you stop and ask your chain or legal.** None of the policy here is legal advice or a substitute for your unit's guidance — verify currency before you rely on it.

**Next:** Module 10 — *Field Craft: Markdown, Code, Tools & Context Files*, where the responsible habits you just built get applied to real artifacts.
</content>
</invoke>
