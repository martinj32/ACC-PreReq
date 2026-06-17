# Know Your Weapon: How AI Actually Works

**Who this is for:** Anyone who has used an AI chatbot by feel and is about to use one for real work. No prior technical knowledge required.

**What you will leave with:** A working mental model of what an LLM is and is not, how a conversation actually works under the hood, the failure modes that will bite you, a repeatable method for verifying output, a decision rule for when to reach for AI and when not to, and the one bright line on what you must never feed it.

---

## What an LLM Actually Is

**BLUF.** An LLM predicts text from learned patterns — not rules, not memory, not live data — and that single fact explains both why it is extraordinarily capable and exactly how it fails.

### Why This Matters

You already use one. What you have been doing by feel — type a request, read a response — is about to get a mental model underneath it. That model will not slow you down. It will make everything that follows click immediately instead of slowly. Treat this like learning your weapon system before you carry it on a mission: you do not need to machine the barrel, but you do need to know what it does, how it cycles, and where it jams.

### Concepts

The model reads a sequence of text and predicts what comes next. One chunk at a time. No lookup table. No truth check. Given everything written so far, what is the statistically most likely next piece?

!!! example "What Prediction Looks Like"
    Open your chatbot. Type: "The capital of France is" — and submit before you finish the sentence.

    The model completes it. Now type: "The capital of France is definitely" and watch the completion shift slightly.

    That is prediction. The word "definitely" changed the statistical context. The model did not look anything up.

**Trained, not programmed.** No one wrote a rule that says "Paris is the capital of France." The model was trained on enough text containing that fact that its weights now make it the likely completion. The upside: it generalizes to almost anything. The failure mode: if the training data was wrong, biased, or thin in some domain, the model learned those patterns too. There is no rulebook to audit.

**The LLM is the engine.** By itself, it is a brain in a jar — capable of reasoning in text, incapable of acting on its own. It reads text and writes text. No body, no memory between chats, no live connection to the world unless something external gives it one. Fluent, confident output is not the same as correct output. Both are true at the same time.

!!! warning "Swap the Verb"
    The model does not "know," "want," "think," or "lie." Those words will mislead you at every later step. It **predicts**. That is the only accurate verb. Catch yourself using the others and swap it in.

!!! note "Verify Before Teaching — Model Names and Specs"
    Model names, tiers, context-window sizes, and pricing change with every release cycle. Any specific name or number in this course is a snapshot. Verify current specifics at the provider's documentation before any course run.

??? note "Instructor Note — Architecture Questions"
    Do not open with attention heads, transformers, or parameter counts. A casual user needs a mental model that survives contact with a real tool, not the mechanism behind it. If a student asks, acknowledge it as a real question and defer: "That is a deeper topic — let's come back to it."

??? note "Instructor Note — Anthropomorphism Runs Deep"
    Students told "it just predicts" will still say "it knew the answer" thirty seconds later. Anthropomorphism is a wired cognitive shortcut. Interrupt it every time it appears in the first two weeks. It re-trains faster than you expect.

### Hands-On

The lab is the chatbot you already have open.

1. Type an incomplete sentence on a topic you know well and submit it. Read what the model predicts comes next.
2. Add the word "definitely" or "obviously" to the same sentence and submit again. Does the completion change?
3. Ask the model a factual question you already know the answer to. Check the output for accuracy.
4. Ask the exact same question again in a new chat. Is the answer identical, or slightly different?
5. Ask yourself: "How would I verify any of these outputs if I did not already know the answer?"

You are watching prediction happen in real time — and building the verification reflex before you need it.

!!! question "Before You Continue"
    The model just gave you a confident-sounding answer. What would it take to verify it? Where would you check?

<div class="quiz-block">
  <p class="quiz-question">A language model was never given a rule that says "Paris is the capital of France." How does it produce that answer?</p>
  <ul class="quiz-options">
    <li data-correct="false">It searched the internet for the answer</li>
    <li data-correct="false">A programmer hard-coded that fact into its rules</li>
    <li data-correct="true">It was trained on enough text containing that fact that the pattern was learned into its weights</li>
    <li data-correct="false">It remembered it from a previous conversation</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can state in one sentence what an LLM does
