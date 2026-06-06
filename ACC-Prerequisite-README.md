# ACC Prerequisite Course Design Package

**Complete curriculum design for students with zero background knowledge preparing for the Agentic Commanders Course (ACC)**

---

## What's in This Package

This folder contains a complete, production-ready prerequisite course design for the Agentic Commanders Course (ACC). It includes:

### **1. ACC-Prerequisite-Course-Design.md** (Main Document)
**The complete curriculum outline.**
- 8 modules spanning 2-3 days
- Learning objectives, key concepts, and hands-on exercises for each module
- Detailed learning progression and module dependencies
- Daily schedule examples (standard, accelerated, and slower paces)
- Grading rubric and assessment criteria
- Appendices with glossary and sample rubrics

**Use this to:** Understand the full scope, plan your cohort schedule, share with stakeholders.

### **2. ACC-Prerequisite-Instructor-Guide.md** (Teaching Implementation)
**Step-by-step guidance for delivering the course.**
- Pre-course setup checklists (test environment, demo files, screen layout)
- Module-by-module teaching tips with demo scripts and timing
- Common student stuck points and solutions
- Troubleshooting quick reference
- Pacing guidance for different cohort speeds
- Assessment and grading details
- Instructor success checklist

**Use this to:** Prepare to teach the course, run your daily classes, troubleshoot problems as they arise.

### **3. ACC-Prerequisite-Module-Summary.md** (Quick Reference)
**One-page summaries of all 8 modules.**
- Module at a glance (duration, goals, deliverables)
- Prerequisite dependency map
- Daily time allocation
- Success indicators by module
- Common misconceptions and corrections
- Materials checklist
- Stretch goals for fast finishers

**Use this to:** Quick planning, student handout, daily pacing reference.

### **4. This File (ACC-Prerequisite-README.md)**
**Package overview and implementation guide.**

---

## Course At a Glance

| Aspect | Detail |
|--------|--------|
| **Duration** | 2-3 days (15 hours total) |
| **Target Students** | No background in LLMs, CLI, Git, Markdown, or programming |
| **Modules** | 8 hands-on modules |
| **End State** | Students ready for ACC Day 1 |
| **Delivery Model** | Instructor-led, hands-on labs, peer discussion |
| **Tools Required** | Claude Code, VS Code, Git, GitHub, terminal, Node.js (or Python) |
| **Instructor Prep Time** | 4-6 hours before first cohort |
| **Passing Criteria** | 7/8 modules completed at 80%+ quality |

---

## The 8 Modules

```
Module 1: LLM & Prompts (90 min)
   ↓
Module 2: Terminal Basics (120 min)
   ↓
Module 3: Git Basics (120 min)
   ↓
Module 4: Markdown (90 min) — can run in parallel with 2-3
   ↓
Module 5: Programming Concepts (120 min)
   ↓
Module 6: Developer Tools Setup (90 min)
   ↓
Module 7: Context Files — CLAUDE.md & me.md (90 min)
   ↓
Module 8: Capstone Project (180 min)
```

**Total instructor preparation:** ~4-6 hours  
**Total instruction:** ~15 hours spread over 2-3 days  
**Student effort outside class:** ~5-10 hours (homework, practice, capstone)

---

## How to Use This Package

### **Step 1: Read All Three Documents (1-2 hours)**
1. Start with **ACC-Prerequisite-Course-Design.md** for the full vision
2. Skim **ACC-Prerequisite-Instructor-Guide.md** to understand the teaching flow
3. Reference **ACC-Prerequisite-Module-Summary.md** for quick lookups

### **Step 2: Plan Your Cohort (1 hour)**
- Decide: 2-day intensive, or 3-day (slower pace)?
- How many students? Any accelerated or slower learners?
- When will you teach? (Next month? Next quarter?)
- Do you have an assistant instructor? (Helpful for modules 5-8)

### **Step 3: Prepare Your Environment (2 hours)**
- Run through pre-course checklist (ENV test, demo files, screen setup)
- Create `_classroom-demos/` folder with example files
- Write instructor notes for each module (or use the guide as-is)
- Test one live demo end-to-end

