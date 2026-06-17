# Field Craft: Markdown, Code, Tools & Context Files

**Who this is for:** An operator who can already command an AI and wants the field craft that makes the work hold up — clean documents, enough code-literacy to read what the machine writes, a verified toolbox, and context files that steer an agent before you type a word.

**What you will leave with:** You can write structured Markdown, read and reason about basic code without freezing, confirm your developer tools are installed and authenticated, and author a `CLAUDE.md` and a `me.md` that actually shape how an agent behaves on a real project.

---

## Markdown: The Lingua Franca

**BLUF.** Markdown is plain text with a handful of formatting marks that render into clean documents — and it is the format your READMEs, your prompts, and your context files are written in, so writing it correctly is non-optional field craft, not decoration.

### Why This Matters

You have been reading Markdown since the first module — every admonition, every table, every code block on these pages is Markdown underneath. Now you write it. Every document you hand an agent, every set of standing orders you give it, and every README you ship is Markdown. Get the formatting wrong and the model reads a wall of undifferentiated text instead of structured instruction. This is the format your authority travels in.

### Concepts

Markdown is a small set of marks that a renderer turns into formatted output. Learn once, use everywhere.

- **Headers.** `#` through `######` for h1–h6. A space is required after the `#`. `# Heading` renders; `#Heading` does not.
- **Emphasis.** `**bold**`, `*italic*`, and `` `inline code` `` with backticks.
- **Lists.** `-` or `*` for unordered, `1.` for ordered. A blank line is required before the list begins, or it will not render as a list.
- **Code blocks.** Three backticks open and close a fenced block. Add a language hint for syntax highlighting: `` ```python ``, `` ```bash ``. A blank line is required before the block.
- **Tables.** A header row, then a separator row of `|---|---|`, then data rows. The separator row is mandatory — without it, nothing renders as a table.
- **Links.** `[visible text](url)`. Images are the same with a leading `!`.
- **Task lists.** `- [ ]` and `- [x]` render as checkboxes (a GitHub-flavored extension).

This course teaches GitHub Flavored Markdown (GFM) — a superset of the CommonMark standard that adds tables, task lists, strikethrough, and fenced code blocks. If it renders in the VS Code preview and on GitHub, it is valid here.

!!! warning "Critical Spacing Rules — Most Beginner Errors Live Here"
    - A space is required between the `#` and the heading text.
    - A blank line is required before any list.
    - A blank line is required before a fenced code block.
    - Tables require both a header row and a separator row (`|---|---|`).

    Four rules. The overwhelming majority of "my Markdown looks broken" reports trace to one of them.

!!! danger "The Smart-Quote Trap"
    Do not draft Markdown in Word or Google Docs. Those applications silently replace straight quotes (`"`) with curly "smart" quotes, which break code blocks and inline code when the file is processed. Write Markdown in VS Code. Use the preview panel (Ctrl+Shift+V) to confirm it renders before you hand it off.

!!! example "Same Content, Two Renders"
    Raw input the model reads:

    ```
    ## Rules
    - Never include real names
    - Flag incomplete entries
    ```

    Renders as a heading and two discrete rules. Drop the blank line before the list or the space after `##`, and the same text collapses into one paragraph the model parses as a single run-on instruction. The formatting *is* the structure.

??? note "Instructor Note — Don't Linger on Syntax"
    Markdown has perhaps fifteen minutes of genuine instruction in it. The rest is reps. Get students writing a README in the first ten minutes; correct the spacing errors as they appear in the wild. Resist building a comprehensive syntax lecture — it does not survive contact with their first real document.

### Hands-On

1. Open VS Code. Create a file `README.md` and open the preview pane (Ctrl+Shift+V).
2. Write a short personal README: an h1 with your name, a bullet list of three skills, one bold term, one inline-code term, and a fenced code block showing your favorite terminal command.
3. Add a table comparing two tools you use, with at least a header row and separator row. Confirm it renders.
4. Deliberately break one rule — remove the space after a `#`, or the blank line before a list. Watch the preview break. Fix it.
5. Save the file. You will reuse it.

