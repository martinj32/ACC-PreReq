# Day 0 — Boot Camp: Before You Touch the Weapon

**Theme:** Foundations. Turn a casual chatbot user into someone ready to unpack the weapon.

**Outcome:** You walk into ACC Day 1 already knowing what an LLM, a prompt, and a system prompt are; comfortable enough in a terminal, files, and Markdown that the environment does not scare you; with a working mental model of git as a safety net; and with the single most important shift in place — understanding that an agentic tool *acts*, and must be briefed like a motivated PFC, not trusted like a search box.

> This course is the on-ramp. It exists to deliver you to the exact line ACC assumes on arrival and no further. ACC re-teaches git and the terminal as it goes; it does **not** re-teach how a model thinks or why an agent is different from a chatbot. Spend your effort accordingly.

---

## Phase 0 — How the Machine Actually Thinks

### Module 0.1 — What an LLM Really Is

**Objective.** Replace the "it just knows things" reflex with an accurate mental model: a large language model is a prediction engine that generates the next likely piece of text, not a database it looks facts up in and not a person who understands you.

**Why it matters.** Every downstream habit — verifying output, writing good prompts, not pasting secrets — rests on understanding that the model is *generating*, not *retrieving*. A student who thinks the model "knows" will trust it exactly when they should not.

**Hands-on.** Ask a chatbot a question about a niche or recent topic and watch it produce a confident, wrong answer. Then ask it to cite sources and watch it invent them. Seeing the failure once is worth more than being told about it ten times.

**Doctrinal framing.** A model is the new guy who is great at sounding right in the briefing room. Confident, fluent, and occasionally making it up entirely. You do not act on his word without checking; you check *because* he is convincing, not despite it.

**Watch-outs.**
- Do not over-explain the math. The student needs the *behavior* (it predicts, it can be wrong, it does not retrieve), not the architecture.
- "It hallucinates" is a term, not an excuse. Frame it as the expected behavior of a prediction engine, so the student plans around it instead of being surprised by it.
- Resist the urge to make the model sound smarter than it is to impress the room. The whole point of the module is calibration.

**The mechanism behind hallucination.** The model has no truth-checking step. It generates tokens that are statistically likely to follow prior context. It cannot distinguish "information I was trained on accurately" from "information I am completing plausibly." The output looks confident regardless of accuracy. This is why "it hallucinates" is a description of behavior, not an explanation of a bug.

**Knowledge cutoff -- three behaviors, not one binary.**
1. The model flags the gap and says so. This is the honest behavior.
2. The model answers confidently using stale training data with no indication it may be wrong. This is the dangerous behavior.
3. The model has a retrieval or search tool and fetches current information.

All three look like confident answers from the outside. Verify time-sensitive content regardless of which behavior you think you are seeing.

**"Trained, not programmed" -- what that actually means.** A program follows rules its author wrote. A trained model learned patterns from billions of examples and built weights that encode those patterns. It was never given a rule that says "the capital of France is Paris" -- it was trained on enough text containing that fact that its weights now make "Paris" the likely completion. The capability: it generalizes across domains without needing a rule for every case. The failure mode: if training data was sparse, biased, or wrong in some domain, the model learned those patterns too. There is no rulebook to audit.

### Module 0.2 — The Context Window

**Objective.** Internalize that the model has a finite working memory — the context window — and that everything in the conversation competes for that space. Understand that the model has no memory between conversations unless something carries it over.

**Why it matters.** This is the single most load-bearing concept in the entire ACC course. Multiple later modules — sub-agents, the session-bookend ceremonies, cost management — exist *only because context is finite*. If this does not land here, none of it lands later.

**Hands-on.** Run one long conversation. Feed it a fact early, pile on unrelated turns, then ask it to recall the early fact and watch it slip. Start a brand-new chat and ask it about the previous one; watch it have no idea. The two demos together make "finite memory" and "no memory between sessions" concrete.

**Doctrinal framing.** The context window is what the element can carry on its back. Load it with the wrong gear and there is no room for what the mission actually needs. Every pound counts, and at the end of the patrol the ruck is empty again — nothing carries to the next one unless you wrote it down.

