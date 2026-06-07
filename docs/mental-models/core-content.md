# Mental Models for AI-Assisted Development

**BLUF.** Six mental models separate operators who use AI effectively from those who waste tokens, break things, and overpay. This module covers all six.

---

## Overview

These are not technical skills. They are conceptual frameworks -- how you think about AI, tools, and the operator's role. The course assumes you have internalized them before you touch a terminal.

**Duration:** 35 minutes (self-contained)

**Learning Objectives:**
- Understand the "harness": an LLM becomes agentic when paired with tools
- Grasp why context windows matter and when they become a constraint
- Treat tokens as a resource with real cost
- Understand what tool calls are and why they enable verification
- Adopt active supervision as your default posture
- Build cost-consciousness as a core habit

!!! note "Why This Matters"
    This course is not about "how to use Claude." It assumes you understand how LLMs, tools, and operators work together. Without these models, you'll blow through context windows, miss verification steps, and submit AI output you cannot defend. With them, you move fast and confidently.

---

## Section 1: The Harness Mental Model

### What is the Harness?

An LLM by itself is a text-in, text-out system. It cannot:
- Read files
- Write to disk
- Run commands
- Call APIs
- Know what time it is
- Verify its own outputs

The **harness** is what makes an LLM into an agent. It gives the LLM:
- **Eyes:** tools to read files, check git status, fetch URLs, query databases
- **Hands:** tools to write files, create directories, modify code, run tests
- **Body:** tools to execute commands, call APIs, move files, deploy code

### The Engine-Harness-Operator Stack

!!! note "Working Vocabulary"
    This course uses the **engine-harness-operator** model:

    - **Engine** -- the LLM. The reasoning brain. Generates, plans, decides.
    - **Harness** -- the tool layer. Gives the engine access to files, commands, and external systems.
    - **Operator** -- you. Directs the mission, approves consequential actions, carries accountability for the result.

    The engine cannot act without a harness. The harness cannot direct without an operator. All three are required.

    External resources may use different terms -- Anthropic's documentation uses "model + tools + orchestration layer." Same concepts, different labels.

### The Simple Formula

```
LLM (knowledge, reasoning, generation) + Tools (sensors + actuators) = Agency
```

**Without tools:** Claude can write code, but can't run it or read your actual file system.

**With tools:** Claude can read your code, run tests, modify files, commit to git, and iterate based on results. It becomes a genuine collaborator.

### Your Job in the Harness

When you invoke Claude with tools enabled, you're building a feedback loop. Claude sees the world (via tools), takes action (via tools), observes the result, and adjusts. That's the harness. That's what makes it agentic.

!!! warning "Don't Step Away"
    Your job is not to give the LLM a task and wait. You are not a spectator.

    1. Set up the right tools (permissions)
    2. Give clear instructions
    3. Supervise the feedback loop
    4. Interrupt if it goes wrong

!!! question "Before You Continue"
    You give Claude a mission: search 200 field reports for grid 38SMB4521 and return every matching excerpt.

    Without a harness, Claude cannot read the files. It can only generate plausible-sounding excerpts from memory -- and you have no way to know which it did.

    With a harness, Claude calls tools against the actual files and returns real results you can trace.

    What does that difference mean for how you verify the output?

<div class="quiz-block">
  <p class="quiz-question">In the engine-harness-operator model, what is the harness?</p>
  <ul class="quiz-options">
    <li data-correct="false">The LLM -- the reasoning brain that generates responses</li>
    <li data-correct="true">The tool layer that gives the LLM access to files, commands, and external systems</li>
    <li data-correct="false">The human operator who directs the mission</li>
    <li data-correct="false">The API endpoint Claude connects to</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Hands-On

1. Open your AI chatbot. Ask it: "Rename the folder 'project' to 'project-v1'." Read the response.
2. Identify: did it rename the folder, or tell you how? That gap is the harness.
3. If you have Claude Code available, ask it the same thing in a project folder. Compare what happens.

You are seeing the difference between a text engine and an agent.

---

## Section 1.5: The Model Landscape -- Families and Tiers

Three major model families dominate current agentic work: Claude (Anthropic), GPT (OpenAI), Gemini (Google). Each family offers multiple tiers -- a fast/cheap option and a slow/powerful option, with one or two in between.

**Claude's tiers (the standard working toolchain):**
- **Haiku** -- fast and cheap. Good for evaluation loops, simple formatting, high-volume tasks.
- **Sonnet** -- balanced. The standard working model.
- **Opus** -- powerful and expensive. Reserve for the hardest reasoning tasks.

!!! tip "The Decision Rule"
    Match the model to the task. Summarization or format conversion: use a fast tier. Complex analysis or planning: use a capable tier. Tight loops: use the cheapest tier that meets quality requirements.

    "Always use the biggest model" is the wrong instinct -- expensive, slower, and often unnecessary.

!!! warning "Verify Before You Run"
    Model names and pricing change with new releases. Verify current model IDs and costs at anthropic.com before any course run. The tier concept is durable; the specific names are not.

