# Mental Models for AI-Assisted Development

**The conceptual scaffolding for the Agentic Commanders Course**

---

## Overview

This module teaches the **mental models** that the ACC assumes you understand. These are not technical skills—they are conceptual frameworks that shape how you think about AI, tools, and development.

**Duration:** 35 minutes (self-contained)

**Learning Objectives:**
- Understand the "harness" concept: an LLM becomes agentic when paired with tools
- Grasp why context windows matter and when they become a constraint
- Recognize tokens as the "currency" of AI interaction
- Understand what tool calls are and why they make AI behavior deterministic
- Adopt the correct operator posture: you supervise, the agent executes
- Internalize cost-consciousness as a core skill, not an afterthought
- See concrete examples of these models in action
- Identify mental models in a real development transcript

**Why This Matters:**
The ACC is not a course on "how to use Claude." It assumes you understand the underlying mental models of how LLMs, tools, and human operators work together. Without these models, you'll make costly mistakes: blow through context windows, build single-threaded workflows when parallel execution is needed, forget to supervise, or assume the AI can do something it can't. With these models, you move fast and confidently.

---

## Section 1: The Harness Mental Model

### What is the Harness?

An LLM by itself is a text-in, text-out system. It can't:
- Read files
- Write to disk
- Run commands
- Call APIs
- Know what time it is
- Verify its own outputs

The **harness** is what makes an LLM into an agent. It's the system that gives the LLM:
- **Eyes:** tools to read files, check git status, fetch URLs, query databases
- **Hands:** tools to write files, create directories, modify code, run tests
- **Body:** tools to execute commands, call APIs, move files, deploy code

### The Simple Formula

```
LLM (knowledge, reasoning, generation) + Tools (sensors + actuators) = Agency
```

**Without tools:** Claude can write code, but can't run it or read your actual file system.

**With tools:** Claude can read your code, run tests, modify files, commit to git, and iterate based on the results. It becomes a genuine collaborator.

### Why This Matters to You

When you invoke an LLM in Claude Code or through the API with tools enabled, you're not just chatting with an intelligent system—you're building a feedback loop. The LLM sees the world (via tools), takes action (via tools), observes the result, and adjusts. That's the harness. That's what makes it agentic.

**Implication:** Your job is not to give the LLM a task and wait. Your job is to:
1. Set up the right tools (permissions)
2. Give clear instructions
3. Supervise the feedback loop
4. Interrupt if it goes wrong

---

## Section 2: Context Windows

### What is a Context Window?

A context window is the amount of text (measured in tokens) that an LLM can "see" at one time. Think of it as the LLM's working memory.

**Claude 3.5 Sonnet:** 200,000 tokens  
**Claude 3 Opus:** 200,000 tokens  
**Claude 3 Haiku:** 200,000 tokens

A typical page of text is ~300-500 tokens. A 50-page document is roughly 15,000-25,000 tokens.

### Why Context Windows Matter

**Case 1: Too Small**
You paste a 100-page spec into Claude, ask it to code, and Claude forgets parts of it mid-way. It contradicts itself or misses requirements. Why? The spec + prompt + conversation history + its reasoning exceeded the context window. The LLM started "losing" information as new tokens arrived.

**Case 2: Just Right**
You maintain a focused conversation. You paste the relevant 10-page specification, ask for code, and Claude writes coherent, complete code. Why? The spec, prompt, conversation, and reasoning all fit comfortably in the context window.

**Case 3: Efficiency**
You're working in Claude Code. You ask Claude to read a 50,000-token codebase, analyze a bug, and fix it. Claude reads the files (tools), analyzes (thinking), writes a fix, runs tests (tools), and iterates. Each tool call starts fresh—Claude doesn't "run out" because it's not carrying the entire codebase in its context. It reads what it needs, when it needs it.

### The Three Rules

1. **Context is not infinite.** At 200,000 tokens, you have real limits. A multi-day conversation, long documents, and verbose reasoning add up fast.

2. **Context is reset per tool call (in Claude Code).** When Claude uses a tool (read file, run command), that tool executes outside the context window. The result comes back in. So Claude can work on massive codebases—it reads files on demand, not all at once.

