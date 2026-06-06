# Mental Models for AI-Assisted Development — Teaching Guide

**For instructors delivering the ACC or the prerequisite course**

---

## Overview

This guide helps you teach the "Mental Models for AI-Assisted Development" module. It's a 35-minute self-contained lesson that precedes the ACC and prerequisite course.

**Key insight:** Students who understand these mental models will excel in the ACC. Students who don't will struggle with inefficiency, wasted tokens, and fundamental misunderstandings about AI-assisted development.

---

## Before You Teach

**Prerequisites for students:**
- Basic familiarity with what an LLM is
- A Claude account or access to Claude Code
- No coding experience required yet

**Your prep (15 minutes):**
1. Read the full module (`ACC-Mental-Models-for-AI-Development.md`)
2. Do the exercise (Section 8) yourself
3. Prepare examples from your own experience that illustrate each model
4. Have Claude Code available for live demos (optional but powerful)

---

## Teaching Structure (35 minutes)

### Opening (3 minutes)

**Hook:** "Everything we're about to teach in the ACC assumes you understand six mental models. Miss these, and you'll write inefficient code, waste tokens, and blame the AI when really the problem is how you're using it."

**Agenda:**
- Six mental models (5-25 minutes)
- Worked examples (5 minutes)
- Exercise (5-10 minutes)

**Handouts:**
- Main module (for reference)
- Quick reference (study guide)
- Workbook (active learning)
- This teaching guide (for instructors)

---

## Teaching the Six Models

### Model 1: The Harness (5 minutes)

**Objective:** Students understand that an LLM becomes agentic when paired with tools.

**Key points:**
- LLM alone: text-in, text-out. Can't read your code. Can't run tests. Can't verify.
- LLM + tools: eyes (read), hands (write), feedback loop (execute, observe, adjust)
- This is why Claude Code is different from web chat

**Live demo (optional):**
- Open Claude Code
- Ask Claude to read a file (show the tool call)
- Ask Claude to write a file (show the tool call)
- Ask Claude to run a command (show the tool call)
- Narrative: "Notice—Claude isn't guessing. It's seeing. It's acting. It's verifying."

**Common misconception:**
- Students think: "Claude can do anything if I just ask it well enough."
- Reality: "Claude can only do what it can see and act on through tools."

**Check for understanding:**
- Q: "Why is reading a file a tool call and not just part of Claude's knowledge?"
- A: "Because files change. Claude's training is static. Tools let Claude see your actual, current code."

---

### Model 2: Context Windows (6 minutes)

**Objective:** Students understand why they can't paste everything into Claude.

**Key points:**
1. Context window = working memory (~200k tokens)
2. Context is NOT infinite
3. Tool calls reset context (Claude reads on-demand, not all at once)
4. You control what's in context

**Real example:**
- "You have a 500-file codebase. You paste all 500 files (100,000 tokens) into a prompt. Claude has 100,000 tokens left. You ask it to understand the architecture, refactor, optimize, and add a feature. Claude runs out of tokens mid-response. It's broken."
- Alternative: "You ask Claude to use tools. 'Find the main entry points. Read them. What's the architecture?' Claude samples strategically. It reads 5-10 key files. It reasons from that sample. It succeeds."

**Live demo (optional):**
- Show a large document
- Paste it into Claude (show it counting tokens)
- Ask Claude to summarize a specific part
- Narrative: "See how many tokens that just cost? If we ask for 10 summaries, we've burned through the context window. Now ask Claude to use a tool instead."

**Common misconception:**
- Students think: "More context = more information = better answers."
- Reality: "Targeted context + smart sampling > massive dumping. Signal vs. noise."

**Check for understanding:**
- Q: "If you have a 1000-file codebase, should you paste all 1000 files into a prompt?"
- A: "No. Use tools to find and read the relevant 10-20 files. Context windowing is about smart sampling."

---

### Model 3: Tokens as Currency (5 minutes)

**Objective:** Students think cost-consciously about communication.