### Hands-On

1. Go to anthropic.com/claude and find the current model tiers.
2. Note the current names for fast, balanced, and powerful models. Do they match what this section lists?
3. Pick one task you might do with AI (summarize a document, write code, analyze options). Decide which tier is appropriate and write one sentence explaining why.

Name drift is real. Bookmarking the docs is part of the job.

---

## Section 1.6: How the Model Fails (And Why That Matters)

### Hallucination -- the Mechanism, Not Just the Label

The model generates tokens that are statistically likely to follow prior context. It has no separate truth-checking step. It cannot distinguish between "information I trained on accurately" and "information I'm completing plausibly because it pattern-matches."

!!! warning "Confident Does Not Mean Correct"
    The result is fluent, confident output that is factually wrong. Not a rare edge case -- a consistent property of how the system works.

    Treat confident output as a starting point for verification, not a conclusion.

### Knowledge Cutoff -- Three Behaviors

The model has no reliable information about events after its training cutoff. But it does not handle this uniformly:

1. The model flags the gap ("My knowledge cutoff is [date], I cannot confirm this")
2. The model answers confidently using stale training data with no indication it may be wrong -- the dangerous one
3. The model has a retrieval tool (web search) and can fetch current information

!!! warning "All Three Look Identical From the Outside"
    Confident answers from cases 1, 2, and 3 are indistinguishable without checking. Verify anything time-sensitive regardless of how the model presents it.

### Nondeterminism

The model uses a sampling parameter (temperature) that introduces randomness. The same prompt on two separate runs produces different outputs -- sometimes slightly, sometimes significantly.

!!! tip "Run Important Prompts More Than Once"
    Do not treat a single output as definitive for high-stakes work. Run important prompts multiple times and compare for consistency. Inconsistency is a signal to verify more carefully.

### Doctrinal Framing

The model is the sharp junior analyst who never says "I don't know." Confident, fluent, and occasionally making it up entirely. You check the work -- not because you expect failure, but because fluency is not evidence of accuracy.

!!! question "Before You Continue"
    You receive an intelligence summary from Claude that includes three specific claims about adversary activity. Claude presents all three confidently. You have no way to tell whether they came from source documents Claude read, or from training data pattern-matching.

    What do you do before you include this summary in a product?

<div class="quiz-block">
  <p class="quiz-question">Which of the following best describes why LLMs hallucinate?</p>
  <ul class="quiz-options">
    <li data-correct="false">The model has bugs in its code that cause incorrect outputs</li>
    <li data-correct="false">The model is intentionally generating false information</li>
    <li data-correct="true">The model generates statistically likely tokens with no separate truth-checking step</li>
    <li data-correct="false">The model's training data was corrupted</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Hands-On

1. Ask Claude (web or Code): "What is the current price per million tokens for Claude Sonnet?" Read the answer.
2. Go to anthropic.com/pricing and compare. Are they the same?
3. Ask Claude: "When is your knowledge cutoff?" Note whether it flags any uncertainty.
4. Ask a follow-up: "What major Claude models were released after your cutoff?" Observe how it handles the gap.

You have just demonstrated all three failure modes — hallucination risk, knowledge cutoff, and stale data — in a single exercise.

---

## Section 2: Context Windows

### What is a Context Window?

A context window is the amount of text (measured in tokens) that an LLM can "see" at one time. Think of it as the LLM's working memory.

**Current Claude models:** 200,000 tokens. A typical page of text is ~300-500 tokens. A 50-page document is roughly 15,000-25,000 tokens.

!!! note "Check the Docs"
    Model specs change with new releases. Verify current context window sizes at docs.anthropic.com before any course run. The 200k figure applies across the current Claude generation.

### Why Context Windows Matter

!!! example "Case 1: Too Small"
    You paste a 100-page spec into Claude, ask it to code, and Claude forgets parts of it mid-way. It contradicts itself or misses requirements. Why? The spec + prompt + conversation history + reasoning exceeded the context window. The LLM started losing information as new tokens arrived.

!!! example "Case 2: Just Right"
    You maintain a focused conversation. You paste the relevant 10-page specification, ask for code, and Claude writes coherent, complete code. Why? The spec, prompt, conversation, and reasoning all fit comfortably in the context window.

!!! example "Case 3: Efficiency"
    You're working in Claude Code. You ask Claude to read a 50,000-token codebase, analyze a bug, and fix it. Claude reads the files (tools), analyzes (thinking), writes a fix, runs tests (tools), and iterates. Each tool call starts fresh -- Claude doesn't "run out" because it's not carrying the entire codebase in context. It reads what it needs, when it needs it.

### The Three Rules

1. **Context is not infinite.** At 200,000 tokens, you have real limits. A multi-day conversation, long documents, and verbose reasoning add up fast.

2. **Tool results accumulate in context.** Tool execution happens outside the LLM's inference -- the filesystem operation itself does not consume context tokens. But every tool call result returns into the running context window and accumulates. A long agentic session that reads many files or runs many commands can silently fill the context window through tool result accumulation, not just conversation.

