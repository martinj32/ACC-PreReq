# AI / Agentics Basics — Day 0 (Pre-Course)

**Theme:** Get a true beginner from zero to a solid foundation in AI literacy and command-line fluency.
**Outcome:** A student who has never touched a terminal walks out able to navigate a filesystem from the command line, has a working mental model of what an LLM is and how it fails, prompts deliberately instead of by feel, and understands that an agent acts on their real machine. They are ready to load an engine into a harness without freezing.

---

## Course BLUF

This block is numbered `0.x` as the foundation layer of the course. It is built for **casual AI users with zero terminal experience**, run over **multiple weeks** in short daily reps rather than long blocks.

Calibration note for instructors: the audience is *zero on the machine, not zero on the chatbot*. They already use ChatGPT or Claude. Do not bore them through the AI weeks; spend the reclaimed time on the terminal, which is the actual washout gate. Every module is do-first: the student touches the thing, then you explain the concept using what they just watched happen.

### The four phases

| Phase | Title | What it builds | Calendar weight |
|---|---|---|---|
| 1 | Know What You Are Talking To | Mental model + failure modes + deliberate prompting | Light (refresher pace) |
| 2 | The Computer Underneath | File and folder literacy, no AI | Medium |
| 3 | The Terminal | Command-line muscle memory | **Heaviest — the spine** |
| 4 | From Chatbot to Agent | The bridge that makes Phases 2 and 3 pay off | Medium |

### What Each Phase Unlocks

| Phase | Skills it delivers |
|---|---|
| 1 | LLM mental model, prompting, context awareness, frontier landscape, data hygiene |
| 2 | File system literacy, plaintext vs. rich text, code editor comfort |
| 3 | Terminal navigation, file operations, paths, flags, command control |
| 4 | Chatbot vs. agent distinction, version control concept, delivery models, supervisor mindset |

---

# PHASE 1 — Know What You Are Talking To

*Start in the tool they already use. Anxiety low, ground familiar. Convert intuition into method.*

## Module 0.1 — What an LLM Actually Is

**BLUF.** An LLM predicts text from learned patterns — not rules, not memory, not live data — and that single fact explains both why it is extraordinarily capable and exactly how it fails.

### Why This Matters

You already use one. What you have been doing by feel — type a request, read a response — is about to get a mental model underneath it. That model will not slow you down. It will make every module after this one click immediately instead of slowly.

### Concepts

The model reads a sequence of text and predicts what comes next. One chunk at a time. No lookup table. No truth check. Given everything written so far, what is the statistically most likely next piece?

!!! example "What Prediction Looks Like"
    Open your chatbot. Type: "The capital of France is" — and submit before you finish the sentence.

    The model completes it. Now type: "The capital of France is definitely" and watch the completion shift slightly.

    That is prediction. The word "definitely" changed the statistical context. The model did not look anything up.

**Trained, not programmed.** No one wrote a rule that says "Paris is the capital of France." The model was trained on enough text containing that fact that its weights now make it the likely completion. The upside: it generalizes to almost anything. The failure mode: if the training data was wrong, biased, or thin in some domain, the model learned those patterns too. There is no rulebook to audit.

**The LLM is the engine.** By itself, it is a brain in a jar — capable of reasoning in text, incapable of acting on its own. It reads text and writes text. No body, no memory between chats, no live connection to the world unless something external gives it one. Fluent, confident output is not the same as correct output. Both are true at the same time.

!!! warning "Swap the Verb"
    The model does not "know," "want," "think," or "lie." Those words will mislead you at every later step. It **predicts**. That is the only accurate verb. Catch yourself using the others and swap it in.

??? note "Instructor Note — Architecture Questions"
    Do not open with attention heads, transformers, or parameter counts. A casual user needs a mental model that survives contact with a real tool, not the mechanism behind it. If a student asks, acknowledge it as a real question and defer: "That is a deeper topic — let's come back to it." Do not let one question pull the module off course.

??? note "Instructor Note — Anthropomorphism Runs Deep"
    Students told "it just predicts" will still say "it knew the answer" thirty seconds later. Anthropomorphism is not careless phrasing; it is a wired cognitive shortcut. Interrupt it every time it appears in the first two weeks. It re-trains faster than you expect.

### Hands-On

The lab is the chatbot you already have open.

1. Ask it something you already know well enough to spot an error.
2. Read the output. Ask yourself: "How would I verify this?"
3. Ask it to continue a sentence you leave unfinished.

You are watching prediction happen in real time.

!!! question "Before You Continue"
    The model just gave you a confident-sounding answer. What would it take to verify it? Where would you check?

<div class="quiz-block">
  <p class="quiz-question">A language model was never given a rule that says "Paris is the capital of France." How does it produce that answer?</p>
  <ul class="quiz-options">
    <li data-correct="false">It searched the internet for the answer</li>
    <li data-correct="false">A programmer hard-coded that fact into its rules</li>
    <li data-correct="true">It was trained on enough text containing that fact that the pattern was learned into its weights</li>
    <li data-correct="false">It remembered it from a previous conversation</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.2, confirm:

- [ ] I can state in one sentence what an LLM does
- [ ] I can explain "trained not programmed" in plain terms
- [ ] I know that confident output and correct output are not the same thing
- [ ] I have watched the model predict — not just heard about it

---

## Module 0.2 — Tokens and Context

**BLUF.** The model reads and writes in tokens — roughly 0.75 of an English word each — and can only hold a fixed number at once; fill that limit and earlier content starts to fall out, which is why long sprawling chats get worse, not better.

### Why This Matters

This is the first place the engine's behavior surprises casual users. They expect a longer conversation to give the model more to work with. The opposite happens once you pass the limit. Knowing why changes how you work.

### Concepts

**Tokens.** The model does not read words; it reads chunks of text called tokens. In English prose, one token is roughly three-quarters of a word. Code and non-English text tokenize less efficiently — more tokens per word. You do not need to count tokens precisely; the instinct to keep input focused is the deliverable.

**The context window.** Every model has a hard ceiling on how many tokens it can hold in a single conversation. That ceiling is the context window. Think of it as a whiteboard with finite space: new writing crowds out old writing once it fills.

!!! example "Watching the Window Fill"
    Open a long document — several pages — and paste it into a fresh chat. Ask a detailed question about something near the top.

    Now open a new chat, paste the same document, and ask about something near the bottom.

    Compare the quality. Models attend better to the beginning and end of their context window than to the middle. Critical instructions buried mid-conversation may be partially ignored.