**Key points:**
1. Tokens ≈ cost + time + context
2. A concise, clear prompt beats a rambling one
3. Clear prompts save iterations (saves tokens overall)
4. Use tools instead of pasting (saves token cost)

**Economic example:**
- "Bad prompt (vague): 'Make this faster.' Claude guesses. You iterate 10 times. 10x tokens spent."
- "Good prompt (specific): 'The user lookup is 2 seconds. Target: <100ms. Here's the schema and current query.' Claude fixes it once. 1x tokens spent."

**Live demo (optional):**
- Show two prompts side by side
- Bad: "I have code that's slow. Fix it."
- Good: "The `getUserProfile` endpoint takes 5 seconds. Bottleneck is the database query (see below). Target: <200ms. Here's the schema and query: [SQL]. What's the fix?"
- Ask Claude to estimate token cost for a response to each
- Narrative: "Notice the good prompt is only slightly longer, but it's longer in the *right way*. It saves iterations."

**Common misconception:**
- Students think: "More detail = more tokens = better answer."
- Reality: "Relevant detail + clarity = efficiency. Rambling = waste."

**Check for understanding:**
- Q: "You're about to ask Claude something. You've written a 500-word rambling prompt. What should you do before sending it?"
- A: "Rewrite it concisely. Clarify what you actually want. Then send it."

---

### Model 4: Tool Calls (4 minutes)

**Objective:** Students understand that tool calls enable verification.

**Key points:**
1. Tool call = request from Claude to execute something
2. Result comes back to Claude
3. Claude observes and adjusts
4. This is how Claude self-corrects (deterministic development)

**Example loop:**
```
Claude: "I'll add an index to the database."
System: [executes migration]
Claude: "Hmm, the migration has a syntax error. Let me fix it."
System: [executes corrected migration]
Claude: "Migration succeeded. Let me benchmark the query."
System: [runs benchmark]
Claude: "Query is now 30x faster. Done."
```

**Live demo (optional):**
- Ask Claude to write code AND run tests
- Show the tool calls (write file, run npm test)
- Show the test results coming back
- Claude sees the results and adjusts
- Narrative: "Without tool calls, Claude is guessing. With them, Claude is verifying."

**Common misconception:**
- Students think: "Claude will tell me if my code works."
- Reality: "Claude doesn't know unless it can see execution results (tool calls)."

**Check for understanding:**
- Q: "How does Claude know if the code it wrote actually works?"
- A: "It runs the code (tool call), sees the output, and verifies."

---

### Model 5: Operator Posture (4 minutes)

**Objective:** Students understand their role as supervisors.

**Key points:**
1. You're the operator
2. Claude executes
3. Supervision loop: specify → Claude asks → you clarify → Claude acts → you review → Claude adjusts
4. Golden rule: "If you don't understand what Claude is about to do, don't let it do it."

**Real disaster story:**
- "Student asked Claude to refactor a database schema. Didn't review. One day later, went to deploy. Schema migrations were broken. Lost data. Had to recover from backups."
- Better: "Student asked Claude to refactor schema. Reviewed the migration SQL first. Asked clarifying questions. Ran it in a test environment first. Only then deployed to production. Success."

**Live demo (optional):**
- Ask Claude to make a big change (refactor code, change schema, etc.)
- Before Claude acts, pause and ask: "Show me what you're about to do."
- Claude shows the change
- You say: "Wait, that would break X. Let me clarify the requirements first."
- Claude adjusts based on feedback
- Narrative: "Notice—I didn't just let Claude loose. I supervised every step."

**Common misconception:**
- Students think: "I'll ask Claude to do X and come back later."
- Reality: "You stay present. You review. You decide next steps."

**Check for understanding:**
- Q: "You ask Claude to add a critical security feature to your API. What should you do before deploying?"
- A: "Review the code. Ask clarifying questions about the security approach. Maybe have Claude write tests first. Then deploy."

---

### Model 6: Cost-Consciousness (5 minutes)

**Objective:** Students think strategically about efficiency.

**Key points:**
1. Cost is not just money (token cost, time cost, iteration cost)
2. Planning beats iterating
3. Clear specs beat vague requests
4. Tight loops beat loose ones