3. **You control what's in context.** You decide what documents to include, how verbose to be, how much history to keep. Strategic use of context is a skill.

!!! warning "Context Fills Silently"
    Most operators don't notice context filling until it causes a problem -- Claude starts contradicting itself, missing earlier instructions, or degrading in quality. By then, you're already deep into a session. Watch for these signals and start fresh sessions proactively.

### When Context Becomes a Constraint

**For a single conversation:**
You're on day 5 of work in the same Claude session. The conversation history is now 80,000 tokens. Adding a 30,000-token spec might push you near the limit.

Solution: Start a fresh conversation, paste the relevant context, or ask Claude Code to read from files instead of pasting everything.

**For a system prompt:**
You're building a system prompt (instructions for Claude). If it's 50,000 tokens, it eats into every single request's context window.

Solution: Keep system prompts concise. Rely on files (CLAUDE.md, me.md) that Claude reads on-demand, not included in every request.

**For file-heavy work:**
You're analyzing a 500-file codebase. Asking Claude to "read the whole codebase" doesn't work -- you'd exceed the context window.

Solution: Use tools. Ask Claude to use find, grep, or file-reading to locate the relevant 10-20 files, then analyze those. Context management is about smart sampling, not cramming everything in.

### Context Windows in the Harness

When Claude Code calls a tool:

1. Claude generates a request: `"Read /path/to/file.js"`
2. The tool executes: it reads the file
3. The result comes back: the file contents are in the response
4. Claude sees the result: it's now in context
5. Claude reasons about what it read
6. Claude acts: calls another tool or generates an output

Claude gets fresh information at each step. It doesn't need the entire codebase in context at once. It samples what it needs, reasons, and acts. That's why Claude Code can work on large projects -- it's designed around the context window limit.

!!! question "Before You Continue"
    You're in a Claude Code session that's been running for two hours. You've read 30 files, run 15 commands, and had a long back-and-forth conversation. Claude starts giving you answers that contradict what it said an hour ago.

    What is the most likely cause, and what do you do?

<div class="quiz-block">
  <p class="quiz-question">Which statement about tool calls and context windows is correct?</p>
  <ul class="quiz-options">
    <li data-correct="false">Tool calls reset the context window, giving you more space</li>
    <li data-correct="false">Tool execution consumes the most context tokens of any operation</li>
    <li data-correct="true">Tool call results return into the context window and accumulate over the session</li>
    <li data-correct="false">Context windows only fill up from conversation text, not tool results</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Hands-On

1. Open Claude (web). Start a fresh conversation. Type: "My name is [your name]. Remember this."
2. Have a long, unrelated conversation — 10 to 20 back-and-forth exchanges on any topic.
3. Ask: "What was my name?" Note whether Claude still knows.
4. If you have Claude Code available, run a long session with several file reads. Ask Claude to summarize what it has done in the session so far. Check the accuracy.

Context is not infinite and not guaranteed. Now you have seen it behave under pressure.

---

## Section 3: Tokens as Currency

### What is a Token?

A token is the unit of text that an LLM processes. Not a word -- a chunk of text the model's vocabulary includes.

**Rough equivalences:**
- 1 token ≈ 0.75 English words (varies by language)
- 1 page of text ≈ 300-500 tokens
- 1 line of code ≈ 5-15 tokens (code is denser than prose)

### Why Tokens Matter: The Economics

**Cost:** Every token you send to Claude costs money. Input tokens are cheaper than output tokens. Total cost = (input tokens × input price) + (output tokens × output price).

!!! note "Check Current Pricing"
    Input tokens are cheaper than output tokens, and larger models cost more per token than smaller ones. These ratios are durable; the specific dollar figures change with model releases. Verify at anthropic.com/pricing before any course run.

**Speed:** More tokens = slower response time.

**Accuracy:** Longer prompts don't always mean better answers. Verbose prompts can introduce noise. Concise, well-structured prompts often outperform rambling ones.

### Tokens as a Mental Model: Four Principles

**Principle 1: Concision is a feature.**
A 100-word, well-structured prompt often beats a 500-word prompt. Less noise, faster thinking, lower cost, faster response.

**Principle 2: Repetition is waste.**
If you ask the same question 3 times in a conversation, that's 3x the tokens. Use copy-paste; iterate once.

**Principle 3: Cheap vs. expensive operations matter.**

- **Cheap:** Read a file (tool call -- the file read is handled by the system, result comes back)
- **Expensive:** Paste a 30,000-token file into the prompt and ask Claude to reason about it

In the first case, you're paying for a small result. In the second, you're paying 30,000 input tokens plus the reasoning cost.

**Principle 4: Plan before you prompt.**
Before asking Claude to work on a project:
- What context does it need?
- How much fits in the prompt?
- What should Claude read via tools instead of you pasting?
- How many iterations might you need?

Then prompt once, strategically.

### Tokens in Practice

!!! warning "The Expensive Approach"
    You paste a 50,000-token codebase into Claude. You ask it to understand the architecture, add a feature, refactor, and optimize. You expect one response. Claude spends all its output tokens on a partial understanding. It doesn't finish. You iterate 5 times. Total cost: high.