**What a full window looks like.** The model starts hedging. It contradicts something it stated confidently ten turns ago. It forgets a constraint you set at the start. That is not a bug; it is the whiteboard running out of space.

!!! tip "The Practical Rule"
    Start a fresh chat when: (1) the task has changed direction and earlier turns are dead weight, or (2) the model is drifting — hedging on things it stated confidently before.

??? note "Instructor Note — Context Window Sizes"
    Approximate sizes as of mid-2026 — verify before teaching, these change with releases: Claude: 200,000 tokens. GPT-4o: 128,000 tokens. Gemini 2.0: 1,000,000+ tokens. Bigger is not always better — a full million-token window degrades quality in the middle. Name that trap before a student assumes more is always more.

??? note "Instructor Note — Token Math"
    Do not spend time on arithmetic. The instinct "shorter and focused beats long and sprawling" is the deliverable, not the numbers. If a student asks how many tokens something is, most major chatbots surface a token count in their interface or API — point them there.

### Hands-On

1. Open a fresh chat and paste several paragraphs of dense text.
2. Ask the model to summarize just the first paragraph.
3. In the same chat, ask it about something from the end of what you pasted.
4. Start a new chat and ask the same question. Compare.

You are probing the window's edges.

!!! question "Before You Continue"
    You set an important constraint at the start of a long conversation. Ten exchanges later, the model seems to have forgotten it. What happened, and what would you do differently next time?

<div class="quiz-block">
  <p class="quiz-question">You are in a long chat and the model starts contradicting instructions you gave at the start. What is the most likely cause?</p>
  <ul class="quiz-options">
    <li data-correct="false">The model changed its mind</li>
    <li data-correct="false">You used the wrong model for this task</li>
    <li data-correct="true">Earlier content has been crowded out of the context window</li>
    <li data-correct="false">The model is testing whether you notice</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.3, confirm:

- [ ] I can define a token in plain terms
- [ ] I can explain what a context window is and what happens when it fills
- [ ] I know the two situations that warrant starting a fresh chat
- [ ] I have observed the window effect — not just read about it

---

## Module 0.3 — How LLMs Fail

**BLUF.** The model will state false things with total confidence, give different answers to the same question, and know nothing past its training cutoff — none of this is a malfunction, and seeing it fail on purpose is the most important inoculation in this course.

### Why This Matters

You are about to trust this tool with real work. Calibrated trust requires knowing exactly where it breaks. A student who leaves this module without producing a hallucination with their own hands has not completed it.

### Concepts

Four failure modes. Know all four.

**Hallucination.** The model has no truth-checking step. It generates tokens that are statistically likely to follow prior context. It cannot distinguish "information I was trained on accurately" from "information I am completing plausibly." Confident output and correct output are entirely unrelated. This is expected behavior of the system, not a rare bug.

**Confident-wrong.** Hallucination is not always dramatic. The model may state a subtly wrong date, a slightly wrong statistic, or a plausible-sounding citation that does not exist. The tone stays equally confident whether the claim is right or wrong. Never use the model's confidence as a signal of accuracy.

**Nondeterminism.** The model uses a temperature parameter that introduces variation. Same prompt, different run, different result — by design. Do not treat one output as "the answer" for high-stakes work. Run important prompts more than once and compare.

**Knowledge cutoff.** The model was trained on data up to a point in time. It does not know what happened after that. Ask about a recent event and it may refuse, guess, or confidently describe something that did not happen.

!!! warning "Build the Verification Reflex Now"
    Anything that matters gets checked before you act on it. Not because the model is bad at its job — because this is how the system works. The operator who skips verification is the weak link, not the model.

??? note "Instructor Note — Eliciting Hallucinations on Demand"
    Make students produce a hallucination with their own hands. Telling them it happens does not land; watching it happen does. Reliable methods:

    - **Invented citations:** Ask for 5 peer-reviewed papers on a narrow topic with authors and publication years. The model produces plausible-sounding but fabricated citations. Ask for a DOI — it will be invented.
    - **Biographical detail:** Ask for the detailed career history of a real but not-famous person. The model fills gaps with plausible-sounding detail.
    - **Recent events past cutoff:** Ask about an event you know happened after the training cutoff. The model may confidently describe what did not happen.

    Pick a topic where you know the correct answer so you can immediately show the error. Never demo on live operational content.

??? note "Instructor Note — Don't Let It Tip Into Cynicism"
    The point is calibrated trust, not distrust. The model is extraordinarily capable *and* it hallucinates. Both are true simultaneously. If students leave deciding the model is useless, the lesson failed.

### Hands-On

1. Ask the model for 5 peer-reviewed sources on a specific narrow topic. Ask for author names, journal names, and publication years.
2. Pick one citation and try to verify it exists.
3. Ask the same question in a new chat. Compare the answers.
4. Ask about something you know happened recently. Watch how it responds.

!!! question "Before You Continue"
    You just watched the model invent a source. What does that mean for the next time it gives you a fact you have not heard before?

<div class="quiz-block">
  <p class="quiz-question">You run the same prompt twice in two separate chats and get different answers. What is the most accurate explanation?</p>
  <ul class="quiz-options">
    <li data-correct="false">One of the chats had a longer context window</li>
    <li data-correct="false">The model updated itself between the two runs</li>
    <li data-correct="true">The model uses randomness by design — the same input does not guarantee the same output</li>
    <li data-correct="false">You phrased the prompt slightly differently without noticing</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.4, confirm:

- [ ] I can name the four core failure modes
- [ ] I have produced a hallucination with my own hands
- [ ] I understand that confidence and correctness are unrelated in model output
- [ ] I know why this module is the reason a human stays in the loop

---

## Module 0.4 — Deliberate Prompting

**BLUF.** Converting prompting-by-feel into method means telling the model who to be, giving it the context it needs, showing it an example, and saying what good output looks like — the same as briefing a person, not typing into a search box.

### Why This Matters

A vague prompt is a vague order, and a vague order gets a vague result from a junior who fills the gaps with assumptions. You have already seen what the model does when it guesses wrong. Deliberate prompting is how you reduce that surface area.

### Concepts

The model meets you halfway the moment you give it structure. Without context, it must guess: who you are, what you need, what "good" looks like. Guessing produces generic output. Four elements close that gap:

- **Role.** Tell the model who to be. "You are a plain-language editor" produces different output than no framing at all.
- **Context.** Tell it what it needs to know that it cannot infer. What is the task, who is the audience, what constraints apply.
- **Example.** Show it what good output looks like before asking for it. One strong example beats three paragraphs of description.
- **Output spec.** Tell it the format, length, and tone you want.