3. **You control what's in context.** You decide what documents to include, how verbose to be, how much history to keep. Strategic use of context is a skill.

### When Context Becomes a Constraint

**For a single conversation:**
- You're on day 5 of work on the same Claude session, asking about a project. The conversation history is now 80,000 tokens. Adding a 30,000-token spec might push you near the limit.
- Solution: Start a fresh conversation, paste the relevant context, or ask Claude Code to read from files instead of pasting everything.

**For a prompt itself:**
- You're building a system prompt (instructions for Claude). If it's 50,000 tokens, it eats into every single request's context window.
- Solution: Keep system prompts concise. Rely on files (CLAUDE.md, me.md) that Claude reads on-demand, not included in every request.

**For file-heavy work:**
- You're analyzing a 500-file codebase. Asking Claude to "read the whole codebase" doesn't work—you'd exceed the context window and Claude wouldn't learn anything.
- Solution: Use tools. Ask Claude to use find, grep, or file-reading to locate the relevant 10-20 files. Then ask it to analyze those. Context windowing is about *smart* sampling, not cramming everything in.

### Context Windows in the Harness

This is where the harness model clarifies things. When Claude Code calls a tool:
1. Claude generates a request: `"Read /path/to/file.js"`
2. The tool executes: it actually reads the file
3. The result comes back: the file contents are in the response
4. Claude sees the result: it's now in context
5. Claude reasons: it reasons about what it read
6. Claude acts: it may call another tool or generate an output

At each step, Claude gets fresh information. It doesn't need the entire codebase in context at once. It samples what it needs, reasons, and acts. That's why Claude Code can work on large projects—it's designed around the context window limit.

---

## Section 3: Tokens as Currency

### What is a Token?

A token is the unit of text that an LLM processes. It's not a word—it's a chunk of text that the model's vocabulary includes.

**Rough equivalences:**
- 1 token ≈ 0.75 English words (varies by language)
- 1 page of text ≈ 300-500 tokens
- 1 line of code ≈ 5-15 tokens (code is denser than prose)

### Why Tokens Matter: The Economics

**Cost:** Every token you send to Claude costs money. Input tokens are cheaper than output tokens, but the total cost = (input tokens × input price) + (output tokens × output price).

**Example:**
- You ask Claude: 500 input tokens (your prompt) → Claude generates 2000 output tokens (the response)
- Cost for Claude 3.5 Sonnet: (500 × $0.001) + (2000 × $0.003) = $0.50 + $6.00 = $6.50

**Speed:** More tokens = slower response time. Not linearly, but it matters.

**Accuracy:** Longer prompts don't always mean better answers. Verbose prompts can introduce noise. Concise, well-structured prompts often outperform rambling ones.

### Tokens as a Mental Model: Four Principles

**Principle 1: Concision is a feature.**
A 100-word, well-structured prompt often beats a 500-word prompt. Why? Less noise, faster thinking, less cost, faster response.

**Principle 2: Repetition is waste.**
If you ask the same question 3 times in a conversation, that's 3x the tokens. Use copy-paste; iterate once.

**Principle 3: Cheap vs. expensive operations matter.**
- **Cheap:** Read a file (you call a tool, file is read by system, result comes back)
- **Expensive:** Paste a 30,000-token file into the prompt and ask Claude to reason about it

Why? In the first case, the file read is a tool call—cheap or free (depends on setup). In the second case, you're consuming 30,000 tokens of context and input cost.

**Principle 4: Plan before you prompt.**
If you're about to ask Claude to work on a project:
- What context does it need? (specs, requirements, existing code)
- How much can you put in the prompt? (context window limit)
- How much should you ask Claude to read? (tool calls instead of pasting)
- How many iterations might you need? (estimate tokens per iteration, multiply)

Then prompt strategically.

### Tokens in Practice

**Bad approach:**
You paste a 50,000-token codebase into Claude. You ask it to understand the architecture, add a feature, refactor, and optimize. You expect one response. Claude spends all its output tokens on a partial understanding. It doesn't finish. You iterate 5 times. Total cost: huge.

**Good approach:**
You ask Claude to use tools to explore the codebase. "Find all files related to authentication, read them, then propose a refactoring." Claude calls tools, reads a few key files, reasons, and proposes. One response, lower cost, better result.

