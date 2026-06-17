# Element Test Page

This page tests every interactive element type before use in real content. Delete after verification.

---

## Admonitions (Callout Boxes)

!!! note "Note"
    Use for supplementary context that helps but isn't required to proceed.

!!! tip "Tip"
    Use for shortcuts, best practices, or things that make the task easier.

!!! warning "Watch Out"
    Use for common mistakes, gotchas, or things that will break if ignored.

!!! danger "Hard Stop"
    Use for security rules, data handling, or anything with real consequences.

!!! example "Example"
    Use to show a concrete worked example before asking students to try.

!!! question "Check Your Understanding"
    Use for reflection prompts before a formal quiz.

---

## Collapsible Details

??? note "Click to expand -- Instructor Note"
    Collapsible blocks are for instructor-only context or extra depth that students can choose to read.

???+ tip "This one starts open"
    Use `???+` to start expanded. Use `???` to start collapsed.

---

## Tabbed Content

=== "Windows"
    ```
    cd C:\Users\YourName
    dir
    ```

=== "WSL / Linux"
    ```bash
    cd ~
    ls -la
    ```

=== "macOS"
    ```bash
    cd ~
    ls -la
    ```

---

## Task Checklist

- [x] Installed Python
- [x] Installed MkDocs
- [ ] Completed Module 0.1
- [ ] Completed Module 0.2

---

## Code Block with Syntax Highlighting

```python
# This is a Python code block with syntax highlighting
def greet(name):
    return f"Hello, {name}"

print(greet("ACC Student"))
```

```bash
# Bash example
pwd
ls -la
cd Documents
```

---

## Quiz -- Single Answer

<div class="quiz-block">
  <p class="quiz-question">An LLM generates its responses by:</p>
  <ul class="quiz-options">
    <li data-correct="false">Looking up facts in a database</li>
    <li data-correct="true">Predicting the next likely token based on patterns learned during training</li>
    <li data-correct="false">Searching the internet in real time</li>
    <li data-correct="false">Following a set of hand-coded rules</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

## Quiz -- Multi-Select

<div class="quiz-block" data-multi>
  <p class="quiz-question">Which of the following should NEVER be pasted into an AI tool? (Select all that apply)</p>
  <ul class="quiz-options">
    <li data-correct="true">A document with real names and unit designations</li>
    <li data-correct="false">A generic prompt asking for help drafting a paragraph</li>
    <li data-correct="true">An API key or password</li>
    <li data-correct="true">CUI or classified material</li>
    <li data-correct="false">A made-up scenario used for practice</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## Inline Highlight

The context window is the model's `short-term memory` for a single session.

---

*If all elements above render correctly, the infrastructure is ready. Delete this page and remove it from the nav before publishing.*