- [ ] I can explain "trained not programmed" in plain terms
- [ ] I know that confident output and correct output are not the same thing
- [ ] I have watched the model predict — not just heard about it

---

## Tokens and Context (Introduction)

**BLUF.** The model reads and writes in tokens — roughly 0.75 of an English word each — and can only hold a fixed number at once; fill that limit and earlier content starts to fall out, which is why long sprawling chats get worse, not better.

### Why This Matters

This is the first place the engine's behavior surprises people. They expect a longer conversation to give the model more to work with. The opposite happens once you pass the limit. Knowing why changes how you work.

!!! note "Where the Deep Treatment Lives"
    This section is the introduction only — enough to understand why long chats degrade. Spending tokens deliberately, model-selection tradeoffs, and managing context as a resource are the subject of Module 8 (Ammunition Discipline). Learn the *what* here; learn the *how to spend* there.

### Concepts

**Tokens.** The model does not read words; it reads chunks of text called tokens. In English prose, one token is roughly three-quarters of a word. Code and non-English text tokenize less efficiently — more tokens per word. You do not need to count tokens precisely; the instinct to keep input focused is the deliverable.

**The context window.** Every model has a hard ceiling on how many tokens it can hold in a single conversation. That ceiling is the context window. Think of it as a whiteboard with finite space: new writing crowds out old writing once it fills.

!!! example "Watching the Window Fill"
    Open a long document — several pages — and paste it into a fresh chat. Ask a detailed question about something near the top.

    Now open a new chat, paste the same document, and ask about something near the bottom.

    Compare the quality. Models attend better to the beginning and end of their context window than to the middle. Critical instructions buried mid-conversation may be partially ignored.

**What a full window looks like.** The model starts hedging. It contradicts something it stated confidently ten turns ago. It forgets a constraint you set at the start. That is not a bug; it is the whiteboard running out of space.

!!! tip "The Practical Rule"
    Start a fresh chat when: (1) the task has changed direction and earlier turns are dead weight, or (2) the model is drifting — hedging on things it stated confidently before.

??? note "Instructor Note — Context Window Sizes"
    Approximate sizes as of course development — verify before teaching, these change with releases: Claude around 200,000 tokens; GPT-4o around 128,000 tokens; Gemini 1,000,000+ tokens. Bigger is not always better — a full million-token window degrades quality in the middle. Do not drill numbers; drill the instinct.

### Hands-On

1. Open a fresh chat and paste several paragraphs of dense text.
2. Ask the model to summarize just the first paragraph.
3. In the same chat, ask it about something from the end of what you pasted.
4. Start a new chat and ask the same question. Compare.

!!! question "Before You Continue"
    You set an important constraint at the start of a long conversation. Ten exchanges later, the model seems to have forgotten it. What happened, and what would you do differently next time?

<div class="quiz-block">
  <p class="quiz-question">You are in a long chat and the model starts contradicting instructions you gave at the start. What is the most likely cause?</p>
  <ul class="quiz-options">
    <li data-correct="false">The model changed its mind</li>
    <li data-correct="false">You used the wrong model for this task</li>
    <li data-correct="true">Earlier content has been crowded out of the context window</li>
    <li data-correct="false">The model is testing whether you notice</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can define a token in plain terms
- [ ] I can explain what a context window is and what happens when it fills
- [ ] I know the two situations that warrant starting a fresh chat
- [ ] I have observed the window effect — not just read about it

---

## Conversation Mechanics & Statelessness

**BLUF.** The model has no memory of its own; every turn, the platform re-feeds the whole conversation back to a stateless engine, and once you understand that, you stop being surprised by what the model "remembers" and what it does not.

### Why This Matters

Most people picture the AI as a person on the other end who is following along. It is not. There is no one there between your messages. Understanding what actually happens each time you hit send tells you when to keep going, when to edit, and when to walk away and start clean — and it explains why a brand-new chat knows nothing about the one you had this morning.

### Concepts

**The model is stateless.** The engine itself remembers nothing between calls. It does not "stay logged in" to your conversation. Each time you send a message, the platform takes the entire thread so far — your first message, its reply, your second message, and so on — and feeds the whole stack back to the model as one block of text. The model reads all of it fresh and predicts the next turn. Then it forgets again.

