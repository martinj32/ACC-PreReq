# Bedrock — AI Literacy

**Who this is for:** Someone who uses AI by feel and wants to understand what is actually happening. No prior technical knowledge required.

**What you will leave with:** A working mental model of how LLMs work, where they fail, how to prompt deliberately, how AI is delivered and paid for, and what you must never send to an AI tool.

---

## What an LLM Actually Is

**BLUF.** An LLM predicts text from learned patterns — not rules, not memory, not live data — and that single fact explains both why it is extraordinarily capable and exactly how it fails.

### Why This Matters

You already use one. What you have been doing by feel — type a request, read a response — is about to get a mental model underneath it. That model will not slow you down. It will make everything that follows click immediately instead of slowly.

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

??? note "Instructor Note — Architecture Questions"
    Do not open with attention heads, transformers, or parameter counts. A casual user needs a mental model that survives contact with a real tool, not the mechanism behind it. If a student asks, acknowledge it as a real question and defer: "That is a deeper topic — let's come back to it."

??? note "Instructor Note — Anthropomorphism Runs Deep"
    Students told "it just predicts" will still say "it knew the answer" thirty seconds later. Anthropomorphism is a wired cognitive shortcut. Interrupt it every time it appears in the first two weeks. It re-trains faster than you expect.

### Hands-On

The lab is the chatbot you already have open.

1. Ask it something you already know well enough to spot an error.
2. Read the output. Ask yourself: "How would I verify this?"
3. Ask it to continue a sentence you leave unfinished.

You are watching prediction happen in real time.

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

## Tokens and Context

**BLUF.** The model reads and writes in tokens — roughly 0.75 of an English word each — and can only hold a fixed number at once; fill that limit and earlier content starts to fall out, which is why long sprawling chats get worse, not better.

### Why This Matters

This is the first place the engine's behavior surprises people. They expect a longer conversation to give the model more to work with. The opposite happens once you pass the limit. Knowing why changes how you work.

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
    Approximate sizes as of mid-2026 — verify before teaching, these change with releases: Claude: 200,000 tokens. GPT-4o: 128,000 tokens. Gemini 2.0: 1,000,000+ tokens. Bigger is not always better — a full million-token window degrades quality in the middle.

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

## How LLMs Fail

**BLUF.** The model will state false things with total confidence, give different answers to the same question, and know nothing past its training cutoff — none of this is a malfunction, and seeing it fail on purpose is the most important thing you can do in this section.

### Why This Matters

You are about to trust this tool with real work. Calibrated trust requires knowing exactly where it breaks. Read this module and then produce a hallucination with your own hands before moving on.

### Concepts

Four failure modes. Know all four.

**Hallucination.** The model has no truth-checking step. It generates tokens that are statistically likely to follow prior context. It cannot distinguish "information I was trained on accurately" from "information I am completing plausibly." Confident output and correct output are entirely unrelated. This is expected behavior of the system, not a rare bug.

**Confident-wrong.** Hallucination is not always dramatic. The model may state a subtly wrong date, a slightly wrong statistic, or a plausible-sounding citation that does not exist. The tone stays equally confident whether the claim is right or wrong. Never use the model's confidence as a signal of accuracy.

**Nondeterminism.** The model uses a temperature parameter that introduces variation. Same prompt, different run, different result — by design. Do not treat one output as "the answer" for high-stakes work. Run important prompts more than once and compare.

**Knowledge cutoff.** The model was trained on data up to a point in time. It does not know what happened after that. Ask about a recent event and it may refuse, guess, or confidently describe something that did not happen.

!!! warning "Build the Verification Reflex Now"
    Anything that matters gets checked before you act on it. Not because the model is bad at its job — because this is how the system works. The operator who skips verification is the weak link, not the model.

??? note "Instructor Note — Eliciting Hallucinations on Demand"
    Make students produce a hallucination with their own hands. Reliable methods:

    - **Invented citations:** Ask for 5 peer-reviewed papers on a narrow topic with authors and publication years. The model produces plausible-sounding but fabricated citations. Ask for a DOI — it will be invented.
    - **Biographical detail:** Ask for the detailed career history of a real but not-famous person. The model fills gaps with plausible-sounding detail.
    - **Recent events past cutoff:** Ask about something you know happened after the training cutoff.

    Pick a topic where you know the correct answer. Never demo on live operational content.

