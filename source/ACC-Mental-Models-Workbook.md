# Mental Models Workbook

**Active learning guide for Mental Models for AI-Assisted Development**

---

## How to Use This Workbook

This workbook is designed to be filled in as you read the main module (`ACC-Mental-Models-for-AI-Development.md`).

**Process:**
1. Read each section of the main module
2. Answer the reflection questions in this workbook
3. Do the hands-on exercises
4. Complete the capstone exercise
5. Review your answers—you should be able to explain each model clearly

**Time:** ~45 minutes (reading + exercises)

---

## Section 1: The Harness

### Reflection Questions

**Q1.1: What is the harness?**

*Your answer:*

```
[Write your explanation of the harness in 2-3 sentences]
```

**Q1.2: What can an LLM do without tools?**

*Your answer:*

```
[List what an LLM can do]
```

**Q1.3: What can an LLM do WITH tools?**

*Your answer:*

```
[List what an LLM can do with tools]
```

**Q1.4: Give an example of a "tool" from the harness concept.**

*Your answer:*

```
[Give a specific example: e.g., "Claude reading a file with the read tool"]
```

### Self-Check

Can you explain to someone else why the harness matters? If yes, ✓. If no, re-read Section 1.

---

## Section 2: Context Windows

### Reflection Questions

**Q2.1: What is a context window?**

*Your answer:*

```
[Write a 1-sentence explanation]
```

**Q2.2: Why is the context window important?**

*Your answer:*

```
[Write 2-3 reasons]
```

**Q2.3: What is the relationship between context windows and token limits?**

*Your answer:*

```
[Explain how they're connected]
```

### The Three Rules (Restate in Your Own Words)

**Rule 1: Context is not infinite**

*Your restatement:*

```
[Explain what this means and why it matters]
```

**Rule 2: Context is reset per tool call**

*Your restatement:*

```
[Explain how tool calls reset context]
```

**Rule 3: You control what's in context**

*Your restatement:*

```
[Explain how you decide what to include]
```

### Real-World Scenario

**Scenario:** You're working on a 1000-file codebase. You want Claude to understand the architecture and suggest improvements.

**Bad approach:** Paste all 1000 files into the prompt.

**Why is this bad?**

```
[Explain using context window concepts]
```

**Better approach:**

```
[Describe a better way using tools and smart sampling]
```

### Self-Check

Can you explain when context windows become a constraint? If yes, ✓. If no, re-read Section 2.

---

## Section 3: Tokens as Currency

### Reflection Questions

**Q3.1: What is a token?**

*Your answer:*

```
[Write a simple explanation]
```

**Q3.2: Estimate the token cost:**

- 1 page of text: approximately **______** tokens
- 1 line of code: approximately **______** tokens
- 1 English word: approximately **______** tokens

(Check your estimates in Section 3)

**Q3.3: Why do tokens matter?**

*Your answer:*

```
[List the three reasons mentioned in the module]
```

### The Four Principles (Restate)

**Principle 1: Concision is a feature**

*Your restatement:*

```
[What does this mean?]
```

**Principle 2: Repetition is waste**

*Your restatement:*

```
[How does this apply to conversations with Claude?]
```

**Principle 3: Cheap vs. expensive operations matter**

*Your restatement:*

```
[Give an example of cheap and expensive]
```

**Principle 4: Plan before you prompt**

*Your restatement:*

```
[What questions should you ask before prompting?]
```

### Cost-Consciousness Exercise

**Scenario:** You're about to ask Claude to work on a project. Plan it first.

**Project:** Build a task management API

**Questions to ask yourself:**

- What context does Claude need?
  ```
  [Your answer]
  ```

- How much can fit in a prompt?
  ```
  [Your answer]
  ```

- How much should Claude read with tools?
  ```
  [Your answer]
  ```

- How many iterations might you need?
  ```
  [Your answer]
  ```

- Total estimated tokens:
  ```
  [Your rough estimate]
  ```

### Self-Check

Can you explain why a concise, well-structured prompt is better than a rambling one? If yes, ✓. If no, re-read Section 3.

---

## Section 4: Tool Calls and Determinism

### Reflection Questions

**Q4.1: What is a tool call?**

*Your answer:*

```
[Write a simple explanation with an example]
```

**Q4.2: Why do tool calls make LLMs more deterministic?**

*Your answer:*

```
[Explain how verification through tools reduces uncertainty]
```

**Q4.3: What types of tool calls exist?**

