# Ammunition Discipline: Tokens, Context & Cost

**Who this is for:** Someone who already knows what a token is (Module 1) and now needs to spend tokens like a professional — choosing the right model, managing a context window that fills silently, and keeping cost under control on real work.

**What you will leave with:** A model-selection rule a junior can apply on the spot, an operational understanding of how context fills (and how to stop it from degrading your work), the four habits that keep token cost down, and a clear picture of how AI is delivered and paid for.

---

## Spend, Don't Just Count: From Knowing a Token to Using One

**BLUF.** You already know what a token *is* from Module 1 — a chunk of text the model reads and writes, roughly three-quarters of an English word. This module is about how to *spend* tokens like a pro: every token costs money and time, and discipline with them is the difference between fast, cheap, defensible work and slow, expensive, sloppy work.

### Why This Matters

Module 1 gave you the mechanics: the model reads and writes in tokens, and a context window is a finite whiteboard. That was literacy. This is fieldcraft. Once you are commanding an agent that reads files, runs commands, and iterates, tokens are ammunition — and ammunition discipline is what keeps you effective when the mission runs long.

### Concepts

This whole module rests on one fact you already own from Module 1, so we do not re-teach it: **a token is the unit of text the model processes, roughly 0.75 of an English word; code is denser, so it costs more tokens per line.** That is the last time we define it. From here, everything is about *spending*.

Three things scale with the tokens you spend:

- **Cost.** Every input token and every output token costs money. Output tokens cost more than input tokens. Total cost = (input tokens x input price) + (output tokens x output price).
- **Speed.** More tokens means a slower response. Long prompts and long histories drag.
- **Accuracy.** Longer is not better. Verbose prompts add noise. A tight, well-structured prompt often beats a rambling one.

!!! note "The Mental Shift"
    In Module 1 you learned to *recognize* a token. Here you learn to *budget* it. The operator who treats tokens as free will blow through context, overpay, and iterate ten times. The operator who treats them as ammunition gets the same result in one disciplined pass.

??? note "Instructor Note — Do Not Re-Define the Token"
    Resist the urge to re-run the Module 1 token explanation. Students who hear "a token is roughly 0.75 words" twice tune out the new material. Open by *asserting* the prior knowledge ("you already know what a token is") and move immediately to spending it. If a student is shaky on the definition, route them back to Module 1, do not re-teach it here.

### Hands-On

1. Take a prompt you would normally send. Optionally paste it into a tokenizer (such as `platform.openai.com/tokenizer`) and note the token count next to the word count.
2. Now rewrite the same request as a structured prompt: task, context, constraint, output format. Count again.
3. Notice which version is *longer in the right way* — more structure, not more noise.

You are not learning what a token is. You are learning to feel its weight.

!!! question "Before You Continue"
    In Module 1 you watched a context window fill and degrade. Knowing that a token costs money and time, what does a sprawling 80-turn conversation cost you that a tight one does not?

<div class="quiz-block">
  <p class="quiz-question">This module deliberately does not re-define what a token is. Why?</p>
  <ul class="quiz-options">
    <li data-correct="false">Tokens are too complex to define in a prerequisite course</li>
    <li data-correct="true">You already learned the definition in Module 1 — this module is about spending tokens well, not defining them</li>
    <li data-correct="false">The definition changes with every model release</li>
    <li data-correct="false">Tokens only matter for agents, not chatbots</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can state, from Module 1, what a token is without re-reading it
- [ ] I understand that cost, speed, and accuracy all scale with tokens spent
- [ ] I know output tokens cost more than input tokens
- [ ] I treat tokens as ammunition, not as free

---

## The Model Landscape: Families, Tiers, and the Selection Rule

**BLUF.** Model families each offer a fast/cheap tier, a balanced tier, and a powerful/expensive tier — and the single most useful cost skill a junior can learn is matching the tier to the task instead of reaching for the biggest model every time.

### Why This Matters

The biggest lever on cost is not prompt length — it is which model you point at the job. Reaching for the most powerful model on every task is like running a diesel generator to charge a phone: expensive, slow, and unnecessary. A simple decision rule fixes most of it.

### Concepts

