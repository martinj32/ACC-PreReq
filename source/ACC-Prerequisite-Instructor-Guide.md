# ACC Prerequisite Course — Instructor Preparation Guide

**For:** Instructors teaching the ACC Foundations prerequisite course  
**Purpose:** Detailed implementation guide, demo scripts, troubleshooting, and timing guidance  
**Last Updated:** 2026-06-05

---

## Quick Reference: Module at a Glance

| Module | Duration | Setup Time | Key Deliverable | Instructional Mode |
|--------|----------|-----------|-----------------|-------------------|
| **M1: LLM & Prompts** | 90 min | 5 min | 5 prompts | Demo + hands-on |
| **M2: Terminal** | 120 min | 10 min | Terminal transcript | Guided labs |
| **M3: Git** | 120 min | 20 min | Commits + push | Guided labs |
| **M4: Markdown** | 90 min | 5 min | Markdown doc | Independent + review |
| **M5: Programming** | 120 min | 10 min | 3 programs | Pseudocode-first |
| **M6: Tools** | 90 min | 30 min | Verification checklist | Lab + troubleshooting |
| **M7: Context Files** | 90 min | 5 min | CLAUDE.md + me.md | Template + iteration |
| **M8: Capstone** | 180 min | 30 min | GitHub repo | Mentored project |

**Total:** ~900 minutes (15 hours) of instruction spread over 2-3 days  
**Instructor Preparation:** ~4-6 hours before first cohort

---

## Pre-Course Instructor Setup

### **1. Test Your Environment (2 hours before class)**

Run these checks so you can demo confidently:

```bash
# Terminal shell works
bash --version

# Git works
git --version
cd /tmp && git init test-repo && cd test-repo && git commit --allow-empty -m "test"

# Node or Python installed (for Module 5 & 8)
node --version  # or python --version

# Claude Code installed
claude --version
claude  # starts and connects

# GitHub CLI works
gh auth status
gh repo view --web  # shows web page

# VS Code launches
code --version
code .  # opens VS Code on current folder

# Markdown preview works in VS Code
# (extension installed)
```

**If anything fails:** Stop and fix it. You cannot troubleshoot student problems if you haven't hit them yourself.

### **2. Prepare Demo Files (1 hour)**

Create a folder `/_classroom-demos/` with:

```
_classroom-demos/
├── M1-prompts/
│   ├── good-prompt.txt
│   ├── vague-prompt.txt
│   └── iterated-prompts.md
├── M2-terminal/
│   ├── demo-commands.sh
│   └── sample-files/
├── M3-git/
│   ├── merge-conflict-example/
│   └── commit-log-example.txt
├── M4-markdown/
│   ├── example-readme.md
│   ├── example-documentation.md
│   └── syntax-reference.md
├── M5-programming/
│   ├── pseudocode-template.txt
│   ├── grade-calculator.js
│   ├── coffee-machine.js
│   └── debugging-examples.js
├── M6-tools/
│   ├── verify-tools.sh
│   └── .env-example
├── M7-context/
│   ├── example-CLAUDE.md
│   ├── example-me.md
│   └── conflict-matrix-example.md
└── M8-capstone/
    ├── capstone-rubric.pdf
    ├── project-ideas.txt
    └── example-project-github-link.txt
```

### **3. Prepare Your Screen Setup (30 min)**

**Recommended for teaching:**
- **Monitor 1:** VS Code with demo file (students see this)
- **Monitor 2:** Terminal window (or same monitor, split screen)
- **Monitor 3 (optional):** Instructor notes / timer / student tracker

Use a terminal multiplexer (tmux) to split your screen if you have one monitor:

```bash
tmux new-session -s teaching -x 200 -y 50
# Split into editor + terminal
tmux split-window -h
# Left pane: VS Code demo file
# Right pane: Terminal with git/CLI commands
```

### **4. Write Instructor Notes for Each Module (1 hour)**

For each module, prepare:
- **Learning objective (1 sentence)**
- **Key stumbling block** (where students get stuck)
- **Verbal explanation (2-3 sentences)** — what you'll say
- **Demo script** — exact commands to run
- **Common questions and answers**
- **Timing markers** (if running long, what to skip)

Example for Module 2 (Terminal):

```markdown
## Module 2: Terminal Basics

**Learning Objective:** Students navigate confidently and manipulate files.

**Key Stumbling Block:** Path confusion (relative vs absolute). 
Expect 30% of class to struggle here.

**Your Opener (30 sec):**
"The terminal is just another way to talk to your computer. 
If you can drag files in Finder, you can do the same in a terminal—
just with words instead of a mouse. Let's start."

**Demo 1: Navigation (5 min)**
```bash
pwd                    # Show where you are
cd ~                   # Home directory
ls                     # List files
ls -la                 # Show hidden files
cd projects            # Change to a folder
pwd                    # Confirm location
```
**Observation:** Students watch. Then they do the same.

**Common Question:** "What's the difference between `cd /` and `cd ./`?"
**Answer:** "Absolute path starts at the root of the whole computer (`/`). 
Relative path starts from where you are (`.`). 
Both can take you places, but absolute never changes."
```

