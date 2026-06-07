# Mental Models Quick Reference

**TL;DR for Mental Models in AI-Assisted Development**

---

## The Six Core Mental Models

### 1. The Harness
**Formula:** LLM + Tools = Agency

An LLM is text-in, text-out. Tools give it:
- **Eyes:** read files, check status, fetch data
- **Hands:** write files, modify code, run commands
- **Feedback loop:** act → observe → adjust

**When it matters:** You're not chatting with a bot. You're building a feedback loop. Claude can read your code, try things, and verify.

**In practice:** You set up permissions (which tools Claude can use), give instructions, and supervise the loop.

---

### 2. Context Windows
**What:** The amount of text (tokens) an LLM can see at once. Claude: 200,000 tokens.

**Rule 1:** Context is not infinite  
**Rule 2:** Tool calls reset context (Claude reads files on-demand, not all at once)  
**Rule 3:** You control what's in context (strategic selection)

**When it matters:** 
- Don't paste massive files. Ask Claude to read them.
- Keep system prompts concise. Use files that Claude reads on-demand.
- Long conversations add up. Start fresh if needed.

**In practice:** You'll work on multi-file projects. Use tools (find, grep) to sample code, not paste everything. Context windowing is a skill.

---

### 3. Tokens as Currency
**What:** A token ≈ 0.75 words. Every token costs money and time.

**Principle 1:** Concision is a feature  
**Principle 2:** Repetition is waste  
**Principle 3:** Use tools (cheap) not pasting (expensive)  
**Principle 4:** Plan before you prompt

**Example trade-off:**
- Bad: "Here's my 50KB codebase [paste]. What's the architecture?" → 50,000 tokens input
- Good: "What are the main modules? Read the src/ folder." → Claude uses tools, ~5,000 tokens

**In practice:** With tight time budgets, efficiency saves hours. Clear prompts outperform rambling ones.

---

### 4. Tool Calls
**What:** Structured requests from Claude to your system. "Read this file. Run this command. Write that file."

**Result:** Verification. Claude can check its own work.

**Example:**
1. Claude generates code
2. Claude calls tool: run tests
3. Claude sees: "2 failed, 1 passed"
4. Claude adjusts: "I see the issue. Let me fix..."
5. Claude runs tests again
6. Claude sees: "3 passed"
7. Claude reports: "Done. Verified."

**In practice:** You won't guess if Claude's code works. Claude will test it and tell you.

---

### 5. Operator Posture
**Your role:** Supervise, don't disappear.

**The supervision loop:**
1. You specify clearly
2. Claude asks clarifying questions
3. You respond
4. Claude acts
5. You review results
6. Claude adjusts based on feedback

**Golden rule:** If you don't understand what Claude is about to do, don't let it do it.

**In practice:** You're responsible for the code. Review before committing. Ask Claude to show you changes. Verify before deploying.

---

### 6. Cost-Consciousness
**What:** Efficiency as a core skill. Not penny-pinching—strategic thinking.

**Cost dimensions:**
- Token cost (input/output tokens)
- Time cost (iteration loops)
- Iteration cost (how many tries to get it right)

**Behaviors:**
- Write clear prompts first (saves iterations)
- Use tools instead of pasting (cheaper)
- Iterate tightly (no dead time between loops)
- Know when Claude helps vs. when you should Google (save tokens)
- Plan before building (prevents surprises)

**In practice:** You have 8 days to ship real apps. Every token and minute counts. Efficiency = speed.

---

## Mental Model Checklist

Before you start coding, ask yourself:

- [ ] **Harness:** What tools do I need Claude to use? (read files, run tests, git commands, etc.)
- [ ] **Context Windows:** What code/docs does Claude need to see? (whole file or just parts?)
- [ ] **Tokens:** Have I written my prompt clearly and concisely? Am I asking Claude to read instead of paste?
- [ ] **Tool Calls:** Will Claude verify its own work? (tests, linting, deployment checks)
- [ ] **Operator Posture:** Am I ready to review and supervise? Or am I vanishing?
- [ ] **Cost-Consciousness:** Have I planned, or am I about to iterate 10 times?

If you can check all of these, you're thinking like a competent agentic developer.

---

## The Four Worked Examples (Section 7)

1. **Harness:** Vibe coding vs. deterministic coding with tools
2. **Context Windows:** Dumping 500 files vs. smart file sampling
3. **Tool Calls:** Trusting text vs. verifying execution
4. **Supervision:** Over-trust disaster vs. active oversight

Read these in the full module. They show all six models in action.

---

## The Exercise (Section 8)

Three code transcripts. For each, identify:
- What mental models are in play?
- What's being done right or wrong?
- What would have prevented problems?

Do this exercise. It cements the models.

---

## Key Vocabulary

| Term | Meaning |
|------|---------|
| **Harness** | LLM + tools together (agency) |
| **Context window** | Working memory (tokens Claude can see) |
| **Token** | Unit of text (~0.75 words) |
| **Tool call** | Request to execute something external |
| **Operator** | You (supervising Claude's work) |
| **Posture** | Your stance (supervising vs. delegating) |
| **Deterministic** | Verifiable (not guessing) |
| **Vibe coding** | Development without verification |

---

## When to Use Each Model

| Situation | Mental Model | What to Do |
|-----------|-------------|-----------|
| "Claude should fix my code" | **Harness** | Set up tools so Claude can read, modify, and test |
| "I want to paste a huge file" | **Context Windows** | Ask Claude to use find/grep instead |
| "This prompt is rambling" | **Tokens** | Rewrite it concisely and clearly |
| "Claude says it works" | **Tool Calls** | Ask Claude to verify with tests first |
| "I'll ask Claude and come back later" | **Operator Posture** | Stay present. Review immediately. |
| "This is taking too many iterations" | **Cost-Consciousness** | Step back. Plan better. Then execute. |

---

## Red Flags

🚨 **You're in trouble if:**

- Claude is generating huge amounts of code and you haven't tested any of it
- You're pasting 100,000-token documents into prompts
- Your questions are vague ("make this better" vs. "add caching to the user lookup")
- You've asked Claude to do 5 things and aren't checking results in between
- You're repeating the same question in a conversation (waste of tokens)
- You don't understand what Claude is about to execute

**Fix immediately.** Stop, regroup, plan, and try again.

---

## Course Outcomes

By the end of this course, you'll have internalized:

✓ The harness is how Claude becomes agentic  
✓ Context windows limit what fits in memory (use tools)  
✓ Tokens are currency (be efficient)  
✓ Tool calls enable verification (not guessing)  
✓ You supervise (you're responsible)  
✓ Cost-consciousness is a core skill (plan and iterate tight)

**Everyone completing this course is assumed to understand these.** If you're unsure, re-read the full module. This is the foundation.

---

**End of Quick Reference**

Use this as a study guide. The full module has details, examples, and the exercise.