*Your answer:*

```
[List the types mentioned in the module]
```

### Tool Call Examples

**Complete the loop:**

Scenario: Claude needs to add error handling to your code.

1. Claude: "[Your restatement of what Claude says]"
2. System: [Describe what tool is called]
3. Claude: "[What Claude does next]"
4. System: [What result comes back]
5. Claude: "[Final action or report]"

### Real-World Scenario

**Scenario:** You ask Claude to optimize a slow database query.

**Without tool calls:**
- Claude says: "Add an index to the users table."
- You hope it works.
- You test it later. It doesn't work.

**With tool calls:**
- Claude says: "I'll add the index and test the query."
- Claude calls tools: [write migration] → [run migration] → [benchmark query]
- Claude reports: "Index added. Query time: 50ms (was 2 seconds)."

**Why is the second approach better?**

```
[Explain using the concept of determinism]
```

### Self-Check

Can you explain how tool calls enable verification? If yes, ✓. If no, re-read Section 4.

---

## Section 5: Operator Posture and Supervision

### Reflection Questions

**Q5.1: What is operator posture?**

*Your answer:*

```
[Describe the stance you take toward AI]
```

**Q5.2: What is the correct posture for development?**

*Your answer:*

```
[Write the answer clearly]
```

**Q5.3: Why is supervision important?**

*Your answer:*

```
[Explain what could go wrong without supervision]
```

### The Supervision Loop (Draw It or Describe It)

The module describes a supervision loop. In your own words or as a diagram:

```
[Sketch or describe the loop]

Example points:
- You specify
- Claude asks questions
- You clarify
- Claude acts
- You review
- Claude adjusts
- You confirm
```

### Red Flags for Broken Supervision

Identify what's wrong in each scenario:

**Scenario 1:** "I'll ask Claude to refactor my entire database schema. I'm going to take a break."

*What's wrong?*

```
[Identify the supervision failure]
```

**Scenario 2:** "Claude says the code is optimized. I'll trust it and deploy."

*What's wrong?*

```
[Identify the supervision failure]
```

**Scenario 3:** "I asked Claude to build a feature. Claude is confused about the requirements. Instead of clarifying, I'm going to ask it to just guess."

*What's wrong?*

```
[Identify the supervision failure]
```

### The Golden Rule (Restate)

"If you don't understand what Claude is about to do, don't let it do it."

*What does this mean practically?*

```
[Give an example of when you'd stop Claude]
```

### Self-Check

Can you explain why you're responsible for supervising Claude's work? If yes, ✓. If no, re-read Section 5.

---

## Section 6: Cost-Consciousness as a Core Skill

### Reflection Questions

**Q6.1: Why does cost matter?**

*Your answer:*

```
[It's not just about money. Explain the three dimensions]
```

**Q6.2: What are the three cost dimensions?**

*Your answer:*

```
1. [Cost dimension 1]
2. [Cost dimension 2]
3. [Cost dimension 3]
```

### Cost-Conscious Behaviors (Rewrite in Your Own Words)

**Behavior 1: Write clear prompts first, not verbose ones**

*Your explanation:*

```
[What makes a prompt efficient?]
```

**Behavior 2: Use tools instead of pasting**

*Your explanation:*

```
[Why is asking Claude to read a file cheaper than pasting it?]
```

**Behavior 3: Iterate tightly, not loosely**

*Your explanation:*

```
[Why does iteration speed matter?]
```

**Behavior 4: Know when to ask Claude vs. when to Google**

*Your examples:*

```
Use Claude for: [give 2 examples]
Use Google for: [give 2 examples]
```

**Behavior 5: Plan before you build**

*Your explanation:*

```
[What kind of planning saves tokens?]
```

### Cost Analysis Exercise

**Task:** Rewrite this vague prompt to be cost-conscious.

**Original:** "I have some code that I want you to look at and tell me if there are any problems with it. It's a web app written in Node.js and React. I'm not really sure what to look for but maybe performance or security stuff?"

**Your cost-conscious rewrite:**

```
[Rewrite the prompt to be clear, specific, and actionable]
```

**Explain why your version is better:**

```
[Explain using token and iteration costs]
```

### Self-Check

Can you explain why cost-consciousness is not about being cheap, but about being smart? If yes, ✓. If no, re-read Section 6.

---

## Section 7: Worked Examples

### Example 1: The Harness in Action

Read Example 1 in Section 7 of the main module.

