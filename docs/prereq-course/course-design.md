# AI and Agentics Basics — Course Design
## Technical Foundations Curriculum

**Target Audience:** Students with NO background knowledge in LLMs, command-line development, version control, or coding concepts.

**Duration:** 2-3 days  
**Total Modules:** 8  
**Format:** Hands-on, project-based learning with immediate application

---

## Course Overview

This course bridges students from zero knowledge to a solid foundational competency in AI-assisted development. Upon completion, students will:

1. Understand what LLMs are, how they work, and how to interact with them
2. Navigate and manipulate file systems confidently from the command line
3. Understand and use Git for basic version control workflows
4. Write clear, structured Markdown for documentation and prompts
5. Understand fundamental programming concepts (variables, functions, logic flow)
6. Set up and authenticate development tools
7. Troubleshoot basic technical problems independently

**Philosophy:** Learn by doing. Every concept is introduced through a real problem students solve themselves, not a lecture they watch. Hands-on exercises always come before abstract concepts.

---

## Course Structure: 8 Modules Over 2-3 Days

### **DAY 1: Foundations of Interaction**

#### **Module 1: "Hello, Claude" — LLMs and Prompts**
*Duration: 90 minutes*

**Learning Objectives:**
- Understand what an LLM is and how it generates text
- Distinguish between prompts and system prompts
- Write clear, specific prompts that get useful responses
- Recognize and avoid common prompt-writing mistakes

**Key Concepts:**
- What is a large language model? (Visual: scaling laws, training data)
- The difference between a prompt (user input) and system prompt (instructions)
- Tokens and context windows (practical, not theoretical)
- Temperature, top-p, and why they matter to you
- The problem with vague prompts, the power of specificity
- Prompt patterns: step-by-step, role-playing, explicit output format
- RGCOA prompt structure: Role, Goal, Context, Output, Asks. Components:
  - **Role** -- the expert perspective the model should apply
  - **Goal** -- the specific task, single and concrete
  - **Context** -- background required to do the task well
  - **Output** -- format, length, structure, and tone
  - **Asks** -- tell the model what to do when it lacks information, what to flag, and what not to assume. Example: "If you need information I haven't provided, ask me before proceeding. Do not invent facts. If you find a contradiction between the source material and a previous instruction, flag it rather than picking one." The Asks element is where you give the model permission to surface uncertainty instead of papering over it with a plausible-sounding guess.

**Hands-On Exercises:**

1. **Ice-Breaker Prompt** (15 min)
   - Open Claude AI (web version)
   - Prompt 1: "What is the weather?"
   - Prompt 2: "I live in Quantico, VA. What outdoor activities are good this time of year?"
   - Observe: How does specificity change the answer?
   - Outcome: One paragraph reflection on what changed

2. **System Prompt Experiment** (20 min)
   - Task: Interview Claude AS a Marine Corps drill sergeant, then AS a kindergarten teacher
   - Method: Use the same interview question; change the system prompt by starting with "You are a..."
   - Observe: How does the system prompt change tone, vocabulary, detail level?
   - Outcome: Screenshot both responses with notes on 3 differences

   Note: Typing "You are a [role]" in the user turn is persona injection -- you are instructing the model mid-conversation, and that instruction is visible in the chat history. A true system prompt is loaded by the platform before the conversation begins and is invisible to the user during the conversation. The exercise demonstrates the behavioral effect of persona instructions; the distinction between user-turn persona and platform system prompt matters when you begin configuring harness files in this course.

3. **Clarity Matters** (20 min)
   - Vague prompt: "Write about networking."
   - Better prompt: "Write a 200-word guide on how to build professional relationships for a newly promoted junior officer."
   - Task: Re-write three vague prompts from a provided list to be specific and actionable
   - Outcome: Before/after comparison with an explanation of what improved

4. **The Context Window Boundary** (25 min)
   - Practical exercise: Paste a 10,000-word document, then ask Claude questions about it
   - Vary the context window (short doc vs long doc)
   - Observe: At what point does Claude miss details or struggle?
   - Outcome: Short log: "When context got [X] chars, Claude stopped [Y]"

5. **Iterative Prompting** (10 min)
   - Start with a vague prompt, get a mediocre response
   - Iterate 3 times, refining based on feedback
   - Track the improvement
   - Outcome: Conversation log with annotations on what changed each round

**Assessment:**
- Submission: A markdown document with 5 well-written prompts (one for each learning objective)
- Rubric: Clarity, specificity, realistic expectations, evidence of iteration

**Estimated Hands-On Time:** 85 minutes | **Lecture/Discussion:** 5 minutes

---

#### **Data Hygiene and OPSEC**

BLUF: the model is not the classification authority. You are. If you paste sensitive information into a consumer AI tool, you have made a disclosure decision. Know what you are doing before you type.

**What never goes into any AI tool:**

- Classified material at any level
- CUI (Controlled Unclassified Information -- defined below)
- PII: real names combined with any other identifier -- SSN, date of birth, home address, phone number, personal email, or any combination that could identify a person
- Personnel records: evaluations, medical, legal, disciplinary
- Operational planning detail: timelines, routes, objectives, force compositions
- Credentials and API keys: passwords, tokens, certificates -- never under any circumstances

**CUI defined:**

Controlled Unclassified Information is information requiring safeguarding per law, regulation, or government-wide policy, but not classified under an Executive Order. The legacy FOUO (For Official Use Only) marking is being replaced by CUI designations across the federal government. If a document is marked FOUO, it is CUI. Other common CUI categories students will encounter: Law Enforcement Sensitive (LES), personnel records, and unclassified intelligence information that reveals sources or methods.