---

## Module-by-Module Teaching Tips

### **Module 1: LLM & Prompts (90 min)**

**Setup:** Open Claude (web or Claude Code), VS Code with a markdown file for notes

**The Opener (2 min):**
"Claude is a language model. It's a pattern-prediction machine trained on text. 
You give it words, it predicts the next words based on what it's seen before. 
Our job is to give it clear instructions—prompts—so it predicts what we need."

**Walk Students Through:**

1. **Bad Prompt Experiment (15 min)**
   ```
   Vague: "What is networking?"
   Better: "In 200 words, explain how a junior officer should build 
            professional relationships with peers and superiors."
   ```
   - Show both responses side-by-side
   - Ask: "What changed?"
   - Let them answer (specificity, context, length)

2. **System Prompt Demo (10 min)**
   - Show same question answered by "a drill sergeant" vs "a kindergarten teacher"
   - Emphasize: the system prompt shapes tone, vocabulary, depth
   - Don't get lost in technical details

3. **Context Window Boundary (10 min)**
   - Paste a long document (10,000+ words) into Claude
   - Ask it a question (it handles fine)
   - Ask it a question about something on page 1 (might forget)
   - Key insight: **context is finite, and you should know the limit**
   - For Claude 3: ~200,000 tokens (roughly 150,000 words)

4. **Iterative Refinement (10 min)**
   - Start with mediocre prompt
   - Get a mediocre response
   - Refine the prompt
   - Get a better response
   - Show: **one prompt is never final; iteration wins**

**Common Confusions:**
- "Isn't it just a chatbot?" → "It's more like a very sophisticated next-word predictor. You're steering it with prompts."
- "Will it always give the same answer?" → "No. It uses probability. Two prompts that mean the same thing might get different answers."
- "How much context can I use?" → "Roughly 200k tokens. If your document is longer than a novel, you might hit the limit. We'll cover that in Module 9 (future course)."

**Timing:** If running long, skip the context window experiment, just tell them the number.

**Deliverable Check:** Students submit 5 prompts. Review for clarity and specificity, not perfection.

---

### **Module 2: Terminal Basics (120 min)**

**Setup:** Each student has a terminal open. You're demonstrating on your screen.

**The Opener (2 min):**
"The terminal is just another language for talking to your computer. 
Graphically, you use a mouse. Here, you use words. Same computer, same files, different interface."

**Absolute Beginner Adjustment:**
If >50% of class has never opened a terminal, add 15 min of "terminal orientation" before diving in.
```bash
# Show them what they're looking at
ls        # Lists files, same as Finder icon view
pwd       # Where am I? (like the folder icon in Finder)
cd        # Go to a folder (like double-clicking)
```

**Walk Them Through the Exercises:**

1. **Orientation Walk (15 min)** — You demo, they type
   - You type `pwd` on your screen, they type `pwd` on theirs
   - Confirm everyone sees the same home directory path
   - Move to 5 different folders, each time:
     - You navigate: `cd /usr/local`
     - They follow
     - Everyone does `pwd` to confirm
     - Everyone does `ls` to see what's inside

2. **File Manipulation Sprint (25 min)**
   - Demonstrate once, then they do it:
     ```bash
     mkdir -p projects/acc-prep/module-2
     cd projects/acc-prep/module-2
     touch file1.txt file2.txt file3.txt
     ls
     cp file1.txt file1-backup.txt
     mv file1-backup.txt backup.txt
     rm file3.txt
     ls
     ```
   - Checkpoint: Have everyone `ls` and confirm they have 3 files (file1.txt, file2.txt, backup.txt)

3. **Path Puzzle (20 min)**
   - You're at `/home/user/projects/`. You want to go to `/home/user/documents/archive/`
   - Show three ways: absolute, relative from projects, relative from home
   - They practice writing paths on a piece of paper, then testing them in terminal
   - Key insight: **paths are just addresses. Absolute addresses start at `/`. Relative addresses start at your current location.**

4. **Help System (15 min)**
   - Show: `ls --help` output
   - "This is your cheat sheet. Every command has one."
   - Have them lookup 3 flags: `-l`, `-a`, `-r`
   - They write a reference card with their findings

5. **Piping and Redirection (25 min)**
   - **Piping example:**
     ```bash
     ls -la | grep "txt"    # Show only .txt files
     ls | wc -l             # Count files
     ```
   - **Redirection example:**
     ```bash
     ls > files.txt         # Save list to file
     echo "hello" >> notes.txt   # Append to file
     cat files.txt          # Read the file
     ```
   - Key insight: **Piping connects commands. Redirection saves output.**

