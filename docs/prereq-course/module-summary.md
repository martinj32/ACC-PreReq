# AI and Agentics Basics — Module Quick Reference

**Condensed view of all 8 modules for quick planning and prep.**

---

## Module 1: LLM & Prompts

| Aspect | Detail |
|--------|--------|
| **Duration** | 90 minutes |
| **Learning Goal** | Understand LLMs, write clear prompts, iterate based on feedback |
| **Key Concepts** | Prompt → response, system prompts, specificity, context windows, temperature, tokens |
| **Materials** | Claude (web or Code), text editor |
| **Hands-On** | 5 exercises: bad vs good prompts, system prompt experiment, clarity exercise, context boundary, iterative prompting |
| **Deliverable** | 5 well-written prompts |
| **Key Insight** | "Specificity wins. Vague prompts get vague answers." |
| **Common Stumble** | "Context windows? How big is too big?" Reassure: for this course, assume ~200k tokens. Advanced limit-testing is later. |

---

## Module 2: Terminal Basics

| Aspect | Detail |
|--------|--------|
| **Duration** | 120 minutes |
| **Learning Goal** | Navigate filesystem, manipulate files, use command flags, pipe/redirect |
| **Key Concepts** | pwd, cd, ls, mkdir, touch, cp, mv, rm, >, >>, \|, man pages, PATH |
| **Materials** | Terminal, any shell (bash, zsh, PowerShell) |
| **Hands-On** | 6 exercises: navigation walk, file manipulation sprint, path puzzle, help system, piping/redirection, real-world scenario |
| **Deliverable** | Terminal transcript showing 6 completed exercises |
| **Key Insight** | "The terminal is just another interface. Same files, same folders—just words instead of mouse clicks." |
| **Common Stumble** | **Path confusion.** Students mix absolute (`/home/user/file.txt`) and relative (`./file.txt`, `../docs/`). Practice this 5+ times. |

---

## Module 3: Git Basics

| Aspect | Detail |
|--------|--------|
| **Duration** | 120 minutes (split: 60 min local, 60 min remote/conflicts) |
| **Learning Goal** | Init repos, commit changes, branch, merge, push to GitHub, resolve conflicts |
| **Key Concepts** | git init, git add, git commit, git log, git branch, git checkout/switch, git merge, git push, merge conflicts, `.gitignore` |
| **Materials** | Terminal, Git CLI, GitHub account, `gh` CLI |
| **Hands-On** | 6 exercises: init & commit, branching sprint, cloning & pushing, merge conflicts, commit messages, `.gitignore` |
| **Deliverable** | GitHub repo with 5+ commits, successful push |
| **Key Insight** | "Git is a time machine. Every commit is a snapshot. You can jump back, try new ideas on branches, and merge them in." |
| **Common Stumble** | **Merge conflicts.** Students panic. Walk through once slowly, let them do one practice conflict. It gets comfortable fast. |

---

## Module 4: Markdown

| Aspect | Detail |
|--------|--------|
| **Duration** | 90 minutes |
| **Learning Goal** | Write clear, structured Markdown documents |
| **Key Concepts** | Headers, bold/italic, lists, code blocks, tables, links, YAML frontmatter |
| **Materials** | Text editor, Markdown preview (VS Code extension) |
| **Hands-On** | 6 exercises: markdown anatomy, personal README, code blocks with syntax, tables, documentation project, YAML frontmatter |
| **Deliverable** | One complete Markdown document (README, documentation, or personal bio) |
| **Key Insight** | "Markdown is the lingua franca of developers. You'll use it everywhere: READMEs, docs, prompts, even commit messages." |
| **Common Stumble** | "Tables are annoying to write in Markdown." True. Show them a table generator online, or just accept the slightly ugly raw format. |

---

## Module 5: Programming Concepts

| Aspect | Detail |
|--------|--------|
| **Duration** | 120 minutes |
| **Learning Goal** | Understand variables, logic, loops, functions, debugging |
| **Key Concepts** | Variables, types (string, number, boolean), operators, if/else, for/while loops, functions, pseudocode, debugging, arrays |
| **Materials** | Code editor, Node.js (or Python), terminal |
| **Hands-On** | 6 exercises: variables & types, if/else, loops (for/while), functions, debugging buggy code, pseudocode planning → implementation |
| **Deliverable** | 3 small programs (greeting function, conditional logic, loop example) |
| **Key Insight** | "Programming is problem-solving. Pseudocode (English-like) comes first. Syntax is just translating that to code." |
| **Common Stumble** | **Logic confusion.** Students understand syntax but get confused by logic flow (off-by-one errors, infinite loops). Use pseudocode-first approach rigorously. |

---

## Module 6: Developer Tools Setup

