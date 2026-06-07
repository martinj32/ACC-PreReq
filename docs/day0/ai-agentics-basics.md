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

**TLDR/BLUF.** An LLM predicts the next chunk of text, one piece at a time, based on patterns it learned from a huge pile of text. It was trained, not programmed. It is a brain in a jar: it reads text and writes text, and it does nothing else on its own. No transformer math today; the goal is a mental model that survives contact with a real tool.

### Learning Objectives
- State in one sentence what an LLM does: predicts text from learned patterns.
- Explain the difference between *trained* (learned from examples) and *programmed* (told exact rules).
- Internalize that the model has no body, no memory between chats, and no live connection to the world unless something gives it one.
- Recognize that fluent, confident output is not the same as correct output.

### What this module covers
- Live demo first: ask the model something, then ask it to keep going, and watch it predict its way forward.
- The "brain in a jar" image: capable of reasoning in text, incapable of acting alone.
- Why "trained not programmed" explains both its flexibility and its unreliability.

### Military Doctrinal Framing
The LLM is the engine. By itself it is a brain in a jar — it can describe the doctrine, but it cannot execute it. Everything you bolt on later (a harness, tools, your judgment) exists to give that brain a body. Get the engine straight first, because confusing the engine with everything around it is the most common beginner mental-model break.

### Watch-Outs
- Do not open with architecture. A casual user does not need attention heads; they need to stop thinking the model is a search engine or a person.
- Do not let "it predicts text" curdle into "so it is dumb." It is extraordinarily capable *and* it is predicting. Both are true.
- Kill the anthropomorphism explicitly. The model does not "know," "want," or "lie." Those words will mislead students at every later step. It predicts. That is the only accurate verb.
- Why hallucination happens -- the mechanism: the model has no truth-checking step. It generates tokens that are statistically likely to follow prior context. It cannot distinguish "information I was trained on accurately" from "information I am completing plausibly." Confident output and correct output are entirely unrelated. This is expected behavior of the system, not a rare bug.
- "Trained not programmed" -- worked explanation: A program follows rules its author wrote. A trained model learned patterns from billions of examples. It was never given a rule that says "X is true" -- it was trained on enough text containing that fact that its weights now make it the likely completion. The capability: it generalizes. The failure mode: if training data was wrong, biased, or sparse in some domain, the model learned those patterns too. There is no rulebook to audit.

### References
- Have them use the chatbot they already have open. That is the lab.

---

## Module 0.2 — Tokens and Context

**TLDR/BLUF.** The model reads and writes in tokens, which are chunks of text roughly three-quarters of a word each. It can only hold so many at once — that is the context window, and it has a hard limit. Fill it, and the model loses track of what was said earlier. This is why long, sprawling chats get worse, not better.

### Learning Objectives
- Define a token in plain terms: approximately 0.75 English words, or about 3-4 characters in English prose. Code and non-English text tokenize less efficiently.
- Explain that the context window is the model's short-term memory for one conversation, with a hard ceiling.
- Predict the symptom of a full window: the model forgets earlier instructions and drifts.
- Connect this to a habit: start a fresh chat for a new topic instead of running one endless thread.

### What this module covers
- Demo: paste a long document, then ask about something from the very top, and watch recall degrade.
- The window as a whiteboard with finite space — new writing crowds out old.
- This concept is exactly why tools like `/clear` and `/context` exist in agentic environments.

### Military Doctrinal Framing
The context window is the radio net. Every voice on the net makes it harder to hear the one you need. A clean, focused net carries signal; a net jammed with three side conversations carries noise. Keeping the conversation tight is keeping the net clean.

### Watch-Outs
- Do not drown them in token math. The instinct "shorter and focused beats long and sprawling" is the deliverable, not the arithmetic.
- They will assume bigger context is always better. Name the trap now: a full window degrades quality.
- Context window comparative sizes (verify before teaching -- these change with releases): Claude models: 200,000 tokens. GPT-4o: 128,000 tokens. Gemini 1.5 Pro / 2.0: 1,000,000+ tokens.
- "Lost in the middle" mechanism: models attend well to context window beginning and end, and comparatively poorly to the middle. Critical instructions buried mid-conversation may be partially ignored. Keep critical constraints at the session start or in the system prompt.
- Practical decision rule: start a fresh chat when (1) the task has changed direction and earlier turns are dead weight, or (2) the model is drifting -- hedging on things it stated confidently earlier.