!!! example "Before and After"
    **Weak prompt:** "Write me a summary."

    **Strong prompt:** "You are summarizing this for a senior leader who has two minutes. Pull out the three most important points. Use bullet points. No jargon. Max 100 words."

    Same model. Different brief. Different result.

The iterative habit matters more than the perfect prompt. A rough ask the model can build on beats silence. Read the output, tighten the next ask based on what missed, repeat. That is the whole skill.

!!! tip "If You Are Stuck, Ask the Model to Interview You"
    Type: "I need help with [task]. Ask me the questions you need answered before you start."

    The model surfaces what context it is missing. Answer the questions, then ask it to proceed.

!!! warning "The Template Trap"
    The four elements are a structure, not a script to recite. Do not build a rigid template you apply mechanically. The durable skill is clarity — giving the model what it needs to not guess. How you deliver that varies by task.

??? note "Instructor Note — Prompt Engineering Creep"
    Resist turning this into a "prompt engineering tricks" hour. Magic phrases and hidden commands are not the lesson. The lesson is clarity. Students who focus on tricks over structure will hit a ceiling fast.

### Hands-On

1. Pick a real task you need help with.
2. Write a one-line version of the request. Submit it. Save the output.
3. Now add role, context, an example of what good looks like, and an output spec. Submit again.
4. Compare the two outputs side by side.

!!! question "Before You Continue"
    What specifically changed between your first output and your second? Which of the four elements made the biggest difference for your task?

<div class="quiz-block">
  <p class="quiz-question">You ask the model to "write a report." It produces something generic and too long. What is the most effective fix?</p>
  <ul class="quiz-options">
    <li data-correct="false">Switch to a more powerful model</li>
    <li data-correct="false">Ask the same question again and hope for a better result</li>
    <li data-correct="true">Add role, context, an example of good output, and a length/format spec to the prompt</li>
    <li data-correct="false">Break the report into smaller pieces and ask for each separately</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.5, confirm:

- [ ] I can name the four elements of a deliberate prompt
- [ ] I have run a before/after comparison with my own real task
- [ ] I treat prompting as a conversation, not a one-shot command
- [ ] I know the difference between prompting by feel and prompting by structure

---

# PHASE 2 — The Computer Underneath

*Genuinely new material for this audience. No AI here. Plain computer literacy. Keep threading short terminal previews in so Phase 3 is not a cliff.*

## Module 0.5 — Files, Folders, and the Tree

**BLUF.** Everything on a computer lives in a file, files live in folders, folders nest into a tree, and the address of any file is the path you walk to reach it — the apps they use have been hiding this structure, and understanding it is the ground everything else stands on.

### Why This Matters

The terminal modules in Phase 3 all depend on being able to think about where things are. A student who cannot read a path is a student who gets lost the moment they type their first command. This module builds the map before the movement.

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

!!! warning "Do Not Assume They Have Seen the Tree"
    Many casual users save files and find them through search or recent items — they have genuinely never navigated the folder structure. Verify by asking: "Can you find a file you saved last week without using search?" Walk through it if not.

??? note "Instructor Note — Extension Visibility"
    Turning extensions on here prevents confusion in Module 0.6 where the difference between `.txt` and `.docx` is the whole lesson. Do not skip this step.

### Hands-On

1. Open File Explorer (Windows) or Finder (Mac).
2. Navigate from your home folder down to Downloads by clicking — do not use search.
3. Find a file. Read its full path in the address bar.
4. Create a new folder on your Desktop. Name it `practice`.
5. Move any file into that folder by dragging.

You are walking the tree by clicking. Phase 3 is the same moves, typed.

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

Before moving to Module 0.6, confirm:

- [ ] I can describe a file, a folder, and how they nest into a tree
- [ ] I can read a path as a route through that tree
- [ ] I have navigated to a specific file without using search
- [ ] File extensions are now visible on my machine

---

## Module 0.6 — Plaintext vs Rich Text

**BLUF.** A plaintext file is just characters — no hidden formatting, no metadata — and that is exactly what models and tools want, because what you see is literally what the machine reads.

### Why This Matters

Students will paste content from Word documents into AI tools and wonder why things break. The answer is hidden characters. Understanding this difference is the diagnosis for a category of problems they will hit repeatedly.

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
    Do not go into encodings (UTF-8, ASCII, etc.) at this level. "Plaintext is honest, rich text hides things" is the entire lesson. If a student asks, acknowledge it as real and defer.

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

Before moving to Module 0.7, confirm:

- [ ] I can distinguish plaintext from rich text and give an example of each
- [ ] I understand why pasting from Word can silently break things
- [ ] I know the common plaintext extensions
- [ ] I have seen what a .docx file actually looks like underneath

---

## Module 0.7 — Looking at Files in a Real Editor

**BLUF.** A code editor is a better text viewer — install one, open a folder, read a file, close it without fear; that is the whole job today.

### Why This Matters

The terminal modules require reading files from the command line. The editor gives students a visual companion to that work — the same files, different view. Installing it now removes the install step as a distraction when the lesson is about something else.

### Concepts

A code editor is not an IDE (a full programming environment). It is a text viewer with good defaults: syntax highlighting, a visible file tree, and a preview mode for formatted files.

VS Code is the standard choice here. Free, runs on Windows and Mac, handles every file type in this course.

**Three things to know today:**

- The **file tree panel** (left side) shows the folder structure from Module 0.5 — the same tree, now labeled.
- The **editor panel** (right side) shows file content.
- **Markdown preview:** click the split-square icon to render a `.md` file's formatting.

!!! example "Rendering a Markdown File"
    Open a `.md` file in VS Code. In the top-right corner, click the preview icon (or press `Ctrl+Shift+V`). The left pane shows raw Markdown; the right pane shows it rendered.

    You are seeing plaintext (Module 0.6) and its rendered output side by side.

!!! warning "Scope Discipline"
    Today's scope: open, view, close. Do not install extensions, change settings, or start editing files. Editors are intimidating by appearance. The goal is comfort at the front door, not a full tour.

??? note "Instructor Note — Install Problems"
    A broken install on one machine should not stall the room. Have a backup viewer (Notepad++ is a lighter alternative) and move on. The lesson is "open and view a file," not "install VS Code perfectly."

### Hands-On