| Aspect | Detail |
|--------|--------|
| **Duration** | 90 minutes |
| **Learning Goal** | Install and authenticate all required tools; understand PATH and environment variables |
| **Key Concepts** | Claude Code, `gh` CLI, VS Code, Node.js (or Python), git, environment variables, `.env` files, `.gitignore`, authentication tokens |
| **Materials** | Computer with admin access, package manager (brew, apt, choco, etc.) |
| **Hands-On** | 6 exercises: install Claude Code, GitHub auth, VS Code setup, .env files & .gitignore, tool verification checklist, troubleshooting practice |
| **Deliverable** | Checklist showing all tools installed and authenticated |
| **Key Insight** | "You need a toolbox. Every tool works together: Claude writes code, git tracks it, GitHub stores it, VS Code edits it." |
| **Common Stumble** | **Windows PATH:** Windows doesn't auto-update PATH after install. Solution: restart the terminal or restart computer. **GitHub auth:** Make sure `gh` is installed before trying `gh auth login`. |

---

## Module 7: Context Files — CLAUDE.md & me.md

| Aspect | Detail |
|--------|--------|
| **Duration** | 90 minutes |
| **Learning Goal** | Write CLAUDE.md and me.md; understand how context shapes Claude's behavior |
| **Key Concepts** | System prompts, project context, personal operating profile, conflict resolution matrices, scope boundaries, decision rules |
| **Materials** | Text editor, examples of CLAUDE.md and me.md files |
| **Hands-On** | 6 exercises: analyze example CLAUDE.md, write personal me.md, write project CLAUDE.md, conflict resolution matrix, set up project context, verify context is read |
| **Deliverable** | CLAUDE.md + me.md for a real (or hypothetical) project |
| **Key Insight** | "CLAUDE.md tells Claude what to build. me.md tells Claude how you work. Together, they make Claude your perfect teammate." |
| **Common Stumble** | Students write generic CLAUDE.md (doesn't constrain anything). Fix: "What SHOULDN'T Claude modify? What's out of scope?" Real constraints are powerful. |

---

## Module 8: Capstone Project

| Aspect | Detail |
|--------|--------|
| **Duration** | 180 minutes (can span 1-2 days or 1 long day) |
| **Learning Goal** | Integrate all concepts: plan → code → commit → push; troubleshoot real problems; ship something real |
| **Key Concepts** | Project planning, full git workflow, iterative development, documentation, testing, pushing to GitHub |
| **Materials** | All tools from modules 1-7 |
| **Hands-On** | Choose one path: CLI tool, web app, or API integration. Build it. Test it. Document it. Push to GitHub. |
| **Deliverable** | Working project on GitHub with 5+ commits, README, and working code |
| **Key Insight** | "You're not building a tutorial project. You're building something real, shipping it, and proving you can do this." |
| **Common Stumble** | Students under-scope (build something too simple) or over-scope (try to build too much). Instructor guidance: "Can you demo this in 2 minutes? If not, it's too big." |

---

## Prerequisite Dependency Map

```
                Module 1
                  LLM & Prompts
                      |
                      v
    Module 2               Module 4
    Terminal Basics        Markdown
         |                     |
         v                     v
    Module 3         [can run in parallel]
    Git Basics
         |
         +---> Module 5
         |     Programming
         |         |
         |         v
         +---> Module 6
         |     Tools Setup
         |         |
         +---> Module 7
         |     Context Files
         |         |
         v---------v
       Module 8
       Capstone Project
```

**Critical path:** M1 → M2 → M3 → M5 → M8 (avoid skipping any)

**Can run in parallel:** M4 (Markdown) while others are sinking in

**Must complete before M8:** M5, M6, M7

---

## Daily Time Allocation (for 2-3 day format)

### **Day 1: Foundations (8 hours)**
- 8:00-9:30: **M1** (90 min)
- 9:30-10:00: Break
- 10:00-12:00: **M2** (120 min)
- 12:00-1:00: Lunch
- 1:00-2:30: **M3 Part 1** (90 min, first half)
- 2:30-2:45: Break
- 2:45-4:15: **M3 Part 2** (90 min, second half)
- 4:15-5:00: **M4** (45 min, intro)
- 5:00-6:00: Lab + troubleshooting

**Homework:** Finish M4, preview M5

### **Day 2: Intermediate (8 hours)**
- 8:00-9:30: **M4 finish + M5 intro** (90 min)
- 9:30-10:00: Break
- 10:00-12:00: **M5** (120 min)
- 12:00-1:00: Lunch
- 1:00-2:30: **M6** (90 min)
- 2:30-2:45: Break
- 2:45-4:15: **M7** (90 min)
- 4:15-5:00: Readiness check
- 5:00-6:00: Lab + capstone prep

**Homework:** Finalize context files, pick capstone project

### **Day 3 (Optional): Capstone (6-8 hours)**
- 8:00-12:00: **M8 Part 1** (240 min, planning + first half of build)
- 12:00-1:00: Lunch
- 1:00-5:00: **M8 Part 2** (240 min, second half + presentations)

---

## Success Indicators by Module

| Module | Student Can… |
|--------|--------------|
| **M1** | Write a specific prompt, iterate on feedback, explain why context matters |
| **M2** | Navigate the terminal, create/delete files, use pipes and redirects |
| **M3** | Create commits with clear messages, create and merge branches, push to GitHub |
| **M4** | Write Markdown with 5+ syntax elements, toggle preview, see the HTML output |
| **M5** | Write pseudocode, translate it to code, debug a syntax or logic error |
| **M6** | Run version checks on all tools, authenticate to GitHub, set up a .env file |
| **M7** | Write a CLAUDE.md that constrains behavior, write a me.md that reflects their style |
| **M8** | Build, test, document, commit, and push a real project to GitHub |

---

## Grading Rubric Summary

### **Module-Level Grading**
- **Pass:** Deliverable is complete and meets 80%+ of rubric
- **Pass with revision:** Deliverable has gaps; student needs to revise
- **Not yet:** Deliverable is incomplete; significant work remains

### **Course-Level Grading**
- **7/8 modules passed:** Course completion
- **8/8 modules passed + capstone >80%:** Honors (distinguished mastery)
- **<7/8:** Remediation needed; not yet at completion level

---

## Stretch Goals (If Time)

### **For Fast Finishers**

**Module 1:** Prompt engineering with vision (multimodal prompts)

**Module 2:** Advanced piping (`find`, `grep`, `sed` combinations)

**Module 3:** Rebase workflow, stashing, orphan branches

**Module 4:** Markdown for slides (Reveal.js or similar)

**Module 5:** Recursion, higher-order functions (map/filter/reduce)

**Module 6:** Docker basics (optional, advanced)

**Module 7:** Multi-repo configuration, shared context templates

**Module 8:** Deployment (Vercel for web, npm publish for CLI, GitHub releases)

---

## Common Misconceptions and Corrections

| Misconception | Reality | Clarification |
|---|---|---|
| "Terminal is dangerous." | It's just an interface. | You can't break anything by typing. Worst case: delete a file (recoverable with git). |
| "Git is complicated." | It's simpler than you think. | Three commands get you 90% of the way: `git add`, `git commit`, `git push`. |
| "I have to memorize syntax." | No. Look it up every time. | Real developers use `git --help` and Stack Overflow constantly. |
| "Markdown is for documentation only." | It's everywhere. | Prompts, slides, READMEs, chat, static site generators. Learn it once, use it forever. |
| "Programming is for people who are 'math people.'" | False. | It's problem-solving, not math. Logic > algebra. |
| "I don't have the right computer." | Probably you do. | Windows, Mac, Linux all work. Cloud VMs work. Even Chromebooks can do most of this (harder). |

---

## Materials Checklist

**Instructor provides:**
- [ ] Slides (one per module)
- [ ] Demo files (`_classroom-demos/` folder)
- [ ] Rubrics (one per module)
- [ ] Troubleshooting guide (this document + more)
- [ ] Example CLAUDE.md and me.md files
- [ ] Capstone project examples (one per path)
- [ ] Solutions guide (for grading + office hours)

**Students provide:**
- [ ] Computer (any OS)
- [ ] GitHub account
- [ ] Time and attention

---

## Additional Resources for Instructors

**Recording of Past Cohorts:**
- Record at least one demo per module for students to rewatch
- Archive in shared folder (Dropbox, Google Drive, or GitHub)

**Recorded Q&A Sessions:**
- Hold async office hours; record common questions + answers
- Post in course repo for future cohorts

**Community Forum / Slack:**
- Create a channel for students to ask questions and help each other
- Reduces "stuck" feelings and builds community

**Cheat Sheets for Students:**
- Terminal command reference (one page)
- Git workflow diagram (one page)
- Markdown quick reference (one page)
- JavaScript/Python syntax cheat sheet (one page)

---

## Course Completion and Next Steps

**Upon completion of this course, students will be able to:**

✓ Understand what LLMs are and how to prompt them clearly  
✓ Navigate the terminal confidently  
✓ Use Git and GitHub for version control  
✓ Write clear Markdown documentation  
✓ Apply basic programming concepts (variables, logic, functions)  
✓ Have all developer tools installed and authenticated  
✓ Create and manage context files (CLAUDE.md, me.md)  
✓ Ship a real working project to GitHub  

**These are the core skills for AI-assisted development.** Students who complete all 8 modules are ready for advanced agentic work.

---

**End of Module Summary**

Use this as a quick reference during planning and teaching. Detailed guidance is in the full Prerequisite Course Design and Instructor Guide.