**Watch-outs.**
- Students conflate "it forgot" with "it is broken." It is neither; it ran out of room or started fresh. Name the cause every time.
- Do not introduce token math yet. "Finite space that fills up" is the concept; counting comes later if at all. A token is approximately 0.75 English words, or about 3-4 characters in English prose. Code and non-English text tokenize less efficiently -- more tokens per apparent word.
- The "no memory between sessions" point surprises people who have used consumer chatbots with memory features. Be explicit that you are teaching the default.

**The "lost in the middle" mechanism.** Models attend well to the beginning and end of a context window, and comparatively poorly to material in the middle. A critical instruction given early in a long conversation may be partially ignored once many turns accumulate on top of it. Keep critical constraints at the session start or in the system prompt -- not buried mid-conversation.

**Practical decision rule: when to start fresh.**
1. Has the task changed direction? Earlier turns are dead weight if the task shifted.
2. Is the model drifting or hedging on things it stated confidently earlier? That is the symptom of a filling context.

Start fresh with a clean brief when either condition applies.

### Module 0.3 — System vs User Prompts

**Objective.** Understand that there are two layers of instruction: the standing orders the tool already carries (the system prompt) and the specific thing you type right now (the user prompt). Your input lands *on top of* instructions you did not write and often cannot see.

**Why it matters.** ACC's prompting framework and its entire personalization layer assume the student already grasps that they are writing the *change order*, not the whole order. Without this, the Day 2 customization modules read as arbitrary.

**Doctrinal framing.** The system prompt is the OPORD already in effect. Your prompt is the FRAGO — today's specific change, layered on standing orders that are already loaded. You are never writing the whole order from scratch.

**Concrete example.** An Army unit deploying an AI assistant for staff work might have a system prompt that says: "You assist U.S. Army staff officers. Do not provide legal advice. Answer in concise, direct language. Respond in under 200 words unless the task requires more." A soldier types: "Draft a paragraph summarizing the logistics situation for the evening SITREP." That soldier wrote the FRAGO. The OPORD -- who the model is, what it will not do, how it should respond -- was already loaded before the conversation began.

**The hidden layer.** Most consumer AI apps have a system prompt set by the platform that the user cannot see. It exists and shapes every response. In Claude Code, the CLAUDE.md file functions as an additional layer of system instructions written by the operator -- that is the layer students write in ACC.

**Watch-outs.**
- Keep it conceptual. The student does not write a system prompt here; they just need to know the layer exists.
- Avoid implying the system prompt is sinister or hidden-with-intent. It is just the layer underneath. Mystery breeds bad assumptions.

### Module 0.4 — Data Hygiene and OPSEC

**Objective.** Build the reflex of scrubbing before sending. Know categorically what never goes into an AI tool: classified material, CUI, PII, operational detail, credentials. When in doubt, leave it out.

**Why it matters.** This is a deliberate front-loaded addition. ACC operates under FOUO handling and assumes this discipline already exists. The habit must form *before* a student touches a real tool, not after they have already pasted something they should not have. For an intelligence audience this is not optional polish; it is the floor.

**Categories that never go into an AI tool.**
- Classified material
- CUI (Controlled Unclassified Information)
- PII: real names plus any identifier -- SSN, DOB, address, phone, email, account numbers
- Personnel records
- Operational planning detail
- Credentials and API keys

**CUI defined for this audience.** CUI is information requiring safeguarding per law or policy but not classified. Examples: FOUO documents (legacy marking being replaced by CUI), Law Enforcement Sensitive (LES), personnel records, unclassified intelligence source and method information. Rule: if the document has any marking, or describes real people, units, operations, or capabilities, it does not get pasted. Full stop.

**Where prompts actually go.** Consumer apps (Claude.ai, ChatGPT.com) transmit to the provider's backend. Prompts may be retained, reviewed by humans, and used to improve the model unless the user opts out. "Authorized for work use" is a property of the contract the organization has signed -- not the impressiveness of the tool. Without an ATO or approved system designation, a consumer app is not authorized for CUI regardless of how useful it is.

**Local session logs.** Claude Code writes conversation history to disk in the .claude/ folder by default. That log is subject to the same handling requirements as its content. Scrub discipline applies to what you type, not just what you paste.

**Scrub checklist.**
- Real names (people, units, organizations)
- Real locations (base names, grid coordinates, country names in operational context)
- Dates tied to real operations or events
- Any document markings (if the document is marked, the content is restricted)
- Phone numbers, email addresses, account identifiers
- Credentials, API keys, passwords -- never, under any circumstances
- System or network names, IP addresses, hostnames