**"Memory" is the transcript, not recall.** When the model refers back to something you said ten messages ago, it is not recalling it — it is re-reading it, because the platform put the whole transcript back in front of it. This is also why the context window matters so much: the conversation grows every turn, and when it overflows the window, the *oldest* turns drop off the top. The model cannot reference what is no longer in front of it.

**No cross-chat memory by default.** A fresh chat starts with a blank transcript. It knows nothing about your other conversations. Some products bolt on a separate "memory" or "projects" feature that injects saved notes into new chats — but that is an added layer, not the model remembering you. Treat every new chat as a stranger who has read nothing unless you have deliberately turned on such a feature.

**Edit vs. continue vs. new chat.** You have three moves, and they do different things:

- **Continue** — add a turn. Everything before stays in context. Use this when the thread so far is helping.
- **Edit** — go back and rewrite an earlier message. Most tools then discard everything after that point and re-run from there. Use this to fix a bad instruction at its source instead of piling corrections on top.
- **New chat** — start with an empty transcript. Use this when the old context is dead weight or actively dragging the model off course.

!!! tip "Edit at the Source, Don't Pile On"
    If your third message had a bad instruction, do not send a fourth message saying "actually, ignore that." Go back and edit the third message. A clean transcript produces cleaner output than one full of corrections the model has to reconcile.

!!! warning "The Model Cannot 'Pick Up Where We Left Off' in a New Chat"
    If you open a new conversation and say "continue what we were doing," the model has no idea what you mean. There is no thread to continue. You either stay in the original chat or paste the relevant context back in yourself.

??? note "Instructor Note — Kill the 'Person on the Other End' Model Early"
    Students carry a chat-app mental model: a helpful person reading along. Replace it with the right one: a stateless engine handed a fresh transcript every turn. Once it clicks, statelessness, context limits, and "why won't it remember my other chat" all stop being mysterious and become the same one fact.

### Hands-On

1. In a chat, tell the model a specific fact ("My callsign is Raptor-6"). Continue a few turns, then ask it to repeat the fact. It can — the transcript is still in front of it.
2. Open a brand-new chat and ask it for your callsign. Watch it have no idea. That is statelessness.
3. Go back to the first chat, edit an early message to change the fact, and re-run. Notice how the later turns regenerate from the edited point.
4. Reflect: when in your own work would "edit the source message" beat "send a correction"?

!!! question "Before You Continue"
    You spent an hour in one chat building up useful context. You close it and open a fresh one tomorrow. What does the new chat know about yesterday's work, and what would you have to do to get that context back?

<div class="quiz-block">
  <p class="quiz-question">When the model refers back to something you said earlier in the same conversation, what is actually happening?</p>
  <ul class="quiz-options">
    <li data-correct="false">The model stored your message in its long-term memory</li>
    <li data-correct="true">The platform re-fed the whole transcript to the stateless model, so it re-read your earlier message</li>
    <li data-correct="false">The model has a running memory of you across all your chats</li>
    <li data-correct="false">The model made an educated guess about what you probably said</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can explain why the model is described as "stateless"
- [ ] I know that conversation "memory" is the re-fed transcript, not recall
- [ ] I know a new chat has no knowledge of my other chats by default
- [ ] I can choose between continue, edit, and new chat for a given situation

---

## How LLMs Fail

**BLUF.** The model will state false things with total confidence, give different answers to the same question, know nothing past its training cutoff, and quietly reflect skewed patterns from its training data — none of this is a malfunction, and seeing it fail on purpose is the most important thing you can do in this section.

### Why This Matters

You are about to trust this tool with real work. Calibrated trust requires knowing exactly where it breaks. Read this section and then produce a hallucination with your own hands before moving on. In doctrinal terms: the model is the sharp junior analyst who never says "I don't know" — confident, fluent, and occasionally making it up entirely. You check the work not because you expect failure, but because fluency is not evidence of accuracy.

### Concepts

Five failure modes. Know all five.

**Hallucination.** The model has no truth-checking step. It generates tokens that are statistically likely to follow prior context. It cannot distinguish "information I was trained on accurately" from "information I am completing plausibly." Confident output and correct output are entirely unrelated. This is expected behavior of the system, not a rare bug.