??? note "Instructor Note — Don't Let It Tip Into Cynicism"
    The point is calibrated trust, not distrust. The model is extraordinarily capable *and* it hallucinates. Both are true simultaneously.

### Hands-On

1. Ask the model for 5 peer-reviewed sources on a specific narrow topic. Ask for author names, journal names, and publication years.
2. Pick one citation and try to verify it exists.
3. Ask the same question in a new chat. Compare the answers.
4. Ask about something you know happened recently. Watch how it responds.

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

### Readiness Check

- [ ] I can name the four core failure modes
- [ ] I have produced a hallucination with my own hands
- [ ] I understand that confidence and correctness are unrelated in model output
- [ ] I know why this is the reason a human stays in the loop

---

## Prompt Engineering

**BLUF.** Converting prompting-by-feel into method means telling the model who to be, giving it the context it needs, showing it an example, and saying what good output looks like — the same as briefing a person, not typing into a search box.

### Why This Matters

A vague prompt is a vague order, and a vague order gets a vague result from a junior who fills the gaps with assumptions. You have already seen what the model does when it guesses wrong. Deliberate prompting is how you reduce that surface area.

### Concepts

The model meets you halfway the moment you give it structure. Without context, it must guess: who you are, what you need, what "good" looks like. Guessing produces generic output. Four elements close that gap:

- **Role.** Tell the model who to be. "You are a plain-language editor" produces different output than no framing at all.
- **Context.** Tell it what it needs to know that it cannot infer. What is the task, who is the audience, what constraints apply.
- **Example.** Show it what good output looks like before asking for it. One strong example beats three paragraphs of description.
- **Output spec.** Tell it the format, length, and tone you want.

!!! example "Before and After"
    **Weak prompt:** "Write me a summary."

    **Strong prompt:** "You are summarizing this for a senior leader who has two minutes. Pull out the three most important points. Use bullet points. No jargon. Max 100 words."

    Same model. Different brief. Different result.

The iterative habit matters more than the perfect prompt. A rough ask the model can build on beats silence. Read the output, tighten the next ask based on what missed, repeat.

!!! tip "If You Are Stuck, Ask the Model to Interview You"
    Type: "I need help with [task]. Ask me the questions you need answered before you start."

    The model surfaces what context it is missing. Answer the questions, then ask it to proceed.

!!! warning "The Template Trap"
    The four elements are a structure, not a script to recite. The durable skill is clarity — giving the model what it needs to not guess. How you deliver that varies by task.

??? note "Instructor Note — Prompt Engineering Creep"
    Resist turning this into a "prompt engineering tricks" hour. Magic phrases are not the lesson. The lesson is clarity. Students who focus on tricks over structure will hit a ceiling fast.

### Hands-On

1. Pick a real task you need help with.
2. Write a one-line version of the request. Submit it. Save the output.
3. Add role, context, an example of what good looks like, and an output spec. Submit again.
4. Compare the two outputs side by side.

!!! question "Before You Continue"
    What specifically changed between your first output and your second? Which of the four elements made the biggest difference for your task?

<div class="quiz-block">
  <p class="quiz-question">You ask the model to "write a report." It produces something generic and too long. What is the most effective fix?</p>
  <ul class="quiz-options">
    <li data-correct="false">Switch to a more powerful model</li>
    <li data-correct="false">Ask the same question again and hope for a better result</li>
    <li data-correct="true">Add role, context, an example of good output, and a length/format spec to the prompt</li>
    <li data-correct="false">Break the report into smaller pieces and ask for each separately</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can name the four elements of a deliberate prompt
- [ ] I have run a before/after comparison with my own real task
- [ ] I treat prompting as a conversation, not a one-shot command
- [ ] I know the difference between prompting by feel and prompting by structure

---

## How AI Is Delivered and Paid For