### References
- Anthropic and OpenAI tokenizer demos, if you want a visual of text breaking into tokens.

---

## Module 0.3 — How LLMs Fail

**TLDR/BLUF.** The model will sometimes state false things with total confidence. It can give different answers to the same question. It does not know about events after its training cutoff. None of this means it is broken — it means you must verify, not trust. Seeing it fail on purpose, early, is the most important inoculation in this course.

### Learning Objectives
- Name the four core failure modes: hallucination, confident-wrong, nondeterminism, knowledge cutoff.
- Demonstrate that "confident" and "correct" are unrelated in model output.
- Build the verification reflex: check anything that matters before acting on it.
- Understand why this is the entire reason a human stays in the loop.

### What this module covers
- Guided demo: get the model to confidently invent a fake citation, a fake quote, or a fake fact.
- Ask the same question twice in fresh chats; compare the differing answers.
- Ask about a very recent event; watch it either refuse or guess.

### Military Doctrinal Framing
Auto-pilot does not work. The operator who treats the model as a magic box gets burned; the operator who learns where it fails compounds. You do not hand a junior the whole operation unsupervised on day one — you check the work. Same here. The model is a motivated junior who will state a guess as fact if you let it.

### Watch-Outs
- Make them *produce* a hallucination with their own hands. Telling them it happens does not land; watching it happen does.
- Do not let this tip into cynicism. The point is calibrated trust, not distrust.
- This module is load-bearing. If it does not land, the rest of the course is built on sand.
- Nondeterminism: the model uses a temperature parameter that introduces variation. Same prompt, different runs, different results -- by design. Do not treat one output as "the answer" for high-stakes work. Run important prompts multiple times and compare for consistency.

### Instructor Note: Reliably Eliciting Hallucinations on Demand
Use these to produce hallucinations in front of the class so students see failure with their own eyes. Pick a topic where you know the correct answer so you can immediately show the error. Never demo on live operational content.
- Invented citations: ask for 5 peer-reviewed academic papers on a narrow topic with authors and publication years. The model will produce plausible-sounding but fabricated citations. Ask for a DOI -- it will be invented.
- Biographical detail: ask for detailed career history of a real but not-famous person (a regional official, a mid-level academic). The model fills gaps with plausible detail.
- Recent events past cutoff: ask about an event you know happened after the training cutoff. The model may confidently describe what did not happen.

### References
- None needed. The student's own failed prompts are the material.

---

## Module 0.4 — Deliberate Prompting

**TLDR/BLUF.** They already prompt by feel. This converts that into method: tell the model who to be, give it the context it needs, show it an example, and say what good output looks like. Treat it like briefing a person, not typing into a search box. This is the seed of the deliberate prompting framework developed throughout this course.

### Learning Objectives
- Improve a weak prompt by adding role, context, an example, and an output spec.
- Explain why a model with no context must guess, and why guessing produces generic output.
- Practice having a conversation with the model: rough ask, read, tighten, repeat.
- Recognize that they do not need a perfect prompt — an attempt the model can build on beats silence.

### What this module covers
- Before/after: run a one-line prompt, then run the same ask with role + context + example + format, and compare.
- The "brief a person" reframe, with a worked example from their own work.
- Asking the model to interview you, or to repeat your request back, to catch a misread early.

### Military Doctrinal Framing
A vague prompt is a vague order, and a vague order gets a vague result from a junior who fills the gaps with assumptions. A good prompt is a clear brief: who you are, what I need, what right looks like. The model meets you halfway the moment you give it a structure to work from.

### Watch-Outs
- Do not teach a rigid template they recite. The structure is the lesson, not the acronym.
- Resist turning this into a "prompt engineering tricks" hour. The durable skill is clarity, not magic phrases.
- Casual users over-trust one-shot prompts. Push the iterative, conversational habit hard.


---

# PHASE 2 — The Computer Underneath

*Genuinely new material for this audience. No AI here. Plain computer literacy. Keep threading short terminal previews in so Phase 3 is not a cliff.*

## Module 0.5 — Files, Folders, and the Tree

**TLDR/BLUF.** Everything on a computer lives in a file, and files live in folders, and folders nest inside other folders to form a tree. The "address" of a file is the path of folders you walk to reach it. This is invisible to most app users, and it is the ground everything else stands on.