1. Download and install VS Code if you have not already.
2. Go to File → Open Folder. Open the `practice` folder from Module 0.5.
3. Click the `.txt` file you have in there. Read it in the editor panel.
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

Before moving to Module 0.8, confirm:

- [ ] VS Code (or equivalent) is installed and opens without errors
- [ ] I can open a folder and navigate its tree in the editor
- [ ] I have opened a Markdown file and toggled the rendered preview
- [ ] I did not change any settings or install any extensions

---

# PHASE 3 — The Terminal

*The spine of the course. Maximum scaffolding, maximum reps, spread across the most calendar time. Every single rep is framed as "this is how the agent will move around your computer for you." Ten minutes a day for two weeks beats one long block.*

## Module 0.8 — What the Terminal Is (and Why It Is Safe)

**BLUF.** The terminal is a typed way to give the computer the same instructions you used to give by clicking — it is not hacking, it is not dangerous by default, and it feels alien for about an hour before it feels normal.

### Why This Matters

The terminal is the spine of this course and the emotional washout point. Some students will feel a bait-and-switch: "I signed up to use AI, why am I typing Unix commands." The answer is in Module 0.13. Defusing the anxiety now is what makes Phase 3 stick.

### Concepts

A command is a typed instruction. It is the same as a click — it tells the computer to do something. The difference is precision: a click is constrained by what a menu shows you; a command can express anything the machine understands.

The terminal is direct comms with the machine. Clicking is talking through an interpreter; the command line is speaking the language directly. It feels uncomfortable until it doesn't — the same as any new comms procedure. You drill it until it is second nature.

The **prompt line** is where your typing goes. It usually ends with a `$` (Mac/Linux) or `>` (Windows PowerShell). When you see that character, the terminal is ready for input.

!!! example "Your First Command"
    Open the terminal. On Windows: search for "PowerShell" or "Terminal" in the Start menu. On Mac: search for "Terminal" in Spotlight.

    Type `date` (Mac/Linux) or `Get-Date` (Windows PowerShell) and press Enter.

    The terminal printed the current date and returned the prompt. That is a command. You did it.

!!! warning "Nothing Today Can Hurt the Machine"
    The commands in this module and the next two are read-only and harmless. You are looking at the filesystem, not modifying it. Anything that can cause real damage comes much later, behind heavy framing.

??? note "Instructor Note — The Bait-and-Switch Objection"
    Address it out loud before a student says it. Name the frustration: "Some of you are wondering why an AI course spent two weeks on the command line." Then make the connection to Module 0.13 explicit: the agent acts through the terminal. The student who does not understand the terminal cannot supervise an agent that is using it.

??? note "Instructor Note — Scope Discipline"
    One command, fully understood, beats ten demoed. Do not show off. A wall of commands in the first session loses the room. Return the prompt, explain what happened, ask if there are questions, then move on.

### Hands-On

1. Open the terminal on your machine.
2. Sit with the blinking cursor for ten seconds. Name the feeling. Then continue.
3. Type the command to print the current date. Press Enter.
4. Close the terminal and open it again.

That is it. You opened it, ran something, and closed it. The anxiety has a smaller surface area now.

!!! question "Before You Continue"
    You typed a command and saw a response. What is the difference between that and clicking a button in an app? What stayed the same?

<div class="quiz-block">
  <p class="quiz-question">What does a terminal actually do?</p>
  <ul class="quiz-options">
    <li data-correct="false">It connects you to the internet through a secure tunnel</li>
    <li data-correct="false">It runs programs faster than clicking does</li>
    <li data-correct="true">It accepts typed instructions and passes them to the operating system — the same as clicking, without the menu</li>
    <li data-correct="false">It is a special tool only developers have access to</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.9, confirm:

- [ ] I can open the terminal on my machine
- [ ] I ran one command and read its output
- [ ] I can find the prompt line and know where my typing goes
- [ ] The anxiety is smaller than it was at the start of this module

---

## Module 0.9 — Navigating: Where Am I, What Is Here

**BLUF.** Three commands cover most of navigation — where am I, what is here, move — and mastering them by typing replaces every click from Module 0.5.

### Why This Matters

Getting "lost" in the filesystem is the number-one beginner panic in Phase 3. These three commands are the reset button. Know them cold and you can always find your way back to a known position.

### Concepts

This is land navigation: where am I, what is around me, how do I move. You read the map in Phase 2; now you move across it on foot.

| Command | Job | Works on |
|---|---|---|
| `pwd` | Print current location | Mac, Linux, WSL, PowerShell |
| `ls` | List folder contents | Mac, Linux, WSL, PowerShell |
| `cd foldername` | Move into a folder | All |
| `cd ..` | Move up one level | All |

`pwd` — **P**rint **W**orking **D**irectory. Your current location in the tree.

`ls` — **L**i**s**t. Everything in the current folder. Add `-la` (Mac/WSL) for details including hidden files.

`cd` — **C**hange **D**irectory. `cd foldername` moves down; `cd ..` moves up.

!!! example "Walking the Tree"
    ```bash
    pwd              # See where you are
    ls               # See what is here
    cd Documents     # Move into Documents
    pwd              # Confirm you moved
    ls               # See what is in Documents
    cd ..            # Move back up one level
    pwd              # Confirm you are back
    ```

    Walk this sequence on your own machine. You are doing the exact same moves you did by clicking in Module 0.5 — same tree, typed instead.

!!! tip "pwd Is Your Reset Button"
    Any time you feel lost in the terminal, type `pwd`. It tells you exactly where you are. You can never be permanently lost if you can always ask "where am I."

??? note "Instructor Note — Reps Over Coverage"
    Same three commands, many short repetitions, spread across several days. Do not introduce file creation yet. One capability at a time. Reps build muscle memory; coverage builds confusion.

### Hands-On

1. Open the terminal. Run `pwd`. Read the path. Find that same location in File Explorer.
2. Run `ls`. Identify three items by name.
3. Run `cd` to move into one of them.
4. Run `pwd` and `ls` again.
5. Run `cd ..` to go back up.

Repeat this cycle until it feels routine.

!!! question "Before You Continue"
    You typed `cd Documents` and then `pwd`. What does `pwd` tell you, and how does it prove you moved?

<div class="quiz-block">
  <p class="quiz-question">You are in the terminal and have no idea where you are in the filesystem. What is the first command you run?</p>
  <ul class="quiz-options">
    <li data-correct="false">`ls` to see what files are nearby</li>
    <li data-correct="true">`pwd` to print your current location</li>
    <li data-correct="false">`cd` to move to a known folder</li>
    <li data-correct="false">Close and reopen the terminal to reset</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.10, confirm:

- [ ] I can print my current location with `pwd`
- [ ] I can list folder contents with `ls`
- [ ] I can move into and back out of folders with `cd` and `cd ..`
- [ ] I have walked the same tree by clicking (0.5) and by typing (this module)

---

## Module 0.10 — Acting: Make, Move, Copy

**BLUF.** Four commands cover most day-to-day file work — make a folder, make a file, copy, move — the same actions from Module 0.5, now typed.

### Why This Matters

Navigation got you to the position; now you act on it. This is where the terminal goes from "I can look around" to "I can do things." These four commands are the ones an agent will use most when it works in your filesystem.

### Concepts

Every action you take, you confirm. You do not assume the round landed — you check the target. The habit starts here.

=== "Mac / WSL / Linux"
    | Command | What it does |
    |---|---|
    | `mkdir foldername` | Make a new folder |
    | `touch filename.txt` | Make a new empty file |
    | `cp source destination` | Copy a file |
    | `mv source destination` | Move or rename a file |

=== "Windows (PowerShell)"
    | Command | What it does |
    |---|---|
    | `mkdir foldername` | Make a new folder |
    | `New-Item filename.txt` | Make a new empty file |
    | `cp source destination` | Copy a file |
    | `mv source destination` | Move or rename a file |

!!! example "Build Something From Scratch"
    ```bash
    mkdir project
    cd project
    touch notes.txt
    ls                              # Verify notes.txt is there
    mkdir drafts
    cp notes.txt drafts/notes-copy.txt
    ls drafts                       # Verify the copy landed
    mv notes.txt notes-v1.txt
    ls                              # Verify the rename happened
    ```

    After each command, run `ls` to confirm the change happened. That is the verify-after-acting habit — build it now.

!!! warning "No Deletion Yet"
    Deletion is irreversible at the command line. There is no Recycle Bin. It comes later, behind heavy framing. For now: make, copy, and move only.

!!! warning "Typos Create New Files"
    If you mistype a filename, the command does not error — it creates a second file with the wrong name. Run `ls` after every action and read the output.

??? note "Instructor Note — The Verify Habit"
    "Trust the action, not the narration" is a principle that runs through all agentic work. Build it here, at the command line, before the agent is involved. A student who verifies every terminal action will verify every agent action later.

### Hands-On

1. Make a folder called `phase3-practice`.
2. Navigate into it.
3. Create a file called `day1.txt`.
4. Copy it to `day1-backup.txt`.
5. Rename `day1.txt` to `day1-v1.txt`.
6. Run `ls` after each step to verify the change.

!!! question "Before You Continue"
    You ran `mv notes.txt notes-final.txt`. What does `ls` show you, and what would it look like if you had made a typo in the destination name?

<div class="quiz-block">
  <p class="quiz-question">You run `mv report.txt final-report.txt` and then `ls`. What are you checking for?</p>
  <ul class="quiz-options">
    <li data-correct="false">Whether the file's contents changed</li>
    <li data-correct="false">Whether the command is still running</li>
    <li data-correct="true">Whether `final-report.txt` exists and `report.txt` is gone — confirming the rename happened correctly</li>
    <li data-correct="false">Whether the file is now read-only</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.11, confirm:

- [ ] I can create a folder and a file from the command line
- [ ] I can copy and move/rename files
- [ ] I run `ls` after every action to verify it happened
- [ ] I have not attempted to delete anything yet

---

## Module 0.11 — Paths, Tab-Completion, and the Up-Arrow

**BLUF.** A path is the full address of a file; tab-completion finishes names so you stop fat-fingering them; the up-arrow recalls your last command — three tools that separate fighting the terminal from flowing in it.

### Why This Matters

Typos in paths fail silently or hit the wrong target. Tab-completion is the single biggest accuracy and morale win in the terminal. The up-arrow turns one good command into a reusable tool. These are not tricks; they are standard operating procedure.

### Concepts

**Absolute vs. relative paths.**

An **absolute path** starts from the root of the filesystem and gives the full route: `C:\Users\YourName\Documents\report.txt` (Windows) or `/home/yourname/documents/report.txt` (Mac/Linux). It works from anywhere.

A **relative path** starts from wherever you currently are: `Documents/report.txt` or `../otherfolder/file.txt`. It only works if you are in the right starting position.

A path is a grid coordinate: precise, unambiguous, and unforgiving of a wrong character. A space or a capital letter in the wrong place either fails or hits the wrong target. The space is load-bearing.

!!! example "Absolute vs. Relative in Practice"
    You are in `/home/yourname/`. Both of these reach the same file:

    - Absolute: `/home/yourname/documents/report.txt`
    - Relative: `documents/report.txt`

    Move to a different folder and the relative path breaks. The absolute path still works.

**Tab-completion.** Start typing a folder or file name and press Tab. The terminal finishes it. If there is more than one match, press Tab twice to see the options. This is not a shortcut — it is the standard. Use it on every path, every time.

**The up-arrow.** Press the up-arrow to cycle through previous commands. Edit a recalled command and re-run it instead of retyping from scratch.

!!! tip "The Most Important Habit in This Module"
    Never finish typing a long path by hand if tab-completion can do it. A typo in a path is invisible until something breaks. Tab-completion makes typos structurally impossible for the completed portion.

??? note "Instructor Note — Exactness as Frustration"
    The terminal's unforgiving exactness is both the lesson and the frustration here. A student annoyed that a capital letter breaks a path is learning the right thing. Name it: "Yes, the space matters. The capital letter matters. That is why tab-completion exists."

### Hands-On

1. Navigate to a folder using the full absolute path — type it out by hand once to feel the length.
2. Navigate to the same folder using tab-completion. Press Tab after each segment.
3. Run `ls` in a folder with several items. Start typing one item's name, press Tab, watch it complete.
4. Run a command. Press the up-arrow. Edit one character and re-run it.

!!! question "Before You Continue"
    You are deep in a nested folder and need to copy a file to a location three levels up. Would you use an absolute or a relative path? Why?

<div class="quiz-block">
  <p class="quiz-question">Why does tab-completion reduce errors in terminal commands?</p>
  <ul class="quiz-options">
    <li data-correct="false">It suggests the most recently used command</li>
    <li data-correct="false">It checks whether the path is valid before you submit</li>
    <li data-correct="true">It completes names from what actually exists on disk, so the completed portion cannot contain a typo</li>
    <li data-correct="false">It speeds up the terminal by caching common paths</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.12, confirm:

- [ ] I can write both an absolute and a relative path to the same file
- [ ] I use tab-completion on every path — it is now a habit, not an option
- [ ] I can recall and edit previous commands with the up-arrow
- [ ] I understand why exactness (spaces, capitalization) matters in a path

---

## Module 0.12 — Commands, Flags, and Knowing When to Stop

**BLUF.** Most commands take flags that change what they do; `--help` shows you all available flags without memorization; and `Ctrl+C` stops anything that will not quit — this rounds out terminal literacy before Phase 4.

### Why This Matters

Students are about to encounter CLI tools that require flags to run correctly. They will also encounter commands that hang. Both situations create confusion and abandonment if the student does not know what to do. This module removes both as blockers.

### Concepts

**Flags** are options you add to a command to change its behavior. They usually start with `-` (short form) or `--` (long form).

```bash
ls          # List files, default view
ls -l       # List files, detailed view
ls -la      # List files, detailed view, including hidden files
```

Same command. Different flags. Different output. Flags are the settings you dial in before you give the order — same command, different mission profile.

**Finding flags.** You do not memorize flags. You look them up.

```bash
ls --help     # Shows all flags and what they do
```

Read the `--help` output top to bottom. It looks overwhelming the first time. Find the flag you need; ignore the rest.

**The prompt is the signal.** When a command finishes, the prompt returns. If the cursor blinks with no prompt and nothing is happening, the command is still running.

**Ctrl+C** stops a running command and returns the prompt. It does not delete anything; it stops execution and hands control back to you.

!!! example "Stopping a Running Command"
    Run `ping google.com` (or `ping -t google.com` on Windows). Watch it run indefinitely. Press `Ctrl+C`. The command stops and the prompt returns.

    You just demonstrated that you can stop anything you start.

!!! warning "Do Not Memorize Flags"
    The concept of a flag and how to look one up is the lesson. Memorizing specific flags is the wrong target. The skill is knowing flags exist and knowing how to find the one you need.

??? note "Instructor Note — Forward Links"
    Name forward connections explicitly. Flags prepare students for CLI tools in agentic environments. `Ctrl+C` is a control mechanism, not an emergency procedure. Students who know they can stop something are less afraid to start it.

### Hands-On

1. Run `ls --help` (Mac/Linux) or `Get-Help ls` (PowerShell). Read the first ten lines without panic.
2. Find the flag that shows hidden files. Run `ls` with that flag.
3. Run `ping google.com` (`ping -t google.com` on Windows). Let it run for five seconds.
4. Press `Ctrl+C`. Confirm the prompt returned.

!!! question "Before You Continue"
    You run a command and nothing happens for thirty seconds — the cursor just blinks. What are the two possibilities, and how do you handle each one?

<div class="quiz-block">
  <p class="quiz-question">You need to run `ls` but want to see hidden files. You do not know the flag. What do you do?</p>
  <ul class="quiz-options">
    <li data-correct="false">Google "ls hidden files" and copy the answer</li>
    <li data-correct="false">Try adding flags at random until one works</li>
    <li data-correct="true">Run `ls --help` and find the flag in the output</li>
    <li data-correct="false">Ask the AI chatbot — the terminal cannot tell you its own flags</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.13, confirm:

- [ ] I can add a flag to a command and observe the difference in output
- [ ] I can use `--help` to find a flag I do not know
- [ ] I know the prompt returning means a command finished
- [ ] I can stop a running command with `Ctrl+C` without fear

---

# PHASE 4 — From Chatbot to Agent

*The bridge that makes Phases 2 and 3 pay off. This is the "oh, that is why I learned all that" moment. Tie everything back to the agent touching the student's real machine.*

## Module 0.13 — Chatbot vs Agent

**BLUF.** A chatbot gives advice; an agent takes action — the difference is read, write, and execute access to the real files and terminal the student just learned, which is exactly why Phases 2 and 3 existed.

### Why This Matters

This is the payoff module. If Phases 2 and 3 felt like a detour, this is where you prove they were not. Everything the agent does, it does through the filesystem and the terminal. A student who cannot read the terrain cannot supervise someone moving across it.

### Concepts

Ask a chatbot to rename a folder: it tells you the command. Ask an agent: it renames the folder.

That is the entire difference. The agent has access.

**Three levels of access:**

- **Read.** The agent can look at your files.
- **Write.** The agent can create and modify your files.
- **Execute.** The agent can run commands in your terminal.

The LLM is the engine. A harness with tools is what gives it hands. You are the operator who points it at the right problem and pulls the plug when it heads somewhere wrong. Engine plus harness plus operator — everything in advanced agentic work stacks on this primitive.

!!! warning "Read, Write, Execute Is a Lot of Trust"
    This is not abstract. An agent with write and execute access can create, modify, or delete files on your real machine. Module 0.16 sets the bright line for what that access means. Do not skip it.

??? note "Instructor Note — Make the Connection Explicit"
    Do not assume students connect the dots. Say it out loud: "Every command you learned in Phase 3 — `pwd`, `ls`, `cd`, `mkdir`, `mv` — that is what the agent runs when it works in your filesystem. You learned to navigate the terrain so you can supervise someone else navigating it." Make the payoff land.

### Hands-On

1. Open your chatbot. Ask it: "Rename the folder 'project' to 'project-v1'." Read what it gives you.
2. Identify: did it rename the folder, or did it tell you how?
3. Think about what would need to change for it to perform the action instead of describe it.

!!! question "Before You Continue"
    You just asked a chatbot to rename a folder. What would an agent do differently — and what are you trusting it with when it does?

<div class="quiz-block">
  <p class="quiz-question">What is the key difference between a chatbot and an agent?</p>
  <ul class="quiz-options">
    <li data-correct="false">An agent uses a more powerful language model</li>
    <li data-correct="false">An agent can access the internet; a chatbot cannot</li>
    <li data-correct="true">An agent can take action on your real system — read, write, and execute — not just give advice</li>
    <li data-correct="false">An agent remembers previous conversations; a chatbot does not</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.14, confirm:

- [ ] I can state the one-line difference between a chatbot and an agent
- [ ] I can explain what read, write, and execute access means in practice
- [ ] I understand why Phases 2 and 3 were prerequisites for this module
- [ ] I can name all three parts of the engine-harness-operator model

---

## Module 0.14 — Why Version Control Exists

**BLUF.** When an agent can change your files, you want a logbook of every change — what changed, when, and why, with the ability to go back — and that logbook is version control.