**BLUF.** The same model reaches you through different doors — flat-rate app, pay-per-token API, or your organization's cloud account — and tokens cost money, so model choice and conversation length have a price.

### Why This Matters

You will be selecting models and making decisions about how to use them. Understanding the cost and delivery model behind the tool prevents both waste and surprise.

### Concepts

**Three ways AI is paid for:**

| Delivery model | What it means | Example |
|---|---|---|
| **Subscription app** | Flat monthly fee, model access included | ChatGPT Plus, Claude.ai Pro |
| **Pay-per-token API** | You pay per token sent and received | Anthropic API, OpenAI API |
| **Bring-your-own-key** | Your organization's API key foots the bill | Enterprise deployments, Claude Code |

**Cloud vs. local delivery.** Most models run in the cloud — your input goes to a remote server, the model runs there, the response comes back. Some smaller models can run entirely on your machine. Local delivery: no connectivity required, data stays local. Trade-off: local models are smaller and less capable.

**The cost ladder.** Token cost scales with model size and reasoning effort. A small, fast model costs less per token than a large frontier model. "Always use the biggest model" is wrong — match the model to the job.

!!! tip "Match the Model to the Job"
    Drafting a quick message: small, fast model. Analyzing a complex document: larger model. Writing and running code in an agentic environment: frontier model with tool use. Using the biggest model for everything is like running a diesel generator to charge a phone.

!!! warning "Cost Is Real"
    On a pay-per-token plan, a long conversation with a large model costs more than a short one. Know your billing model before you start a long task.

??? note "Instructor Note — Skip the Pricing Tables"
    Specific token prices change frequently. Do not teach current prices — they will be wrong within a quarter. Teach the structure: tokens cost money, bigger models cost more, match the model to the job.

### Hands-On

1. Open your chatbot's settings or account page. Find which model you are using.
2. If you have API access, open the pricing page. Read it for structure — not memorization.
3. Identify which delivery model you are currently on.

!!! question "Before You Continue"
    You need to run an analysis task with a very long document and several back-and-forth exchanges. What factors determine the cost of that task, and how would you reduce it?

<div class="quiz-block">
  <p class="quiz-question">Why is "always use the most powerful model" not good advice?</p>
  <ul class="quiz-options">
    <li data-correct="false">Powerful models make more mistakes than smaller ones</li>
    <li data-correct="false">Powerful models are slower and less reliable</li>
    <li data-correct="true">Larger models cost more per token — for simple tasks, the cost is not justified by the capability difference</li>
    <li data-correct="false">You can only access the most powerful models through a paid subscription</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can name the three ways AI is paid for
- [ ] I understand that tokens cost money and model choice affects cost
- [ ] I know the difference between cloud and local delivery
- [ ] I can identify which delivery model I am currently using

---

## Data Handling: What Never to Paste

**BLUF.** Once you are pasting real work into a cloud-connected tool, what you paste matters — personal data, sensitive material, and anything above the system's authorization ceiling must never go in, and that rule does not expire.

### Why This Matters

The previous module established that most AI delivery is cloud-based. This module establishes what that means for what you can send. The capability is real. The boundary is real. Both are true at the same time.

### Concepts

Authorization is a property of the system, not the impressiveness of the tool. A highly capable model running on an unauthorized system does not become authorized because it is impressive. The boundary is set by policy, not capability.

**What must never go into an unauthorized system:**

- Personally identifiable information (PII): names combined with identifiers, Social Security Numbers, DOBs, home addresses
- Sensitive, controlled, or classified material of any kind
- Anything above the system's authorization ceiling

**The default posture:** When in doubt, do not paste. Ask someone who can authorize it before you proceed.

**The classify-before-you-paste habit.** Before pasting anything into an AI tool, take two seconds: what is this, and is this system authorized for it? Build that pause until it is automatic.

!!! danger "This Bright Line Does Not Expire"
    It does not expire at the end of this course. It does not expire under time pressure. It does not move because the tool is impressive. One careless paste in an unauthorized system is the kind of mistake that has real and lasting consequences. Default to no until you hear yes from someone who can authorize it.

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