### Learning Objectives
- Describe a file, a folder, and how folders nest into a tree.
- Read a path as a route through that tree.
- Find where their downloads, documents, and desktop actually live.
- Recognize that the apps they use have been hiding this structure from them.

### What this module covers
- Open the graphical file browser (Finder or File Explorer) and walk the tree by clicking.
- Show the same location written as a path.
- Create, rename, and move a folder by clicking — the moves they will soon repeat by typing.

### Military Doctrinal Framing
The filesystem is the terrain. Before you can maneuver, you have to read the map: where things are, how they connect, how to name a location precisely. Every command you learn next is movement across this terrain.

### Watch-Outs
- Many casual users have genuinely never seen the folder tree. Do not assume; verify by having them find a file they saved last week.
- Hidden files and extensions are off by default on most machines. Turn extension visibility on now; it prevents confusion in 0.6.

### References
- The student's own machine. No external material.

---

## Module 0.6 — Plaintext vs Rich Text

**TLDR/BLUF.** A plaintext file is just characters — nothing hidden. A rich-text file (like a Word document) hides formatting and metadata you cannot see. Models and tools want plaintext, because what you see is exactly what the machine reads. This is the foundation for understanding Markdown and structured data.

### Learning Objectives
- Distinguish plaintext from rich text and give an example of each.
- Explain why "what you see is what the machine reads" matters for AI tools.
- Identify common plaintext extensions (`.txt`, `.md`, `.csv`, `.json`) versus rich formats (`.docx`).
- Understand why pasting from Word can silently break things (smart quotes, hidden characters).

### What this module covers
- Open a `.txt` and a `.docx` and show what each actually contains underneath.
- Demonstrate Word turning a straight hyphen into an em dash, and why that breaks a Markdown bullet.
- Preview Markdown as "plaintext with light structure" — the full lesson comes in the Markdown module.

### Military Doctrinal Framing
Plaintext is a message in the clear: no hidden traffic, no surprises, readable by anyone and anything on the net. Rich text is a message with attachments you cannot see. When you hand a file to a machine, you want it in the clear.

### Watch-Outs
- The smart-quote and em-dash trap is real and will bite them in later work. Show it now so it is muscle memory, not a mystery later.
- Do not go deep on encodings. "Plaintext is honest, rich text hides things" is enough at this level.


---

## Module 0.7 — Looking at Files in a Real Editor

**TLDR/BLUF.** A code editor is just a better text viewer. Installing one and learning to open a folder and read a file is a small, low-stakes win that makes the rest of the course concrete. A gentle VS Code intro: open, view, close. Nothing more today.

### Learning Objectives
- Install a code editor and open a folder in it.
- Open a plaintext file, read it, and close it without fear.
- Locate the file tree panel and the editor panel.
- Render a Markdown file to preview, connecting back to 0.6.

### What this module covers
- Install VS Code (or the editor your program standardizes on).
- Open the folder from 0.5; browse its tree in the editor.
- Open a `.md` file and toggle the rendered preview.

### Military Doctrinal Framing
The editor is your optic. You could squint at the terrain with the naked eye, but the optic shows you the file clearly, with the structure visible. Same terrain, better look. Learn to raise it before you need it.

### Watch-Outs
- Editors are intimidating by appearance. Constrain today's scope to open and view. No editing, no extensions, no settings.
- Do not let an install problem on one machine stall the room. Have a backup viewer and move on; perfection is not the goal here.

### References
- Editor's own getting-started page.

---

# PHASE 3 — The Terminal

*The spine of the course. Maximum scaffolding, maximum reps, spread across the most calendar time. Every single rep is framed as "this is how the agent will move around your computer for you." Ten minutes a day for two weeks beats one long block.*

## Module 0.8 — What the Terminal Is (and Why It Is Safe)

**TLDR/BLUF.** The terminal is a typed way to give the computer the same instructions you used to give by clicking. It is not hacking, it is not dangerous by default, and it is not just for programmers. It feels alien for about an hour, then it feels normal. Demystifying it is the whole job of this module.

### Learning Objectives
- Open the terminal on their machine.
- State that a command is a typed instruction, equivalent to a click they already know.
- Read the prompt line and identify where their typing goes.
- Lose the fear: nothing they type today can hurt the machine.

### What this module covers
- Open the terminal. Sit with the blinking cursor. Name the anxiety, then defuse it.
- Type one harmless command (print the current date) and watch it respond.
- Map "click an icon" to "type a command" so it feels like a translation, not a new world.

