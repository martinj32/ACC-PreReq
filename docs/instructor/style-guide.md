# Content Style Guide

Reference for authoring consistent, interactive course pages. Use this before building or editing any module.

---

## Element Types and When to Use Each

### Admonitions (Callout Boxes)

Syntax: `!!! type "Title"`

| Type | Color | Use for |
|---|---|---|
| `note` | Blue | Supplementary context -- helpful but not required to proceed |
| `tip` | Green | Shortcuts, best practices, things that make the task easier |
| `warning` | Orange | Common mistakes, gotchas, things that break if ignored |
| `danger` | Red | Security rules, data handling, hard rules with real consequences |
| `example` | Purple | Concrete worked example before asking the student to try |
| `question` | Teal | Reflection prompt before a formal quiz |

```markdown
!!! warning "Watch Out"
    Students frequently try to skip this step. It will break M3 if skipped.
```

---

### Collapsible Sections

Syntax: `??? type "Title"` (starts collapsed) or `???+ type "Title"` (starts open)

| Use `???` (collapsed) for | Use `???+` (open) for |
|---|---|
| Instructor-only notes | Extra depth students should read but that breaks flow inline |
| Spoilers / answers the student should try first | Context that helps before the exercise |
| Deep reference content | |

```markdown
??? note "Instructor Note -- Common Stumble"
    Students on Windows frequently hit a PATH issue here. Have them run `echo $PATH` first.

???+ tip "Why This Matters"
    Understanding this concept now will save 30 minutes of debugging in Module 3.
```

---

### Tabbed Content

Syntax: `=== "Tab Label"` blocks under each other, with content indented.

Use tabs for:
- OS-specific instructions (Windows / WSL / macOS)
- Weak vs. strong prompt comparisons
- Before / after code examples

```markdown
=== "Windows (WSL)"
    ```bash
    cd /mnt/c/Users/YourName
    ls -la
    ```

=== "macOS"
    ```bash
    cd ~
    ls -la
    ```
```

---

### Task Checklists

Syntax: `- [ ]` and `- [x]` list items.

Use for:
- End-of-module readiness checks ("You are ready to move on when you can...")
- Setup steps where students verify each item before proceeding
- Course readiness checks

```markdown
Before moving to the next module, confirm:

- [ ] You can open a terminal without help
- [ ] You know what `pwd`, `ls`, and `cd` do
- [ ] You ran `ls -la` and read the output
```

---

### Quiz Blocks

**Single-answer quiz** -- one correct option, others wrong:

```html
<div class="quiz-block">
  <p class="quiz-question">Question text here?</p>
  <ul class="quiz-options">
    <li data-correct="false">Wrong option</li>
    <li data-correct="true">Correct option</li>
    <li data-correct="false">Wrong option</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>
```

**Multi-select quiz** -- multiple correct options, add `data-multi` to the block:

```html
<div class="quiz-block" data-multi>
  <p class="quiz-question">Which of these apply? (Select all that apply)</p>
  <ul class="quiz-options">
    <li data-correct="true">Correct option</li>
    <li data-correct="false">Wrong option</li>
    <li data-correct="true">Also correct</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>
```

**Placement rules:**
- One quiz per major concept -- not one per module
- Place after the concept is introduced and an example is shown, not before
- Always precede a quiz with a `!!! question` reflection prompt
- Never put a quiz at the very top of a module

---

### Code Blocks

Always specify the language for syntax highlighting.

````markdown
```bash
pwd
ls -la
cd Documents
```

```python
def greet(name):
    return f"Hello, {name}"
```
````

Use inline code (backticks) for short references within a sentence: `pwd`, `git commit`, `.gitignore`.

---

## Module Structure Template

Every module should follow this order:

```
## Module X.X — Title

**BLUF.** One sentence: what this module is and why it matters.

### Why This Matters
2-3 sentences connecting to something the student already understands.

### Concepts
Content here. Mix prose with admonitions.

!!! example "Worked Example"
    Show before ask.

### Hands-On
Clear instruction for what the student does. Use tabs for OS differences.

!!! question "Before You Continue"
    Reflection prompt.

<div class="quiz-block">
  ...
</div>

### Readiness Check
- [ ] Student can do X
- [ ] Student can explain Y
```

---

## Tone Rules

- Lead with the **why** before the **what**
- Use military doctrinal framing where it fits -- but only when it genuinely fits, not as decoration
- One idea per paragraph
- Short sentences over long ones
- Define every term the first time it appears in a module, even if defined elsewhere
- Active voice: "Run `pwd`" not "The `pwd` command can be run"