**Confident-wrong.** Hallucination is not always dramatic. The model may state a subtly wrong date, a slightly wrong statistic, or a plausible-sounding citation that does not exist. The tone stays equally confident whether the claim is right or wrong. Never use the model's confidence as a signal of accuracy.

**Nondeterminism.** The model uses a temperature parameter that introduces variation. Same prompt, different run, different result — by design. Do not treat one output as "the answer" for high-stakes work. Run important prompts more than once and compare.

**Knowledge cutoff.** The model was trained on data up to a point in time. It does not know what happened after that. Worse, it does not handle the gap uniformly — three behaviors look identical from the outside:

- It flags the gap ("My knowledge cutoff is [date], I cannot confirm this") — the honest behavior.
- It answers confidently from stale training data with no indication it might be wrong — the dangerous behavior.
- It has a retrieval tool (web search) and fetches current information — but you have to confirm the tool actually fired.

You cannot tell which one you got without checking. Verify anything time-sensitive regardless of how confident the answer looks. (Grounding tools that close the cutoff gap are the subject of Module 3.)

**Bias-spotting (literacy).** The model learned from human-written text, and human text carries skewed patterns, stereotypes, and uneven coverage. The model reproduces those patterns. Ask it to "describe a nurse" or "describe a hacker" and notice the defaults it reaches for. Ask it about a region or group that is thinly represented in its training data and watch the output get generic or lean on cliché. **This is literacy: your job in this module is simply to notice when output is skewed or stereotype-shaped.** The ethical duty — what you owe the people affected by a biased product, and unit policy on it — is Module 9 (Rules of Engagement). Here, just learn to see it.

!!! warning "Build the Verification Reflex Now"
    Anything that matters gets checked before you act on it. Not because the model is bad at its job — because this is how the system works. The operator who skips verification is the weak link, not the model.

!!! danger "Knowledge Cutoff: All Three Cases Look the Same"
    A confident answer from a model with stale data and a confident answer from a model that searched the web are indistinguishable on the screen. Never let confidence stand in for a check on anything that could have changed since training.

??? note "Instructor Note — Eliciting Hallucinations on Demand"
    Make students produce a hallucination with their own hands. Reliable methods:

    - **Invented citations:** Ask for 5 peer-reviewed papers on a narrow topic with authors and years. Ask for a DOI — it will be invented.
    - **Biographical detail:** Ask for the detailed career history of a real but not-famous person. The model fills gaps with plausible detail.
    - **Recent events past cutoff:** Ask about something you know happened after the training cutoff.

    Pick a topic where you know the correct answer. Never demo on live operational content.

??? note "Instructor Note — Don't Let It Tip Into Cynicism"
    The point is calibrated trust, not distrust. The model is extraordinarily capable *and* it hallucinates. Both are true simultaneously. Bias-spotting is the same: name the skew, do not conclude the tool is useless.

### Hands-On

1. Ask the model for 5 peer-reviewed sources on a specific narrow topic. Ask for author names, journal names, and publication years.
2. Pick one citation and try to verify it exists.
3. Ask the same question in a new chat. Compare the answers.
4. Ask about something you know happened recently. Watch how it responds.
5. Ask the model to "describe a typical [role]" for two roles that carry common stereotypes. Note the defaults it reaches for — that is bias you can see.

!!! question "Before You Continue"
    You just watched the model invent a source. What does that mean for the next time it gives you a fact you have not heard before?

<div class="quiz-block">
  <p class="quiz-question">You run the same prompt twice in two separate chats and get different answers. What is the most accurate explanation?</p>
  <ul class="quiz-options">
    <li data-correct="false">One of the chats had a longer context window</li>
    <li data-correct="false">The model updated itself between the two runs</li>
    <li data-correct="true">The model uses randomness by design — the same input does not guarantee the same output</li>
    <li data-correct="false">You phrased the prompt slightly differently without noticing</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-block">
  <p class="quiz-question">You ask the model to "describe a typical software engineer" and it returns a narrow, stereotyped picture. As a matter of AI literacy, what is the right read?</p>
  <ul class="quiz-options">
    <li data-correct="false">The model is broken and should not be used</li>
    <li data-correct="false">The model has a personal opinion it is expressing</li>
    <li data-correct="true">The output reflects skewed patterns in its training data — recognize the skew and account for it</li>
    <li data-correct="false">The stereotype must be accurate because the model is usually right</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can name the five failure modes