!!! question "Before You Continue"
    Your table is not rendering — it shows up as raw pipe characters. What is the single most likely cause, and how do you confirm it?

<div class="quiz-block">
  <p class="quiz-question">You write <code>#Mission Brief</code> at the top of a file and it renders as plain text, not a large heading. Why?</p>
  <ul class="quiz-options">
    <li data-correct="false">Markdown headings must be all uppercase</li>
    <li data-correct="true">A space is required between the <code>#</code> and the heading text</li>
    <li data-correct="false">You need to add a blank line after the heading</li>
    <li data-correct="false">The file must end in <code>.markdown</code>, not <code>.md</code></li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can write a Markdown document using at least five distinct syntax elements
- [ ] I know the four critical spacing rules and can spot a violation
- [ ] I draft Markdown in VS Code and verify it in preview, never in Word
- [ ] I can build a table, a fenced code block, and a task list from memory

---

## Programming Concepts: Reading What the Machine Writes

**BLUF.** You do not need to write production code to command an agent — but you do need enough literacy to read what it produces, follow its logic, and spot when it has done something wrong, because the operator who cannot read the output cannot verify it.

### Why This Matters

An agent will write code, scripts, and config and hand them to you. If those are opaque, you are signing for output you cannot evaluate — which violates the supervisor mindset from Module 7 and the accountability rule from Module 9. The bar here is recognition, not authorship: read a function and predict what it does; spot a loop that will never end; recognize a bug class when you see one. That literacy is the floor for verification.

### Concepts

A small vocabulary covers most of what you will read:

- **Variables.** A named container for a value. `count = 0` stores the number zero under the name `count`. Common types: strings (text), numbers, booleans (true/false), arrays/lists (ordered collections), objects (labeled fields).
- **Operators.** Arithmetic (`+ - * /`), comparison (`== < >`), and logical (`and`/`or`/`not`). Comparison and logic are how a program makes decisions.
- **Conditionals.** `if / else` — run one block when a condition is true, another when it is false. This is branching logic.
- **Loops.** `for` and `while` — repeat a block. The classic failure is the *off-by-one* error (looping one time too many or too few) and the *infinite loop* (a `while` whose condition never becomes false).
- **Functions.** A named, reusable block that takes inputs (parameters) and returns an output. `greet(name)` takes a name and returns a greeting. Functions are how code stays readable and reusable.

**Pseudocode first.** Before syntax, write the steps in plain English. "Get the scores. Add them up. Divide by how many there are. Decide a letter grade from the average." That is the algorithm. Syntax is just translating those steps into a language. When you read agent-written code, do the reverse — narrate each block back into plain English. If you cannot narrate it, you cannot verify it.

!!! tip "Logic Beats Math"
    Programming is problem-solving, not algebra. The skill is decomposing a task into ordered, unambiguous steps. If you can write a clear set of instructions for a motivated junior, you can read code.

!!! example "Read This Function"
    ```javascript
    function isStrongPassword(pw) {
      if (pw.length < 8) {
        return false;
      }
      return true;
    }
    ```

    Narrate it: "Take a password. If it is shorter than eight characters, fail. Otherwise, pass." You just verified a function's logic without writing a line. Now ask the harder question: is "length 8 or more" actually a *strong* password rule? Reading the code is step one; judging whether it is correct is the operator's job.

??? note "Instructor Note — Concepts, Not Syntax Mastery"
    The deliverable is reading literacy, not a programmer. Use pseudocode rigorously and one accessible language (JavaScript or Python) for examples. Off-by-one and infinite-loop errors are the highest-value bug classes to drill because they recur constantly in agent output. Do not let this turn into a coding bootcamp.

### Hands-On

