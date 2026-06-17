# Terminal Basics — The Machine

**Who this is for:** Someone who uses computers every day but has never thought about the structure underneath the apps.

**What you will leave with:** You can navigate your filesystem without using search, you know the difference between plaintext and rich text and why it matters, and you have a code editor installed and open without fear.

---

## Files, Folders, and the Tree

**BLUF.** Everything on a computer lives in a file, files live in folders, folders nest into a tree, and the address of any file is the path you walk to reach it — the apps you use have been hiding this structure, and understanding it is the ground everything else stands on.

### Why This Matters

The terminal modules all depend on being able to think about where things are. A student who cannot read a path gets lost the moment they type their first command. This module builds the map before the movement.

### Concepts

A **file** holds data: a document, an image, a script. A **folder** (also called a directory) holds files and other folders. Folders nest inside folders, forming a tree. Every file on the machine has exactly one location in that tree.

The **path** is the route through the tree to reach a file. On Windows it looks like `C:\Users\YourName\Documents\report.txt`. On a Mac or Linux machine it looks like `/home/yourname/documents/report.txt`. Read it left to right: each backslash or forward slash is one step down the tree.

Most apps hide this. When you save a file in Word, you pick a name and Word decides where it goes. The tree exists whether you see it or not.

!!! example "Finding a File You Saved Last Week"
    Open File Explorer (Windows) or Finder (Mac). Navigate to your Downloads folder. Find a file you downloaded recently.

    Look at the address bar at the top — that is the path. Read it. That string of words separated by slashes is the route through the tree to reach that exact file.

!!! tip "Turn on File Extensions Now"
    By default, Windows hides file extensions (the `.docx`, `.txt`, `.pdf` after the name). Turn them on before the next module: File Explorer → View → Show → File name extensions.

    You will need to see extensions throughout this course.

!!! warning "Do Not Assume You Have Seen This"
    Many people save files and find them through search or recent items — they have genuinely never navigated the folder tree. Test yourself: can you find a file you saved last week without using search? If not, that is what this module fixes.

??? note "Instructor Note — Extension Visibility"
    Turning extensions on here prevents confusion in the next module where the difference between `.txt` and `.docx` is the whole lesson. Do not skip this step.

### Hands-On

1. Open File Explorer (Windows) or Finder (Mac).
2. Navigate from your home folder down to Downloads by clicking — do not use search.
3. Find a file. Read its full path in the address bar.
4. Create a new folder on your Desktop. Name it `practice`.
5. Move any file into that folder by dragging.

You are walking the tree by clicking. The Terminal module is the same moves, typed.

!!! question "Before You Continue"
    You just moved a file by dragging. Write out the path to where it now lives. Could you give someone else those directions and have them find it?

<div class="quiz-block">
  <p class="quiz-question">What is a file path?</p>
  <ul class="quiz-options">
    <li data-correct="false">The name of a file, including its extension</li>
    <li data-correct="false">A shortcut that opens a file faster</li>
    <li data-correct="true">The route through the folder tree that locates a specific file</li>
    <li data-correct="false">The history of changes made to a file</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can describe a file, a folder, and how they nest into a tree
- [ ] I can read a path as a route through that tree
- [ ] I have navigated to a specific file without using search
- [ ] File extensions are now visible on my machine

---

## Plaintext vs Rich Text

**BLUF.** A plaintext file is just characters — no hidden formatting, no metadata — and that is exactly what models and tools want, because what you see is literally what the machine reads.

### Why This Matters

At some point you will paste content from Word into an AI tool and wonder why things break. The answer is hidden characters. Understanding this difference diagnoses a category of problems you will hit repeatedly.

### Concepts

**Plaintext** is exactly what it says: text, nothing else. Open a `.txt` file in any program on any machine and you see every character the file contains. No hidden formatting. No metadata. What you see is what the machine reads.

**Rich text** files like `.docx` store formatting instructions alongside the text — bold, font size, margins, revision history, all packed in alongside the words. When you paste from Word into a terminal or a markdown document, those hidden characters come with it.

Common plaintext extensions: `.txt`, `.md`, `.csv`, `.json`, `.py`

Common rich text extensions: `.docx`, `.xlsx`, `.pdf`

!!! example "The Word-to-Markdown Trap"
    Type a bullet point in Word using a hyphen. Word automatically converts your straight quote to a "smart quote" and your double hyphen to an em-dash.

    Paste that into a Markdown file. The Markdown parser reads the curly apostrophe as a plain character. The em-dash breaks the bullet. What looked fine in Word is broken in plaintext.

    The fix: write Markdown in a code editor, not Word.