- [ ] I have produced a hallucination with my own hands
- [ ] I understand that confidence and correctness are unrelated in model output
- [ ] I can spot when output is skewed or stereotype-shaped
- [ ] I know why this is the reason a human stays in the loop

---

## Verifying AI Output as a Method

**BLUF.** "Verify it" is not a vibe — it is five concrete techniques, and once you have them as drills, the mandated reflex becomes a skill you can actually execute under time pressure.

### Why This Matters

Every section so far ends with "verify before you act." That is correct, but on its own it is just an instruction to feel nervous. This section turns the reflex into method. When the model hands you a fact, a citation, or an analysis you cannot personally vouch for, you run one or more of these — and you know which one fits.

### Concepts

Five techniques. Reach for the one that fits the claim.

**1. Cite-and-check.** Ask the model to state its source for a claim, then go confirm the source actually says it. A model that invents the claim will often invent the source too — so the source has to be checked, not just requested. If it cannot produce a checkable source, treat the claim as unverified.

**2. Cross-source.** Confirm the claim against an independent, authoritative source you trust — not another AI, and not a source the first one handed you. Two AI tools agreeing is not corroboration if they trained on the same internet.

**3. Re-run for consistency.** Because the model is nondeterministic, run the same prompt two or three times (ideally in fresh chats). Claims that hold steady across runs are more likely grounded in training; claims that wobble run to run are a red flag to dig in.

**4. Second-tool check.** Take the same question to a genuinely different tool — a different model family, a search engine, a calculator, the actual document. The point is independence: a different system is unlikely to make the *same* mistake in the same place.

**5. Lateral reading.** Instead of going deeper into the single answer in front of you, open new tabs and read *about* the claim and its sources from the outside. This is how professional fact-checkers work: they leave the document to judge it, rather than staring harder at it.

!!! tip "Match the Technique to the Stakes"
    A throwaway brainstorm needs no verification. A name, number, date, citation, or claim that will go into a product gets at least one technique. A claim that will inform a decision gets cross-source plus a second-tool check. Scale the rigor to the consequence.

!!! warning "Two AIs Agreeing Is Not Verification"
    If you check a Claude answer by asking ChatGPT and they match, you have not verified anything — you have two pattern-matchers that read overlapping training data. Real cross-sourcing means an independent, authoritative source: the primary document, an official record, a subject-matter expert.

??? note "Instructor Note — Make Them Run the Drills"
    Verification only sticks as muscle memory. Have students run all five on one planted false claim in the same session so they feel which technique catches it. The lecture version does not transfer; the drill does.

### Hands-On

1. Ask the model a factual question whose answer you do not already know. Save the answer.
2. **Cite-and-check:** Ask it for the source. Go confirm the source exists and says what was claimed.
3. **Re-run:** Ask the identical question in two fresh chats. Did the answer hold steady or drift?
4. **Second-tool / cross-source:** Take the claim to a search engine or the primary document. Does it hold?
5. Write one sentence: which technique would you reach for first for the kind of work you actually do, and why?

!!! question "Before You Continue"
    The model gives you a specific statistic that will go into a brief your commander reads. Which of the five techniques do you run before that number leaves your hands — and why that one?

<div class="quiz-block">
  <p class="quiz-question">You want to verify a factual claim a model gave you. Which approach is genuinely independent corroboration?</p>
  <ul class="quiz-options">
    <li data-correct="false">Ask a second AI chatbot the same question and see if it agrees</li>
    <li data-correct="false">Ask the same model to confirm it is sure</li>
    <li data-correct="true">Check the claim against an authoritative primary source you trust</li>
    <li data-correct="false">Re-read the model's answer more carefully</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can name the five verification techniques
- [ ] I understand why two AIs agreeing is not corroboration
- [ ] I can scale verification rigor to the stakes of the output
- [ ] I have run at least one technique against a real claim with my own hands

---

## When to Use AI — and When Not To