### Why This Matters

The agent is about to start editing files. Without version control, one bad run can overwrite work with no way to recover it. This module plants the "why" before the commands, because the commands only make sense when the reason is already loaded.

### Concepts

Every time a file changes, version control records a snapshot: what changed, when, and a note about why. Stored locally on your machine. Every snapshot can be rewound.

Version control is the duty logbook. Every change recorded: what, when, why, who. The agent is about to start making entries in your files; the logbook is how you keep accountability over a teammate who works fast and never sleeps.

**Two layers:**

- **Local logbook.** Your machine keeps the record. You can always rewind to any previous snapshot without needing the internet.
- **Remote copy.** The same history synchronized to a cloud server. Backup — and the mechanism for teammates working on the same files.

No commands today. You are loading the reason. The commands come in the module that covers git.

!!! note "Why Software People Seem to Remember Everything"
    They do not. They have the log. "Who changed this and when?" is a two-second lookup. "What did this file look like last Tuesday?" is one command. The logbook is doing the remembering.

??? note "Instructor Note — Resist Teaching Git Commands Here"
    The concept is the prerequisite; the hands-on git module teaches the commands. Overloading now defeats the gentle ramp. If a student asks "how do I actually do this," tell them: "You will do it in the next session. Today you need to know why."

??? note "Instructor Note — Audience Framing"
    For a military audience, the duty logbook framing lands immediately. For a civilian audience, "undo button for your whole project" works better. Read the room.

### Hands-On

No commands today. Do this instead:

1. Think about a file you have edited multiple times over the past month.
2. Ask yourself: "If I needed to see what it looked like three weeks ago, could I?"
3. Ask yourself: "If something went wrong, what would I lose?"

That gap — between what you want to recover and what you can currently recover — is what version control fills.

!!! question "Before You Continue"
    An agent just ran a batch edit on 40 files. You look at one and it is not right. Without version control, what are your options? With version control, what changes?

<div class="quiz-block">
  <p class="quiz-question">Why does version control matter specifically once an agent can edit your files?</p>
  <ul class="quiz-options">
    <li data-correct="false">Agents edit files faster than humans, so you need a backup</li>
    <li data-correct="false">Version control prevents the agent from making mistakes</li>
    <li data-correct="true">The agent can make many changes quickly — version control gives you a complete record and the ability to rewind any of them</li>
    <li data-correct="false">Agents require version control to function</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.15, confirm:

- [ ] I can explain version control as a logbook of file changes I can rewind
- [ ] I understand why it matters once an agent has write access
- [ ] I can distinguish the local logbook from the remote copy
- [ ] I am not yet expected to know any git commands

---

## Module 0.15 — How AI Is Delivered and Paid For

**BLUF.** The same model reaches you through different doors — flat-rate app, pay-per-token API, or your organization's cloud account — and tokens cost money, so model choice and conversation length have a price.

### Why This Matters

Students will be selecting models and making decisions about how to use them. Understanding the cost and delivery model prevents both waste and surprise.

### Concepts

**Three ways AI is paid for:**

| Delivery model | What it means | Example |
|---|---|---|
| **Subscription app** | Flat monthly fee, model access included | ChatGPT Plus, Claude.ai Pro |
| **Pay-per-token API** | You pay per token sent and received | Anthropic API, OpenAI API |
| **Bring-your-own-key** | Your organization's API key foots the bill | Enterprise deployments, Claude Code |

**Cloud vs. local delivery.** Most models run in the cloud — your input goes to a remote server, the model runs there, the response comes back. Some smaller models can run entirely on your machine. Local delivery: no connectivity required, data stays on your machine. Trade-off: local models are smaller and less capable.

**The cost ladder.** Token cost scales with model size and reasoning effort. A small, fast model costs less per token than a large frontier model. "Always use the biggest model" is wrong — match the model to the job.

!!! tip "Match the Model to the Job"
    Drafting a quick message: small, fast model. Analyzing a complex document: larger model. Writing and running code in an agentic environment: frontier model with tool use. Using the biggest model for everything is like running a diesel generator to charge a phone.

!!! warning "Cost Is Real"
    On a pay-per-token plan, a long conversation with a large model costs more than a short one. Know your billing model before you start a long task.

??? note "Instructor Note — Skip the Pricing Tables"
    Specific token prices change frequently. Do not teach current prices — they will be wrong within a quarter. Teach the structure: tokens cost money, bigger models cost more, match the model to the job. The behavior is the deliverable.

### Hands-On

1. Open your chatbot's settings or account page. Find which model you are using.
2. If you have API access, open the pricing page. Read it for structure (input vs. output tokens, model tiers) — not memorization.
3. Identify which delivery model you are currently on.

!!! question "Before You Continue"
    You need to run an analysis task with a very long document and several back-and-forth exchanges. What factors determine the cost of that task, and how would you reduce it?

<div class="quiz-block">
  <p class="quiz-question">Why is "always use the most powerful model" not good advice?</p>
  <ul class="quiz-options">
    <li data-correct="false">Powerful models make more mistakes than smaller ones</li>
    <li data-correct="false">Powerful models are slower and less reliable</li>
    <li data-correct="true">Larger models cost more per token — for simple tasks, the cost is not justified by the capability difference</li>
    <li data-correct="false">You can only access the most powerful models through a paid subscription</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.16, confirm:

- [ ] I can name the three ways AI is paid for
- [ ] I understand that tokens cost money and model choice affects cost
- [ ] I know the difference between cloud and local delivery
- [ ] I can identify which delivery model I am currently using

---

## Module 0.16 — Data Handling: What Never to Paste

**BLUF.** Once you are pasting real work into a cloud-connected tool, what you paste matters — personal data, sensitive material, and anything above the system's authorization ceiling must never go in, and that rule does not expire.

### Why This Matters

Module 0.15 established that most AI delivery is cloud-based. This module establishes what that means for what you can send. The capability is real. The boundary is real. Both are true at the same time.

### Concepts

Authorization is a property of the system, not the impressiveness of the tool. A highly capable model running on an unauthorized system does not become authorized because it is impressive. The boundary is set by policy, not capability.

**What must never go into an unauthorized system:**

- Personally identifiable information (PII): names combined with identifiers, Social Security Numbers, DOBs, home addresses
- Sensitive, controlled, or classified material of any kind
- Anything above the system's authorization ceiling

**The default posture:** When in doubt, do not paste. Ask someone who can authorize it before you proceed.