**Bracketed placeholder technique.** Replace specifics with [NCO], [location], [unit]. The model can still help with the analysis; it does not need the identifiers.

**Hands-on.** Run a scrub drill: hand the student a realistic-but-fake document salted with names, ranks, units, and locations, and have them produce a paste-safe version using bracketed placeholders. The skill is recognizing what to strip, then doing it by reflex.

**Doctrinal framing.** You do not transmit in the clear because the net is always assumed compromised. An AI tool is the open net. Scrub before you send, every time, no exceptions -- the habit is the protection, not the good intentions.

**Watch-outs.**
- Do not let this collapse into "AI is dangerous, avoid it." The goal is safe use, not fear.
- Policy specifics shift. Teach the durable reflex (scrub, when in doubt leave it out) and point at current policy for the line itself, rather than baking a version that goes stale.
- A student who has already been using chatbots loosely may need to unlearn a habit, not just learn one. Surface that directly.

---

## Phase 1 — Driving the Model With Words

### Module 1.1 — Prompting as a Deliberate Skill

**Objective.** Move from one-line questions to deliberate prompts: be specific, state the format you want, give an example, and say what you do *not* want. Treat the prompt as something you construct, not something you blurt.

**Why it matters.** This is where a casual user already has partial skill, so it is the confidence bridge between "I use chatbots" and "I am learning a craft." It also sets up ACC's prompting framework as a refinement rather than a foreign concept.

**Hands-on.** Take one weak prompt and improve it live in three passes — add specificity, add a format request, add an example — and watch the output sharpen each time. The before/after is the lesson.

**Doctrinal framing.** A vague prompt is a vague order, and a vague order gets you a vague result executed with full confidence. Clear intent, clear constraints, clear measure of done. The model briefs back exactly as well as you briefed it.

**Watch-outs.**
- Do not hand over a giant template to memorize. The skill is the *instinct* to be specific, not a fill-in-the-blank form.
- More words is not better. Teach precision, not volume — a tight prompt beats a long one.

**Chain-of-thought prompting.** Ask the model to show its reasoning before answering. Append "think step by step" or "walk me through your reasoning before giving the final answer." This dramatically improves accuracy on multi-step tasks and makes the model's logic visible for verification. Use for complex analysis and planning.

**Few-shot prompting.** Provide one or more examples of the input-output pattern before the actual request. The model infers the pattern. Useful when the output format is precise or when describing what you want in words alone keeps producing the wrong result.

### Module 1.2 — Structure Beats Vibes

**Objective.** Grasp that a repeatable structure produces more reliable results than improvising each time, and that a prompting framework is just a checklist for not forgetting the parts that matter.

**Why it matters.** ACC teaches a specific framework. The student does not need that exact one yet — they need to accept the *premise* that structure helps, so the framework arrives as "here is a good one" rather than "here is a strange new ritual."

**Doctrinal framing.** A framework is a pre-combat checklist. You could brief from memory every time and mostly be fine, but the checklist is why you do not discover the missing piece at the worst moment.

**RGCOA -- the five components.**
- **Role:** tell the model who to be and what expertise to draw on
- **Goal:** the specific task in one sentence
- **Context:** background, constraints, audience, relevant information
- **Output:** what a good response looks like -- format, length, tone, inclusions and exclusions
- **Asks:** what to do when information is missing, what to flag, what not to assume. "If you need information I have not provided, ask before proceeding. Do not invent facts. If you find a contradiction, flag it." The Asks element gives the model permission to surface uncertainty instead of generating a plausible-sounding guess.

**Worked military example -- weak vs RGCOA.**

Weak: "Summarize this report."

RGCOA: "Role: intelligence analyst preparing products for a brigade commander. Goal: BLUF-formatted summary of the attached report. Context: covers threat activity in the past 72 hours; commander reads this at 0500 before BUB. Output: BLUF (two sentences max), Key Points (three bullets), Recommended Action (one sentence) -- total under 150 words. Asks: flag contradictions in the source; say so if uncertain."

**Watch-outs.**
- Do not get into a framework holy war. The taxonomy matters; the brand name does not. Teach that explicitly so students do not fixate on one acronym.
- Keep the student iterating, not worshipping the structure. The structure serves the result, never the reverse.