1. Write pseudocode for a grade calculator: take a list of test scores, output the average and a letter grade. Steps only, no syntax.
2. Read this loop and predict its output before running anything: a `for` loop that prints the numbers 1 through 5. Then say what changes if the loop bound is wrong by one.
3. You are handed a buggy snippet with a `while` loop whose condition never changes. Identify why it will run forever and what one line fixes it.
4. Take a short function an AI wrote for you in a previous module. Narrate each block back into plain English. Flag any block you cannot narrate — that is your verification gap.

!!! question "Before You Continue"
    An agent hands you a 30-line script. What is the first thing you do before you run it or sign for it?

<div class="quiz-block">
  <p class="quiz-question">Why does an operator who commands agents still need to read code, even if they never write it from scratch?</p>
  <ul class="quiz-options">
    <li data-correct="false">Because agents refuse to run unless you can write the code yourself</li>
    <li data-correct="true">Because you cannot verify — and therefore cannot responsibly sign for — output you cannot read</li>
    <li data-correct="false">Because reading code makes the model produce fewer hallucinations</li>
    <li data-correct="false">Because code literacy lowers the token cost of a request</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can name variables, conditionals, loops, and functions and say what each does
- [ ] I can write pseudocode for a simple task before any syntax
- [ ] I can read a short function and narrate its logic in plain English
- [ ] I can recognize an off-by-one error and an infinite loop when I see one

---

## Developer Tools: The Toolbox

**BLUF.** Every tool in the agentic workflow plays one role — the model writes, git tracks, GitHub stores, VS Code edits — and before you can build, each one has to be installed, authenticated, and verified, or you will lose your first session to a setup failure instead of work.

### Why This Matters

The toolbox is the difference between "I have an idea" and "I shipped it." A missing or unauthenticated tool stops you cold at the worst possible moment — mid-build, under time pressure. Verifying the toolbox up front, with a checklist, is the same discipline as a pre-mission equipment check. You confirm the kit works before you need it, not when it fails.

### Concepts

The core toolbox for this course:

- **Claude Code** — the agentic harness; the model with a body. Verify with `claude --version`.
- **`gh` (GitHub CLI)** — authenticates to GitHub and drives pull requests from the terminal. Verify with `gh --version`; authenticate with `gh auth login` (choose HTTPS for simplicity); confirm with `gh auth status`.
- **git** — the version control engine (the duty logbook from Module 6). Verify with `git --version`.
- **VS Code** — the editor; install the WSL and Markdown Preview extensions. Verify with `code --version`.
- **Node.js or Python** — the runtime that executes code. Verify with `node --version` or `python --version`.

**PATH and "command not found."** When you type a command, the system searches a list of directories called the **PATH** to find the executable. "Command not found" almost always means the tool installed but is not on the PATH yet. The fix is usually to restart the terminal (Windows in particular does not refresh PATH after an install until the terminal restarts). Use `which <command>` (or `where` on native Windows) to ask the system where it is finding a command.

**Environment variables and `.env` files.** Programs read configuration — including secrets like API keys — from environment variables. A `.env` file holds those values for a project. It must never be committed to git.

!!! danger "`.env` Goes in `.gitignore` Before Your First Commit"
    A credential committed even once stays in git history — adding it to `.gitignore` afterward does not remove it. Create `.gitignore` with `.env` in it *before* the first commit. This is the same OPSEC-enforcement rule you met in Module 6; it is not a recoverable mistake. The data-handling bright line from Module 1 reaches all the way down to your config files.

!!! tip "Verify the Whole Toolbox in One Pass"
    Run every `--version` check in sequence before you start a project. A green checklist up front saves the session that would otherwise die on a missing tool mid-build.

??? note "Instructor Note — Windows PATH and gh Order"
    Two failures dominate this module. First, Windows does not auto-update PATH after an install — have students restart the terminal as the default fix before debugging anything deeper. Second, `gh auth login` fails confusingly if `gh` itself is not installed yet; confirm `gh --version` passes before touching auth.