**The classify-before-you-paste habit.** Before pasting anything into an AI tool, take two seconds: what is this, and is this system authorized for it? Build that pause until it is automatic.

!!! danger "This Bright Line Does Not Expire"
    It does not expire at the end of this course. It does not expire under time pressure. It does not move because the tool is impressive. One careless paste in an unauthorized system is the kind of mistake that has real and lasting consequences. Default to no until you hear yes from someone who can authorize it.

??? note "Instructor Note — Audience Calibration"
    For a military or intel audience, this is second nature but still worth stating explicitly — including the "paraphrase and summarize" loophole, which does not exist. For a civilian audience, use concrete examples from their domain: medical records, financial data, HR files, client information.

??? note "Instructor Note — Do Not Soften This Module"
    This is one of two modules where the tone is deliberately direct and does not retreat to nuance. Soften it and students hear "be careful sometimes." The message is: this is a hard rule.

### Hands-On

No prompting today. Do this instead:

1. Think about the last three things you pasted into an AI tool.
2. For each one: was the system authorized for that type of content?
3. Identify one category of content you work with regularly that you will never paste into an unauthorized tool.

Write that category down. It is your personal bright line.

!!! question "Before You Continue"
    You are under a deadline and want to paste a document into your AI tool to summarize it quickly. You are not sure whether the system is authorized for that content. What do you do?

<div class="quiz-block">
  <p class="quiz-question">You have a borderline-sensitive document and an unauthorized but highly capable AI tool that would save hours of work. What is the correct call?</p>
  <ul class="quiz-options">
    <li data-correct="false">Paste it — the efficiency gain justifies a judgment call</li>
    <li data-correct="false">Summarize the key points in your head first, then paste the summary</li>
    <li data-correct="true">Do not paste. The authorization status of the system does not change based on capability or time pressure. Ask before proceeding.</li>
    <li data-correct="false">Paste it, but delete the conversation immediately after</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before moving to Module 0.17, confirm:

- [ ] I can identify the categories that must never go into an unauthorized system
- [ ] I know the default posture: when in doubt, do not paste
- [ ] I understand that authorization is a property of the system, not the tool's capability
- [ ] I have identified my personal bright line for content I handle regularly

---

## Module 0.17 — The Supervisor Mindset

**BLUF.** You delegate to the agent, verify its work, and own the outcome — the agent is a capable, fast, assumption-prone junior who will confidently fill gaps you did not address, and your job is to command well and check, not to type more.

### Why This Matters

Every failure mode from Module 0.3 — hallucination, confident-wrong, nondeterminism — applies to agent actions, not just text output. The difference is that agent actions touch real files and real systems. The supervisor mindset is what keeps that from becoming a problem.

### Concepts

**The motivated-junior model.** The agent is a junior teammate with file-system access. Capable. Fast. Willing to fill ambiguity with plausible-sounding assumptions. It will never push back or say "I'm not sure" unless you build that into the prompt. It executes your intent — including the parts you left implicit.

**Three duties of the supervisor:**

1. **Delegate clearly.** Vague intent produces confident but wrong execution. Say what you need, what good looks like, and what is off-limits.
2. **Verify the work.** Check what the agent actually did, not just what it said it did. These are not the same.
3. **Own the outcome.** The capability does not transfer the accountability. You are still the one who signs for the result.

!!! warning "Two Failure Modes to Name and Counter"
    **Blind trust:** "It sounds right." Confident output from an agent is not verified output. Check the work before you act on it.

    **Learned helplessness:** "I can't check this, it's too technical." You do not need to replicate the agent's work. You need to check whether the output makes sense, whether constraints were honored, whether anything looks wrong. That is a human judgment call, not a technical skill.

!!! example "The Delegate-Verify-Own Loop in Practice"
    You ask the agent to reorganize a folder of files by date.

    - **Delegate:** "Move all files with a date in the filename into subfolders organized by year. Do not delete anything. Show me what you plan to do before you do it."
    - **Verify:** Check that files landed where they should. Spot-check three of them. Confirm nothing was deleted.
    - **Own:** If one file landed in the wrong folder, you catch it, fix it, and note what to specify more precisely next time.

??? note "Instructor Note — Reinforce Throughout, Not Just at the End"
    This is the through-line of the entire course, not a capstone topic. Every agentic action in later modules should be framed with the supervisor loop. Students who only hear it once at the end will not carry it forward.

??? note "Instructor Note — Capstone Exercise"
    Optimize the capstone for the loop, not the polish. A finished artifact with no verification is a worse outcome than a rough artifact that was checked. The win is the mindset: delegate, verify, own. If the agent makes a mistake and the student catches it and corrects it — that is success.

### Hands-On

Give the agent (or chatbot, depending on available tooling) a small real task:

1. Write a clear brief: who you are, what you need, what good output looks like, and what is off-limits.
2. Submit it. Read the output.
3. Verify: does it do what you asked? Did it make any assumptions you did not authorize? Is anything wrong?
4. If something is off, correct it. Identify what you should have specified more precisely.

That loop — delegate, verify, correct — is the whole skill.

!!! question "Before You Continue"
    The agent completed a task and the output looks correct at first glance. What would you check to actually verify it, and how would you know if an unauthorized assumption had been made?

<div class="quiz-block">
  <p class="quiz-question">An agent completes a task and narrates what it did in clear, confident language. What do you do next?</p>
  <ul class="quiz-options">
    <li data-correct="false">Accept the output — confident narration is a reliable signal of correct execution</li>
    <li data-correct="false">Run the task again to confirm consistency</li>
    <li data-correct="true">Verify the actual output against what you asked for — the narration describes intent, not necessarily what happened</li>
    <li data-correct="false">Ask the agent to verify its own work</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

Before beginning Day 1, confirm:

- [ ] I can state the three duties of the supervisor: delegate, verify, own
- [ ] I know the difference between a capable junior and a trustworthy one
- [ ] I have completed at least one delegate-verify-correct loop with a real task
- [ ] I am the commander, not the typist

---

## Day 0 Close

A student who completes this block has the four essential foundations: a working mental model of the engine, deliberate prompting, comfort moving around a real machine from the command line, and the supervisor mindset. They are ready to load an engine into a harness without freezing at the first command prompt.

The terminal was the spine on purpose. It is also a filter: some casual users will not finish Phase 3, and that is the course doing its job, not failing. The ones who do finish are ready for advanced agentic work.

---

*Outline template, unbranded. Drop your own program header, classification marking, and footer before distribution.*
