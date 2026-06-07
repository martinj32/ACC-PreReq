# ACC Curriculum Index

**Navigation guide for all prerequisite and foundation materials**

---

## Course Structure Overview

The Agentic Commanders Course (ACC) builds on a foundation. This document maps the learning journey.

```
┌─────────────────────────────────────────────────────┐
│   Mental Models for AI-Assisted Development         │
│   (Conceptual scaffolding — 35 minutes)             │
│   ← You are here. Read this first.                  │
└──────────────────┬──────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────┐
│   ACC Prerequisite Course (8 Modules, 2-3 days)     │
│   - Module 1: LLM & Prompts                         │
│   - Module 2: Terminal Basics                       │
│   - Module 3: Git Basics                            │
│   - Module 4: Markdown                              │
│   - Module 5: Programming Concepts                  │
│   - Module 6: Developer Tools                       │
│   - Module 7: Context Files (CLAUDE.md, me.md)      │
│   - Module 8: Capstone Project                      │
└──────────────────┬──────────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────────┐
│   Agentic Commanders Course (3 days)                │
│   - Day 1: Core Concepts & First Apps               │
│   - Day 2: Advanced Patterns & Multi-Agentic Work   │
│   - Day 3: Capstone & Synthesis                     │
└─────────────────────────────────────────────────────┘
```

---

## Mental Models First

**File:** `ACC-Mental-Models-for-AI-Development.md`

**Duration:** 35 minutes (self-contained)

**Purpose:** Teach the conceptual frameworks the ACC assumes students know.

**Contents:**
1. The Harness Mental Model (LLM + tools = agency)
2. Context Windows (what, why, when they matter)
3. Tokens as Currency (cost and context)
4. Tool Calls (reading files, writing, running commands)
5. Operator Posture (supervision vs. automation)
6. Cost-Consciousness as a Skill
7. Four Worked Examples
8. Exercise: Identify models in a transcript

**What You'll Know After:**
- How an LLM becomes agentic (tools)
- Why you can't paste everything into context (windowing)
- Why clear prompts save time and money (tokens)
- How Claude verifies its own work (tool calls)
- Your role in the relationship (supervise)
- How to think about efficiency (cost-consciousness)

**Quick Reference:** `ACC-Mental-Models-Quick-Reference.md`

---

## Prerequisite Course (Foundation)

**Files:**
- `ACC-Prerequisite-Course-Design.md` (full curriculum, 8 modules)
- `ACC-Prerequisite-Module-Summary.md` (condensed quick reference)
- `ACC-Prerequisite-Instructor-Guide.md` (for instructors)

**Duration:** 2-3 days (16 hours total)

**Target Audience:** Students with zero background knowledge

**Modules:**

### Module 1: LLM & Prompts (90 min)
**Learn:** What LLMs are, how to write clear prompts, context windows, temperature

**Deliverable:** 5 well-written prompts

**Key insight:** "Specificity wins. Vague prompts get vague answers."

---

### Module 2: Terminal Basics (120 min)
**Learn:** Navigate files, use command line, pipes, redirects, PATH

**Deliverable:** Terminal transcript showing 6 exercises

**Key insight:** "The terminal is just another interface."

---

### Module 3: Git Basics (120 min)
**Learn:** Init repos, commit, branch, merge, push, resolve conflicts

**Deliverable:** GitHub repo with 5+ commits

**Key insight:** "Git is a time machine."

---

### Module 4: Markdown (90 min)
**Learn:** Headers, lists, code blocks, tables, links, frontmatter

**Deliverable:** One complete Markdown document

**Key insight:** "Markdown is the lingua franca of developers."

---

### Module 5: Programming Concepts (120 min)
**Learn:** Variables, logic, loops, functions, debugging, pseudocode

**Deliverable:** 3 small programs

**Key insight:** "Programming is problem-solving."

---

### Module 6: Developer Tools (90 min)
**Learn:** Install Claude Code, GitHub auth, VS Code, .env, PATH