One working rule: if the document carries ANY marking, or if it describes real people, real units, real operations, or real capabilities, it does not get pasted into a consumer AI tool. The marking is not required for the rule to apply -- the content triggers it.

**Where your prompts go:**

Consumer AI applications (Claude.ai, ChatGPT.com, and similar) transmit your input to a provider-operated backend. Depending on the service tier and opt-out settings, that input may be reviewed by humans or used in future model training. "This tool is impressive" is not the same as "this tool is authorized for work use." Authorization is a property of the contract your organization has signed and the system's ATO (Authority to Operate) -- not the capability of the tool or how widely your colleagues use it. Without an approved system designation and an ATO, a consumer application is not authorized for CUI input, regardless of how the tool is marketed.

**Local session logs:**

Claude Code writes conversation history to disk in the `.claude/` folder of your project. That log file is subject to the same handling requirements as its content. A log containing CUI requires the same protection as CUI. Scrub discipline applies to what you type, not just what you paste.

**Scrub checklist -- remove all of the following before pasting:**

- Real names (of any person)
- Real unit designations
- Real locations: base names, grid coordinates, facility names
- Dates tied to real operations or events
- Any document markings (CUI, FOUO, LES, classification)
- Phone numbers, personal email addresses, account identifiers
- Credentials, API keys, and passwords -- never under any circumstances
- System names and network names
- IP addresses belonging to real infrastructure

**Bracketed placeholder technique:**

Replace removed specifics with bracketed labels that describe the type of information. The model does not need the real identifier to help you. Examples: [NCO], [LOCATION], [UNIT], [DATE], [SYSTEM]. The model reasons about structure and process, not identity. Your scrubbed prompt is fully functional for the task.

**Hands-On: Scrub Drill**

The instructor provides a realistic-but-fabricated one-page document containing: a soldier's name and rank, a unit designation, a base name, a grid coordinate, a date, and a document marking. The document is fake but representative of what students handle daily.

Task: Produce a paste-safe version of the document using bracketed placeholders. Preserve the structure and substance. Remove everything on the scrub checklist.

Debrief: Each student explains what they removed and why. Instructor highlights any missed items. Class discusses: what information is retained after scrubbing, and whether the model can still accomplish the task with scrubbed input.

Outcome: A scrubbed version of the document plus a written list of what was removed and the category each item falls into.

---

#### **LLM Failure Modes**

BLUF: the model generates plausible text, not verified fact. These are the failure modes you will encounter. Know them before you rely on the output.

**Hallucination:**

The model has no truth-checking mechanism. It generates tokens that are statistically likely to follow the prior text, regardless of whether they correspond to fact. The model cannot distinguish "information I trained on accurately" from "a completion that sounds plausible." Confident output and correct output are entirely unrelated. A model can produce a detailed, well-cited, grammatically perfect answer that is entirely fabricated. The confidence of the response is not evidence of its accuracy.

**Knowledge cutoff -- three behaviors:**

The model has a training data cutoff: a point after which it has no direct knowledge. Students need to understand three distinct behaviors, not just "the model might be out of date":

- (a) The model flags uncertainty and tells you it may not have current information. This is the honest behavior. Do not mistake it for inability.
- (b) The model answers confidently using stale training data with no indication that the information may be wrong. This is the dangerous behavior. The model is not lying -- it does not know that time has passed. It answers with the same confidence it would apply to well-established facts.
- (c) The model has a retrieval or search tool and pulls current information from external sources. In this case, check whether the tool was actually invoked and verify the source.

Students must verify time-sensitive content regardless of which behavior they observe. The only safe assumption is that anything that could have changed since training may have changed.

**Nondeterminism:**

The model uses a temperature parameter that introduces randomness into each generation. The same prompt submitted twice will produce different output. For low-stakes tasks this is irrelevant. For high-stakes output -- analysis that will inform a decision, a document that will be forwarded -- run the prompt multiple times and compare results. Consistent answers across runs increase confidence. Divergent answers are a signal to verify before use.

**Hands-On: Hallucination in the Wild**

Task: Ask the model to produce five peer-reviewed academic papers on a narrow, specific topic. Request full citations: author, title, journal, year, volume, and page numbers. The model will produce plausible-sounding citations. Select one and attempt to verify it using an actual academic database (Google Scholar, PubMed, or similar).

The fabricated citation will typically be unverifiable. The exercise produces a hallucination reliably and makes the failure mode concrete before students depend on model output in a consequential context.

Debrief: What made the citation look legitimate? What would you have done if you had not verified it? Where else in your workflow might you accept plausible-sounding output without checking?

Outcome: A written record of the citation the model produced, the verification attempt, and a one-paragraph reflection on where hallucination risk is highest in your own work.

---

#### **Model Landscape: Knowing Your Tools**

BLUF: there is no single "the AI." There are model families, each with a tiered structure. Match the capability level to the task.

**Three major families:**

- Claude (Anthropic)
- GPT (OpenAI)
- Gemini (Google)

Each family has a different architecture, training process, and policy. Output quality, behavior, and capability vary. The course focuses on Claude. Students working in other environments will encounter GPT and Gemini and should apply the same analytical framework to both.

**Tier structure:**

Every major provider organizes its models into tiers: a fast, low-cost tier; one or more mid-range options; and a high-capability, higher-cost tier. The pattern is consistent across providers.

Claude's current tiers:

| Tier | Model | Use |
|------|-------|-----|
| Fast / cheap | Haiku | High-volume, low-complexity tasks |
| Balanced | Sonnet | Standard working model |
| Powerful / expensive | Opus | Complex reasoning, high-stakes analysis |

**When to use which tier:**