### Military Doctrinal Framing
The terminal is direct comms with the machine. Clicking is talking through an interpreter; the command line is speaking the language yourself. It feels uncomfortable until it doesn't, the same as any new comms procedure. You drill it until it is second nature.

### Watch-Outs
- This is the emotional washout point. Some casual users feel a bait-and-switch here: "I signed up to use AI, why am I typing Unix." Address it out loud and tie every rep to the agent payoff.
- Do not show off. A wall of commands in the first session loses the room. One command, fully understood, beats ten demoed.
- Reassure honestly: today's commands are read-only and harmless. Save anything destructive for much later, behind heavy framing.

### References
- None. The terminal is the lab.

---

## Module 0.9 — Navigating: Where Am I, What Is Here

**TLDR/BLUF.** Three commands cover most of navigation: one to ask where you are, one to list what is here, one to move. That is it. Master moving around the tree from 0.5 by typing instead of clicking, and the terminal stops being scary.

### Learning Objectives
- Use the "where am I" command to print the current location.
- Use the "list" command to see what is in the current folder.
- Use the "change directory" command to move into and back out of folders.
- Mentally connect each command to the click it replaces.

### What this module covers
- `pwd` (where am I), `ls` (what is here), `cd` (move) — taught as the navigation trio.
- Walk the exact same tree they clicked through in 0.5, now by typing.
- Moving up a level versus down into a folder.

### Military Doctrinal Framing
This is land navigation. Where am I, what is around me, how do I move to the next position. You learned to read the map in Phase 2; now you move across it on foot. Everything else in the terminal is built on being able to navigate without getting lost.

### Watch-Outs
- Getting "lost" in the tree is the number-one beginner panic. Teach "where am I" as the reset button they can always hit.
- Keep it navigation-only this module. Do not introduce file creation yet; one capability at a time.
- Reps over coverage. Same three commands, many short repetitions across several days.

### References
- None.

---

## Module 0.10 — Acting: Make, Move, Copy

**TLDR/BLUF.** Beyond looking around, four moves cover most day-to-day file work: make a folder, make a file, copy, move. These are the same actions they did by clicking in 0.5, now typed. This is where the terminal goes from "I can look" to "I can do."

### Learning Objectives
- Create a folder and a file from the command line.
- Copy a file to a new location.
- Move or rename a file.
- Verify each action by listing the folder afterward.

### What this module covers
- `mkdir`, `touch`, `cp`, `mv` — taught as the action set.
- The verify-after-acting habit: list the folder to confirm the change happened.
- Building a small folder structure entirely by typing.

### Military Doctrinal Framing
Navigation got you to the position; now you act on it. Every action you take, you confirm — you do not assume the round landed, you check the target. Listing the folder after each command is your battle-damage assessment.

### Watch-Outs
- Introduce the verify habit now, hard. "Trust the tool call, not the narration" is the principle -- build it here.
- Hold off on deletion. When you eventually teach it, frame it heavily; deletion is irreversible at the command line and there is no recycle bin.
- Watch for typos in filenames. A mistyped name creates a second file rather than erroring; teach them to list and notice.


---

## Module 0.11 — Paths, Tab-Completion, and the Up-Arrow

**TLDR/BLUF.** A path is the full address of a file. Tab-completion finishes names for you so you stop fat-fingering them. The up-arrow recalls your last command. These three quality-of-life tools are the difference between fighting the terminal and flowing in it.

### Learning Objectives
- Write an absolute path and a relative path to the same file.
- Use tab-completion to finish folder and file names.
- Use the up-arrow to recall and edit previous commands.
- Explain why exact spelling and spacing in a path matters.

### What this module covers
- Absolute versus relative paths, walked on their own tree.
- Tab-completion as the antidote to typos and the reason names exist.
- Command history with the up-arrow; editing a recalled command instead of retyping.

### Military Doctrinal Framing
A path is a grid coordinate: precise, unambiguous, and unforgiving of a wrong digit. Tab-completion is your forward observer calling the coordinate so you do not transpose it. Sloppy coordinates put rounds in the wrong place; sloppy paths put files in the wrong folder.

### Watch-Outs
- Exactness is the lesson and the frustration. A space or a capital letter in the wrong place fails silently or hits the wrong target. The principle: "the space is load-bearing."
- Tab-completion is the single biggest morale and accuracy win in the terminal. Teach it early and insist on it.


---