**Deliverable:** Checklist of all tools installed

**Key insight:** "Your tools work together."

---

### Module 7: Context Files (90 min)
**Learn:** CLAUDE.md, me.md, conflict resolution, scope boundaries

**Deliverable:** CLAUDE.md + me.md for a real project

**Key insight:** "CLAUDE.md tells Claude what to build. me.md tells Claude how you work."

---

### Module 8: Capstone Project (180 min)
**Learn:** Full workflow (plan → code → commit → push), ship something real

**Deliverable:** Working project on GitHub

**Key insight:** "You're not building a tutorial. You're shipping real code."

**Paths:**
- Path A: CLI Tool (password checker, markdown converter, task logger)
- Path B: Web App (note-taking app, unit converter, quote generator)
- Path C: API Integration (weather app, movie search, joke generator)

---

## Prerequisite Learning Progression

```
Module 1: LLM Basics
    ↓
Module 2: Terminal ←→ Module 3: Git ←→ Module 4: Markdown
    ↓
Module 5: Programming
    ↓
Module 6: Tools Setup
    ↓
Module 7: Context Files
    ↓
Module 8: Capstone (integrates all)
```

**Critical path:** M1 → M2 → M3 → M5 → M8 (don't skip)

**Can run in parallel:** M4 (Markdown) while others sink in

**Must complete before M8:** M5, M6, M7

---

## Daily Schedule (Prerequisite Course)

### Day 1: Foundations (8 hours)
| Time | Activity |
|------|----------|
| 8:00-9:30 | Module 1: LLM Basics |
| 9:30-10:00 | Break |
| 10:00-12:00 | Module 2: Terminal Basics |
| 12:00-1:00 | Lunch |
| 1:00-2:30 | Module 3: Git Part 1 |
| 2:30-2:45 | Break |
| 2:45-4:15 | Module 3: Git Part 2 |
| 4:15-5:00 | Module 4: Markdown (intro) |
| 5:00-6:00 | Lab + troubleshooting |

### Day 2: Intermediate (8 hours)
| Time | Activity |
|------|----------|
| 8:00-9:30 | Module 4: Markdown (finish) |
| 9:30-10:00 | Break |
| 10:00-12:00 | Module 5: Programming |
| 12:00-1:00 | Lunch |
| 1:00-2:30 | Module 6: Developer Tools |
| 2:30-2:45 | Break |
| 2:45-4:15 | Module 7: Context Files |
| 4:15-5:00 | Readiness check |
| 5:00-6:00 | Lab + capstone prep |

### Day 3: Capstone (6-8 hours, optional)
| Time | Activity |
|------|----------|
| 8:00-12:00 | Module 8: Build (part 1) |
| 12:00-1:00 | Lunch |
| 1:00-5:00 | Module 8: Build (part 2) + present |

---

## ACC Readiness Checklist

Before Day 1 of the ACC, you should be able to:

**Conceptual (Mental Models)**
- [ ] Explain what the "harness" is and why it matters
- [ ] Describe context windows and why they limit what you can paste
- [ ] Explain tokens and why concise communication matters
- [ ] Understand tool calls and how they enable verification
- [ ] Explain your role as operator/supervisor
- [ ] Think cost-consciously about prompts and iterations

**Technical (Prerequisite Course)**
- [ ] Write specific, iterative prompts
- [ ] Navigate the terminal confidently
- [ ] Use git (init, add, commit, branch, merge, push)
- [ ] Write Markdown with multiple syntax elements
- [ ] Understand programming concepts (variables, logic, functions)
- [ ] Have Claude Code, git, Node.js/Python, and VS Code installed
- [ ] Write CLAUDE.md and me.md files
- [ ] Have shipped a real project to GitHub

**Psychological**
- [ ] Understand that Claude is not magic (it needs supervision)
- [ ] Know that you're responsible for the code
- [ ] Be comfortable asking Claude clarifying questions
- [ ] Expect to iterate tightly (not once and done)
- [ ] Be ready to move fast (8 days, lots of output expected)

---

## How Mental Models Connect to the Prerequisite Course

**Module 1 (LLM & Prompts)** assumes you understand:
- Why context windows exist (Section 2 of Mental Models)
- Why tokens matter (Section 3)

**Module 2-3 (Terminal & Git)** assumes you understand:
- Why you need tools (the harness, Section 1)
- That you'll supervise Claude using these tools (Section 5)

**Module 6 (Developer Tools)** assumes you understand:
- The harness: setting up the right tools (Section 1)

**Module 7 (Context Files)** assumes you understand:
- How CLAUDE.md shapes Claude's behavior (related to context, Section 2)
- How me.md shapes your operator posture (Section 5)

**Module 8 (Capstone)** assumes you understand all six mental models:
- You set up a harness (tools)
- You use context windowing (reading strategically)
- You communicate cost-consciously (clear prompts)
- You rely on tool calls for verification
- You supervise the entire build
- You think about efficiency

---

## How Mental Models Connect to the ACC

The ACC (Agentic Commanders Course) happens after the prerequisite course. It's 3 intensive days where you build real applications.

**Why mental models matter in the ACC:**

**Day 1:** You receive 8 commands to execute. Each one involves:
- Reading specs and existing code (context windowing)
- Asking Claude to build a feature or fix a bug (tool calls)
- Supervising the work and reviewing (operator posture)
- Iterating based on feedback (cost-consciousness)

If you don't understand mental models, you'll:
- Waste tokens pasting everything
- Not verify Claude's work
- Miss supervision moments
- Iterate inefficiently

If you do understand them, you'll move fast and ship quality code.

**Day 2:** You work on multi-agentic patterns. You might ask Claude Code to spin up a separate agent or coordinate multiple agents. This requires understanding:
- The harness (how agents interact with tools and each other)
- Context windowing (how to pass data between agents efficiently)
- Tokens (cost of multi-agent systems)
- Supervision (orchestrating agent behavior)

**Day 3:** Capstone and synthesis. By now, mental models are instinctive.

---

## File Structure

```
/ACC-Student-Files/
│
├── ACC-Mental-Models-for-AI-Development.md ← START HERE (35 min)
├── ACC-Mental-Models-Quick-Reference.md (study guide)
├── ACC-Curriculum-Index.md (this file)
│
├── ACC-Prerequisite-Course-Design.md (full course, 8 modules)
├── ACC-Prerequisite-Module-Summary.md (quick reference)
├── ACC-Prerequisite-Instructor-Guide.md (for instructors)
│
├── README.md (overview)
├── CLAUDE.md (project instructions)
├── me.md (student profile, example)
│
└── [other project files]
```

---

## Reading Order (For You, the Student)

### Day 1: Conceptual Foundation
1. Read `ACC-Mental-Models-for-AI-Development.md` (35 min)
2. Read `ACC-Mental-Models-Quick-Reference.md` (5 min, re-read as needed)
3. Do the exercise in Section 8 of the Mental Models module

### Days 2-3: Technical Foundation (Prerequisite Course)
1. Read `ACC-Prerequisite-Course-Design.md` (overview)
2. Work through Modules 1-7 (2 days, ~16 hours)
3. Do Module 8 (Capstone Project)

### Day 4: Synthesis
- Read through both the mental models and prerequisite materials again
- Verify your understanding: can you explain each concept clearly?

### Days 5+: Ready for ACC
- Enter the ACC with confidence
- Notice the mental models in action throughout the course

---

## Key Vocabulary Reference

| Term | Module | Meaning |
|------|--------|---------|
| **Harness** | Mental Models 1 | LLM + tools together |
| **Agency** | Mental Models 1 | AI's ability to act independently |
| **Context Window** | Mental Models 2 | Working memory (tokens Claude can see) |
| **Token** | Mental Models 3 | Unit of text (~0.75 words) |
| **Tool Call** | Mental Models 4 | Request to execute something external |
| **Operator** | Mental Models 5 | You (supervising Claude's work) |
| **Posture** | Mental Models 5 | Your stance (supervising vs delegating) |
| **Cost-Conscious** | Mental Models 6 | Thinking about efficiency |
| **Vibe Coding** | Mental Models | Development without verification |
| **Deterministic** | Mental Models | Verifiable (not guessing) |
| **Repository** | Prerequisite 3 | Project folder managed by git |
| **Commit** | Prerequisite 3 | Snapshot of changes in git |
| **Markdown** | Prerequisite 4 | Structured plain-text format |
| **Pseudocode** | Prerequisite 5 | Logic written in English-like syntax |
| **Authentication** | Prerequisite 6 | Proving your identity (API keys, tokens) |
| **System Prompt** | Prerequisite 7 | Instructions that shape Claude's behavior |

---

## Common Questions

**Q: Do I have to do the prerequisite course if I already know terminal/git?**

A: The prerequisite course is for baseline competency. If you're strong on terminal and git, you can accelerate through Modules 2-3. But don't skip Module 1 (LLMs), 5 (programming concepts), 6 (tool setup), 7 (context files), or 8 (capstone). The capstone especially—it integrates everything.

**Q: What if I don't understand the mental models?**

A: Re-read them. Do the exercise in Section 8. Talk to an instructor. These are not optional—the ACC assumes you understand them. If you're confused, slow down.

**Q: How long does this all take?**

A: Mental models (35 min) + prerequisite course (16-20 hours) + integration time (a few days) = roughly 1 week of intensive learning before the ACC.

**Q: Can I skip parts of the prerequisite course?**

A: No. Every module builds on earlier ones. Don't skip Module 3 (Git) or you'll get stuck in Module 8 (Capstone). Don't skip Module 7 (Context Files) or you'll be confused in the ACC.

**Q: What if I already code in Python/JavaScript?**

A: Good. Module 5 (Programming Concepts) will feel familiar. But read it anyway—it covers problem-solving and debugging, not just syntax. Modules 1-4, 6-8 are still required.

**Q: What's the difference between mental models and the prerequisite course?**

A: **Mental Models** are conceptual (how AI, tools, and humans work together). **Prerequisite Course** is technical (terminal, git, code, tools). You need both.

---

## Instructor Notes

**For teaching this curriculum:**

1. **Mental Models first.** It's short (35 min). Start here. Everything else makes sense after.

2. **Don't rush the prerequisite course.** It's 16-20 hours of hands-on learning. Each module builds.

3. **The capstone is essential.** It integrates all 7 modules. Students who skip it or phone it in will struggle in the ACC.

4. **Supervised practice.** Especially for Modules 2-3 (terminal/git), students learn by doing under guidance, not by lectures.

5. **Normalize troubleshooting.** When students say "it's broken," say "great, let's debug." Troubleshooting is a skill.

6. **Context files (Module 7) are powerful.** Students who understand CLAUDE.md and me.md will excel in the ACC.

---

## Transition to ACC

Upon completion of this curriculum, students are ready for the Agentic Commanders Course because they:

✓ Understand the mental models that shape AI-assisted development  
✓ Know what prompts are and how to write clear ones  
✓ Can navigate the terminal confidently  
✓ Understand Git and GitHub workflows  
✓ Can write clear Markdown  
✓ Know basic programming concepts  
✓ Have all developer tools installed and authenticated  
✓ Have written CLAUDE.md and me.md files  
✓ Have shipped a real project to GitHub  
✓ Understand their role as operator and supervisor  

**The ACC assumes all of this.** Day 1 starts immediately with project work. No remediation time.

---

**End of Curriculum Index**

Use this as a navigation guide. Start with Mental Models. Work through the prerequisite course. You'll be ready.