- Simple tasks (summarize, reformat, rewrite, translate): fast tier. Cost-effective, sufficient.
- Complex analysis, multi-step reasoning, planning, synthesis: capable tier. Pay for the ceiling you need.
- Running in a loop or processing many items at once: always fast tier. Cost compounds.
- Default for this course: Sonnet. It is the standard for all exercises unless otherwise specified.

Match the weapon to the target. Using Opus for bulk reformatting is waste. Using Haiku for a nuanced analytical task is risk.

**Names change:**

The specific model names above are current as of course development but will be superseded. Before each course run, verify current model names at docs.anthropic.com. Teach students the axis (fast/balanced/powerful), not a frozen roster of names. The axis persists; the names rotate.

---

#### **Module 2: The Terminal is Friendly — Command Line Basics**
*Duration: 120 minutes*

**Windows Students: Use WSL**

On Windows, use WSL (Windows Subsystem for Linux), not native PowerShell. PowerShell is a different environment with different commands. The command `touch` does not exist in PowerShell -- the equivalent is `New-Item filename`. Throughout this course, all terminal exercises assume a Linux/Unix environment. WSL provides that environment on Windows.

Install WSL: open PowerShell and run `wsl --install`. On Windows 11, no administrator privileges are required. The first launch will prompt you to create a Linux username and password -- use something you will remember, it is separate from your Windows login. After setup, open the WSL terminal for all course exercises.

Your Windows files are accessible inside WSL at `/mnt/c/Users/YourName/`. To navigate to your Windows Documents folder from inside WSL: `cd /mnt/c/Users/YourName/Documents`.

Path conversion rule: `C:\Users\Jake\Documents` becomes `/mnt/c/Users/Jake/Documents`. Backslashes become forward slashes. The drive letter (C) becomes lowercase after `/mnt/`. This conversion trips up every Windows beginner -- practice it explicitly in the path exercises.

VS Code integration: install the "WSL" extension in VS Code. From a WSL terminal, type `code .` to open the current folder in VS Code with full WSL integration. All terminal operations in VS Code's integrated terminal will then run in the WSL environment.

**Learning Objectives:**
- Navigate directories and list files confidently from the terminal
- Create, edit, and delete files and folders
- Understand PATH, home directory, and relative vs absolute paths
- Use basic command flags and understand help systems
- Run commands in sequence and understand exit codes

**Key Concepts:**
- The file system: folders, files, hierarchy
- Current working directory and the `pwd` command
- Listing files with `ls` and its flags
- Moving and copying files
- Creating and deleting files/folders
- The concept of a "path" — relative and absolute
- Understanding man pages and help flags (`--help`)
- Piping (|) and redirection (>, >>, <) basics
- Stopping a running command: press Ctrl+C. This sends an interrupt signal and stops the current process. Use it whenever a command hangs, runs too long, or you need to abort. Ctrl+C is the single most important key combination in the terminal -- name it explicitly and drill it.
- Environment variables and PATH
- Hidden files and dotfiles

**Hands-On Exercises:**

1. **Orientation Walk** (15 min)
   - Task: Start in the home directory, navigate to 5 different locations
   - Use `pwd` after each move to confirm location
   - `ls` to see what's in each folder
   - Create a simple text file in one of them
   - Outcome: Screenshot showing successful navigation and file creation

2. **File Manipulation Sprint** (25 min)
   - Create a folder structure: `projects/acc-prep/module-2/`
   - Inside: create 3 text files (use `touch` and `echo`)
   - Copy one file to another location
   - Rename a file
   - Delete a file
   - List the final structure
   - Outcome: Terminal transcript showing all steps

3. **Path Puzzle** (20 min)
   - Given a file at `/home/user/projects/claude/config.txt`, practice writing:
     - The absolute path to that file
     - The relative path from `/home/user/` to that file
     - The relative path from `/home/user/projects/` to that file
   - Navigate using those paths to verify they work
   - Outcome: Markdown document with path examples and proof they work

4. **The Help System** (15 min)
   - Task: Use `man ls`, `ls --help`, `help cd` to answer questions
   - Questions like: "What does the -l flag do?" "What about -a?" "How do you list by file size?"
   - Outcome: A help reference card for `ls`, `cd`, `mkdir`, `rm`, `cp`, `mv`

5. **Piping and Redirection** (25 min)
   - Create a text file with 10 lines (use `echo` in a loop or paste content)
   - List files and save the output to a file
   - Count the number of files in a directory using piping
   - Append text to a file
   - Outcome: Bash script transcript showing 3 piping examples and 2 redirection examples

6. **Real-World Scenario** (20 min)
   - Scenario: "You have a folder with 50 files from last year. You need to find all `.txt` files, sort them by date, and move them to an archive folder."
   - Task: Create the scenario (fake files), then solve it using basic commands
   - Outcome: Annotated terminal transcript with explanation of each step

**Assessment:**
- Hands-on quiz: 10 terminal tasks (navigate, create, copy, delete, find, pipe)
- Rubric: Completion, efficiency, understanding (not speed)
- Allowable: Tab completion, `--help` flags, man pages

**Estimated Hands-On Time:** 110 minutes | **Lecture/Discussion:** 10 minutes

---

### **DAY 1 (Continued) / DAY 2: Version Control and Setup**

#### **Module 3: Git Basics — Version Control for Humans**
*Duration: 120 minutes*

**Learning Objectives:**
- Initialize a local Git repository
- Stage changes, commit with clear messages, and view history
- Understand branches and why they matter
- Clone a repository, fetch, and push changes
- Recognize and resolve merge conflicts (basics)
- Write meaningful commit messages