---

## Phase 2 — Operating the Computer the Tool Lives On

### Module 2.1 — Files, Folders, and Paths

**Objective.** Build a working model of the file system: files live in folders, every file has an address (a path), and extensions tell you what kind of file it is. Distinguish plain text from rich text.

**Why it matters.** ACC has students referencing files by path and working inside a project folder from Day 1. A student who only knows "Documents" and "Downloads" is lost the moment a path appears.

**Hands-on.** Have the student find a file's full path on their own machine, then create a folder, put a file in it, and say its path out loud. The address has to stop being abstract.

**Doctrinal framing.** A path is a grid coordinate. "The file is around here somewhere" is not a location; the full path is the ten-digit grid that puts everyone on the same point.

**Watch-outs.**
- Mac and Windows differ in slashes and layout. Teach the concept, then show their specific OS — do not let the difference become a source of dread.
- Hidden files and extensions are often turned off by default. Show them how to reveal both, or paths later will not match what they see.

### Module 2.2 — The Terminal, Demystified

**Objective.** Remove the fear of the command line. Understand what a terminal is, what a command is, how to read one before running it, and how to navigate and run a single thing without panic.

**Why it matters.** ACC needs students "knowledgeable but not fluent" in the terminal. Your job is to *delete the fear*, not build mastery. A frozen student on Day 1 is a student who falls behind on everything that follows.

**Hands-on.** Have them open the terminal, see where they are, move into a folder, list what is there, and run one harmless command — narrating what each one does before pressing enter. Five minutes of this dissolves most of the dread.

**Doctrinal framing.** The terminal is just talking to the machine directly instead of through the menus. Same building, back door instead of the lobby. The hacker-movie mystique is theater; it is a text box that takes orders.

**WSL setup for Windows (recommended path for this course).** Open PowerShell, run `wsl --install` (Windows 11). First launch asks for a Linux username and password. Windows files inside WSL are at `/mnt/c/Users/YourName/`. Path conversion: `C:\Users\Jake\Documents` becomes `/mnt/c/Users/Jake/Documents`. In VS Code: install the "WSL" extension; from a WSL terminal run `code .` to open the current folder.

**Stopping a running command.** `Ctrl+C` interrupts and stops whatever is currently running in the terminal. Always `Ctrl+C`, not `Ctrl+Z`.

**`touch` on different platforms.** `touch filename` works in WSL and macOS. In native PowerShell it does not exist -- use `New-Item filename` instead.

**Command reference.**

| Action | WSL/Linux/macOS | Note |
|---|---|---|
| Where am I | `pwd` | |
| List files | `ls` | |
| List with details and hidden | `ls -la` | |
| Move into folder | `cd foldername` | |
| Move up one level | `cd ..` | |
| Go to home | `cd ~` | |
| Make a folder | `mkdir foldername` | |
| Make an empty file | `touch filename` | touch not in PowerShell |
| Copy a file | `cp source dest` | |
| Move or rename | `mv source dest` | |
| Stop a running command | `Ctrl+C` | Always Ctrl+C, not Ctrl+Z |

**Watch-outs.**
- Do not teach twenty commands. Four or five and the confidence to read an unfamiliar one is the entire goal.
- Reading before running is itself the lesson, and it pairs with the agent-trust module later. Build the "look before you execute" habit here.
- Resist going deep. This is the single most tempting place to over-invest and the place ACC needs the least.

### Module 2.3 — A Real Text Editor

**Objective.** Get comfortable in VS Code: opening a folder, viewing and editing files, and understanding it as the place the work lives — distinct from a word processor.

**Why it matters.** VS Code is ACC's environment. Meeting it cold on Day 1 is one more thing to fear. Meeting it here makes it familiar furniture.

**Doctrinal framing.** Your editor is your workbench. You do not learn where every tool hangs on day one of the fight; you learn it in the shop beforehand so your hands already know the layout.

**Watch-outs.**
- Do not tour every feature. Open, read, edit, save. The rest reveals itself with use.
- Keep word-processor instincts from leaking in — there is no autoformatting magic here, and that is a feature.

### Module 2.4 — Markdown

**Objective.** Read and write Markdown fluently enough to be unbothered by it: headers, bold, lists, code blocks. Recognize it as plain text with light, visible formatting marks.