---

## Section 4: Tool Calls and Determinism

### What is a Tool Call?

A tool call is a structured request from an LLM to an external system. It says, "I want you to execute this specific action and give me the result."

**Example tool calls in Claude Code:**

```
Tool Call 1: read("/home/user/project/app.js")
Result: [file contents come back]

Tool Call 2: run("npm test")
Result: [test output comes back]

Tool Call 3: write("/home/user/project/config.json", "[new config content]")
Result: [confirmation that file was written]
```

Claude doesn't execute these itself—it *requests* that the system execute them. The system then reports back.

### Why Tool Calls Make LLMs Deterministic

Without tools: Claude generates text. You can't be sure if it's:
- Hallucinating (making up facts)
- Outdated (using training data knowledge)
- Correct (reasoning from assumptions you didn't validate)

With tools: Claude can verify its own reasoning.

**Example:**
- Claude: "Your function should handle edge case X."
- You: "How do you know?"
- Claude: "I read your code (tool call). Line 42 shows [behavior]. That's vulnerable to [attack]. Here's a fix (tool call: write file)."
- You: "Does it work?"
- Claude: "Yes. I ran tests (tool call: npm test). All pass."

That's determinism. Verification at each step.

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

If you ask Claude to read a file, Claude calls the tool. The system reads it. Claude gets the result. That's why Claude Code can work on your actual projects—Claude isn't guessing at your code structure, it's reading it live.

If you ask Claude to "create a script," without tools, Claude generates text (code) and hopes it works. With tools, Claude creates the script, runs it, sees if it works, and fixes it.

That's the difference between "helpful AI chat" and "agentic development."

---

## Section 5: Operator Posture and Supervision

### What is Operator Posture?

Your posture is your stance toward the AI. Are you:
- Delegating (asking it to do everything while you step away)?
- Supervising (watching closely, intervening as needed)?
- Collaborating (both thinking, both deciding)?

The **correct posture for development** is **active supervision.**

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
- Responsible for the code
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

Notice: You are at every decision point. Claude executes and reports back. You decide next steps.

### When Supervision Breaks Down

**Mistake 1: Over-trust**
You ask Claude to "refactor the entire backend" and don't look at the results for hours. When you review, there are 20 breaking changes you didn't expect. Claude made *reasonable* refactoring decisions, but not *your* decisions.

**Fix:** Review after each major step. Ask Claude to show you changes before committing.

**Mistake 2: Under-involvement**
You ask Claude a vague question ("Make this faster") and Claude spends 5000 tokens on guesses. You iterate 10 times without getting what you meant.

**Fix:** Be specific. "The bottleneck is the database query in `getUserProfile`. It should return in <100ms. Current time: 2 seconds. Here's the schema..."

**Mistake 3: Automation Fallacy**
You think: "I'll ask Claude to run the full build, test, and deploy pipeline." Claude executes all three tool calls. One fails silently. Your code deploys broken.

**Fix:** Verify intermediate results. Have Claude show you test output before deploying. Chain actions with verification between them.

### The Golden Rule

**If you don't understand what Claude is about to do, don't let it do it.**

It's that simple. If Claude says "I'll refactor the database schema," and you don't understand the changes, ask Claude to explain first. Or ask to review the SQL before execution. You're the operator. You're responsible.

---

## Section 6: Cost-Consciousness as a Core Skill

### Why Cost Matters

Developing with AI is not free. Each token costs money. Each tool call takes time. At scale—across a team, across months—costs add up.

But "cost-consciousness" is not about pinching pennies. It's about:
- **Efficiency:** Getting results faster, not slower
- **Sustainability:** Building habits that scale
- **Judgment:** Knowing when to spend tokens and when not to

### The Three Cost Dimensions

**Dimension 1: Token Cost**
- Every input token costs money
- Every output token costs more
- A 10,000-token conversation costs 10x less than a 100,000-token conversation

**Dimension 2: Time Cost**
- Longer conversations take longer
- More tool calls take longer (but not proportionally—tools run in parallel)
- Waiting for responses is dead time

**Dimension 3: Iteration Cost**
- If you need 10 iterations to get it right, that's 10x the tokens
- If you're clear the first time, it's 1x

### Cost-Conscious Behaviors

**1. Write clear prompts first, not verbose ones.**

Bad: "Hey Claude, I have this thing I want to build. It's kind of an app that lets people do stuff. I'm not sure about the details yet, but it should be flexible. What do you think? Can you help me figure out what to build?"

Tokens: ~80, but produces a rambling response that needs 5 iterations to clarify.

Good: "I'm building a task manager. Key features: create/read/update/delete tasks, filter by priority and status, tag support, due dates. Tech stack: Node.js, React, PostgreSQL. Constraints: offline-first sync, mobile-friendly, <2sec load time. What's the API schema?"

Tokens: ~120, but produces a focused response you can use immediately.

The "good" prompt is actually slightly longer, but it's longer in the *right way*. It saves iterations.

**2. Use tools instead of pasting.**

Bad: You paste a 50,000-token codebase into the chat.
Cost: 50,000 input tokens.

Good: "There's a bug in the auth module. Read `/src/auth/login.js` and identify it."
Cost: Claude calls the read tool. System reads the file. Result comes back (~5,000 tokens). Much cheaper.

**3. Iterate tightly, not loosely.**

Bad: You ask Claude to build a feature. It builds. You look at it a day later. You ask for changes. Claude re-reads the code it wrote. You iterate again after another day.

Cost: High because there's dead time and context re-reads.

Good: You ask Claude. It builds. You review immediately. You say, "This doesn't match spec because of X." Claude adjusts. Repeat.

Cost: Lower because iterations are tight and context is warm.

**4. Know when to ask for help versus when to solve it yourself.**

Some problems are worth 10,000 tokens to solve with Claude. Some are better solved in 2 minutes with a Google search. Know the difference.

- **Use Claude:** Architectural decisions, complex logic, refactoring large codebases, understanding unfamiliar code
- **Use Google:** Syntax lookup, "how do I do X in JavaScript," simple API usage

**5. Plan before you build.**

Spend 5 minutes planning. This often saves 50 minutes of iteration.

"Here's my plan:
1. Create the database schema
2. Build CRUD API endpoints
3. Add authentication
4. Test each layer

Does this make sense? Any red flags?"

Claude affirms or suggests changes. You build. You don't waste tokens on surprises.

### Cost Consciousness in the ACC

The ACC assumes you think like this. When you have 8 days to build real applications, you don't have time to waste tokens on vague prompts and bad planning. Efficient communication is the gate. If you can't ask Claude a clear question, you can't work fast.

---

## Section 7: Worked Examples

### Example 1: The Harness in Action

**Scenario:** You're building a CLI tool and need to know if it actually runs.

**Without the harness (vibe coding):**
You: "Can you write a Node.js CLI that reads a JSON file and prints it?"
Claude: "Sure, here's some code."
[Claude generates code]
You: "Thanks. I'll copy-paste this locally and test it."
[You leave. You copy the code. You discover it has a typo. It doesn't run. You text Claude. You wait for clarification.]

**With the harness (deterministic development):**
You: "Write a Node.js CLI that reads a JSON file and prints it. Call it `reader.js`. Test it."
Claude: "I'll create the file and test it."
[Claude calls: write("/path/to/reader.js", "[code]")]
[Claude calls: run("node /path/to/reader.js test.json")]
[Claude sees: "ENOENT: no such file or directory"]
Claude: "The test file doesn't exist. Let me create a test file first."
[Claude calls: write("/path/to/test.json", '{"name":"test"}')]
[Claude calls: run("node /path/to/reader.js test.json")]
[Claude sees: "{"name":"test"}" — success]
Claude: "Done. Your CLI works."

**Why it matters:**
- First approach: You're guessing. Claude is guessing. Lots of iteration.
- Second approach: Claude has feedback. It fixes its own mistakes. You know it works.

**Tokens:**
- First: ~200 tokens for code generation + later clarification
- Second: ~500 tokens total, but you're done in one go

---

### Example 2: Context Windows and Smart Sampling

**Scenario:** You have a 500-file codebase. You need to add a new feature.

**Bad approach:**
You: "Here's my entire codebase [paste all 500 files as a 100,000-token dump]. Add a new feature to handle notifications."
Claude: Overwhelmed. Loses track. Misses files. Makes contradictory changes.

**Good approach:**
You: "I'm adding notifications to my app. The code is in `/src/`. Can you identify the event bus, the user model, and the API router? Then propose where to hook notifications."
Claude: "I'll search for those files."
[Claude calls: find("/src/", "-name *event*")]
[Result: 2 event-related files]
[Claude calls: read("/src/events/bus.js")]
[Claude calls: find("/src/", "-name *user*")]
[Claude calls: read("/src/models/User.js")]
[Claude calls: find("/src/", "-name *router*") or find("/src/", "-name *api*")]
[Claude calls: read relevant router file]
Claude: "Here's the event structure, user model, and API entry point. Notifications should hook in here [specific location]. Here's the design."

**Why it matters:**
- Bad approach: 100,000 tokens in context from the start. Claude can't reason efficiently.
- Good approach: Claude reads what it needs (maybe 10,000 tokens total across all reads). Smart sampling.

**Context window:**
- Bad: Uses 100,000 tokens, leaves 100,000 remaining
- Good: Uses 20,000 tokens, leaves 180,000 remaining

---

### Example 3: Tool Calls Enabling Verification

**Scenario:** You're adding a security feature (password hashing).

**Without tools:**
You: "I'm adding bcrypt password hashing. Here's my current code [paste]. Should I add salt rounds?"
Claude: "You should use 10-12 salt rounds for security."
You: "OK thanks."
[You implement it. You realize later you didn't validate if the hashing actually works.]

**With tools:**
You: "Add bcrypt password hashing to the authentication. Verify it works."
Claude: "I'll add bcrypt, write a test, and verify."
[Claude calls: write("/src/auth/hash.js", "[bcrypt implementation]")]
[Claude calls: write("/test/hash.test.js", "[unit tests]")]
[Claude calls: run("npm test")]
[Result: "2 passing, 0 failing"]
Claude: "Done. Hash function works. Salt rounds: 12 (recommended). Tests verify it correctly hashes and validates."

**Why it matters:**
- Without tools: You're trusting Claude's text. No verification.
- With tools: You're trusting Claude's *executed* code. Much more reliable.

---

### Example 4: Operator Supervision Preventing Disaster

**Scenario:** You ask Claude to refactor your database schema.

**Without supervision (over-trust):**
You: "Refactor the schema for better performance."
Claude: "I'll add indexes, denormalize some fields, and restructure tables."
[Claude makes changes]
[You don't review for a day]
[You go to deploy]
[Oops: migrations are broken, data is lost, deployment fails]

**With supervision (active oversight):**
You: "The database is slow on user queries. Here's the current schema [paste]. Identify bottlenecks and propose fixes."
Claude: "Query on `users.email` is slow (no index). Joining with `posts` is expensive (missing foreign key optimization). Here's what I'll change [shows migration]."
You: "Show me the migration SQL before you apply it."
Claude: "Here's the migration. It adds an index on email, creates a composite index on user_id + created_at, and adds a foreign key constraint."
You: "Will this lose data?"
Claude: "No. Composite index is additive. Foreign key constraint will reject only orphaned records (if any). Safe."
You: "OK, apply it."
[Claude applies migration]
You: "Run the slow query again. How's the time?"
[Claude runs benchmark]
Claude: "Query time: 50ms (was 2s). 40x faster."

**Why it matters:**
- Over-trust: You lose data and have to recover.
- Supervision: You prevent the disaster by reviewing at each step.

---

## Section 8: Exercise — Identify the Mental Models

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

Claude: "The index is additive—no data movement. It'll take <1 second even with millions of rows."

Developer: "Approved. Ship it."

---

### Analysis Questions

For each section, answer:

1. **SECTION A: What mental models are being violated?**
   - What should the developer have done differently?
   - What would have prevented the later discovery of edge cases?

2. **SECTION B: What mental models are in play?**
   - How does the harness differ from Section A?
   - Why is the developer more confident in this outcome?

3. **SECTION C: Identify the mental models and explain each one.**
   - Context windows: How does Claude use tools to avoid loading the entire database into context?
   - Operator posture: Where does the developer verify before deploying?
   - Cost-consciousness: Where is the developer being efficient?

### Model Answers

**SECTION A: Violations**

- **Harness model violated:** Claude is not verifying its own work. It generates code without testing.
- **Tool calls missing:** Claude doesn't call tools to test the fix. It guesses that the fix works.
- **Operator posture broken:** Developer is under-involved. They don't review before testing locally.
- **Context issue:** The developer pasted code, which is less efficient than asking Claude to read the file.

**What should have happened:**
Developer: "There's a bug in `/src/payment.js`. It fails silently on timeouts. Fix it and verify with tests."
Claude: [read file] → [identify issue] → [write fix] → [run tests] → [report success]

**SECTION B: Mental Models**

- **The harness:** Claude read the file (eyes), made a change (hands), ran tests (feedback loop), and verified.
- **Tool calls:** All the verification happens through tools, not guesses.
- **Operator posture:** Developer is supervising. They reviewed the result and approved merging.
- **Tokens:** Efficient. Claude read only the file it needed, not a massive code dump.

**SECTION C: Mental Models**

- **Context windows:** Claude doesn't load the entire database. It reads the schema and specific query. It samples what it needs.
- **Operator supervision:** Developer asks clarifying questions first ("Can you share the schema?"). Developer verifies before deploying ("Approved. Ship it." only after understanding the impact).
- **Tool calls for verification:** Claude runs a migration in a safe environment first, measures performance before production deployment.
- **Cost-consciousness:** Developer is efficient. They ask specific questions. Claude makes targeted fixes. No waste.
- **Tokens:** Efficient prompt, tight iteration, no rambling.

---

## Summary: The Mental Models

| Model | Core Idea | Why It Matters |
|-------|-----------|----------------|
| **Harness** | LLM + tools = agency | Without tools, Claude is a chat bot. With tools, Claude is a developer. |
| **Context Windows** | Limited working memory | You can't fit everything in context. Use tools to read on-demand. |
| **Tokens as Currency** | Every token costs time and money | Concise, clear prompts save iterations and money. |
| **Tool Calls** | Requests that execute outside context | Verification is possible. Hallucinations can be caught. |
| **Operator Posture** | You supervise, Claude executes | You're responsible. Review before committing. Intervene early. |
| **Cost-Consciousness** | Efficiency is a core skill | Plan before building. Iterate tightly. Use the right tool for the job. |

---

## How This Applies to the ACC

The **Agentic Commanders Course** assumes you understand these models cold. On Day 1:

- You'll receive 8 commands per day to execute in Claude Code
- Each command involves writing specifications, reading code, iterating with Claude, and shipping
- You have limited time and token budgets
- You need to move fast without spinning your wheels
- You need to supervise Claude's work and verify it works

If you understand:
- Why the harness matters (you set up tools and supervise)
- Context windows (you read strategically, not pasting everything)
- Tokens (you're efficient in your communication)
- Tool calls (you verify, not guess)
- Operator posture (you drive decisions, Claude executes)
- Cost-consciousness (you plan and iterate tight)

Then you're ready.

If you don't—if you think Claude is magic, or that you can skip verification, or that costs don't matter—the ACC will expose those gaps quickly. Not in a mean way, but practically: you'll run out of tokens, miss deadlines, or ship broken code.

---

## Next Steps

1. **Read this module twice.** Once to understand, once to internalize.

2. **Do the exercise.** Identify the models in the transcript. Get comfortable naming them.

3. **In your first Claude Code session, notice the models in action.**
   - When you invoke a tool, notice: "I'm using the harness right now."
   - When you stay concise in your prompt, notice: "I'm being cost-conscious."
   - When you review Claude's work before applying it, notice: "I'm supervising."

4. **Build the habit.** These models aren't just concepts—they're habits of thought. With practice, they become instinctive.

5. **When you hit the ACC, these habits will be your superpower.** You'll move faster than students who are still figuring out these concepts.

---

**End of Mental Models Module**

This scaffolding is what the ACC builds on. Master it, and everything that follows will make sense.