**Key Concepts:**
- What is version control and why it matters
- Local vs remote repositories
- The three Git states: working directory, staging area, committed
- Branches: what they are and why they exist
- Commits: immutable records of change
- The difference between `git add` and `git commit`
- Remote repositories (GitHub, origin)
- Merge conflicts: cause and resolution
- Commit messages as documentation
- `.gitignore` and what shouldn't be committed

**Hands-On Exercises:**

1. **Your First Repository** (20 min)
   - Create a new folder, init a Git repo
   - Create a simple file (e.g., README.md)
   - Stage it, commit it, view the log
   - Make changes, stage them, commit again
   - View the diff between commits
   - Outcome: Terminal showing init → commit → log, with annotations

2. **Branching Sprint** (20 min)
   - On main, create a file
   - Create a new branch called `feature/add-content`
   - Make changes on that branch, commit
   - Switch back to main, verify the file is unchanged
   - Merge the feature branch into main
   - Delete the feature branch
   - Outcome: Terminal transcript showing branch creation, switching, merging, deletion

3. **Cloning and Pushing** (20 min)
   - Clone a small public repository (e.g., `github.com/octocat/Hello-World`)
   - Make a change locally (edit a file, add a comment)
   - Attempt to push (will fail if not your repo — expected)
   - Create your own GitHub repo, clone it, make changes, push successfully
   - Outcome: Proof of successful clone and push (screenshot of GitHub showing your commit)

4. **Merge Conflicts (Simple)** (25 min)
   - Create a repo with a file
   - Create two branches from main, each modifying the same line
   - Merge one branch — succeeds
   - Merge the other — conflict!
   - Resolve the conflict manually
   - Complete the merge
   - Outcome: Terminal showing conflict resolution with annotations

5. **Meaningful Commit Messages** (15 min)
   - Bad message examples: "fix stuff", "update", "work"
   - Good message examples: "Add authentication logic to login form", "Fix off-by-one error in pagination"
   - Task: Write 5 commit messages for provided scenarios
   - Verify they follow the convention: present tense, action-focused, informative
   - Outcome: Markdown document with 5 well-written commit messages and explanations

6. **The `.gitignore` File** (25 min)
   - Create a repo with files that should NOT be committed (`.env`, `node_modules/`, `*.log`)
   - Create a `.gitignore` file before making any commits. This order matters: if a credential file is committed first, adding it to `.gitignore` later does NOT remove it from history. The file remains recoverable. Create `.gitignore` before the first commit -- it is the OPSEC enforcement layer for git.
   - Minimum entries for any project: `.env`, any credential files, `.DS_Store`, `__pycache__/`, `.venv/`
   - Verify that the ignored files don't show up in `git status`
   - Create a proper `.gitignore` for a Python project
   - Outcome: `.gitignore` file with explanatory comments

7. **Pull Requests** (20 min)
   - A pull request (PR) is a proposal on GitHub to merge one branch into another, with a review step before the merge occurs. The PR displays a diff showing exactly what changed, line by line. This is the quality gate for agentic work: when an agent produces changes on a branch, the PR is how you review what it did before it touches main.
   - Task: Create a branch, make changes, push the branch to GitHub, and open a PR using the GitHub CLI.
   - Command: `gh pr create --title "Add content" --body "Description of what changed and why"`
   - Review the PR diff in the GitHub web interface. Confirm that only the intended changes appear.
   - Merge the PR from the GitHub interface.
   - Outcome: A merged PR visible in the repository's pull request history, with a screenshot of the diff view.

**Assessment:**
- Hands-on project: Create a repo, make 3 commits, create and merge a branch, open and merge a PR
- Rubric: Correct Git workflow, meaningful messages, successful merge, working .gitignore
- Bonus: Resolve a merge conflict without help

**Estimated Hands-On Time:** 110 minutes | **Lecture/Discussion:** 10 minutes

---

#### **Module 4: Markdown — Documenting Like a Pro**
*Duration: 90 minutes*

**Learning Objectives:**
- Write clear, well-structured Markdown documents
- Understand the relationship between Markdown and HTML
- Use headings, lists, code blocks, tables, and links correctly
- Format code snippets and inline code
- Create table of contents and README files
- Recognize Markdown as a universal documentation language

**Key Concepts:**
- Markdown vs HTML vs Word processors
- Headers (h1 through h6)
- Emphasis: bold, italic, code (inline)
- Lists: ordered and unordered, nested
- Code blocks and syntax highlighting
- Links and image references
- Tables and alignment
- Blockquotes and horizontal rules
- Escaping special characters
- YAML frontmatter (intro)
- Markdown for system prompts and documentation
- Markdown as a lingua franca for developers

**GitHub Flavored Markdown (GFM):**