**Planning example:**
- Bad: "Build me a task manager."
- Good: "Build a task manager. Features: create/read/update/delete tasks, filter by status, tags. Stack: Node.js + React + PostgreSQL. Offline-first sync. Mobile-friendly. <2sec load time. Start with the API schema."

The good version is longer, but it's longer in the right way. It prevents 10 iterations of "Wait, what about X?"

**Live demo (optional):**
- Show a vague request to Claude
- Get a response
- Iterate 3-4 times to clarify
- Show the token cost accumulating
- Now restart with a clear, specific request
- Get a complete response in one shot
- Narrative: "Planning saves tokens and time. Vagueness costs both."

**Common misconception:**
- Students think: "Efficiency is about being cheap."
- Reality: "Efficiency is about moving fast and shipping quality. Cost-consciousness is how you do it."

**Check for understanding:**
- Q: "Before you ask Claude to work on a project, what should you do?"
- A: "Clarify the specs, define constraints, maybe sketch the architecture. Then ask Claude to build it."

---

## Worked Examples (5 minutes)

**Objective:** See all six models in action.

**Process:**
1. Read Example 1 aloud (1 min)
   - Pause at key points
   - Ask: "What went wrong? What went right?"
   - Connect to the six models
2. Repeat for Examples 2, 3, 4 (4 min total)

**Key teaching moment:** "Notice how Example A (vibe coding) violates multiple models, while Example B (real development) uses all of them together."

---

## Exercise (5-10 minutes)

**Objective:** Students identify models in a transcript.

**Process:**
1. Have students read the three transcripts (3 min reading)
2. Work through SECTION A together (2 min)
   - Q: "What models are violated?"
   - A: [Guide students to identify harness, tool calls, operator posture]
3. Have students analyze SECTIONS B and C on their own or in pairs (3-5 min)
4. Debrief (2 min)
   - Ask a student: "What's the core difference between A and B?"
   - Expected answer: "Tool calls, verification, supervision."

**If short on time:**
- Do SECTION A together
- Assign B and C as homework

---

## Closing (2 minutes)

**Summary:**
"You now understand the six mental models that the ACC assumes. As you move through the prerequisite course and into the ACC:

- Notice the harness in action (Claude reading your code, running tests)
- Think strategically about context (sample smartly, don't paste everything)
- Be cost-conscious (clear specs, tight iterations)
- Rely on tool calls (verify, don't guess)
- Supervise actively (review, ask questions, decide)
- Plan before building (prevents wasted iterations)

Get comfortable with these six models. By the ACC, they should be instinctive."

**Next steps:**
1. Complete the workbook (`ACC-Mental-Models-Workbook.md`)
2. Review the quick reference before bed
3. Do the prerequisite course (8 modules, 2-3 days)
4. Enter the ACC ready to move fast

---

## Common Student Questions

**Q: "If I'm a strong coder, can I skip the mental models?"**

A: "No. These aren't coding skills—they're frameworks for how to work with AI. Experienced coders still need to understand context windows and tokens. Different mindset."

**Q: "Is this only for the ACC, or does it apply to all AI development?"**

A: "This applies to any development with Claude Code or agentic systems. The principles are universal."

**Q: "What if I don't understand a model?"**

A: "Re-read it. Do the workbook. Talk to an instructor. Don't move forward until it clicks. These are foundational."

**Q: "Can tool calls be turned off?"**

A: "Yes, but don't. The whole power of Claude Code is that Claude can read your code, run tests, and verify. Without tools, you're back to 'vibe coding.'"

**Q: "What's the token cost of this entire module?"**

A: "Reading it? Zero (you're reading text, not prompting Claude). Explaining it to Claude to check your understanding? ~1,000-2,000 tokens. Cheap."

---

## Classroom Dynamics

### For Fast Learners
- Have them read the quick reference during the module
- Ask them to create their own examples during the worked examples section
- In the exercise, have them identify which models are MOST important in each transcript

### For Slower Learners
- Go through the six models more slowly (might take 45-50 minutes instead of 35)
- Use more live demos
- Do the exercise together as a class instead of individually
- Assign the workbook as homework and review answers next session

### For Skeptical Learners
- Emphasize: "This isn't AI hype. This is how real development with Claude works."
- Use concrete examples from projects they know
- Show them the token bill for efficient vs. inefficient prompts
- Have them try vague vs. clear prompts themselves

---

## Assessment

**Informal:**
- Can students explain the six models in their own words?
- Can students identify models in a transcript?
- Can they plan a project using these models?

**Formal (if grading):**
- Workbook completion (all questions answered)
- Exercise analysis (correct identification of models)
- Self-assessment (honest rating of understanding)

**Passing bar:** Students should rate themselves 4+/5 on at least 5 of 6 models.

---

## Pacing Notes

**If running 35 minutes exactly:**
- Spend 4-5 min per model
- 5 min on worked examples
- 3-5 min on exercise (SECTION A together, B/C as homework)

**If running 45 minutes (recommended):**
- Spend 5-6 min per model
- 5 min on worked examples
- 10 min on exercise (all three sections together)

**If running 60 minutes:**
- Spend 6-7 min per model
- 7 min on worked examples
- 15 min on exercise + debrief
- 5 min for questions and synthesis

---

## Materials Checklist

**For students:**
- [ ] Main module (`ACC-Mental-Models-for-AI-Development.md`)
- [ ] Quick reference (`ACC-Mental-Models-Quick-Reference.md`)
- [ ] Workbook (`ACC-Mental-Models-Workbook.md`)

**For you:**
- [ ] This teaching guide
- [ ] Claude Code available (for live demos)
- [ ] Examples from your own experience (1-2 per model)
- [ ] Slides (optional, but nice to have)

**Classroom setup:**
- [ ] Projector/screen (if demos)
- [ ] Everyone has the workbook (print or digital)

---

## Troubleshooting

**"Students don't seem engaged"**
- Use a live demo. Live demos are powerful.
- Ask students to explain concepts to each other in pairs
- Use examples from their field (military, tech, etc.)

**"Students are confused about context windows"**
- This is the hardest concept. Spend extra time here.
- Demo: paste a large document, show token count, ask about implications
- Use the analogy: "Context window is like your desk. You can only fit so much on it."

**"Students think tokens are money and get anxious"**
- Emphasize: "Tokens are your resource. Like gasoline. You want to use them wisely, not hoard them."
- Show token costs ($0.001 input, $0.003 output for Sonnet). It's cheaper than you think.

**"Students ask 'Isn't this just good prompting?'"**
- Good answer: "It is. Good prompting + supervision + cost-consciousness + tool use = agentic development. The mental models tie it together."

---

## After This Module

**Next session:** Prerequisite Module 1 (LLM & Prompts)
- Students will now understand why context and tokens matter
- They'll be ready to learn prompt engineering

**Throughout the prerequisite course:**
- Point out where mental models show up
- "Remember the harness? That's why we're learning git."
- "This is tool use at work."

**In the ACC:**
- Mental models should be instinctive by now
- Don't re-teach them, just reference them
- "Remember context windows? This is why you're sampling code strategically."

---

## Your Role as Instructor

**Be the model:**
- When you demo Claude Code, narrate using mental model language
- "Notice I'm not pasting the entire codebase. I'm using tools to read on-demand. Context windowing."
- "Claude ran the tests and saw a failure. Now it's adjusting. Tool calls enable verification."

**Be an enforcer:**
- When students ask vague questions, redirect: "Be more specific. What exactly do you want?"
- When students propose pasting huge amounts of code: "Use tools instead. Why?"
- When students ignore Claude's recommendations: "Did you understand what Claude proposed? If not, ask it to explain."

**Be a cheerleader:**
- Students who get these models will move fast in the ACC
- Celebrate that: "You're thinking like an agentic developer now."

---

**End of Teaching Guide**

Teach this well, and your students will excel in the ACC. Teach it poorly, and they'll struggle for the first 2 days of the course. It's worth the 35-45 minutes.

Good luck.