Three major families dominate current agentic work: **Claude** (Anthropic), **GPT** (OpenAI), and **Gemini** (Google). Each offers multiple tiers — a fast/cheap option, a powerful/expensive option, and one or two in between.

**Claude's tiers — the standard working toolchain:**

- **Haiku** — fast and cheap. Evaluation loops, simple formatting, high-volume tasks.
- **Sonnet** — balanced. The standard working model for most tasks.
- **Opus** — powerful and expensive. Reserve for the hardest reasoning.

!!! warning "Verify Before You Run"
    Model names, tiers, pricing, and context-window sizes change with every release. The *tier concept* is durable; the specific names and numbers are not. Verify current model IDs, prices, and context sizes at the provider's documentation (anthropic.com/pricing, docs.anthropic.com) before any course run. Every model name and number in this module carries this flag.

**The model-selection heuristic (apply this on the spot).** Sort the task into one of three buckets:

- **Fast / cheap tier** — the job is mechanical and low-judgment: summarize, reformat, classify, extract, run a tight evaluation loop. Pick the smallest tier that meets the quality bar.
- **Reasoning tier** — the job needs real analysis, planning, or multi-step logic: assess options, write or refactor non-trivial code, reason over a hard problem. Use the balanced or powerful tier.
- **Big-context tier** — the job needs a large body of material held at once: a long document, a sprawling codebase, a multi-source comparison. Choose the model whose context window comfortably fits the material, then verify the size before you rely on it.

!!! tip "The Decision Rule in One Line"
    Match the model to the task: mechanical work goes to the fast tier, hard thinking goes to the reasoning tier, and large material goes to the big-context tier. "Always use the biggest model" is the wrong instinct — it is expensive, slower, and usually unnecessary.

??? note "Instructor Note — Name Drift Is Real"
    The specific tier names (Haiku/Sonnet/Opus) will drift, and competitor names will change too. Teach the *shape* — fast, balanced, powerful — and make bookmarking the provider docs part of the job. Do not let students memorize current model IDs as if they were permanent.

### Hands-On

1. Go to the provider's model page (e.g., anthropic.com/claude) and find the current tiers. Note the current names for fast, balanced, and powerful. Do they match what this section lists?
2. Pick three tasks you might actually do: a format conversion, a complex analysis, and a long-document read.
3. Assign each to a tier using the heuristic, and write one sentence per task explaining why.

Name drift is real. Bookmarking the docs is part of the discipline.

!!! question "Before You Continue"
    You have a high-volume task: classify 2,000 short messages as urgent or routine. The work is simple but there is a lot of it. Which tier, and why is reaching for the most powerful model the wrong call here?

<div class="quiz-block">
  <p class="quiz-question">You need to convert 500 records from one format to another — mechanical, no judgment, but high volume. Which tier fits?</p>
  <ul class="quiz-options">
    <li data-correct="false">The most powerful tier — accuracy matters at volume</li>
    <li data-correct="true">The fast/cheap tier — the task is mechanical, so use the smallest tier that meets the quality bar</li>
    <li data-correct="false">The big-context tier — there are a lot of records</li>
    <li data-correct="false">It does not matter which tier you choose</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-block">
  <p class="quiz-question">Why is "always use the most powerful model" bad advice?</p>
  <ul class="quiz-options">
    <li data-correct="false">Powerful models make more mistakes than smaller ones</li>
    <li data-correct="false">Powerful models are slower and less reliable</li>
    <li data-correct="true">Larger models cost more per token — for simple tasks the cost is not justified by the capability difference</li>
    <li data-correct="false">You can only access powerful models through a paid subscription</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can name the three tiers in a model family: fast, balanced, powerful
- [ ] I can apply the fast / reasoning / big-context heuristic to a real task
- [ ] I know that model names, tiers, pricing, and context sizes must be verified before use
- [ ] I understand why the biggest model is the wrong default

---

## Context Windows, Operationally: The Window That Fills Silently

**BLUF.** You know from Module 1 that a context window is finite working memory; the operational reality is that in an agentic session it fills *silently* — every tool result accumulates — and your job is to manage what is in it through smart sampling, not to cram everything in.

### Why This Matters