!!! warning "Pasting from Word Silently Breaks Things"
    Smart quotes, em-dashes, non-breaking spaces, and invisible formatting characters all travel with Word content. When you paste into a terminal, a chat interface, or a Markdown file, those characters come along. If something looks correct but behaves wrong, hidden characters are the first thing to check.

??? note "Instructor Note — Encodings"
    Do not go into encodings (UTF-8, ASCII, etc.) at this level. "Plaintext is honest, rich text hides things" is the entire lesson.

### Hands-On

1. Open Notepad (Windows) and type a few sentences. Save as `test.txt`.
2. Open the same file in VS Code. Compare how it looks.
3. Now open any `.docx` file in VS Code (not Word). Look at what is actually inside it.

You are seeing the difference between "what a human reads" and "what a machine reads."

!!! question "Before You Continue"
    You paste a block of text from a Word document into your AI chatbot and the formatting looks off. What is the most likely cause, and what would you do instead?

<div class="quiz-block">
  <p class="quiz-question">Why do models and command-line tools prefer plaintext over rich-text formats like .docx?</p>
  <ul class="quiz-options">
    <li data-correct="false">Plaintext files are smaller and load faster</li>
    <li data-correct="true">What you see in a plaintext file is exactly what the machine reads — no hidden characters or formatting</li>
    <li data-correct="false">Rich text files require a license to open</li>
    <li data-correct="false">Models cannot open .docx files at all</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can distinguish plaintext from rich text and give an example of each
- [ ] I understand why pasting from Word can silently break things
- [ ] I know the common plaintext extensions
- [ ] I have seen what a .docx file actually looks like underneath

---

## Looking at Files in a Real Editor

**BLUF.** A code editor is a better text viewer — install one, open a folder, read a file, close it without fear; that is the whole job today.

### Why This Matters

The terminal modules require reading files from the command line. The editor gives you a visual companion to that work — the same files, different view. Installing it now removes the install step as a distraction when the lesson is about something else.

### Concepts

A code editor is not an IDE (a full programming environment). It is a text viewer with good defaults: syntax highlighting, a visible file tree, and a preview mode for formatted files.

VS Code is the standard choice here. Free, runs on Windows and Mac, handles every file type in this course.

**Three things to know today:**

- The **file tree panel** (left side) shows the folder structure — the same tree, now labeled.
- The **editor panel** (right side) shows file content.
- **Markdown preview:** click the split-square icon to render a `.md` file's formatting.

!!! example "Rendering a Markdown File"
    Open a `.md` file in VS Code. In the top-right corner, click the preview icon (or press `Ctrl+Shift+V`). The left pane shows raw Markdown; the right pane shows it rendered.

    You are seeing plaintext and its rendered output side by side.

!!! warning "Scope Discipline"
    Today's scope: open, view, close. Do not install extensions, change settings, or start editing files. The goal is comfort at the front door, not a full tour.

??? note "Instructor Note — Install Problems"
    A broken install on one machine should not stall the room. Have a backup viewer (Notepad++ is a lighter alternative) and move on. The lesson is "open and view a file," not "install VS Code perfectly."

### Hands-On

1. Download and install VS Code if you have not already.
2. Go to File → Open Folder. Open the `practice` folder from the previous module.
3. Click the `.txt` file you created. Read it in the editor panel.
4. Find a `.md` file anywhere on your machine. Open it. Toggle the preview.

!!! question "Before You Continue"
    You are looking at the same Markdown file in two panes — raw on the left, rendered on the right. Which version does the machine work with? Which version does the human read?

<div class="quiz-block">
  <p class="quiz-question">What is the main reason to use a code editor instead of Word for working with plaintext files?</p>
  <ul class="quiz-options">
    <li data-correct="false">Code editors have more fonts and formatting options</li>
    <li data-correct="false">Code editors are faster to open</li>
    <li data-correct="true">Code editors work in plaintext — no hidden characters, no automatic formatting changes</li>
    <li data-correct="false">Word cannot open .txt files</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] VS Code (or equivalent) is installed and opens without errors
- [ ] I can open a folder and navigate its tree in the editor
- [ ] I have opened a Markdown file and toggled the rendered preview
- [ ] I did not change any settings or install any extensions