**BLUF.** AI is the right tool for open-ended language work and the wrong tool for precise facts, live data, authoritative citation, and anything sensitive — and a one-page checklist keeps you from reaching for it on the jobs it is built to fail.

### Why This Matters

A capable tool used on the wrong job produces confident, fluent, wrong results — the most dangerous kind. Knowing the boundary is as important as knowing the capability. This is the decision you make *before* you type, not after the output disappoints you.

### Concepts

**What AI is good at.** Drafting and rewriting, summarizing long text, brainstorming options, explaining concepts, reformatting and restructuring, translating, generating a first pass you will then verify and own. Anything where the value is in the language and you remain the check on the facts.

**Where AI is the wrong tool — reach for something else:**

- **Precise math or calculation.** It predicts plausible numbers; it does not compute reliably. Use a calculator or spreadsheet. (Some tools can call a calculator behind the scenes — confirm it actually did, do not assume.)
- **Real-time or post-cutoff facts.** Prices, today's weather, current events, live status. Without a grounding tool it is guessing from stale data. (Grounding is Module 3 — and even then you verify the tool fired.)
- **Authoritative citation or the official record.** When the exact source, regulation, or wording is what matters, go to the source. The model can point you toward it; it cannot be it.
- **Anything sensitive or above the system's authorization ceiling.** This is not a "wrong tool" judgment call — it is a hard stop. See the data-handling rule below.

**The decision checklist — run it before you type:**

1. Is this open-ended language work, or does it need a precise/authoritative answer? (Precise → wrong tool.)
2. Does the answer depend on current or post-cutoff information? (Yes → wrong tool without verified grounding.)
3. Will I be able to verify the output before anyone relies on it? (No → do not use it for this.)
4. Is the content sensitive, controlled, or above this system's authorization ceiling? (Yes → hard stop, do not paste.)

If it clears all four, AI is a good fit — and you still verify what matters.

!!! danger "The Authorization Question Is a Hard Stop, Not a Tradeoff"
    Question 4 is not weighed against convenience. If the content is sensitive or above the system's ceiling, the answer is no regardless of how useful the tool would be. Full treatment is in "Data Handling" below and it does not expire.

!!! tip "Wrong-Tool Tell"
    If you find yourself about to trust the model on a number, a date, a citation, or a live fact, stop. Those are exactly the four cases it is built to get confidently wrong.

??? note "Instructor Note — This Is a Pre-Decision, Not a Post-Mortem"
    Students reach for AI reflexively and judge fit afterward. Drill the checklist as something they run *before* typing. The win is catching the wrong-tool case in advance, not regretting it after a bad output.

### Hands-On

1. List the last five things you used (or wanted to use) an AI tool for.
2. Run each one through the four-question checklist.
3. Flag any that were actually wrong-tool cases — precise math, live facts, authoritative citation, or sensitive content.
4. For one flagged case, write down what the *right* tool would have been.

!!! question "Before You Continue"
    A teammate is about to ask a chatbot to compute exact payroll figures from a personnel roster. Two separate things are wrong with that. Name both.

<div class="quiz-block">
  <p class="quiz-question">Which task is the LLM the WRONG tool for?</p>
  <ul class="quiz-options">
    <li data-correct="false">Drafting a first version of a memo you will edit and verify</li>
    <li data-correct="false">Rewriting a dense paragraph in plainer language</li>
    <li data-correct="true">Producing the exact current price of a commodity and treating it as authoritative</li>
    <li data-correct="false">Brainstorming a list of possible approaches to a problem</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can name the kinds of work AI is well-suited for
- [ ] I can name the four wrong-tool cases
- [ ] I can run the four-question checklist before reaching for AI
- [ ] I know the authorization question is a hard stop, not a tradeoff

---

## Data Handling: What Never to Paste

**BLUF.** Once you are pasting real work into a cloud-connected tool, what you paste matters — personal data, sensitive material, and anything above the system's authorization ceiling must never go in, and that rule does not expire.

### Why This Matters

Most AI delivery is cloud-based: your input leaves your machine and goes to a provider's server. This section establishes what that means for what you can send. The capability is real. The boundary is real. Both are true at the same time. This is the security spine of the whole course — what flows *in*. (What you do with the output, and whether a use is ethical or lawful, is Module 9.)