6. **Real-World Scenario (20 min)**
   - Scenario: "Find all .txt files modified in the last week and list them by date."
   - Walk them through:
     ```bash
     find . -name "*.txt" -mtime -7
     find . -name "*.txt" -mtime -7 | sort
     ```
   - Emphasize: **problem-solving with commands builds with time, not memorization.**

**Common Stuck Points:**
- **"Permission denied"** → They tried to `rm` a system file or access `/root/`. Redirect to a safe sandbox folder.
- **"Command not found"** → They typed a typo or the tool isn't installed. Use `which` to check.
- **"No such file or directory"** → They're in the wrong folder or used a wrong path. Have them `pwd` and `ls` to verify where they are.
- **Relative path confusion** → Have them practice 5 times in a row with different folders.

**Timing:** This is the slowest module for absolute beginners. Don't rush.

**Deliverable Check:** Run their command transcript. Do they show the 6 exercises completing?

---

### **Module 3: Git Basics (120 min, split across 2 sessions)**

**Setup:** Each student has a code editor (VS Code) and terminal side-by-side

**The Opener (2 min):**
"Git is a time machine for your code. Every time you save a version of your code (a 'commit'), 
Git remembers what it looked like. You can jump back to any earlier version, 
see what changed, and work on multiple ideas at once (branches)."

**Session 1: Local Repository (60 min)**

1. **Init a Repo (10 min)**
   ```bash
   cd /tmp
   mkdir my-first-repo
   cd my-first-repo
   git init
   git config user.email "you@example.com"
   git config user.name "Your Name"
   ```
   - Explain: `git init` creates a `.git/` folder (hidden)
   - That folder is where Git stores all the history
   - `.git/` is invisible but crucial

2. **Create and Commit (15 min)**
   ```bash
   echo "# My First Project" > README.md
   git status                # See unstaged changes
   git add README.md         # Stage the file
   git status                # See staged changes
   git commit -m "Initial commit: add README"
   git log                   # See the commit history
   ```
   - Checkpoint: Everyone runs `git log` and sees their commit

3. **Make Changes and Commit (10 min)**
   ```bash
   echo "This is a test project." >> README.md
   git diff                  # See what changed
   git add README.md
   git commit -m "Update README with description"
   git log --oneline         # See compact log
   ```
   - Key insight: **Each commit is a snapshot. Diffs show what changed between snapshots.**

4. **Branching (15 min)**
   ```bash
   git branch feature/add-docs      # Create a branch
   git checkout feature/add-docs    # Switch to it (or git switch)
   git branch                       # See all branches
   echo "Docs here" > DOCS.md
   git add DOCS.md
   git commit -m "Add documentation file"
   git switch main                  # Switch back
   ls                               # DOCS.md is gone (it's on the other branch)
   ```
   - Key insight: **Branches are separate lines of work. Switching branches changes your files.**

5. **Merge (10 min)**
   ```bash
   git merge feature/add-docs       # Merge the branch into main
   ls                               # DOCS.md is now here
   git branch -d feature/add-docs   # Delete the branch (optional)
   ```
   - Explain: **Merge brings changes from another branch into the current branch.**

**Session 2: Remote Repository & Conflicts (60 min)**

1. **Set Up GitHub Repo (10 min)**
   - Go to GitHub.com, create a new repo (call it `my-first-repo`)
   - Copy the HTTPS clone URL
   - Back in terminal:
     ```bash
     git remote add origin <URL>
     git branch -M main              # Ensure main branch exists
     git push -u origin main         # Push to GitHub
     ```
   - Verify on GitHub.com — the repo appears with your commits

2. **Clone a Repo (10 min)**
   ```bash
   cd /tmp
   git clone https://github.com/octocat/Hello-World.git
   cd Hello-World
   git log                           # See the history
   ```
   - Key: **Cloning downloads a full copy of the project and its history.**

3. **Merge Conflicts (25 min)**
   - **Create a conflict scenario:**
     ```bash
     # On main
     echo "Line 1: Version A" > conflict-demo.txt
     git add conflict-demo.txt
     git commit -m "Add conflict-demo.txt with version A"
     
     # Create branch
     git checkout -b feature/version-b
     echo "Line 1: Version B" > conflict-demo.txt
     git add conflict-demo.txt
     git commit -m "Change to version B"
     
     # Back to main
     git checkout main
     echo "Line 1: Version A - Updated" > conflict-demo.txt
     git add conflict-demo.txt
     git commit -m "Update version A"
     
     # Try to merge — CONFLICT!
     git merge feature/version-b
     ```
   - Show the conflict markers in the file
   - Explain: Git doesn't know which version is right, so it asks you
   - Resolve by choosing one (or manually editing)
     ```bash
     # Edit the file, keep the version you want
     git add conflict-demo.txt
     git commit -m "Resolve conflict: keep version A"
     ```