### Hands-On

1. Run the full version-check sweep: `claude --version`, `git --version`, `gh --version`, `code --version`, and `node --version` (or `python --version`). Record the result of each.
2. For any that fail, diagnose with `which` (or `where`). If it is "command not found" right after an install, restart the terminal and retry.
3. Authenticate to GitHub: `gh auth login`, choose HTTPS, then confirm with `gh auth status`.
4. Create a practice folder. Inside it, create a `.gitignore` containing `.env` *before anything else*, then create a `.env` with a dummy `API_KEY=placeholder` line. Confirm `git status` does not show the `.env`.

!!! question "Before You Continue"
    You install a new CLI tool, then immediately get "command not found" when you run it. Before assuming the install failed, what is the first thing to try?

<div class="quiz-block">
  <p class="quiz-question">You committed a real <code>.env</code> file once, noticed, and added it to <code>.gitignore</code> in the next commit. Is the credential safe?</p>
  <ul class="quiz-options">
    <li data-correct="false">Yes — <code>.gitignore</code> removes it from the repository</li>
    <li data-correct="true">No — it remains in git history and must be treated as compromised and rotated</li>
    <li data-correct="false">Yes, as long as the file is deleted from the working directory</li>
    <li data-correct="false">No, but only if the repository is public</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] Every tool passes its `--version` check
- [ ] GitHub CLI is authenticated and `gh auth status` confirms it
- [ ] I can diagnose "command not found" using PATH and `which`/`where`
- [ ] My `.gitignore` excludes `.env` and was created before the first commit

---

## Context Files: Standing Orders at File Scale

**BLUF.** `CLAUDE.md` tells an agent what to build and what never to touch; `me.md` tells it how you work — together they are persistent, file-scale standing orders that steer the agent before you type a single prompt, and a context file that constrains nothing steers nothing.

### Why This Matters

You met the idea of persistent instructions in Module 4, where you personalized your AI through a settings field. Context files are the same idea at file scale — version-controlled, project-specific, living in the repo with the work. They are the primary lever for steering an agent that Module 7 pointed forward to. A weak `CLAUDE.md` is the single most common failure: students write a friendly project description that *constrains nothing*, and the agent does whatever it wants. The power is in the boundaries.

### Concepts

Two files do most of the work in the Claude Code harness:

- **`CLAUDE.md` — what to build.** Project-scoped instructions the harness reads at the start of a session: what the project is, what it is *not* (the scope boundary), hard rules and constraints, which files the agent may modify, and what "done" looks like.
- **`me.md` — how you work.** Your operating profile: your role, your communication preference (BLUF, examples, level of detail), your decision style, and how you want the agent to interact with you.

Every element in these files is Markdown you just learned. `##` headers create distinct instruction blocks the model reads as separate sections; a bulleted list under a `## Rules` header becomes discrete, unambiguous rules. Break the formatting and the model reads a wall of text instead of structured orders — the Markdown section is not a coincidence in this module's order.

**Constraints are the deliverable.** The strongest line in a `CLAUDE.md` is usually a prohibition. "Never modify `schema.sql`." "Do not invent new sections — use the template." "Never put real names in output; use `[NAME]`." Those are the lines that change agent behavior. Ask of every draft: *what should the agent NOT do, and what is out of scope?* If the file has no answer, it is documentation, not steering.

!!! example "A CLAUDE.md That Actually Constrains"
    ```markdown
    # Project: Daily Brief Generator

    ## What this does
    Pulls the unit's daily log and produces a formatted brief.

    ## Rules
    - Never include real names in output — use [NAME] as a placeholder
    - Use the provided template structure; do not invent new sections
    - Flag any entry with incomplete location or time data

    ## Files
    - brief-template.md — the output template (read-only, never modify)
    - input-log.txt — the daily log to process
    ```

    Every rule is enforceable and every boundary is explicit. Compare it to "build me a nice brief tool" — which gives the agent nothing to obey.