This course teaches GitHub Flavored Markdown, a superset of CommonMark. GFM adds tables, task lists (`- [ ]`), strikethrough (`~~text~~`), and fenced code blocks with language hints (` ```python `). If it renders in VS Code preview and on GitHub, it is valid for this course.

**Critical spacing rules -- most beginner errors live here:**

- A space is required between the `#` and the heading text: `# Heading` is correct, `#Heading` is not. Without the space, it renders as plain text.
- A blank line is required before any list. A list that immediately follows a paragraph with no blank line may not render as a list.
- A blank line is required before a fenced code block.
- Tables require both a header row and a separator row (`|---|---|`). A table without the separator row will not render.

**Smart-quote warning:**

Do not paste Markdown from Word or Google Docs. Those applications auto-replace straight quotes (`"`) with curly "smart" quotes, which break code blocks and inline code. Write Markdown in VS Code. Use the preview panel (Ctrl+Shift+V) to verify rendering before submitting.

**Hands-On Exercises:**

1. **Markdown Anatomy** (15 min)
   - Read a well-formatted markdown file
   - Identify all the Markdown syntax used
   - Recreate it from scratch
   - Outcome: Your own markdown file with 10+ different syntax elements

2. **Personal README** (20 min)
   - Write a markdown file about yourself for the class
   - Include: heading, bullet-point list, a link, bold/italic text, a code block
   - Format: name, role, skills, interests, favorite terminal command
   - Outcome: README.md committed to Git

3. **Code Blocks and Syntax** (15 min)
   - Create a markdown file with code examples in multiple languages
   - Use proper syntax highlighting (```python, ```bash, ```javascript)
   - Include inline code and code blocks
   - Outcome: Markdown file with at least 3 language examples

4. **Tables and Organization** (15 min)
   - Create a table comparing features of 3 tools
   - Create a second table for a simple project plan
   - Practice alignment (left, center, right)
   - Outcome: Markdown file with 2 well-formatted tables

5. **Documentation Project** (20 min)
   - Choose a simple process you know (making coffee, debugging, a workflow)
   - Document it in markdown with headers, lists, and code blocks
   - Include a table of contents
   - Target: 300-500 words, properly formatted
   - Outcome: Complete markdown document

6. **Markdown Frontmatter** (5 min)
   - Learn about YAML frontmatter
   - Add it to your README (title, author, date)
   - Understand it as metadata, not content
   - Outcome: README with YAML frontmatter

**Assessment:**
- Submission: A markdown document (documentation or personal README)
- Rubric: Clarity, proper formatting, use of 5+ syntax elements, readability

**Estimated Hands-On Time:** 85 minutes | **Lecture/Discussion:** 5 minutes

---

### **DAY 2: Programming Foundations and Tool Setup**

#### **Module 5: Programming Concepts — Thinking Like a Developer**
*Duration: 120 minutes*

**Learning Objectives:**
- Understand variables, data types, and operators
- Understand control flow: if/else, loops
- Understand functions and why they matter
- Read and write simple pseudocode
- Understand the concept of debugging
- Recognize programming patterns in everyday problems

**Key Concepts:**
- Variables: naming, assignment, types (string, number, boolean, array, object)
- Data types and type errors
- Operators: arithmetic, comparison, logical
- Conditionals: if/else/else-if
- Loops: for, while, forEach
- Functions: parameters, return values, scope
- Errors and debugging strategies
- Comments and code readability
- Pseudocode and planning before coding
- Arrays and objects (data structures)
- Recursion (intro)

**Hands-On Exercises:**

Note: These exercises use pseudocode and one real language (JavaScript recommended for accessibility). The goal is concepts, not syntax mastery.

1. **Variables and Types** (15 min)
   - Task: In pseudocode, write code that:
     - Stores your name, age, and whether you code
     - Calculates next year's age
     - Combines name and age in a sentence
   - Then implement in JavaScript
   - Outcome: Pseudocode + JavaScript with comments

2. **Control Flow: The Decision Tree** (20 min)
   - Scenario: "A coffee machine that asks for coffee type and size"
   - Write pseudocode with if/else logic for price calculation
   - Implement in JavaScript
   - Test with different inputs
   - Outcome: JavaScript function that handles 3 coffee types × 2 sizes

3. **Loops in Practice** (20 min)
   - Task: Write code that:
     - Prints numbers 1-10
     - Prints "I will learn to code" 5 times
     - Sums all numbers from 1-100
     - Loops through an array of words and prints each
   - Outcome: 4 code examples with comments explaining what each loop does

4. **Functions: Reusable Logic** (20 min)
   - Write a function that takes a name and returns a greeting
   - Write a function that takes two numbers and returns their sum
   - Write a function that checks if a password is long enough (8+ chars)
   - Write a function that counts vowels in a word
   - Outcome: 4 JavaScript functions with clear names and comments

5. **Debugging Basics** (20 min)
   - Given 5 buggy code snippets (syntax errors, logic errors, off-by-one)
   - Read and identify the bug
   - Fix it and test
   - Understand: typos, logic errors, boundary conditions
   - Outcome: Annotated code with bugs fixed and explanations

6. **Pseudocode Planning** (25 min)
   - Scenario: "Build a simple grade calculator: input test scores, output average and letter grade"
   - Write pseudocode first (no syntax)
   - Outline the steps before writing code
   - Implement in JavaScript
   - Test edge cases
   - Outcome: Pseudocode + working code + test cases

**Assessment:**
- Hands-on: Write 3 small programs (a function, a conditional, a loop)
- Rubric: Logic correctness, clarity, comments, proper use of concepts

**Estimated Hands-On Time:** 110 minutes | **Lecture/Discussion:** 10 minutes

---

#### **Module 6: Developer Tools — Installation and Authentication**
*Duration: 90 minutes*

**Learning Objectives:**
- Install and configure Claude Code
- Authenticate with GitHub and cloud platforms
- Understand environment variables and `.env` files
- Set up a code editor (VS Code)
- Test your development environment
- Troubleshoot common setup issues

**Key Concepts:**
- Package managers and dependencies
- Authentication and API keys (safety first)
- Environment variables and `.env` files
- The difference between local and global installs
- Code editors and their role in development
- Terminal emulators and shells (bash, zsh)
- PATH and executable discovery
- Version management (checking tool versions)
- HTTPS vs SSH authentication
- Token-based authentication

**Hands-On Exercises:**

1. **Install Claude Code** (15 min)
   - Follow official installation instructions for your OS
   - Verify installation: `claude --version`
   - Run Claude: `claude`
   - Confirm you can interact with Claude
   - Outcome: Screenshot of Claude running with version info

2. **GitHub Authentication** (20 min)
   - Install GitHub CLI (`gh`)
   - Authenticate: `gh auth login`
   - Follow the prompts (choose HTTPS)
   - Verify: `gh auth status`
   - Clone a test repository
   - Outcome: Proof of successful `gh auth status` and cloned repo

3. **VS Code Setup** (15 min)
   - Install VS Code
   - Open a folder in VS Code
   - Install 2-3 useful extensions (Markdown Preview, Git Graph, Prettier)
   - Create a simple file and view it
   - Outcome: VS Code window with extensions installed

4. **Environment Variables** (20 min)
   - Understand: `.env` files and why they exist
   - Create a `.env` file with sample variables
   - Learn: how applications read environment variables
   - Safety: understand that `.env` should not be committed
   - Create a `.gitignore` that excludes `.env`
   - Outcome: `.env` file + updated `.gitignore`

5. **Tool Verification Sprint** (15 min)
   - Create a checklist and verify:
     - `claude --version`
     - `node --version` (or python)
     - `git --version`
     - `gh --version`
     - `code --version`
   - Document any missing tools
   - Outcome: Verification checklist (screenshot or file)

6. **Troubleshooting Dry Run** (5 min)
   - Common issue simulation: missing tool, wrong PATH
   - Practice diagnosing: "Where is this command?" (`which` or `where`)
   - Understand: "Command not found" means it's not on PATH
   - Outcome: Understanding of how to find and install missing tools

**Assessment:**
- Checklist: All required tools installed and authenticated
- Rubric: Working installation, correct authentication, understanding of each tool

**Estimated Hands-On Time:** 85 minutes | **Lecture/Discussion:** 5 minutes

---

#### **Module 7: Context and Configuration — CLAUDE.md and me.md**
*Duration: 90 minutes*

**Learning Objectives:**
- Understand why context files matter
- Write a CLAUDE.md file for a real project
- Write a personal me.md file
- Understand how Claude Code reads and uses these files
- Structure project context clearly
- Practice setting up a development workspace

**Key Concepts:**
- System prompts in the Claude Code harness
- CLAUDE.md: project documentation
- me.md: personal operating profile
- Conflict resolution matrices
- Decision-making frameworks
- Project scope and constraints
- Files Claude can and cannot access
- The role of context in agentic development
- `.claude/` folder structure

**Hands-On Exercises:**

1. **The CLAUDE.md Anatomy** (15 min)
   - Read the following example CLAUDE.md:

```markdown
# Project: Daily Brief Generator

## What this does
Pulls the unit's daily log and produces a formatted brief.

## Rules
- Never include real names in the output -- use [NAME] as a placeholder
- Use the provided template structure, do not invent new sections
- Flag any entries with incomplete location or time data

## Files
- `brief-template.md` -- the output template (read-only)
- `input-log.txt` -- the daily log to process
```

   Note: Every element in this file is Markdown syntax you just learned. The `##` headers create sections the model reads as distinct instruction blocks. The bullet list under Rules creates discrete, unambiguous rules. If the formatting breaks -- a header without a space, a list without a blank line before it -- the model reads a wall of text instead of structured instructions.

   - Identify sections: project name, goals, constraints, deliverables
   - Understand how it guides Claude's behavior
   - Outcome: Annotation of the example CLAUDE.md with notes on each section and what behavior each element produces

2. **Write Your me.md** (20 min)
   - Create a personal profile:
     - Your name and role
     - Your decision-making style (fast/slow, risk tolerance)
     - What you value in work (clarity, speed, thoroughness)
     - Your communication preference (BLUF, examples, details)
     - How you prefer Claude to interact with you
   - Outcome: A completed me.md (5-10 lines)

3. **Project CLAUDE.md** (25 min)
   - Scenario: You're building a simple task manager for Marines
   - Write a CLAUDE.md including:
     - What the project is
     - What it's NOT (scope boundary)
     - Key constraints (security, usability)
     - Files Claude can modify
     - Success criteria
   - Outcome: A complete CLAUDE.md for the scenario project

4. **Conflict Resolution Matrix** (15 min)
   - Understand: when requirements conflict, how do you choose?
   - Example: "Fast vs Secure" — which wins?
   - Create a simple matrix for your scenario project:
     - Speed vs Security
     - Simplicity vs Features
     - Completeness vs Time-to-delivery
   - Outcome: Matrix showing your priorities (rate each pair)

5. **Set Up a Project Context** (10 min)
   - Create a new folder for a practice project
   - Create `.claude/` folder inside it
   - Add your CLAUDE.md and me.md
   - Run Claude Code in that folder
   - Outcome: Project folder with context files in place

6. **Context Verification** (5 min)
   - Open Claude Code in your project
   - Ask Claude about the project (it should reference your CLAUDE.md)
   - Observe how context influences its behavior
   - Outcome: Conversation showing Claude understanding your context

**Assessment:**
- Submission: CLAUDE.md + me.md for a real project
- Rubric: Clarity, completeness, enforceability, practical usefulness

**Estimated Hands-On Time:** 85 minutes | **Lecture/Discussion:** 5 minutes

---

### **DAY 2 (Continued) / DAY 3: Integration and Readiness**

#### **Module 8: Putting It All Together — Your First Project**
*Duration: 180 minutes (can span 1-2 hours across Day 2 into Day 3)*

**Learning Objectives:**
- Integrate all prerequisite concepts into one project
- Practice the full workflow: plan → code → commit → push
- Troubleshoot real problems
- Prepare for the demands of advanced agentic development
- Demonstrate readiness to progress to advanced work

**Key Concepts:**
- Project planning (SMEAC intro)
- Git workflow in a real project
- Using Claude Code for code assistance
- Iterative development
- Testing your own work
- Committing progress incrementally
- Documentation as you build

**Hands-On Exercises:**

This is the capstone project. Students choose one of three paths:

**Path A: CLI Tool** (Recommended for terminal-focused students)
- Build a simple CLI tool (e.g., a password strength checker, a markdown to HTML converter, a task logger)
- Requirements:
  - Takes input from the user or a file
  - Processes it with logic
  - Outputs the result
  - Includes basic error handling
  - Is documented in README.md
  - Has at least 3 commits
- Technology: JavaScript (Node.js) or Python
- Outcome: GitHub repo with working tool + README + commits

**Path B: Web App** (Recommended for web-focused students)
- Build a simple web app (e.g., a note-taking app, a unit converter, a quote generator)
- Requirements:
  - HTML + CSS + basic JavaScript
  - Takes user input
  - Does something with it
  - Is documented in README.md
  - Runs locally (`python -m http.server` or similar)
  - Has at least 3 commits
- Technology: HTML/CSS/JavaScript
- Outcome: GitHub repo with working app + README + commits

**Path C: API Integration** (Recommended for advanced students)
- Build a CLI or web app that uses a free public API (weather, movies, jokes, etc.)
- Requirements:
  - Authenticates with or calls a real API
  - Handles errors gracefully
  - Displays results in a readable format
  - Is documented in README.md
  - Has at least 3 commits
- Technology: Node.js + fetch or Python + requests
- Outcome: GitHub repo with working app + README + commits

**Workflow for All Paths:**

1. **Plan (20 min)**
   - Choose your project (use the three paths above)
   - Write a one-paragraph description
   - List 3-5 features you'll build
   - Commit to git (first commit: "Initial project plan")

2. **Set Up (20 min)**
   - Create `.claude/` folder with CLAUDE.md and me.md
   - Initialize git repository
   - Create a basic file structure
   - Commit: "Project setup"

3. **Build Phase 1 (60 min)**
   - Build the core functionality (simplest version first)
   - Use Claude Code to help: ask questions, get code suggestions, iterate
   - Make at least one commit per feature
   - Commit messages: "Add [feature]", "Fix [bug]"

4. **Test and Iterate (40 min)**
   - Use your own tool — does it work?
   - Find and fix bugs
   - Ask Claude to help you improve (error handling, efficiency)
   - Make commits for each improvement
   - Commit: "Handle edge case X", "Improve error messages"

5. **Document (20 min)**
   - Write a clear README.md
   - Include: what it does, how to use it, any requirements
   - Add comments to complex code
   - Final commit: "Update documentation"

6. **Push to GitHub (10 min)**
   - Verify all commits are local
   - Push to GitHub
   - Verify it appears on GitHub.com
   - Outcome: Working repo publicly available

**Stretch Goals (Optional):**
- Add a second feature or improvement
- Deploy the app online (Vercel for web apps, GitHub releases for CLI tools)
- Add automated tests
- Create a video walkthrough

**Assessment:**
- Submission: GitHub repo link with evidence of 5+ commits
- Rubric:
  - Does it work? (50%)
  - Is it documented? (20%)
  - Are commits meaningful? (15%)
  - Did you iterate based on feedback? (10%)
  - Did you help yourself when stuck? (5%)
- Bonus: 1 point per stretch goal

**Estimated Time:** 170 minutes | **Mentoring/Troubleshooting:** 10 minutes

---

## Course Learning Progression

```
Module 1: LLM Basics
    ↓
Module 2: Terminal Basics ←→ Module 3: Git Basics
    ↓
Module 4: Markdown (can run in parallel)
    ↓
Module 5: Programming Concepts
    ↓
Module 6: Developer Tools Setup
    ↓
Module 7: Context and Configuration
    ↓
Module 8: Capstone Project (integrates all modules)
```

**Prerequisite Dependencies:**
- Module 2 (Terminal) needed before Module 3 (Git)
- Modules 1-4 can run in some parallel (e.g., Markdown while Terminal is sinking in)
- Modules 5-7 should complete before Module 8
- Module 6 (Tools) must happen before Module 8
- Module 7 (Context) ideally happens before Module 8 but can be mini-intro before 8 begins

---

## Daily Schedule Outline

### **Day 1: Foundations (8 hours)**

| Time | Activity | Module |
|------|----------|--------|
| 8:00 - 9:30 | Module 1: LLM Basics & Prompts | M1 (90 min) |
| 9:30 - 10:00 | Break |
| 10:00 - 12:00 | Module 2: Command Line Basics | M2 (120 min) |
| 12:00 - 1:00 | Lunch |
| 1:00 - 2:30 | Module 3: Git Basics Part 1 | M3 (part 1) |
| 2:30 - 2:45 | Break |
| 2:45 - 4:15 | Module 3: Git Basics Part 2 | M3 (part 2) |
| 4:15 - 5:00 | Module 4: Markdown | M4 (45 min) |
| 5:00 - 6:00 | Lab time / Troubleshooting | |

**Homework:** Finish Module 4 if incomplete, read ahead to Module 5

### **Day 2: Intermediate (8 hours)**

| Time | Activity | Module |
|------|----------|--------|
| 8:00 - 9:30 | Module 4: Markdown (if needed) + finish setup | M4 (remaining) |
| 9:30 - 10:00 | Break |
| 10:00 - 12:00 | Module 5: Programming Concepts | M5 (120 min) |
| 12:00 - 1:00 | Lunch |
| 1:00 - 2:30 | Module 6: Developer Tools Setup | M6 (90 min) |
| 2:30 - 2:45 | Break |
| 2:45 - 4:15 | Module 7: Context and Configuration | M7 (90 min) |
| 4:15 - 5:00 | Wrap-up and readiness check | |
| 5:00 - 6:00 | Lab time / Troubleshooting | |

**Homework:** Prep for capstone, gather project ideas

### **Day 3 (Optional, if including capstone): Capstone (6-8 hours)**

| Time | Activity |
|------|----------|
| 8:00 - 12:00 | Module 8: Capstone Project (first half) |
| 12:00 - 1:00 | Lunch |
| 1:00 - 5:00 | Module 8: Capstone Project (second half) + presentations |
| 5:00 onwards | Celebration and retrospective |

---

## Materials and Resources

### **Required for Students:**
- A computer (macOS, Linux, or Windows) with at least 4GB RAM
- Terminal / command-line access
- A text editor (we recommend VS Code, free)
- An internet connection
- A GitHub account (free)
- Claude access (API account or web access)

### **Provided by Instructor:**
- Slides and demos for each module
- Worked examples for each exercise
- Troubleshooting guides and common errors
- Sample `.env` files and code templates
- Example CLAUDE.md and me.md files
- Capstone project rubric and evaluation guide

### **Recommended Reading:**
- "Learn Git in Y Minutes" (online reference)
- "The Markdown Guide" (online reference)
- "Prompt Engineering Guide" (Anthropic docs)
- "JavaScript for Beginners" (Khan Academy or similar)

---

## Grading and Progression

### **Completion Requirements:**

All 8 modules must be completed. Each module has a graded exercise.

| Module | Grade | Passing |
|--------|-------|---------|
| 1: LLM Basics | 5 well-written prompts | 80%+ clarity/specificity |
| 2: Terminal | 10 terminal tasks | 8/10 correct |
| 3: Git | Create, branch, merge, push | All steps successful |
| 4: Markdown | Documentation file | Uses 5+ syntax elements |
| 5: Programming | 3 small programs | Logic correct, readable |
| 6: Tools | All tools installed & authenticated | Version checks all pass |
| 7: Context | CLAUDE.md + me.md | Complete and coherent |
| 8: Capstone | Working project on GitHub | Runs, documented, commits |

**Overall:** 7/8 modules passed = course complete. 8/8 = honors.

---

## Instructor Notes

### **Pacing:**
- The course is designed to be **hands-heavy, lecture-light**. Instructor time is spent in the lab answering questions, not lecturing.
- If a student is falling behind, accelerate them: "Let's pair on this one, then you take the next three."
- If a student is ahead, give them stretch goals from Module 8 early.

### **Common Sticking Points:**
1. **Terminal path concepts:** Students confuse relative/absolute paths. Have them practice navigation 3-4 times.
2. **Git merge conflicts:** Most student struggle here. Make sure you demonstrate conflict resolution twice and let them practice on a small, safe example.
3. **Programming logic:** Pseudocode helps. Make them write pseudocode BEFORE any code.
4. **API keys in `.env`:** Emphasize: never commit `.env`. Show them a `.gitignore` example.
5. **Authentication:** GitHub SSH vs HTTPS is a fork in the road. Recommend HTTPS for beginners, let advanced students use SSH.

### **Troubleshooting Mindset:**
- Normalize debugging and troubleshooting as skills, not failures.
- When a student says "it's broken," ask: "What does the error message say?" or "What did you expect vs what happened?"
- Have them use `--help`, man pages, and Google before you give the answer.

### **Differentiation:**
- **Accelerated path:** Skip Module 5 parts (they may know programming), move faster through setup, give capstone stretch goals.
- **Slower path:** Add a Module 2.5 on "CLI Practice Drills" (30 min), break Module 5 into 2 sessions, pair them with a mentor.
- **Accessibility:** Provide terminal recordings for screen-reader users, text-based alternatives to visual demos.

---

## Course Completion Outcomes

After completing this course, students will be able to:
- ✓ Write clear, structured prompts and understand system prompts
- ✓ Navigate the terminal confidently
- ✓ Use Git for version control
- ✓ Write Markdown
- ✓ Understand basic programming concepts
- ✓ Have all developer tools installed and authenticated
- ✓ Create and manage context files (CLAUDE.md, me.md)
- ✓ Build and ship a working project to GitHub

**These are the core skills for AI-assisted development.** Students who complete all 8 modules are ready for advanced agentic work.

---

## Appendix: Sample Rubric for Capstone Project

**Criteria (100 points total)**

| Criterion | Points | Evidence |
|-----------|--------|----------|
| **Code Works** | 50 | App runs without errors, does what was promised, handles basic errors |
| **Git Workflow** | 15 | 5+ commits with clear messages, pushed to GitHub, no credentials in history |
| **Documentation** | 15 | README is clear, includes setup/usage, code has comments on complex logic |
| **Iteration** | 10 | Evidence of feedback loops, bug fixes, improvements based on testing |
| **Polish** | 10 | Code is readable, organized, no debug statements left behind |
| **Bonus** | +5 | Deployment, tests, second feature, or other ambition |

**Passing:** 70+ points (grades: 70-79 Pass, 80-89 Good, 90+ Excellent)

---

## Appendix: Glossary of Terms

- **LLM:** Large Language Model (like Claude)
- **Prompt:** A user's input to an LLM
- **System Prompt:** Instructions that shape how an LLM behaves
- **Terminal/CLI:** Command-line interface (text-based interface to your computer)
- **Git:** Version control system for tracking code changes
- **Repository:** A project folder managed by Git
- **Commit:** A saved snapshot of changes in Git
- **Markdown:** A plain-text format for structured writing
- **Function:** A reusable block of code
- **Variable:** A named storage for data
- **Authentication:** Proving your identity to a system (like GitHub login)
- **API Key/Token:** A secret string that lets code authenticate as you

---

**End of Prerequisite Course Design**

This course prepares students with zero background knowledge to become competent, confident learners ready to master agentic development.