## Module 0.12 — Commands, Flags, and Knowing When to Stop

**TLDR/BLUF.** Most commands take options, called flags, that change what they do. You also need to know how to tell whether something is still running and how to stop it. This rounds out terminal literacy and prepares students for CLI flags and context recovery techniques.

### Learning Objectives
- Add a simple flag to a command and observe the changed behavior.
- Read a command's built-in help to discover its flags.
- Tell whether a command has finished or is still running.
- Stop a running command safely and return to the prompt.

### What this module covers
- A command with and without a flag, side by side (for example, listing with and without the "show details" flag).
- Finding help: `--help` and how to read it without panic.
- The prompt returning as the signal a command finished; how to interrupt one that hasn't.

### Military Doctrinal Framing
Flags are the settings you dial in before you give the order — same command, different mission profile. Knowing how to stop a running command is knowing how to call a check-fire. You never want to be the operator who cannot halt their own element.

### Watch-Outs
- This prepares students for CLI flags and the Escape key as pause, not abort. Name those forward links so students know where they are headed.
- Do not catalog flags. Teach the *concept* of a flag and how to look the rest up. Memorization is the wrong target.
- "How do I get out of this?" is a real beginner fear. Make stopping and exiting a deliberate, practiced, calm move.


---

# PHASE 4 — From Chatbot to Agent

*The bridge that makes Phases 2 and 3 pay off. This is the "oh, that is why I learned all that" moment. Tie everything back to the agent touching the student's real machine.*

## Module 0.13 — Chatbot vs Agent

**TLDR/BLUF.** A chatbot gives advice. An agent takes action. The difference is read, write, and execute access to your real files and terminal — the exact terrain and movement you just learned. Ask a chatbot to rename a folder and it tells you the command; ask an agent and it renames the folder.

### Learning Objectives
- State the one-line difference: chatbot advises, agent acts.
- Explain that the agent acts through the filesystem and terminal from Phases 2 and 3.
- Recognize read, write, and execute as three distinct levels of access.
- Articulate why this capability is both powerful and a lot of trust to extend.

### What this module covers
- Side by side: chatbot returns instructions; agent performs the task on disk.
- The agent as engine plus harness plus operator — name all three.
- Why everything in Phases 2 and 3 was the prerequisite for understanding this.

### Military Doctrinal Framing
The LLM can tell you what is in the doctrine. A harness with tools can execute it. This is the human-machine team: the engine reasons, the harness gives it hands, and you are the operator who points it at the right problem and pulls the plug when it heads somewhere wrong. Engine plus harness plus operator. Everything in advanced agentic work stacks on this primitive.

### Watch-Outs
- This is the payoff module. If Phases 2 and 3 felt like a detour, this is where you prove they weren't. Make the connection explicit.
- Read, write, execute is a lot of trust. Set up the bright line that Module 0.16 enforces; do not let them get comfortable handing over access without it.


---

## Module 0.14 — Why Version Control Exists

**TLDR/BLUF.** When an agent can change your files, you want a logbook of every change: what changed, when, and why, with the ability to go back. That logbook is version control. No commands today — just the concept and the reason it matters before you ever hand an agent write access.

### Learning Objectives
- Explain version control as a logbook of file changes you can rewind.
- State why this matters specifically once an agent can edit files.
- Distinguish the local logbook from the shared cloud copy at a concept level.
- Hold the "why" without yet learning any commands.

### What this module covers
- The logbook concept: every change tracked and reversible.
- Why "software people seem to remember everything" — they have the log.
- A glance at the shared cloud copy (the teammate and backup angle), concept only.

### Military Doctrinal Framing
Version control is the duty logbook. Every change recorded: what, when, why, who. The agent is about to start making entries in your files; the logbook is how you keep accountability over a teammate who works fast and never sleeps.

### Watch-Outs
- Resist teaching git commands here. The concept is the prerequisite; the hands-on git module later teaches the commands. Overloading now defeats the gentle ramp.
- For a military audience, lean on the logbook framing; it is already intuitive. For a civilian audience, the "undo button for your whole project" framing lands better.


---

## Module 0.15 — How AI Is Delivered and Paid For

**TLDR/BLUF.** The same model reaches you through different doors: a flat-rate app, a pay-per-use API, or your own cloud account footing the bill. It can run in the cloud or, sometimes, locally. And it costs money per token, which is why model choice and conversation length have a price. This demystifies the plumbing behind cost and model selection decisions.