### Concepts

Authorization is a property of the system, not the impressiveness of the tool. A highly capable model running on an unauthorized system does not become authorized because it is impressive. The boundary is set by policy, not capability.

**What must never go into an unauthorized system:**

- Personally identifiable information (PII): names combined with identifiers, Social Security Numbers, DOBs, home addresses
- Sensitive, controlled, or classified material of any kind
- Anything above the system's authorization ceiling

**The default posture:** When in doubt, do not paste. Ask someone who can authorize it before you proceed.

**The classify-before-you-paste habit.** Before pasting anything into an AI tool, take two seconds: what is this, and is this system authorized for it? Build that pause until it is automatic.

!!! danger "This Bright Line Does Not Expire"
    It does not expire at the end of this course. It does not expire under time pressure. It does not move because the tool is impressive. One careless paste in an unauthorized system is the kind of mistake that has real and lasting consequences. The "paraphrase and summarize it first" loophole does not exist. Default to no until you hear yes from someone who can authorize it.

??? note "Instructor Note — Audience Calibration"
    For a military or intel audience, state this explicitly — including the "paraphrase and summarize" loophole, which does not exist. For a civilian audience, use concrete examples: medical records, financial data, HR files, client information.

??? note "Instructor Note — Do Not Soften This Module"
    Soften it and students hear "be careful sometimes." The message is: this is a hard rule.

### Hands-On

No prompting today. Do this instead:

1. Think about the last three things you pasted into an AI tool.
2. For each one: was the system authorized for that type of content?
3. Identify one category of content you work with regularly that you will never paste into an unauthorized tool.

Write that category down. It is your personal bright line.

!!! question "Before You Continue"
    You are under a deadline and want to paste a document into your AI tool to summarize it quickly. You are not sure whether the system is authorized for that content. What do you do?

<div class="quiz-block">
  <p class="quiz-question">You have a borderline-sensitive document and an unauthorized but highly capable AI tool that would save hours of work. What is the correct call?</p>
  <ul class="quiz-options">
    <li data-correct="false">Paste it — the efficiency gain justifies a judgment call</li>
    <li data-correct="false">Summarize the key points in your head first, then paste the summary</li>
    <li data-correct="true">Do not paste. Authorization does not change based on capability or time pressure. Ask before proceeding.</li>
    <li data-correct="false">Paste it, but delete the conversation immediately after</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can identify the categories that must never go into an unauthorized system
- [ ] I know the default posture: when in doubt, do not paste
- [ ] I understand that authorization is a property of the system, not the tool's capability
- [ ] I have identified my personal bright line for content I handle regularly

---

## Summary

| Concept | Core Idea | Why It Matters |
|---|---|---|
| **What an LLM Is** | Prediction from learned patterns — not rules, memory, or live data | Fluent output is not correct output. The only verb is "predicts." |
| **Tokens & Context (intro)** | Finite working memory measured in tokens | Long chats degrade as the window fills. Deep management is Module 8. |
| **Conversation Mechanics** | Stateless engine re-fed the whole transcript each turn | Explains "memory," no cross-chat recall, and edit vs. continue vs. new chat. |
| **How LLMs Fail** | Five modes: hallucination, confident-wrong, nondeterminism, cutoff, bias | All expected behavior. Verify anything that matters; spot the skew. |
| **Verifying Output** | Cite-and-check, cross-source, re-run, second-tool, lateral reading | Turns "verify it" from a feeling into five executable drills. |
| **When to Use AI** | Right for language work, wrong for precise/live/authoritative/sensitive | A four-question checklist run before you type, not after. |
| **Data Handling** | Authorization is a property of the system, not the tool | When in doubt, do not paste. The bright line does not expire. |

## End of Module

Know your weapon. You now have the mental model under the tool you were already using by feel: what it is, how a conversation actually works, where it breaks, how to verify it, when to reach for it, and what never goes in. Next steps:

1. Produce a hallucination with your own hands before moving on — if you have not yet, do it now.
2. Run all five verification techniques against one planted false claim in a single session.
3. Run your last five AI uses through the four-question "when to use it" checklist.
4. Write down your personal bright line for content you handle and keep it. It does not expire.