### **Step 4: Set Up Materials (1-2 hours)**
- Slides (create or use existing templates)
- Rubrics (customize from samples in the guide)
- Handout cheat sheets (terminal, git, markdown, javascript)
- Capstone project rubric and examples

### **Step 5: Run Your First Cohort (2-3 days + office hours)**
- Day 1: Modules 1-4
- Day 2: Modules 5-7
- Day 3 (optional): Module 8 capstone
- Follow-up: Office hours for tool setup and capstone troubleshooting

### **Step 6: Iterate Based on Feedback**
- Collect student feedback (what worked, what was confusing)
- Note timing adjustments (was 90 minutes too long? too short?)
- Improve demos and examples based on student questions
- Document and share improvements with future cohorts

---

## Key Design Principles

### **1. Hands-On First, Theory Second**
Every module starts with a **problem students solve**, not a lecture. Examples:
- Module 1: "Write a prompt, get a response, see how specificity helps."
- Module 2: "Navigate the filesystem, create files, practice paths."
- Module 5: "Write pseudocode for a real problem, then translate to code."

### **2. Maximize "Aha" Moments**
Learning sticks when students discover it themselves. The instructor guides the discovery but doesn't skip ahead:
- "What does the error message say?" (not "do this instead")
- "What would you do if I wasn't here?" (not "type this command")

### **3. Build Incrementally**
Each module builds on previous ones:
- Terminal → Git → Capstone (you need CLI skills for Git, Git skills for shipping projects)
- Programming concepts → Capstone (you need logic to build real apps)

### **4. Normalize Confusion**
- "Everyone struggles with merge conflicts. Here's three examples."
- "Relative paths trip up professionals. You're not alone."
- "Bugs are normal. Here's how to read error messages and fix them."

### **5. Practical, Not Academic**
Every concept connects to something students will do:
- "You'll write 100 prompts this year. Let's nail the skill."
- "Every project you ship uses Git. This is not optional."
- "Your CLAUDE.md will save hours of back-and-forth with Claude."

---

## Typical Student Experience

### **Day 1 Morning**
- 8:00 AM: Arrive, open terminal/VS Code
- 8:30 AM: Module 1 — learn how prompts work, write 5 of them
- 10:00 AM: Break
- 10:15 AM: Module 2 — navigate the filesystem like a pro
- 12:00 PM: Lunch

### **Day 1 Afternoon**
- 1:00 PM: Module 3 Part 1 — create your first Git repo, make commits
- 2:30 PM: Break
- 2:45 PM: Module 3 Part 2 — push to GitHub, handle a merge conflict
- 4:15 PM: Module 4 intro — learn Markdown
- 5:00 PM: Lab time, troubleshooting

### **Day 1 Evening**
- Finish Module 4 homework at home

### **Day 2**
- Modules 5, 6, 7 (Programming, Tools, Context Files)
- Capstone project prep

### **Day 3 (Optional)**
- Build and ship your capstone project (CLI tool, web app, or API integration)
- Present to the group
- Celebrate before moving to ACC Day 1

### **Post-Course**
- Office hours for tool setup issues
- Help with capstone if students need it
- Transition to ACC, which starts immediately with Day 1 intensity

---

## Instructor Decision Points

### **Pacing: Which Timeline Works for Your Cohort?**

**Option A: 2-Day Intensive (16-hour days)**
- All 8 modules in 2 long days
- Good for: motivated, experienced learners who can absorb fast
- Risk: burnout, incomplete capstone
- Recommendation: Use Module 8 stretch goals to let capstone overflow to a async "Week 1 of ACC"

