# Course Map & Schedule

**Mission Brief: How This Course Runs.** AI and Agentics Basics is a single, linear path that takes you from no AI experience to confidently commanding an AI agent — and to the doorstep of advanced agentic work. One spine, each concept taught once, every module gated by a readiness check before you move on.

---

## How This Course Is Built

This is a **single ascending track**, not a menu. Each module assumes you completed the one before it. Concepts are introduced exactly where they become load-bearing, practiced immediately, then built on — never re-taught.

```
 1  Know Your Weapon            How AI Actually Works
 2  Briefing the Machine        Prompting as a Mission Order
 3  Feeding the Machine         Grounding & Multimodality
 4  Standing Orders             Making the AI Know You
        ── conceptual foundation complete; tools now enter ──
 5  Know the Terrain            Filesystem & Terminal
 6  The Duty Logbook            Version Control with Git
 7  From Advisor to Operator    Commanding an Agent
 8  Ammunition Discipline       Tokens, Context & Cost
 9  Rules of Engagement         Ethics & Responsible AI Use
        ── integrate ──
10  Field Craft                 Markdown, Code, Tools & Context Files
11  The Proving Ground          Capstone Build
12  Crossing the LD             Bridge to Advanced Agentics
```

---

## The Modules

| # | Module | What you leave with |
|---|---|---|
| 1 | **Know Your Weapon: How AI Actually Works** | A working model of the engine: prediction, tokens/context, the four failure modes, how to verify output, when to use AI and when not to, and the data-handling bright line. |
| 2 | **Briefing the Machine: Prompting as a Mission Order** | Deliberate prompting — the four-element brief plus intermediate technique (few-shot, chain-of-thought, decomposition, structured output, system vs. user). |
| 3 | **Feeding the Machine: Grounding & Multimodality** | How to give the model real information (web search, file upload, retrieval) and work with images, documents, and voice — and the failure modes of each. |
| 4 | **Standing Orders: Making the AI Know You** | Persistent context — custom instructions, projects, memory — so you stop re-briefing the model every session. |
| 5 | **Know the Terrain: Filesystem & Terminal** | Confident file and command-line navigation. This is the ground the agent operates on. |
| 6 | **The Duty Logbook: Version Control with Git** | Git as the logbook: commit, branch, merge, push — and why it is mandatory once an agent can write to your files. |
| 7 | **From Advisor to Operator: Commanding an Agent** | The engine-harness-operator stack, read/write/execute access, tool calls, and the delegate-verify-own loop. |
| 8 | **Ammunition Discipline: Tokens, Context & Cost** | Operating efficiently: model selection, context management, and cost discipline under a real agent session. |
| 9 | **Rules of Engagement: Ethics & Responsible AI Use** | Accountability for output, bias, disclosure, dual-use awareness, and the DoD AI ethical principles. |
| 10 | **Field Craft: Markdown, Code, Tools & Context Files** | Markdown, basic programming logic, a verified toolbox, and CLAUDE.md + me.md for a real project. |
| 11 | **The Proving Ground: Capstone Build** | A real project shipped to GitHub — built, supervised, and defended, including a recovered agent mistake. |
| 12 | **Crossing the LD: Bridge to Advanced Agentics** | A map of what advanced agentic work adds — grounding/RAG, MCP, guardrails, workflow patterns, multi-agent — and how your foundation maps onto it. |

A [Glossary & Quick Reference](modules/glossary.md) anchors every term as you go.

---

## Dependency Chain (do not skip)

- **Modules 1-4** are the conceptual foundation. Everything after assumes them.
- **Module 5 (Terminal)** must precede **Module 7 (Commanding an Agent)** — you cannot supervise an agent navigating ground you do not know.
- **Module 6 (Git)** must precede **Module 7** and **Module 11** — the supervisor mindset assumes you can rewind an agent's edits.
- **Module 9 (Ethics)** lands after **Module 7** on purpose: you grasp accountability viscerally only after you have felt an agent take real action. The data-handling bright line still appears in Module 1 as a hard safety rule that cannot wait.
- **Module 11 (Capstone)** requires Modules 6, 7, 9, and 10.

---

## Delivery & Pacing

The course runs in two phases:

**Phase 1 — Foundations (Modules 1-4): multi-week, short daily reps.** Built for someone who uses AI by feel. Delivered in short daily sessions over multiple weeks so the mental model sets before tools enter.

**Phase 2 — Operator Block (Modules 5-12): 3-4 day intensive.** Hands-on. Each module has a deliverable.

### Sample Intensive Schedule

| Day | Modules |
|---|---|
| **Day 1 — Terrain & Logbook** | M5 Terminal, M6 Git |
| **Day 2 — The Agentic Leap** | M7 Commanding an Agent, M8 Tokens/Context/Cost, M9 Ethics |
| **Day 3 — Field Craft** | M10 Markdown, Programming, Tools, Context Files |
| **Day 4 — Proving Ground** | M11 Capstone build + present, M12 Bridge brief |

Durations are instructional time; add breaks separately.

---

## Course Completion Checklist

You have completed this course when you can do all of the following without help:

**Conceptual**

- [ ] Explain what an LLM is and why it sometimes produces wrong answers
- [ ] Name the four failure modes and verify output with a repeatable method
- [ ] Explain grounding — how to give the model real information instead of trusting its memory
- [ ] Describe the engine-harness-operator stack and your role as operator
- [ ] Apply the DoD AI ethical principles to your own use

**Technical**

- [ ] Write deliberate prompts, including intermediate technique
- [ ] Personalize an AI tool with persistent instructions
- [ ] Navigate the terminal confidently
- [ ] Use git (init, add, commit, branch, merge, push) — and rewind a bad change
- [ ] Write Markdown and read basic program logic
- [ ] Write a CLAUDE.md that actually constrains an agent
- [ ] Ship a working project to GitHub

**Mindset**

- [ ] Delegate, verify, and own — you sign for the result
- [ ] Treat confidence as no evidence of correctness
- [ ] Apply the data-handling bright line every time, under pressure

---

## Common Questions

**Q: Can I skip a module?**
No. This is a single ascending track. Module 11 (Capstone) specifically requires Modules 6, 7, 9, and 10. Skipping a dependency will stall you.

**Q: I already use the command line / already prompt well.**
Move through the relevant module quickly to confirm the foundation, but do not skip the readiness check. The agentic modules (7+) assume every prior concept.

**Q: How long does the full course take?**
Foundations (Modules 1-4) run multi-week in short daily reps; the Operator Block (Modules 5-12) is a 3-4 day intensive. Roughly 2-3 weeks of active learning if done consistently. The terminal and capstone phases need the most time.

**Q: What comes after this course?**
The ACC main course — advanced agentic work. Module 12 is the bridge to it.