4. **Meaningful Commits (10 min)**
   - Bad commit messages: "fix", "update", "work"
   - Good commit messages: "Fix login validation error", "Add password strength check"
   - Emphasis: **Your future self (and teammates) need to understand what you changed and why.**

5. **Real Workflow Practice (10 min)**
   - Scenario: Add a feature, commit it, push it, verify on GitHub
   ```bash
   git checkout -b feature/add-footer
   echo "Footer content" >> README.md
   git add README.md
   git commit -m "Add footer to README"
   git push origin feature/add-footer
   ```
   - On GitHub, show the new branch appearing

**Common Stuck Points:**
- **"fatal: origin already exists"** → They're re-adding origin. Use `git remote -v` to check, then `git remote remove origin` if needed.
- **Merge conflicts feeling overwhelming** → Walk through one example slowly, then have them create a practice conflict. It gets easier.
- **"I lost my commits!"** → They did a `git reset --hard`. Reassure them: commits are still there (`git reflog`), but this is advanced. For now: don't do that.
- **Authentication fails** → Check `gh auth status`. If not logged in, run `gh auth login`.

**Timing:** Merge conflicts and pushing to GitHub are new concepts. Don't rush.

**Deliverable Check:** Repo on GitHub with 5+ commits and a successful push.

---

### **Module 4: Markdown (90 min)**

**Setup:** VS Code with Markdown preview extension enabled

**The Opener (2 min):**
"Markdown is how developers write. It's plain text that looks nice when rendered as HTML. 
You'll write READMEs, documentation, and even prompts in Markdown."