**Option B: 3-Day Standard (8-hour days, this package's default)**
- Days 1-2: Modules 1-7
- Day 3: Capstone
- Good for: most cohorts
- Timing: very close to this package
- Best balance of depth and momentum

**Option C: 4-Day Slower (6-hour days)**
- Add an extra day for Module 5 (Programming)
- Slower learners appreciate the breathing room
- Good for: diverse experience levels in the cohort

**Option D: Online Async**
- Each module is self-contained and works on video
- Record your demos, students watch on their own schedule
- Office hours for Q&A and pair programming
- Capstone is synchronous (they need help)

### **Group Dynamics: What's Your Cohort Like?**

**Mostly experienced (they've coded, used Git):**
- Skip/accelerate modules 2, 3, 5
- Spend more time on modules 1, 6, 7 (these are new to everyone)
- Capstone: stretch goals (deploy, tests, second feature)

**Mostly inexperienced (no coding background):**
- Extend module 5 (programming) into two sessions
- Add a "Terminal Mastery Drill Day" after Module 2
- Keep capstone simple (CLI tool or single-page web app)
- Budget extra office hours for tool setup

**Mixed experience:**
- Pair experienced students with inexperienced ones (peer mentoring)
- Have stretch goals ready for fast finishers
- Keep modules self-paced where possible

### **Capstone Scope: Which Path Matters Most?**

**CLI Tool (recommended for military/structured ops background):**
- Example: task manager, note taker, credential validator
- Simplest to troubleshoot (text in, text out, no graphics)
- Easiest to deploy (just ship the code, no hosting)

**Web App (good for visual learners):**
- Example: calculator, unit converter, quote generator
- Requires HTML/CSS/JS (3 languages to juggle)
- Easy to demo (just open in a browser)
- Easiest to deploy (Vercel, GitHub Pages)

**API Integration (for advanced learners):**
- Example: weather app, stock ticker, joke generator
- Requires authentication and error handling (realistic)
- Shows integration with real-world systems
- Good portfolio piece

---

## Troubleshooting Common Course Issues

### **"We're way behind schedule. Do we drop anything?"**
No. Every module is a prerequisite. Instead:
- Keep daily order (can't skip M2, M3, M5 before M8)
- Reduce practice repetitions if needed (instead of 5 path-navigation exercises, do 3)
- Combine M4 + M7 (both use .md files, some overlap)
- Shorten capstone (MVP only, skip stretch goals)
- But don't skip; just accelerate

### **"Some students know this stuff already."**
Have acceleration paths ready:
- Module 2 (Terminal): Skip basics, practice piping/grep/find
- Module 3 (Git): Skip init, do rebase + stashing
- Module 5 (Programming): Skip pseudocode, do recursion + higher-order functions
- Module 8 (Capstone): Deploy to production, write tests, do second feature

### **"A student can't get a tool working (GitHub auth, Claude setup, etc.)."**
This is normal and happens every cohort:
- For blocking issues (can't authenticate), pair the student with an instructor 1:1 during lab time
- Don't slow the whole group; the rest keep going
- Use troubleshooting guide (tool refresh, restart terminal, check PATH, reinstall if needed)
- If unresolved after 15 min of pairing, move them to async office hours and have them catch up after class

### **"Students are overwhelmed."**
Normalize it:
- "Learning feels hard because your brain is growing."
- "Confusion is the feeling of learning. Stay with it."
- Offer optional Thursday "office hours" lab session
- Encourage peer pairing (sometimes students help each other faster than instructor)

### **"Capstone ideas are too ambitious."**
Redirect before building:
- "Can you demo this in 2 minutes without bugs?" If not: scope down
- "What's the absolute minimum version?" Build that first, add features later
- Capstone rubric weights **does it work** at 50%. Simplicity is rewarded, complexity that breaks is not

---

## Assessment and Grading

### **Module-Level (Formative)**
- Each module has a deliverable (prompts, transcript, commits, markdown file, programs, checklist, context files, GitHub repo)
- Grading: pass/pass-with-revision/not-yet
- **Pass:** 80%+ of rubric criteria met
- **Pass-with-revision:** <80%, student revises and resubmits
- **Not-yet:** Incomplete, significant work remains

### **Course-Level (Summative)**
- **Passing:** 7/8 modules passed → eligible for ACC
- **Honors:** 8/8 modules passed + capstone >80% → ready to excel in ACC
- **Remediation:** <7/8 modules → retake next cohort or take 1:1 tutoring on missing modules

### **No Failing Grade**
- If a student doesn't pass, they redo the module, get help, and try again
- This is not a test; it's a ramp
- Everyone who completes the course is ready for ACC

---

## After Students Complete This Course

**They will have:**
- ✓ Opened Claude and written 100+ prompts
- ✓ Navigated the terminal 50+ times
- ✓ Made 20+ commits and resolved merge conflicts
- ✓ Written 5+ Markdown documents
- ✓ Built and debugged 3+ programs
- ✓ Installed and authenticated 6+ development tools
- ✓ Written their own CLAUDE.md and me.md
- ✓ Shipped a real project to GitHub

**They will understand:**
- What LLMs are, how to interact with them clearly
- That the terminal is just another interface, not scary
- Git workflows and why version control matters
- How to document clearly and why it matters
- Basic programming logic (not syntax, logic)
- Why context (CLAUDE.md, me.md) shapes behavior
- How to ship code and iterate based on feedback

**They will be ready for ACC because:**
- The ACC assumes all of this knowledge
- Day 1 of ACC starts at full speed (Vertex auth, Daily 8, permissions, building apps)
- There's no review time in ACC; remediation has to happen before
- Completing this course proves they can learn at the pace ACC demands

---

## Instructor Success Factors

### **Before Course Starts**
- [ ] You've done every exercise in this course yourself (yes, even the capstone)
- [ ] You've hit common bugs and fixed them (authentication, PATH, merge conflicts)
- [ ] You've written demo files and test scripts
- [ ] You've timed every module (is 90 min right for M1? for your pace? adjust)
- [ ] You have a troubleshooting mindset (not "here's the answer" but "what does the error say?")

### **During Course**
- [ ] You ask "What does the error message say?" instead of giving answers
- [ ] You let students be stuck for 5-10 minutes before helping (that's where learning lives)
- [ ] You normalize confusion: "Everyone struggles here. Here's 3 people who had this same issue."
- [ ] You have students explain their understanding back to you (accountability)
- [ ] You adjust timing (if M2 is taking too long, it's okay to extend; something else compresses)

### **After Course**
- [ ] You collect feedback and iterate on the course
- [ ] You document what worked and what didn't for next cohort
- [ ] You celebrate students' capstone projects (they built something real!)
- [ ] You warm-handoff students to ACC (email ACC instructor, introduce students in person if possible)

---

## File Organization for Your Course Folder

```
ACC-Prerequisite-Course/
├── README.md (this file)
├── ACC-Prerequisite-Course-Design.md (full curriculum)
├── ACC-Prerequisite-Instructor-Guide.md (teaching guide)
├── ACC-Prerequisite-Module-Summary.md (quick ref)
│
├── _instructor-prep/
│   ├── environment-setup.sh (test script for your computer)
│   ├── demo-scripts/ (one per module)
│   ├── slides/ (PowerPoint or Markdown slides)
│   ├── rubrics/ (one per module)
│   └── solutions/ (answer keys for exercises)
│
├── _classroom-demos/
│   ├── M1-prompts/
│   ├── M2-terminal/
│   ├── M3-git/
│   ├── M4-markdown/
│   ├── M5-programming/
│   ├── M6-tools/
│   ├── M7-context/
│   └── M8-capstone/
│
├── _student-materials/
│   ├── cheatsheets/ (terminal, git, markdown, javascript)
│   ├── templates/ (CLAUDE.md template, me.md template, etc.)
│   ├── examples/ (example capstone projects)
│   └── faqs.md (common student questions)
│
└── _recordings/
    └── module-demos/ (video recordings of live demos)
```

---

## Next Steps

1. **Read** all three documents (Course Design, Instructor Guide, Module Summary)
2. **Plan** your cohort timing (2-day intensive? 3-day standard?)
3. **Prepare** demo files, slides, and rubrics
4. **Test** your environment and practice one demo
5. **Teach** your first cohort (give yourself grace; it's okay if timing is off)
6. **Iterate** based on feedback
7. **Celebrate** your students' capstone projects
8. **Transition** them to ACC Day 1

---

## Questions?

- **For specific teaching questions:** See ACC-Prerequisite-Instructor-Guide.md
- **For curriculum structure questions:** See ACC-Prerequisite-Course-Design.md
- **For quick reference:** See ACC-Prerequisite-Module-Summary.md
- **For module details:** Jump to that module in the Course Design

---

## Version History

- **v1.0** (2026-06-05): Initial release. 8 modules, 2-3 day format, production-ready.

---

**This course bridges students from zero to ACC-ready in 15 hours. You've got this.**