Module 1 showed you a long chat degrade. In agentic work the same thing happens faster and more quietly, because the agent is reading files and running commands, and every result lands back in the window. By the time the model starts contradicting itself, you are already deep in a session. Managing context is an operator skill.

### Concepts

You already know the shape from Module 1: a finite whiteboard, and once it fills, old content gets crowded out. Here is what changes when an agent is doing the work.

**The three operational rules:**

1. **Context is not infinite.** A multi-day conversation, long documents, and verbose reasoning add up fast against the window.
2. **Tool results accumulate.** The filesystem operation itself does not consume context — but every tool *result* returns into the running window and stays. A long session that reads many files or runs many commands can fill the window through tool-result accumulation, not just conversation.
3. **You control what is in context.** You decide which documents to include, how verbose to be, how much history to keep. Strategic use of context is a skill, not an accident.

!!! warning "Context Fills Silently"
    Most operators do not notice the window filling until it causes a problem — the model starts contradicting itself, missing earlier instructions, or degrading in quality. By then you are already deep in. Watch for the signals and start a fresh session *proactively*.

**Smart sampling beats cramming.** The fix for nearly every context problem is the same: do not pour everything in. Let the agent *sample* what it needs.

- **Single conversation getting long?** Start fresh, paste only the relevant context, or have the agent read from files instead of carrying everything in history.
- **System prompt bloated?** Keep it concise. Rely on files (`CLAUDE.md`, `me.md`) the agent reads on demand rather than stuffing everything into every request.
- **File-heavy work?** Do not ask the agent to "read the whole codebase." Have it use `find`/`grep` to locate the relevant 10–20 files, then read only those.

!!! note "Why the Agent Doesn't Drown in a Big Codebase"
    When an agent calls a tool, it gets fresh information at each step: it reads what it needs, reasons, acts, and reads again. It does not hold the entire codebase in context at once. That is *why* an agent can work on large projects — it is designed around the window limit. The operator's job is to keep it sampling, not dumping.

!!! warning "Bigger Is Not Always Better"
    A model with a very large context window still attends better to the beginning and end than to the middle. Filling a huge window with everything does not improve results — critical instructions buried in the middle can be partially ignored. (Context-window sizes are version-sensitive — verify current numbers before teaching.)

### Hands-On

1. In Claude Code (or any agent), start a session and ask it to find and read only the files relevant to a specific question, using search rather than reading everything. Watch it sample.
2. Run a longer session with several file reads and commands. Then ask it to summarize what it has done so far. Check the accuracy — that is the window under pressure.
3. Notice the first sign of drift (a contradiction, a forgotten constraint). That is your cue to start fresh.

!!! question "Before You Continue"
    You are two hours into an agent session: 30 files read, 15 commands run, a long back-and-forth. The agent starts contradicting what it said an hour ago. What filled the window — and what do you do?

<div class="quiz-block">
  <p class="quiz-question">Which statement about tool calls and the context window is correct?</p>
  <ul class="quiz-options">
    <li data-correct="false">Tool calls reset the context window, giving you more space</li>
    <li data-correct="false">Tool execution consumes the most context tokens of any operation</li>
    <li data-correct="true">Tool-call results return into the context window and accumulate over the session</li>
    <li data-correct="false">Context windows only fill from conversation text, not tool results</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can state the three operational context rules
- [ ] I understand that tool results accumulate and fill the window silently
- [ ] I can name the smart-sampling fix for long chats, bloated prompts, and file-heavy work
- [ ] I know the signs of a full window and that I should start fresh proactively

---

## Ammunition Discipline: The Habits That Keep Cost Down

**BLUF.** Cost-consciousness is not penny-pinching — it is the operator habit of getting the result in one disciplined pass instead of ten loose ones, and it comes down to four principles and a short list of behaviors a junior can run today.

### Why This Matters

Developing with AI is not free. Each token costs money, each tool call takes time, and at scale — across a team, across months — it adds up. The waste rarely hides in a single big prompt. It hides in *iteration*: ten vague passes where one clear pass would do.

### Concepts

**The three cost dimensions:**