**Why it matters.** Non-negotiable. Every artifact in ACC — skills, commands, the harness instruction files, the spec documents — is Markdown. A student who cannot read Markdown cannot read Day 2 at all.

**Hands-on.** Write a short Markdown file with a heading, a couple of bold words, a bullet list, and a code block, then view it rendered. Seeing the marks turn into formatting is the click moment.

**Doctrinal framing.** Markdown is field-expedient formatting. No heavy kit, no special software — a few marks anyone can read on a plain page, and it works the same everywhere you take it.

**Watch-outs.**
- Do not drift into exotic syntax (tables, footnotes) on the first pass. Headers, emphasis, lists, code blocks carry almost everything.
- Stress that it is *just text*. The reassurance that there is nothing hidden under it is half the value.

---

## Phase 3 — The Safety Net

### Module 3.1 — Git and GitHub, the Concept

**Objective.** Understand git as a system of save points and history, and GitHub as the shared copy in the cloud. Know *why* you would want either: an undo of last resort and a place work survives the machine.

**Why it matters.** ACC keeps git "light touch" and walks each step as it goes, so you owe the *concept*, not fluency. It pairs directly with ACC's Day 2 model of three ways to go back — undo the conversation, undo the files, save forever.

**Hands-on.** Optional and minimal: make a change, save a checkpoint, make a worse change, and roll back to the checkpoint. The feeling of "I can always get back" is the entire deliverable.

**Doctrinal framing.** Git is the save point before the breach. If the room goes bad, you reload and you are back at the door at full strength. GitHub is uploading that save so it survives even if the machine is lost.

**Watch-outs.**
- This is the second great over-investment trap after the terminal. Every hour spent making them *fluent* in git is stolen from the concepts ACC does not re-teach. Aim for "not afraid," not "competent."
- Do not touch branching, merging, or conflicts. Save, history, restore, cloud copy. That is the floor and the ceiling.

---

## Phase 4 — The Hinge

### Module 4.1 — From Chatbot to Agent

**Objective.** Make the central leap: an agentic tool does not just produce text, it takes *actions* — it can read your files, run commands, and reach the internet on your behalf. Understand that this changes everything about how much you verify and permit.

**Why it matters.** This is the conceptual hinge the entire ACC course swings on. ACC Day 1 opens by installing an agentic tool and assumes the student already understands why an actor that can touch the file system is a different animal from a chat box. This module is the direct handoff.

**Hands-on.** Contrast the two side by side: a chatbot that can only tell you how to rename a file, versus an agent that can rename it. Naming the difference in front of them — *says* versus *does* — is the module.

**Doctrinal framing.** A chatbot is the analyst who briefs you. An agent is the element that executes. You brief the executing element far more carefully, because it does not just describe the action — it carries it out. ACC's line from here on: treat every agent like a motivated PFC. Over-plan, over-brief, never assume.

**Watch-outs.**
- The "motivated PFC" framing is the whole posture: capable and eager, which is exactly why a sloppy brief is dangerous. Plant it here so ACC can build on it.
- Do not let "it can act" tip into fear. Capability plus verification is the message — permission, review, and a safety net make action safe.
- This module only works if Phases 0 through 3 landed. An agent acting on your files is only un-scary if you already understand files, the terminal, and that git can undo a mistake. If students wobble here, the gap is upstream.

---

## Handoff to ACC Day 1

By the end of Day 0 the student should clear this check:

| Capability | Floor to hit |
|---|---|
| Mental model of an LLM | Knows it predicts, can be wrong, does not retrieve |
| Context window | Knows working memory is finite and resets between sessions |
| System vs user prompt | Knows their input layers on top of standing instructions |
| Data hygiene | Scrubs by reflex; knows what never gets pasted |
| Prompting | Writes specific, structured prompts and iterates |
| File system | Finds and states a file's full path |
| Terminal | Opens it, navigates, runs one command without fear |
| Editor | Opens a folder and edits a file in VS Code |
| Markdown | Reads and writes headers, emphasis, lists, code blocks |
| Git | Understands save points, history, and the cloud copy as a safety net |
| Agent vs chatbot | Understands the tool can act, and must be briefed and verified |

Hit that line and the student walks into ACC Day 1 standing exactly where it expects them. Everything past this line is ACC's job.