**Without the harness:** What went wrong?

```
[Identify the problems]
```

**With the harness:** What went right?

```
[Identify the improvements]
```

**Key difference:**

```
[One sentence: what's the core difference?]
```

---

### Example 2: Context Windows and Smart Sampling

Read Example 2 in Section 7 of the main module.

**Bad approach:** Why doesn't it work?

```
[Explain using context window concepts]
```

**Good approach:** Why does it work better?

```
[Explain the smart sampling technique]
```

**Token efficiency:**

```
[Calculate rough token difference]
```

---

### Example 3: Tool Calls Enabling Verification

Read Example 3 in Section 7 of the main module.

**Without tools:** What's the risk?

```
[What could go wrong?]
```

**With tools:** What's the safety mechanism?

```
[How do tool calls provide verification?]
```

---

### Example 4: Operator Supervision Preventing Disaster

Read Example 4 in Section 7 of the main module.

**Without supervision (over-trust):** What disaster happened?

```
[Describe the failure]
```

**With supervision (active oversight):** What was prevented?

```
[Describe how supervision prevented disaster]
```

**Supervision checkpoint:** Where did the developer ask clarifying questions?

```
[Identify 2-3 checkpoints]
```

---

## Section 8: Exercise — Identify the Mental Models

This is the capstone exercise. Read the three transcripts in Section 8 of the main module.

### SECTION A Analysis

**What mental models are being violated?**

```
[List them]
```

**What should have happened instead?**

```
[Describe a better approach]
```

**Which mental model was most violated?**

```
[Identify one and explain]
```

---

### SECTION B Analysis

**What mental models are in play?**

```
[List them and briefly explain each]
```

**Why is the developer more confident in this outcome?**

```
[Explain using the mental models]
```

**What's the key difference from Section A?**

```
[One sentence]
```

---

### SECTION C Analysis

**Identify the mental models and explain each:**

Mental Model 1: **______**

```
[How does it show up in this example?]
```

Mental Model 2: **______**

```
[How does it show up in this example?]
```

Mental Model 3: **______**

```
[How does it show up in this example?]
```

**Operator supervision:** Where does the developer verify before deploying?

```
[Identify 2-3 verification points]
```

**Cost-consciousness:** Where is the developer being efficient?

```
[Identify specific behaviors]
```

---

## Synthesis Exercise

**Your Task:** Describe a project YOU want to build. Then, apply the mental models.

**Project idea:**

```
[Describe a small app, CLI tool, or feature you'd like to build]
```

**Apply the Mental Models:**

1. **Harness:** What tools will you ask Claude to use?

   ```
   [Answer]
   ```

2. **Context Windows:** What code/docs does Claude need to read? How will you sample smartly?

   ```
   [Answer]
   ```

3. **Tokens:** How will you write your prompt to be cost-conscious?

   ```
   [Answer]
   ```

4. **Tool Calls:** How will Claude verify its own work?

   ```
   [Answer]
   ```

5. **Operator Posture:** Where will YOU supervise and review?

   ```
   [Answer]
   ```

6. **Cost-Consciousness:** How will you plan to avoid wasted iterations?

   ```
   [Answer]
   ```

---

## Final Self-Assessment

Rate your understanding of each mental model (1-5, where 5 = can explain clearly):

| Mental Model | Rating | Evidence |
|---|---|---|
| **The Harness** | __/5 | [Can I explain what it is and why it matters?] |
| **Context Windows** | __/5 | [Can I explain when they matter?] |
| **Tokens as Currency** | __/5 | [Can I explain cost-consciousness?] |
| **Tool Calls** | __/5 | [Can I explain verification?] |
| **Operator Posture** | __/5 | [Can I explain my role?] |
| **Cost-Consciousness** | __/5 | [Can I plan efficiently?] |

**Total Score:** ___/30

**Target for ACC Readiness:** 24+/30 (80%+)

---

## Next Steps

- [ ] Re-read any section where you rated yourself <4
- [ ] Review the quick reference guide (`ACC-Mental-Models-Quick-Reference.md`)
- [ ] Discuss the models with a peer or instructor
- [ ] Watch for these models in action in your first Claude Code session
- [ ] Move on to the prerequisite course when you're confident

---

## Notes

Use this space to jot down questions or insights:

```
[Your notes here]
```

---

**End of Workbook**

Keep this workbook. Review it before the ACC starts. These mental models should be instinctive by Day 1 of the course.