- **Token cost.** Every input token costs; every output token costs more. A 10,000-token conversation costs a fraction of a 100,000-token one.
- **Time cost.** Longer conversations and more tool calls take longer. Waiting is dead time.
- **Iteration cost.** Ten passes to get it right is 10x the tokens. Clear the first time is 1x.

**Four principles:**

1. **Concision is a feature.** A tight, well-structured prompt often beats a long one — less noise, faster thinking, lower cost.
2. **Repetition is waste.** Asking the same thing three times is 3x the tokens. Iterate once, deliberately.
3. **Cheap vs. expensive operations matter.** A tool call that reads a file returns a small result. Pasting a 30,000-token file into the prompt costs 30,000 input tokens *plus* the reasoning cost.
4. **Plan before you prompt.** Decide what context the agent needs, what it should read via tools instead of you pasting, and how many iterations you expect — then prompt once, strategically.

!!! tip "Use Tools Instead of Pasting"
    Bad: paste a 50,000-token codebase and ask for a refactor — 50,000 input tokens and a partial result. Good: "There's a bug in the auth module. Read `/src/auth/login.js` and identify it." The agent reads only what it needs (~5,000 tokens) and gives you a focused answer.

!!! warning "Iteration Is Where Cost Hides"
    A vague 80-token prompt that needs five clarifying rounds costs far more than a structured 120-token prompt that lands the first time. Longer in the *right* way is cheaper than short and vague. One clear prompt beats five loose ones every time.

**A few more cost-conscious behaviors:**

- **Iterate tightly, not loosely.** Review immediately and correct in the same session — tight loops keep context warm and avoid re-reads.
- **Know when to ask the agent vs. solve it yourself.** Use the agent for architecture, complex logic, and unfamiliar code. Use a quick search for syntax lookups and trivial API usage.
- **Plan before you build.** Five minutes of "here is my plan, any red flags?" often saves fifty minutes of iteration.

??? note "Instructor Note — Frame It as Discipline, Not Stinginess"
    The point is not to spend as few tokens as possible — it is to get a defensible result efficiently. Tie it back to the operator posture from Module 7: a clear brief is cost-conscious *and* good supervision. The two habits reinforce each other.

### Hands-On

1. Take a prompt you would normally send. Apply the four principles: cut repetition, add structure, narrow scope, specify output format.
2. Count words before and after. Is the revised version clearer *and* tighter?
3. Submit the revised prompt. Did you get a usable first response, or still need follow-ups?
4. For one task this week, decide up front: what should the agent read via tools instead of you pasting?

!!! question "Before You Continue"
    You need to debug a slow API endpoint. You have the source file, the database schema, and the server logs. What is the most cost-efficient way to give the agent what it needs — and what would the expensive version look like?

<div class="quiz-block">
  <p class="quiz-question">Which behavior is the most cost-conscious?</p>
  <ul class="quiz-options">
    <li data-correct="false">Always use the most capable model for every task</li>
    <li data-correct="false">Paste full documents into the prompt so the agent has complete context</li>
    <li data-correct="true">Ask the agent to read specific files via tools rather than pasting large documents</li>
    <li data-correct="false">Repeat key instructions several times so the agent doesn't forget them</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can name the three cost dimensions: token, time, iteration
- [ ] I can apply the four cost principles to a real prompt
- [ ] I know that tools beat pasting for large material
- [ ] I understand that iteration is where most cost hides

---

## How AI Is Delivered and Paid For

**BLUF.** The same model reaches you through different doors — a flat-rate app, a pay-per-token API, or your organization's managed key — and whether it runs in the cloud or on your machine changes both the cost and what you are allowed to send it.

### Why This Matters

You will be selecting models and deciding how to use them. Understanding the delivery and billing model behind the tool prevents both waste and surprise — and connects directly to the data-handling boundary you learned in Module 1.

### Concepts

**Three ways AI is paid for:**

| Delivery model | What it means | Example |
|---|---|---|
| **Subscription app** | Flat monthly fee, model access included | ChatGPT Plus, Claude.ai Pro |
| **Pay-per-token API** | You pay per token sent and received | Anthropic API, OpenAI API |
| **Bring-your-own-key** | Your organization's API key foots the bill | Enterprise deployments, Claude Code |