!!! tip "Make It Conflict-Aware"
    When two requirements collide — fast vs. secure, simple vs. featured — say which wins, up front. A one-line conflict-resolution rule ("when speed and security conflict, security wins") prevents the agent from silently choosing for you.

!!! warning "Context Files Are Sent to the Provider"
    A `CLAUDE.md` or `me.md` is transmitted with every request, exactly like the custom instructions in Module 4. The data-handling bright line from Module 1 and the ammunition discipline from Module 8 both apply: nothing sensitive, controlled, or above the system's authorization ceiling goes in a context file, and every line you add spends context budget. Keep them tight. *(Module 4 is where personalizing was taught; Module 8 is where context-budget cost was taught — this is the same discipline at file scale, not a re-teach.)*

??? note "Instructor Note — The Generic-CLAUDE.md Failure"
    The predictable miss is a `CLAUDE.md` that describes the project warmly and constrains nothing. Drive the fix with one question: "What should Claude NOT modify? What is out of scope?" Make students name a real prohibition and a real read-only file. A constraint they can point to is worth more than a paragraph of friendly description.

### Hands-On

1. Write a `me.md` (5–10 lines): your role, your communication preference, your decision style, and one thing you want the agent to always do and one to never do.
2. Write a `CLAUDE.md` for a scenario project — a simple task manager for a unit. Include: what it is, what it is NOT, at least two hard rules, the files the agent may modify, at least one read-only file, and the success criteria.
3. Add a one-line conflict-resolution rule (e.g., "when speed and security conflict, security wins").
4. Place both files in a project folder, run the agent there, and ask it to summarize the project. Confirm it references your `CLAUDE.md` — that is proof the context was read.
5. Re-read your `CLAUDE.md` and underline every line that is a genuine prohibition. If there are none, rewrite until there is at least one.

!!! question "Before You Continue"
    Two students write a `CLAUDE.md` for the same project. One is a warm paragraph describing the goal; the other names three things the agent must never do. Which one will actually change the agent's behavior, and why?

<div class="quiz-block">
  <p class="quiz-question">What most reliably makes a <code>CLAUDE.md</code> actually steer an agent's behavior?</p>
  <ul class="quiz-options">
    <li data-correct="false">A detailed, friendly description of the project's purpose</li>
    <li data-correct="false">Using as many Markdown features as possible</li>
    <li data-correct="true">Explicit constraints — what NOT to do, what is out of scope, which files are read-only</li>
    <li data-correct="false">Making the file as long and comprehensive as possible</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I have a `me.md` that reflects my real communication and working style
- [ ] My `CLAUDE.md` states what the project is NOT and names at least one read-only file
- [ ] My `CLAUDE.md` contains at least one genuine, enforceable prohibition
- [ ] The agent reads my context files and references them when I ask about the project
- [ ] I understand context files carry the same data-handling and context-cost discipline as Modules 1, 4, and 8

---

## Summary

| Section | Key Point | Operator Takeaway |
|---|---|---|
| Markdown | Plain text + a few marks, four spacing rules that cause most errors | Your authority travels in Markdown — write it correctly |
| Programming Concepts | Variables, conditionals, loops, functions; pseudocode first | Read what the machine writes well enough to verify it |
| Developer Tools | Install, authenticate, and verify the whole toolbox up front | A green checklist before the build, not a failure mid-build |
| Context Files | `CLAUDE.md` = what to build; `me.md` = how you work | Constraints steer the agent; a file with none steers nothing |

!!! note "End of Module"
    You now hold the field craft: clean documents, enough code-literacy to verify, a confirmed toolbox, and context files that constrain a real agent. Everything is staged for the next module, where you stop practicing the pieces and prove them — a full capstone build under your command.