**Show, Don't Tell:**
- Open an example README.md in raw view (ugly, shows #, *, etc.)
- Open the preview (beautiful, formatted)
- Emphasize: **Markdown is the source, preview is the output.**

**Walk Them Through:**

1. **Markdown Anatomy (15 min)**
   - Create a file `demo.md`
   - Add elements one by one, toggling preview:
     ```markdown
     # Heading 1
     ## Heading 2
     ### Heading 3
     
     This is a **bold** word and an *italic* word.
     
     - Bullet 1
     - Bullet 2
       - Nested bullet
     
     1. Numbered 1
     2. Numbered 2
     
     `inline code` and code blocks:
     ```javascript
     console.log("Hello");
     ```
     
     [Link text](https://example.com)
     ![Alt text](image.jpg)
     
     | Header 1 | Header 2 |
     |----------|----------|
     | Cell 1   | Cell 2   |
     ```
   - As you add each element, toggle preview and show the output

2. **Personal README (20 min)**
   - Students write about themselves:
     - Name (h2)
     - Role (paragraph)
     - Skills (bullet list)
     - Interests (paragraph with **bold** emphasis)
     - Favorite command (inline code)
   - Checkpoint: Everyone toggles preview and shows themselves

3. **Code Blocks with Syntax (15 min)**
   - Key: ` ```language ` for syntax highlighting
   ```markdown
   ```python
   def hello():
       return "world"
   ```
   
   ```bash
   echo "Hello"
   ```
   
   ```javascript
   console.log("Hello");
   ```
   ```
   - Insight: **Pick the right language for highlighting.**

4. **Tables (10 min)**
   ```markdown
   | Feature | Tool A | Tool B |
   |---------|--------|--------|
   | Speed   | Fast   | Slow   |
   | Cost    | $100   | Free   |
   | Ease    | Hard   | Easy   |
   ```
   - Practice alignment (`:---` left, `:---:` center, `---:` right)

5. **Documentation Project (25 min)**
   - Choose a simple process (how to make coffee, debug code, etc.)
   - Write it in Markdown with:
     - Main heading
     - Sections (h2)
     - Numbered steps
     - Code blocks if applicable
     - A table of contents at the top
   - Target: 300-500 words, properly formatted
   - Outcome: One complete, formatted Markdown document

6. **YAML Frontmatter (5 min)**
   ```markdown
   ---
   title: My Document
   author: Your Name
   date: 2026-06-05
   ---
   
   # Content starts here
   ```
   - Explanation: **Metadata that some tools read, but humans skip.**

**Common Confusions:**
- "Do I need to use Markdown?" → "Everywhere. README files, documentation, prompts to Claude, even your commit messages benefit from being clear like Markdown."
- "Can I mix HTML?" → "Yes, but Markdown is cleaner. Stick to Markdown unless you need HTML."
- "What about tables?" → "Markdown tables are basic but work. They're a little ugly to write but look great rendered."

**Deliverable Check:** Submit one Markdown file with at least 5 syntax elements (headings, bold/italic, lists, code blocks, one more).

---

### **Module 5: Programming Concepts (120 min)**

**Key Philosophy:** Pseudocode first, code second. If students can think through the logic, syntax is just typing.

**Setup:** VS Code with JavaScript runtime (Node.js) or Python available

**The Opener (3 min):**
"Programming is problem-solving. You break a big problem into small steps, 
write them in pseudocode (English-like), then translate pseudocode to real code. 
The syntax (exact words, punctuation) matters, but the logic is what counts."

**Walk Them Through:**

1. **Variables and Types (15 min)**
   - Pseudocode:
     ```
     name = "Alice"
     age = 25
     codes = true
     
     next_year_age = age + 1
     greeting = "Hello, " + name + ". Next year you'll be " + next_year_age
     
     show greeting
     ```
   - Translate to JavaScript:
     ```javascript
     const name = "Alice";
     const age = 25;
     const codes = true;
     
     const nextYearAge = age + 1;
     const greeting = `Hello, ${name}. Next year you'll be ${nextYearAge}`;
     
     console.log(greeting);
     ```
   - Run it. Show the output.
   - Insight: **Variables store data. Types matter (string vs number).**

2. **Control Flow: If/Else (20 min)**
   - Scenario: "Coffee shop charges different prices by size."
   - Pseudocode:
     ```
     size = "medium"
     
     if size is "small":
       price = 3
     else if size is "medium":
       price = 4
     else if size is "large":
       price = 5
     else:
       price = 0
     
     show price
     ```
   - JavaScript:
     ```javascript
     const size = "medium";
     let price;
     
     if (size === "small") {
       price = 3;
     } else if (size === "medium") {
       price = 4;
     } else if (size === "large") {
       price = 5;
     } else {
       price = 0;
     }
     
     console.log(price);
     ```
   - Key: **`if` checks a condition. If true, run this code. Else, run that code.**

3. **Loops: For and While (20 min)**
   - Scenario: "Print the word 'Go' ten times."
   - Pseudocode:
     ```
     repeat 10 times:
       show "Go"
     ```
   - JavaScript:
     ```javascript
     for (let i = 0; i < 10; i++) {
       console.log("Go");
     }
     ```
   - Scenario 2: "Sum all numbers from 1 to 100."
   - Pseudocode:
     ```
     total = 0
     for number from 1 to 100:
       total = total + number
     show total
     ```
   - JavaScript:
     ```javascript
     let total = 0;
     for (let i = 1; i <= 100; i++) {
       total = total + i;
     }
     console.log(total);
     ```
   - Key: **Loops repeat code. You're automating repetition.**

4. **Functions: Reusable Logic (20 min)**
   - Scenario: "A greeting function."
   - Pseudocode:
     ```
     function greet(name):
       return "Hello, " + name + "!"
     
     show greet("Alice")
     show greet("Bob")
     ```
   - JavaScript:
     ```javascript
     function greet(name) {
       return `Hello, ${name}!`;
     }
     
     console.log(greet("Alice"));
     console.log(greet("Bob"));
     ```
   - Scenario 2: "A function that checks password strength."
   - Pseudocode:
     ```
     function is_strong_password(password):
       if length of password >= 8:
         return true
       else:
         return false
     
     show is_strong_password("abc")     # false
     show is_strong_password("abcdefgh") # true
     ```
   - JavaScript:
     ```javascript
     function isStrongPassword(password) {
       return password.length >= 8;
     }
     
     console.log(isStrongPassword("abc"));     // false
     console.log(isStrongPassword("abcdefgh")); // true
     ```
   - Key: **Functions take input (parameters), do something, return output. You call them multiple times.**

5. **Debugging: Reading Errors (20 min)**
   - Show 5 intentionally buggy code snippets:
     ```javascript
     // Bug 1: Missing semicolon (usually caught by editor)
     const x = 5
     console.log(x)
     
     // Bug 2: Off-by-one error
     for (let i = 1; i <= 5; i++) {
       console.log(i);
     } // This prints 1,2,3,4,5 — correct!
     
     // Bug 3: Undefined variable
     console.log(myVariable);  // Error: myVariable is not defined
     
     // Bug 4: Wrong comparison operator
     if (age = 18) {  // Oops, = not ==
       console.log("Adult");
     }
     
     // Bug 5: Logic error
     function max(a, b) {
       if (a < b) return a;  // Should be a > b
       else return b;
     }
     ```
   - Walk through each: "What's the error? What should it be?"
   - Insight: **Read error messages carefully. They tell you what went wrong.**

6. **Pseudocode Planning (25 min)**
   - Scenario: "Build a grade calculator. Input: test scores. Output: average + letter grade."
   - Pseudocode first:
     ```
     scores = [85, 90, 78, 92]
     
     total = sum of all scores
     average = total / number of scores
     
     if average >= 90:
       grade = "A"
     else if average >= 80:
       grade = "B"
     else if average >= 70:
       grade = "C"
     else:
       grade = "F"
     
     show "Average: " + average + ", Grade: " + grade
     ```
   - JavaScript:
     ```javascript
     const scores = [85, 90, 78, 92];
     
     const total = scores.reduce((a, b) => a + b, 0);
     const average = total / scores.length;
     
     let grade;
     if (average >= 90) grade = "A";
     else if (average >= 80) grade = "B";
     else if (average >= 70) grade = "C";
     else grade = "F";
     
     console.log(`Average: ${average}, Grade: ${grade}`);
     ```
   - Test edge cases: what if all scores are 100? What if all are 60?

**Common Stuck Points:**
- **"I don't understand variables."** → Real-world analogy: "A variable is a box. You put data in it, label it, and later you take the data out."
- **"How do I know which loop to use?"** → "For loop if you know how many times. While loop if you know the stopping condition but not the count."
- **"What's the difference between = and ==?"** → "Single = assigns a value. Double == compares two values."
- **"Arrays are confusing."** → Show an array as a list: `const fruits = ["apple", "banana", "orange"]. Then: `fruits[0]` is "apple"."

**Deliverable Check:** 3 small programs (a greeting function, a loop, a conditional). Code should be readable, commented, and runnable.

---

### **Module 6: Developer Tools Setup (90 min)**

**Critical:** This module has the most blocking issues. Test your environment thoroughly beforehand.

**The Opener (1 min):**
"You need a toolbox. Claude Code, GitHub, VS Code, and a shell. Let's get them all running."

**Walk Them Through:**

1. **Install Claude Code (15 min)**
   - Run: `claude --version`
   - If it fails, troubleshoot (missing install, PATH issue, etc.)
   - Run: `claude` and have them interact (ask it "what is today's date?")
   - Checkpoint: Everyone has a working Claude Code session

2. **GitHub CLI (15 min)**
   - Install `gh`: `brew install gh` (macOS) or `choco install gh` (Windows) or `sudo apt install gh` (Linux)
   - Authenticate: `gh auth login` (choose HTTPS)
   - Verify: `gh auth status`
   - Clone a test repo: `gh repo clone octocat/Hello-World`
   - Checkpoint: Everyone has successfully cloned a repo

3. **VS Code Setup (10 min)**
   - Install VS Code
   - Open a folder in VS Code
   - Install 2-3 extensions: Markdown Preview, Git Graph, Prettier
   - Show: syntax highlighting, preview pane
   - Checkpoint: Everyone has VS Code running

4. **Environment Variables and .env (15 min)**
   - Create a `.env` file:
     ```bash
     API_KEY=my-secret-key-123
     DATABASE_URL=postgres://localhost:5432/mydb
     DEBUG=true
     ```
   - Explain: "These are settings for your app. Never commit this to git."
   - Show: `.gitignore` should exclude `.env`
     ```
     .env
     .env.local
     *.log
     node_modules/
     ```

5. **Verification Checklist (20 min)**
   - Have students run and screenshot:
     ```bash
     claude --version
     node --version
     git --version
     gh --version
     code --version
     ```
   - All should return a version number (not "command not found")
   - Checkpoint: Everyone has a complete checklist

6. **Troubleshooting Practice (10 min)**
   - Walk through common issues:
     - "command not found" → Use `which` to check PATH, reinstall if needed
     - "Permission denied" → Likely a shell script that needs `chmod +x`
     - "Module not found" → Missing dependency, need to install
   - Have them practice: "If you get 'command not found', what's the first thing you'd do?" (Answer: `which` + `echo $PATH`)

**Common Stuck Points (This Module is CRITICAL):**
- **Windows PATH issues:** Windows doesn't update PATH automatically. Restart the terminal after install.
- **GitHub auth fails:** They may not have a GitHub account or didn't install `gh`. Help them here.
- **Node/Python not installed:** They'll need to install one or the other. Recommend Node (simpler for this cohort).
- **VS Code extensions not found:** Extensions can be searched and installed from VS Code's extensions panel.

**Deliverable Check:** Checklist showing all tools installed and working (`claude --version`, etc.).

---

### **Module 7: Context Files (90 min)**

**The Opener (2 min):**
"CLAUDE.md is the instruction manual for your project. me.md is the manual for you. 
Together, they tell Claude Code how to help you best."

**Walk Them Through:**

1. **Understanding CLAUDE.md (15 min)**
   - Show an example CLAUDE.md (from d1-kit-alpha)
   - Highlight sections:
     - Project name and goal
     - What it's NOT (scope boundaries)
     - Files Claude can modify
     - Decision-making rules (if speed vs thoroughness matter)
   - Key: **CLAUDE.md constrains Claude's behavior. It says "this is what we're building and how."**

2. **Understanding me.md (10 min)**
   - Show an example me.md
   - Sections:
     - Name and role
     - Decision style (fast/slow, risk tolerance)
     - Communication preference (BLUF first, detail, examples)
     - What you value
   - Key: **me.md tells Claude how YOU work. "I like BLUF first." "I prefer examples over theory."**

3. **Conflict Resolution Matrix (15 min)**
   - When speed vs thoroughness collide, which wins in your world?
   - Create a simple matrix:
     ```markdown
     | Trade-off | Winner | Why |
     |-----------|--------|-----|
     | Speed vs Security | Security | We're building for the military |
     | Simplicity vs Features | Simplicity | We launch in 2 weeks |
     | Cost vs Performance | Cost | Budget is fixed |
     ```
   - Students create their own for a hypothetical project

4. **Write Your me.md (15 min)**
   - Students complete their own me.md:
     - Name: your role in the military or your civilian role
     - Decision style: do you like fast / slow / data-driven / gut-feel?
     - Communication: BLUF first, examples, details, jokes?
     - Values: speed, clarity, thoroughness, innovation?
     - Claude preference: "I like when Claude explains," "I prefer working code over explanation," etc.

5. **Write a Project CLAUDE.md (20 min)**
   - Scenario: "Simple task manager for Marines."
   - Students write a CLAUDE.md that includes:
     - Project: Task manager for field teams
     - Goal: Track 1-5 tasks per operator, mark complete
     - Not: user auth, cloud sync, mobile app
     - Constraints: Terminal only, no external dependencies, OPSEC safe
     - Files Claude can modify: *.js, tests/, README.md
     - Files Claude cannot modify: .env, package.json
     - Success: MVP works, commits are clean

6. **Set Up a Project (15 min)**
   - Create a folder: `my-practice-project`
   - Create `.claude/` inside it
   - Add `CLAUDE.md` and `me.md`
   - Run Claude Code in that folder
   - Ask Claude: "What are we building?" (It should cite your CLAUDE.md)
   - Outcome: Claude acknowledges your context

**Deliverable Check:** CLAUDE.md + me.md for a real project (or hypothetical). Rubric: clarity, enforceability, usefulness.

---

### **Module 8: Capstone Project (180 min, across multiple days)**

**The Opener (2 min):**
"You're going to build and ship a real project. Not a tutorial, not a code-along. 
A real thing that does something useful. Then you push it to GitHub."

**Setup:**
- Have students pick their path (CLI tool, web app, or API integration)
- Provide three template CLAUDE.md files (one per path)
- Have them clone/fork a starter template (optional, not required)

**Coaching Throughout (Not Direct Answers):**
- "What does the error message say?" (instead of "here's the fix")
- "Can you draw what this should do?" (instead of "here's the code")
- "What would you do if I wasn't here?" (instead of "use npm install")
- "That's good progress. What's next?" (instead of "now do X")

**Checkpoint Moments (Formative Assessment):**
- **After planning (20 min):** "Can you tell me in one sentence what you're building?"
- **After setup (40 min):** "Show me your folder structure. What's in each file?"
- **After first feature (100 min):** "Does it run? Show me it working."
- **After iteration (140 min):** "What did you change after testing? Why?"
- **After push (170 min):** "Show me your GitHub repo with your commits."

**Deliverable Check:**
- GitHub repo link
- Proof of 5+ commits (they used git)
- README.md (documented)
- Code runs (tested)
- Rubric: Does it work (50%), documented (20%), commits (15%), iteration (10%), polish (5%), bonus (+5%)

---

## Troubleshooting Quick Reference

### **Student Can't Authenticate**
```bash
# Check GitHub CLI
gh auth status

# If not logged in
gh auth login
# Choose HTTPS (easier for beginners)
# Authenticate in browser when prompted

# Check Claude Code
claude --version

# If not working, reinstall
# macOS: brew install anthropic/cli/claude
# Windows: choco install claude
# Linux: Instructions vary by distro
```

### **"Command Not Found"**
```bash
# Check if command exists
which <command>

# If not found, install it or add to PATH
# Check PATH
echo $PATH

# If tool was just installed, restart terminal
```

### **Terminal Path Confusion**
```bash
# Show where you are
pwd

# List files in current directory
ls

# Move to a specific directory
cd /path/to/folder

# Move up one level
cd ..

# Move to home
cd ~
```

### **Git Merge Conflicts**
```bash
# See conflict status
git status

# Edit the conflicted file, choose the version you want

# Stage the resolved file
git add <file>

# Complete the merge
git commit -m "Resolve conflict in <file>"
```

### **VS Code Markdown Preview Not Working**
- Install "Markdown Preview Enhanced" extension
- Or install "Markdown All in One" extension
- Restart VS Code
- Open a `.md` file and press `Cmd+Shift+V` (Mac) or `Ctrl+Shift+V` (Windows/Linux)

### **JavaScript/Node Issues**
```bash
# Check if Node is installed
node --version

# If not, install from nodejs.org

# Run a JS file
node filename.js

# Run Node interactively
node
# Type: console.log("Hello")
# Exit: Ctrl+D or .exit
```

### **Git Push Fails**
```bash
# Verify remote is set
git remote -v

# If origin missing
git remote add origin <URL>

# If wrong URL
git remote remove origin
git remote add origin <new-URL>

# Try again
git push -u origin main
```

---

## Timing and Pacing Guide

### **For a Cohort Moving at Standard Pace**

| Day | Morning | Afternoon | Evening |
|-----|---------|-----------|---------|
| **D1** | M1 (90m) + M2 (120m) = 210m | M3-Part1 (60m) + Break + M3-Part2 (60m) + M4 (45m) = 165m | Lab + review |
| **D2** | M4-finish + M5 (120m) = 165m | M6 (90m) + M7 (90m) = 180m | Capstone prep |
| **D3** | M8-Capstone (AM) = 240m | M8-Capstone (PM) + presentations = 180m | Celebration |

### **For a Cohort Moving Faster (Skip Stretch Content)**
- Skip "optional" demos (context window experiment, em-dash preservation in Markdown)
- Combine M1 + M2 into one "morning block" if group knows terminal
- Do capstone in one long day (10 hours) instead of two

### **For a Cohort Moving Slower**
- Add a "Terminal Mastery" day between M2 and M3 (extra 90 min practice)
- Extend M5 into two half-days (programming concepts are dense)
- Allow capstone to roll into a "bonus day 4" if needed

---

## Assessment and Grading

### **Per-Module Rubric (Simplified)**

| Module | Artifact | Pass Criteria |
|--------|----------|--------------|
| **M1** | 5 prompts | 4/5 are clear, specific, coherent |
| **M2** | Terminal transcript | 8/10 commands correct, navigation successful |
| **M3** | Commits + push | Commits have messages, push succeeds |
| **M4** | Markdown doc | 5+ syntax elements, readable |
| **M5** | 3 programs | All run, logic is correct |
| **M6** | Checklist | All tools installed, all version checks pass |
| **M7** | CLAUDE.md + me.md | Both complete, coherent, enforceable |
| **M8** | GitHub repo | 5+ commits, README, code runs |

### **Overall Grade Calculation**
- 7/8 modules passed = **Passed, ACC-ready**
- 8/8 modules passed + capstone >80% = **Honors**
- <7/8 = Offer remediation or next cohort

---

## Resources for Instructors

### **Slides and Demos**
- Keep demo files in a shared GitHub repo (`_classroom-demos/`)
- Slides should be copy-paste friendly (include all commands)
- Record one demo of each module for students to rewatch later (optional but high value)

### **Handout Templates**
- Terminal cheat sheet (common commands)
- Git workflow diagram (init → add → commit → push)
- Markdown quick reference
- JavaScript syntax cheat sheet (variables, functions, loops)

### **Bonus Materials (If Time)**
- "Debugging Mindset" worksheet (how to think when code breaks)
- "Pseudocode Planning" template (fill-in form for breaking down problems)
- "Code Review Checklist" (what to look for when reviewing student projects)

---

## Common Instructor Questions

**Q: A student is way ahead. What do I give them?**
A: Capstone stretch goals (deploy to Vercel, add tests, second feature). Or pair them with a struggling student as a peer mentor.

**Q: A student is falling way behind.**
A: Assess where they got lost (usually terminal or git). Pair them with you during lab time for a 30-min focused catch-up. Don't slow the whole group.

**Q: Can I skip Module X?**
A: No. Every module is a prerequisite for the next. M2 (terminal) is required for M3 (git). M5 (programming) is required for M8 (capstone). Can't skip.

**Q: Can I teach this online?**
A: Yes, with adjustments. Use breakout rooms for pair programming. Record demos. Use screen-sharing for troubleshooting. Assign 1-on-1 office hours for tool setup (authentication, PATH issues).

**Q: What's the hardest part for students?**
A: **Tie:** Terminal path concepts and programming logic. Give these modules extra time and practice.

---

## Instructor Success Checklist

Before teaching your first cohort, verify:

- [ ] You've completed all 8 modules yourself
- [ ] You've hit the main bugs in your environment and fixed them
- [ ] Demo files are ready in `_classroom-demos/`
- [ ] You have working examples of every exercise
- [ ] You've written instructor notes for each module
- [ ] You've set up your screen layout (code editor + terminal visible)
- [ ] You have a timer (visible to students, for pacing)
- [ ] You've practiced one 5-minute demo (do it fast, confidently)
- [ ] You know your "unstuck" phrases: "What does the error say?", "What did you expect?", "Try it yourself first."
- [ ] You have a system for capturing student questions and parking them (whiteboard?)

---

**End of Instructor Guide**

You're ready to teach. The course works. The students will learn. Help them stay stuck just long enough to solve it themselves—that's where learning lives.