### Learning Objectives
- Name the three ways AI is paid for: prepaid plan, pay-per-token API, bring-your-own-cloud.
- Distinguish cloud delivery from local delivery at a high level.
- Explain that tokens cost money, so bigger models and longer thinking cost more.
- Connect this to a practical instinct: match the model to the job, not always the biggest one.

### What this module covers
- App versus API versus bring-your-own-key, in plain terms.
- Cloud versus local: connectivity and control trade-offs.
- The cost ladder concept (small/cheap to large/expensive) developed further in this course.

### Military Doctrinal Framing
Cost is your fuel budget for the mission. Different models burn at different rates, and how hard you make the model think is throttle position. "The biggest model is always best" is wrong; the right call depends on whether your limit is time, money, or speed.

### Watch-Outs
- Do not drown them in pricing tables. The instinct "match model to job, mind the meter" is the deliverable.
- Tie this to a behavior, not trivia. Otherwise it is forgettable. The behavior is deliberate model choice.


---

## Module 0.16 — Data Handling: What Never to Paste

**TLDR/BLUF.** Once you are pasting real work into a tool that may send it to a cloud, what you paste matters. Some information must never go into an unauthorized system: personal data, sensitive material, anything you are not cleared to share. The rule is simple and it does not expire: when in doubt, do not paste, and ask.

### Learning Objectives
- Identify categories that must not go into an unauthorized tool: personal identifiable information, sensitive or controlled material, anything above the system's authorization.
- State the default posture: when in doubt, do not paste; ask first.
- Explain why the cloud delivery from 0.15 makes this matter.
- Carry the rule past the classroom — it applies to their real work, always.

### What this module covers
- The bright line, with concrete examples drawn from the student's actual domain.
- Why authorization is a property of the system, not the impressiveness of the tool.
- The habit: classify before you paste.

### Military Doctrinal Framing
This is your bright line and it does not expire at 1700. The tool not being authorized for sensitive data is not a suggestion; it is the boundary. An impressive capability does not move the boundary. Default to no until you hear yes from someone who can authorize it.

### Watch-Outs
- For a military or intel audience, this is second nature but still worth stating; for a civilian audience, it is genuinely new and needs concrete examples (medical, financial, others' personal data).
- Do not soften this module. A single careless paste is the kind of mistake that has real consequences.


---

## Module 0.17 — The Supervisor Mindset

**TLDR/BLUF.** You delegate to the agent, you verify its work, and you remain accountable for the result. The model is a motivated junior teammate who works fast, never sleeps, and will confidently assume things you did not say. Your job is not to type more; it is to command well and check the work. This is the mindset all responsible agentic work depends on.

### Learning Objectives
- State the three duties of the supervisor: delegate, verify, own the outcome.
- Explain why a capable but assumption-prone teammate must be checked, not trusted blind.
- Connect verification to the failure modes from Module 0.3.
- Adopt the posture that they are the commander, not the typist.

### What this module covers
- The motivated-junior model: capable, fast, and willing to fill gaps with guesses.
- Delegate-verify-own as a loop, not a one-time act.
- A capstone exercise: give the agent (or chatbot, depending on tooling) a small real task, then verify and correct it as the supervisor.

### Military Doctrinal Framing
The agent is a junior teammate with file-system access who takes your intent and executes. You give clear intent, you check the work, and you carry the accountability up the chain — the same as commanding any junior. The capability does not transfer the responsibility. You are still the one who signs for the result.

### Watch-Outs
- This is the through-line of the entire course. Reinforce it, do not just state it once at the end.
- Casual users drift toward two failure modes: blind trust ("it sounds right") and learned helplessness ("I can't check this"). Name both and counter both.
- The win is the mindset, not a finished artifact. Optimize the capstone for the loop, not the polish.


---

## Day 0 Close

A student who completes this block has the four essential foundations: a working mental model of the engine, deliberate prompting, comfort moving around a real machine from the command line, and the supervisor mindset. They are ready to load an engine into a harness without freezing at the first command prompt.

The terminal was the spine on purpose. It is also a filter: some casual users will not finish Phase 3, and that is the course doing its job, not failing. The ones who do finish are ready for advanced agentic work.

---

*Outline template, unbranded. Drop your own program header, classification marking, and footer before distribution. Module content is scaffolded for a builder, not written out as full teaching text — expand each "What this module covers" section into the live lesson during development.*