**Cloud vs. local delivery.** Most models run in the cloud — your input goes to a remote server, the model runs there, the response comes back. Some smaller models run entirely on your machine: no connectivity required, data stays local. The trade-off is capability — local models are smaller and less capable than cloud frontier models.

**The cost ladder.** Token cost scales with model size and reasoning effort. A small, fast tier costs less per token than a large frontier tier. This is the same ladder the model-selection heuristic walks — match the model to the job and you are also matching the cost to the job.

!!! warning "Cost Is Real on Pay-Per-Token"
    On a pay-per-token plan, a long conversation with a large model costs more than a short one with a small model. Know your billing model *before* you start a long task. On a flat-rate app the marginal cost is hidden, but on an API or a managed key it is real and it accrues.

!!! danger "Delivery Connects to Data Handling"
    Cloud delivery means your input leaves your machine. That is exactly why the Module 1 data-handling rule exists: authorization is a property of the *system*, not the impressiveness of the model. A capable model on an unauthorized cloud system does not become authorized because it is capable. This is a one-line reminder, not a re-teach — the full rule lives in Module 1 and the ethics treatment is Module 9.

??? note "Instructor Note — Skip the Pricing Tables"
    Specific token prices change every quarter. Do not teach current numbers — teach the structure: tokens cost money, bigger models cost more, cloud sends your data off-machine, match the model and the delivery to the job. (All specific prices and tiers carry the verify-before-teaching flag.)

### Hands-On

1. Open your chatbot's settings or account page. Find which model you are currently using and note the name.
2. Open the provider's pricing page. Find one fast/small and one large/powerful model and read the price difference. Notice the *structure*, do not memorize numbers.
3. Identify which delivery model you are on: subscription app, pay-per-token API, or organization-managed key.
4. Pick one task you might do this week. Decide which tier *and* which delivery model fit, and write one sentence explaining why.

!!! question "Before You Continue"
    You need to run an analysis on a very long document with several back-and-forth exchanges, on a pay-per-token plan. What factors determine the cost of that task, and how would you reduce it?

<div class="quiz-block">
  <p class="quiz-question">Why does cloud delivery connect directly to data handling?</p>
  <ul class="quiz-options">
    <li data-correct="false">Cloud models are less accurate, so output must be checked</li>
    <li data-correct="true">Cloud delivery sends your input off your machine to a remote server — so authorization of the system, not the model's capability, governs what you may send</li>
    <li data-correct="false">Local models are always authorized for any content</li>
    <li data-correct="false">Cloud delivery is free, so there is no reason not to use it</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can name the three ways AI is paid for
- [ ] I know the difference between cloud and local delivery and the trade-off
- [ ] I can identify which delivery model I am currently using
- [ ] I understand that cloud delivery is why the data-handling boundary matters (full rule in Module 1)

---

## Summary

| Concept | Core Idea | Why It Matters |
|---|---|---|
| **Spending Tokens** | You know what a token is — now budget it | Cost, speed, and accuracy all scale with tokens spent. |
| **Model Tiers** | Fast, balanced, powerful in every family | Matching tier to task is the biggest lever on cost. |
| **Selection Heuristic** | Fast / reasoning / big-context buckets | A junior can pick the right model on the spot. |
| **Context, Operationally** | The window fills silently as tool results accumulate | Smart sampling beats cramming; start fresh proactively. |
| **Cost Discipline** | Four principles, tight iteration | Iteration is where cost hides — one clear pass beats ten. |
| **Delivery & Payment** | App, API, or managed key; cloud vs. local | Billing affects cost; cloud delivery governs what you may send. |

!!! warning "Verify Before Delivery"
    Every model name, tier, price, and context-window size in this module is version-sensitive and changes with releases. Verify all of them at the provider's documentation before any course run. The concepts are durable; the numbers are not.

---

## End of Module

You can now spend tokens like a professional: pick the right tier with a heuristic a junior can apply, keep a silently-filling context window under control with smart sampling, run the four cost-discipline habits, and read the delivery door you are working through.

This closes the loop opened in Module 1: you learned what a token *is* there, and you learned how to *spend* it here. Carry the ammunition-discipline mindset into every session — the operator who wastes tokens is slower and more expensive than the one who does not, and both are doing the same work.