!!! tip "The Efficient Approach"
    Ask Claude to use tools to explore the codebase. "Find all files related to authentication, read them, then propose a refactoring." Claude calls tools, reads a few key files, reasons, and proposes. One response, lower cost, better result.

!!! question "Before You Continue"
    You need Claude to analyze a 200-page field manual. You have two options:

    A. Paste the entire manual into the chat and ask your question.

    B. Ask Claude to search the manual using tools and read only the relevant sections.

    Which is more cost-effective? Which produces more reliable results? Why?

<div class="quiz-block">
  <p class="quiz-question">Which of the following behaviors is the most cost-conscious?</p>
  <ul class="quiz-options">
    <li data-correct="false">Always use the most capable model available for every task</li>
    <li data-correct="false">Paste full documents into the prompt so Claude has complete context</li>
    <li data-correct="true">Ask Claude to read specific files via tools rather than pasting large documents</li>
    <li data-correct="false">Repeat key instructions multiple times so Claude doesn't forget them</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Hands-On

1. Write a vague prompt asking Claude to help you with a project. Count the words.
2. Rewrite it as a structured prompt: task, context, constraints, output format. Count the words again.
3. Submit both and compare the quality of the first response each time. Which required fewer follow-up iterations?
4. Optional: paste each prompt into a tokenizer (platform.openai.com/tokenizer) and count the actual token cost.

Longer is not always better. Structured is better.

---

## Section 4: Tool Calls and Determinism

### What is a Tool Call?

A tool call is a structured request from an LLM to an external system. It says: "Execute this specific action and return the result."

**Example tool calls in Claude Code:**

```
Tool Call 1: read("/home/user/project/app.js")
Result: [file contents come back]

Tool Call 2: run("npm test")
Result: [test output comes back]

Tool Call 3: write("/home/user/project/config.json", "[new config content]")
Result: [confirmation that file was written]
```

Claude doesn't execute these itself -- it requests that the system execute them, then reasons about the result.

### Why Tool Calls Enable Verification

Without tools, Claude generates text. You can't be sure if it's:
- Hallucinating (making up facts)
- Outdated (using stale training data)
- Correct (reasoning from assumptions you didn't validate)

With tools, Claude can verify its own reasoning.

!!! example "Verification in Action"
    - Claude: "Your function should handle edge case X."
    - You: "How do you know?"
    - Claude: "I read your code (tool call). Line 42 shows [behavior]. That's vulnerable to [attack]. Here's a fix (tool call: write file)."
    - You: "Does it work?"
    - Claude: "Yes. I ran tests (tool call: npm test). All pass."

    That's determinism. Verification at each step, not guesses.

### The Tool Call Loop

```
Claude: "I need to know X. I'll read the file."
System: [Claude calls read tool, executes, returns contents]
Claude: "I see X is [value]. I'll now do Y."
System: [Claude calls tool to do Y]
Claude: "Here's what happened: Z. Next step is..."
```

This loop is the core of agentic development. Claude reasons, acts, observes, adjusts, repeats.

### Types of Tool Calls You'll Use

**Reading (sensory input):**
- Read files
- List directories
- Check git status
- Fetch URLs
- Query databases

**Writing (motor output):**
- Create files
- Edit files
- Delete files
- Move/copy files

**Executing (action):**
- Run commands
- Run tests
- Deploy code
- Call APIs

**Thinking (reasoning):**
- Extended thinking (native Claude feature)
- Multi-step planning

### Why Tool Calls Matter to You

If you ask Claude to read a file, Claude calls the tool. The system reads it. Claude gets the result. That's why Claude Code can work on your actual projects -- Claude isn't guessing at your code structure, it's reading it live.

If you ask Claude to "create a script" without tools, Claude generates text and hopes it works. With tools, Claude creates the script, runs it, sees if it works, and fixes it.

That's the difference between "helpful AI chat" and "agentic development."

!!! tip "Tools Are Your Audit Trail"
    Every tool call is a verifiable action. Claude read that specific file. Claude ran that specific test. Claude wrote that specific content. You can trace every step. That's not possible with pure text generation.

!!! question "Before You Continue"
    Claude tells you it has verified that your export script produces correctly formatted output.

    In the first scenario, Claude reviewed the output description you pasted and said it looks correct.

    In the second scenario, Claude called a read tool on the actual output file and checked it against the template.

    Which scenario gives you a defensible product? Why?

<div class="quiz-block">
  <p class="quiz-question">What is the primary reason tool calls make LLM behavior more deterministic?</p>
  <ul class="quiz-options">
    <li data-correct="false">Tool calls force the model to use lower temperature settings</li>
    <li data-correct="true">Tool calls enable Claude to verify its reasoning against actual system state rather than generating from memory</li>
    <li data-correct="false">Tool calls prevent hallucinations by blocking uncertain outputs</li>
    <li data-correct="false">Tool calls reset the model's context window between steps</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Hands-On

1. In Claude Code, ask: "What is in my current directory?" Watch it call the list tool and return real results.
2. Ask: "Read [name a specific file in your project]." Watch it read the actual file — not guess at the contents.
3. Ask Claude to make a small edit to a file. Before it writes, ask: "What exactly are you going to change and why?" Verify before approving.

You are tracing the tool call loop live. Every action is visible. That is the audit trail.

---

## Section 5: Operator Posture and Supervision

### What is Operator Posture?

The frame that holds this section together: the agent is a motivated PFC who has been given file-system access and a mission. Capable, fast, eager -- and will execute confidently on an ambiguous brief rather than stopping to ask for clarification. Over-plan, over-brief, verify the work. The capability does not transfer the accountability. You sign for the result.

**Human in the loop** means a human is positioned to review and approve consequential agent actions before they execute -- you are the decision point the loop depends on, not a passive observer.

Your posture is your stance toward the AI:
- **Delegating** -- asking it to do everything while you step away
- **Supervising** -- watching closely, intervening as needed
- **Collaborating** -- both thinking, both deciding

The correct posture for development is **active supervision.**

### Why Active Supervision?

Claude is powerful, but it:
- Can't read your mind
- Doesn't know your project constraints
- Can't test in your production environment
- Makes mistakes (hallucinations, missed details)
- Doesn't have judgment about tradeoffs

You are:
- The expert on your project
- The one with judgment and context
- Responsible for the output
- Able to verify results

### The Supervision Loop

```
1. You specify: "Add authentication to the API"
2. Claude asks: "What framework? What database? What security requirements?"
3. You clarify: "Express, PostgreSQL, OAuth 2.0"
4. Claude acts: "I'll create the auth module and middleware"
5. You review: Claude shows you the code
6. You verify: You test it or identify issues
7. Claude adjusts: "I see the issue. Let me fix it."
8. You confirm: "Good. Now add password reset."
```

You are at every decision point. Claude executes and reports back. You decide next steps.

### When Supervision Breaks Down

**Mistake 1: Over-trust**
You ask Claude to "refactor the entire backend" and don't look at the results for hours. When you review, there are 20 breaking changes you didn't expect. Claude made reasonable refactoring decisions, but not *your* decisions.

Fix: Review after each major step. Ask Claude to show you changes before committing.

**Mistake 2: Under-involvement**
You ask Claude a vague question ("Make this faster") and Claude spends 5,000 tokens on guesses. You iterate 10 times without getting what you meant.

Fix: Be specific. "The bottleneck is the database query in `getUserProfile`. It should return in <100ms. Current time: 2 seconds. Here's the schema..."

**Mistake 3: Automation Fallacy**
You ask Claude to run the full build, test, and deploy pipeline. Claude executes all three steps. One fails silently. Your code deploys broken.

Fix: Verify intermediate results. Have Claude show you test output before deploying. Chain actions with verification between them.

### The Golden Rule

!!! danger "If You Don't Understand It, Don't Approve It"
    If Claude says "I'll refactor the database schema" and you don't understand the changes, ask Claude to explain first. Review the SQL before execution. You're the operator. You're responsible.

    If you don't understand what Claude is about to do, don't let it do it.

!!! question "Before You Continue"
    Claude has been running a long session and proposes to "clean up the database by removing duplicate records." It sounds reasonable.

    What questions do you ask before approving this action? What could go wrong if you approve without reviewing?

<div class="quiz-block">
  <p class="quiz-question">Which of the following best describes active supervision when working with an AI agent?</p>
  <ul class="quiz-options">
    <li data-correct="false">Give the agent a task and check back when it's done</li>
    <li data-correct="true">Review outputs at each step and intervene before consequential actions execute</li>
    <li data-correct="false">Let the agent make all technical decisions while you handle communication</li>
    <li data-correct="false">Configure the agent to run without human review for efficiency</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Hands-On

1. Give Claude a task with a vague brief: "Improve my code." Read what it produces.
2. Give the same task with a specific brief: name the file, the improvement goal, the constraint, and what success looks like.
3. Compare. Which result could you review and approve without asking follow-up questions?
4. Label your vague brief: which supervision failure mode does it most resemble — over-trust, under-involvement, or automation fallacy?

A clear brief is supervision before the task starts.

---

## Section 6: Cost-Consciousness as a Core Skill

### Why Cost Matters

Developing with AI is not free. Each token costs money. Each tool call takes time. At scale -- across a team, across months -- costs add up.

"Cost-consciousness" is not about pinching pennies. It's about:
- **Efficiency:** Getting results faster
- **Sustainability:** Building habits that scale
- **Judgment:** Knowing when to spend tokens and when not to

### The Three Cost Dimensions

**Dimension 1: Token Cost**
- Every input token costs money
- Every output token costs more
- A 10,000-token conversation costs 10x less than a 100,000-token conversation

**Dimension 2: Time Cost**
- Longer conversations take longer
- More tool calls take longer (but not proportionally -- tools can run in parallel)
- Waiting for responses is dead time

**Dimension 3: Iteration Cost**
- If you need 10 iterations to get it right, that's 10x the tokens
- If you're clear the first time, it's 1x

### Cost-Conscious Behaviors

**1. Write clear prompts first, not verbose ones.**

!!! warning "Verbose Does Not Mean Better"
    "Hey Claude, I have this thing I want to build. It's kind of an app that lets people do stuff. I'm not sure about the details yet, but it should be flexible. What do you think? Can you help me figure out what to build?"

    ~80 tokens, but produces a rambling response that needs 5 iterations to clarify.

!!! tip "Structured Prompts Save Iterations"
    "I'm building a task manager. Key features: create/read/update/delete tasks, filter by priority and status, tag support, due dates. Tech stack: Node.js, React, PostgreSQL. Constraints: offline-first sync, mobile-friendly, <2sec load time. What's the API schema?"

    ~120 tokens, but produces a focused response you can use immediately. Longer in the right way.

**2. Use tools instead of pasting.**

Bad: Paste a 50,000-token codebase into the chat. Cost: 50,000 input tokens.

Good: "There's a bug in the auth module. Read `/src/auth/login.js` and identify it." Cost: Claude calls the read tool. Result comes back (~5,000 tokens). Much cheaper.

**3. Iterate tightly, not loosely.**

Bad: Ask Claude to build a feature. Look at it a day later. Ask for changes. Claude re-reads the code it wrote. Iterate again after another day.

Good: Ask Claude. It builds. Review immediately. "This doesn't match spec because of X." Claude adjusts. Repeat.

Tight iterations keep context warm and reduce re-reads.

**4. Know when to ask Claude versus when to solve it yourself.**

- **Use Claude:** Architectural decisions, complex logic, refactoring large codebases, understanding unfamiliar code
- **Use Google:** Syntax lookup, simple API usage, "how do I do X in language Y"

**5. Plan before you build.**

Spend 5 minutes planning. This often saves 50 minutes of iteration.

"Here's my plan: (1) Create the database schema. (2) Build CRUD API endpoints. (3) Add authentication. (4) Test each layer. Does this make sense? Any red flags?"

Claude affirms or suggests changes. You build. No token waste on surprises.

### Cost Consciousness in Practice

Efficient communication is the gate. If you can't ask Claude a clear question, you can't work fast. This course assumes you think this way from the start.

!!! question "Before You Continue"
    You need to debug a slow API endpoint. You have the endpoint's source file, the database schema, and the server logs.

    What's the most cost-efficient way to give Claude what it needs? What would the expensive version look like?

<div class="quiz-block">
  <p class="quiz-question">You need Claude to review 10 field reports for mentions of a specific location. What is the most cost-efficient approach?</p>
  <ul class="quiz-options">
    <li data-correct="false">Paste all 10 reports into the chat and ask Claude to search them</li>
    <li data-correct="false">Ask Claude to summarize each report individually in 10 separate conversations</li>
    <li data-correct="true">Ask Claude to use tools to search the report files and read only matching sections</li>
    <li data-correct="false">Use the most capable model available to ensure the best results</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Hands-On

1. Write a prompt you would normally send to Claude for help with a task.
2. Apply the cost-conscious principles: cut repetition, add structure, narrow the scope, specify output format.
3. Count words before and after. Is the revised version clearer and shorter?
4. Submit the revised prompt. Did you get a usable first response, or did you still need multiple follow-ups?

Iteration is where cost hides. One clear prompt beats five vague ones every time.

---

## Section 7: Worked Examples

The following examples show all six mental models in action on scenarios relevant to this course.

???+ example "Example 1: The Harness in Action"
    **Scenario:** You need to produce an intelligence summary from a folder of raw source documents. You need to know if the output is actually grounded in the sources.

    **Without the harness (unverified generation):**

    You: "Can you write an intelligence summary covering adversary logistics activity?"

    Claude: "Sure, here's a summary." [Claude generates from training data and general inference]

    You: "Thanks. I'll include this in the brief."

    [You submit the brief. A reviewer flags two claims that are not in your source documents. You cannot trace them. The brief is pulled.]

    **With the harness (grounded, traceable output):**

    You: "Write an intelligence summary on adversary logistics activity. Read the source documents in `/reports/AO-North/` and base the summary only on what is in those files."

    Claude: "I'll read the source documents and summarize from them."

    [Claude calls: list("/reports/AO-North/")] → [Result: 14 files]

    [Claude calls: read on each relevant file] → [Sees 3 files have no logistics content]

    Claude: "I found logistics-relevant content in 11 of 14 files. Three files cover unrelated activity -- I excluded them. Here is the summary with source citations by filename."

    **Why it matters:**

    - First approach: You're trusting Claude's generation. Output may be accurate or hallucinated. You cannot tell.
    - Second approach: Claude read the actual sources. Every claim is traceable. You can defend it.

    **Tokens:** First: ~200 tokens + later damage control. Second: ~500 tokens total, but the product is defensible.

???+ example "Example 2: Context Windows and Smart Sampling"
    **Scenario:** You have a folder of 500 field reports. You need to identify all mentions of a specific grid coordinate.

    **Bad approach:**

    You: "Here are all 500 field reports [100,000-token dump]. Find every mention of grid 38SMB4521."

    Claude: Overwhelmed. Loses track. Misses reports. Returns incomplete results with no way to verify coverage.

    **Good approach:**

    You: "I need every mention of grid 38SMB4521 across the field reports in `/reports/field/`. Search the collection and return relevant excerpts with source filenames."

    [Claude calls: find("/reports/field/", "-name *.txt")] → [500 files returned]

    [Claude calls: grep("38SMB4521", "/reports/field/")] → [7 matching files with line references]

    [Claude calls: read on each of the 7 matching files]

    Claude: "Found 9 mentions across 7 reports. Here are the excerpts with source file and date. Three reports are from the same 72-hour window and describe the same activity from different collection sources."

    **Why it matters:**

    - Bad approach: 100,000 tokens in context from the start. Claude cannot reason efficiently and coverage is unverifiable.
    - Good approach: Claude searches first, reads only matching files (~10,000 tokens total). Complete, verifiable coverage.

    **Context window:** Bad: uses 100,000 tokens, leaves 100,000 remaining. Good: uses 20,000 tokens, leaves 180,000 remaining.

???+ example "Example 3: Tool Calls Enabling Verification"
    **Scenario:** You are formatting a database of reporting for export to a standardized template. You need to confirm the output is correct before it goes to the customer.

    **Without tools:**

    You: "I need to convert this reporting database to standard format. Here's a sample row [paste]. What does the output format look like?"

    Claude: "Based on the standard template, your output should look like this [generates example]."

    [You apply the format manually. Three fields are transposed. The customer received malformed data for two weeks before anyone caught it.]

    **With tools:**

    You: "Convert the reporting database at `/data/raw_reports.csv` to the standard export format. Write the output to `/data/export_ready.csv`. Verify the output is correctly structured."

    [Claude calls: read("/data/raw_reports.csv")]

    [Claude calls: write("/data/export_ready.csv", "[converted data]")]

    [Claude calls: read("/data/export_ready.csv") to spot-check]

    Claude: "Done. Output file has 847 rows. Field order matches the template. Row count matches source. Spot-checked 10 records -- all correctly converted."

    **Why it matters:**

    - Without tools: You're trusting Claude's text description. No verification.
    - With tools: Claude read the actual output file and confirmed it. Defensible.

???+ example "Example 4: Operator Supervision Preventing Disaster"
    **Scenario:** You ask Claude to draft and format a situation report from unstructured notes.

    **Without supervision (over-trust):**

    You: "Draft a SITREP from my notes."

    [Claude drafts a SITREP, inferring details not in the notes to fill gaps. You don't review carefully. You submit to the operations center.]

    [The SITREP includes a casualty figure Claude inferred from context that is not in your notes and is not accurate. Correction required.]

    **With supervision (active oversight):**

    You: "Draft a SITREP from my notes in `/notes/0600-update.txt`. Use only information in that file. Flag any required fields you cannot fill from the source."

    [Claude reads the file]

    Claude: "Here is the draft SITREP. I could not fill the following required fields: friendly forces count (SECTION 3), next reporting period (SECTION 6). I flagged both with [REQUIRED -- NOT IN SOURCE]. Do not submit until those are filled."

    You: "Review the enemy activity section -- does that match my notes exactly?"

    Claude: "Yes. I can trace each sentence in that section to a specific line in your source file. Here are the line references."

    You: "Fill in the missing fields. Friendly count is 42. Next report is 1800Z."

    Claude: "Updated. SITREP is complete. All required fields are filled. No inferred content."

    **Why it matters:**

    - Over-trust: Claude fills gaps with plausible inference. You submit inaccurate reporting.
    - Supervision: You control what goes into the product. Claude flags gaps instead of inventing answers.

---

## Section 8: Exercise -- Identify the Mental Models

### Your Task

Read the following transcript of a developer working with Claude Code. For each marked section, identify which mental model(s) from this module are in play.

**Transcript:**

---

**[SECTION A]**

Developer: "I have a bug in my payment processing. It's sometimes failing silently. Here's the code [pastes 2,000 tokens of payment module code]. What's wrong?"

Claude: "I see the issue. In the `processPayment` function, there's no error handling for network timeouts. The function doesn't catch `ECONNRESET` errors. Let me fix it."

[Claude generates code]

Claude: "Here's the fix. Add a try-catch block around the API call and log errors."

Developer: "Thanks. I'll test it locally."

[Developer leaves. Tests the code later. Discovers the fix doesn't handle all edge cases.]

---

**[SECTION B]**

Developer: "There's a bug in payment processing. It fails silently on network timeouts. Can you read `/src/payment.js` and identify the issue?"

Claude: "I'll read the file and diagnose."

[Claude calls: read("/src/payment.js")]

Claude: "Found it. Line 42-45: the `processPayment` function doesn't catch network errors. Here's the fix."

[Claude calls: write("/src/payment.js", "[updated code with error handling]")]

Claude: "Let me test it."

[Claude calls: run("npm test -- payment")]

Claude: "Tests pass. All edge cases covered: ECONNRESET, ECONNREFUSED, timeout, and retry logic."

Developer: "Great. Merge it."

---

**[SECTION C]**

Developer: "How can I optimize database queries? My user profile page loads in 5 seconds."

Claude: "Query optimization depends on your schema and queries. Can you share your database schema and the slow query?"

Developer: "Here's the schema. The slow query is: `SELECT * FROM users WHERE id = $1 JOIN posts...`"

Claude: "I see the issue. Missing index on `users.id` and inefficient join. Let me create a migration and test it."

[Claude calls: read("/migrations/latest.js")] to understand migration format

[Claude calls: write("/migrations/001_add_indexes.js", "[migration code]")]

[Claude calls: run("npm run migrate")]

[Claude calls: run("npm run benchmark -- user-profile")]

Claude: "Index added. Page load time: 200ms (was 5000ms). 25x faster."

Developer: "Perfect. How long will the migration take in production?"

Claude: "The index is additive -- no data movement. It'll take <1 second even with millions of rows."

Developer: "Approved. Ship it."

---

!!! question "Analyze the Transcript"
    For each section, identify which mental models are in play and explain what the developer did right or wrong.

    1. **SECTION A:** What mental models are being violated? What should the developer have done differently?
    2. **SECTION B:** What mental models are in play? How does the harness change the outcome?
    3. **SECTION C:** Identify all the mental models and explain each one.

??? tip "Model Answers"
    **SECTION A: Violations**

    - **Harness model violated:** Claude is not verifying its own work. It generates code without testing.
    - **Tool calls missing:** Claude doesn't call tools to test the fix. It guesses that the fix works.
    - **Operator posture broken:** Developer is under-involved. They don't review before testing locally.
    - **Context issue:** The developer pasted code, which is less efficient than asking Claude to read the file.

    What should have happened: "There's a bug in `/src/payment.js`. It fails silently on timeouts. Fix it and verify with tests." → [read file] → [identify issue] → [write fix] → [run tests] → [report success]

    **SECTION B: Mental Models**

    - **The harness:** Claude read the file (eyes), made a change (hands), ran tests (feedback loop), and verified.
    - **Tool calls:** All verification happens through tools, not guesses.
    - **Operator posture:** Developer supervised. Reviewed the result and approved merging.
    - **Tokens:** Efficient. Claude read only the file it needed, not a massive code dump.

    **SECTION C: Mental Models**

    - **Context windows:** Claude doesn't load the entire database. It reads the schema and specific query. Smart sampling.
    - **Operator supervision:** Developer asks clarifying questions first. Verifies before deploying ("Approved. Ship it." only after understanding the impact).
    - **Tool calls for verification:** Claude runs the migration in a safe environment, measures performance before production deployment.
    - **Cost-consciousness:** Specific questions. Targeted fixes. Tight iteration. No waste.
    - **Tokens:** Focused prompt, tight iteration, no rambling.

---

## Summary: The Mental Models

| Model | Core Idea | Why It Matters |
|---|---|---|
| **Harness** | LLM + tools = agency | Without tools, Claude is a chat bot. With tools, Claude is a collaborator. |
| **Context Windows** | Limited working memory | You can't fit everything in context. Use tools to read on-demand. |
| **Tokens as Currency** | Every token costs time and money | Concise, clear prompts save iterations and money. |
| **Tool Calls** | Requests that execute outside context | Verification is possible. Hallucinations can be caught. |
| **Operator Posture** | You supervise, Claude executes | You're responsible. Review before committing. Intervene early. |
| **Cost-Consciousness** | Efficiency is a core skill | Plan before building. Iterate tightly. Use the right tool for the job. |

---

## Next Steps

1. **Read this module twice.** Once to understand, once to internalize.

2. **Do the exercise.** Identify the models in the transcript. Get comfortable naming them.

3. **In your first Claude Code session, notice the models in action.**
   - When you invoke a tool, notice: "I'm using the harness right now."
   - When you stay concise in your prompt, notice: "I'm being cost-conscious."
   - When you review Claude's work before applying it, notice: "I'm supervising."

4. **Build the habit.** These models aren't just concepts -- they're habits of thought. With practice, they become instinctive.

---

## Readiness Check

Before moving on, confirm:

- [ ] You can explain what the harness is and why tools are required for agency
- [ ] You know the three parts of the engine-harness-operator stack and what each does
- [ ] You can describe what a context window is and what happens when tool results accumulate
- [ ] You understand what tokens cost and can identify the efficient vs. expensive approach
- [ ] You can explain what a tool call is and why it enables verification
- [ ] You know what active supervision means and can name the three ways it breaks down
- [ ] You can identify cost-conscious vs. wasteful prompting behavior

---

**End of Mental Models Module**

This scaffolding is the foundation of competent agentic development. Master it, and everything that follows will make sense.
