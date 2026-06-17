# Standing Orders: Making the AI Know You

**Who this is for:** Someone who already uses an AI tool and is tired of re-briefing a stranger every session.

**What you will leave with:** You have set up persistent instructions — standing orders — in your tool of choice, so the model already knows who you are, how you communicate, and what to never do before you type a single word.

---

## Why Default Settings Are a Starting Point, Not a Destination

**BLUF.** Most AI tools let you set persistent instructions that shape every conversation — your role, your preferences, what to always and never do — so you stop re-briefing the model from scratch each session.

### Why This Matters

Without customization, every new chat starts cold. The model does not know who you are, how you like to communicate, or what context is always relevant. Every session you either re-explain yourself or accept generic output. Personalization is a one-time investment that pays back on every single conversation after.

Think of it as the standing orders a unit posts so every shift runs the same way without a re-brief. You write them once. The watch reads them on every relief.

### Concepts

Most major platforms expose persistent customization. The mechanism varies but the concept is the same: instructions the model reads at the start of every conversation, before you type anything.

**ChatGPT — Custom Instructions**

Find it at: Settings → Personalization → Custom Instructions

Two fields:

- "What would you like ChatGPT to know about you?" — Background, role, context that is always true.
- "How would you like ChatGPT to respond?" — Tone, length, format, things to always do and never do.

Applied automatically to every new conversation.

**Claude — Projects**

Find it at: Claude.ai → Projects → Create a Project → Set Instructions

One field for the system prompt — use it the same way. Everything in a Project shares the same persistent context. You can also upload documents the model references across all conversations in that project.

**What to put in:**

- Your role and what you do day to day
- How you prefer responses (length, format, tone)
- Things to always do: "Lead with a one-sentence summary." "Use bullet points." "Define technical terms."
- Things to never do: "No emojis." "No padding or filler." "Do not apologize."
- Recurring context: your tools, your team's terminology, your domain

**What to keep out:** The data-handling bright line from Module 1 applies here in full — custom instructions are sent to the platform's servers on every request, so nothing sensitive, controlled, or above the system's authorization ceiling goes in. That rule does not change because this is a settings field instead of a chat box.

!!! example "Before and After Custom Instructions"
    **Without custom instructions:** Ask "Summarize this document." The model produces a five-paragraph response in a neutral, hedging tone with an introduction, conclusion, and multiple caveats.

    **With custom instructions:** "I'm an analyst. Lead with BLUF. Use bullets. No padding. Max 150 words."

    Same document. Same model. Direct, structured output that matches how you actually communicate.

!!! tip "Start With One Thing"
    Tell it one thing it gets wrong every time. Fix that first. Build from there. A tight 50-word custom instruction that actually sticks beats a 1,000-word template copied from the internet that the model ignores after three turns.

!!! warning "Custom Instructions Count Against Your Context Window"
    They are loaded on every message. A very long custom instruction reduces the effective window for your actual conversation. Keep them under 500 words. If you need more context, use a Project document instead.

??? note "Instructor Note — Platform Drift"
    Custom instruction interfaces change frequently. Verify the location of these settings before teaching — the menu path may have moved since this was written. The concept is stable; the UI is not.

??? note "Instructor Note — Security Back-Reference, Not a Re-Teach"
    Do not re-teach data handling here. Point back to Module 1's bright line and move on: everything in a custom instruction goes to the platform's servers on every request, so nothing sensitive, nothing controlled, nothing above the authorization ceiling. One line, then keep going. The discipline was already established; this is a reminder that it does not have an exception for settings fields.

### Hands-On

1. Open your AI tool of choice. Find the custom instructions or project settings.
2. Write at least three instructions:
    - One about who you are and what you do
    - One about how you like responses formatted
    - One about something to never do
3. Start a new chat. Ask a question you have asked before without custom instructions.
4. Compare the two outputs.

!!! question "Before You Continue"
    You wrote a custom instruction that says "always lead with a one-sentence summary." On one response, the model ignores it. What are the two most likely causes?

<div class="quiz-block">
  <p class="quiz-question">What is the main purpose of custom instructions in an AI tool?</p>
  <ul class="quiz-options">
    <li data-correct="false">To make the model smarter or more capable</li>
    <li data-correct="false">To save your conversation history across sessions</li>
    <li data-correct="true">To set persistent context the model reads at the start of every conversation, so you stop re-briefing it each session</li>
    <li data-correct="false">To share your settings with teammates</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I have found the custom instruction settings in my AI tool
- [ ] I have written at least three instructions (who I am, how I want responses, what to never do)
- [ ] I ran a before/after comparison and noticed a difference
- [ ] I did not include any sensitive or controlled information in my instructions

---

## Going Further: Projects, Memory, and Personas

**BLUF.** Beyond basic custom instructions, most major platforms offer structured ways to give the model persistent context across sessions — projects, memory, and saved personas. Used well, they turn a generic tool into one that already knows your work.

### Why This Matters

Custom instructions are a single set of standing orders. The next step is organizing persistent context by mission type — a dedicated workspace for analysis, another for writing, another for research — so the model never carries the wrong context into the wrong task.

### Concepts

**Projects (Claude)**

A Project is a dedicated workspace with its own system prompt and document library. Use it when:

- You have a recurring task with the same context requirements every time
- You want to upload reference documents the model can consult in every conversation
- You need different configurations for different types of work

Create one project for analysis work, one for writing, one for research. Each has its own instructions and document set. You never carry context from one type of work into another.

**Memory (ChatGPT)**

ChatGPT's memory feature records facts from your conversations and surfaces them in future sessions. The model notes things like your name, your role, your preferences, and past decisions.

You can view, edit, and delete memory entries at any time: Settings → Personalization → Memory.

!!! warning "Memory Is Not a Replacement for Custom Instructions"
    Memory is reactive — it records what comes up. Custom instructions are proactive — you set them deliberately. Use both: custom instructions for stable preferences, memory for things that evolve over time.

**Personas**

Some platforms (and all agentic harnesses) support named personas with defined instructions. A persona is a named configuration — a specific role, tone, and set of constraints — that you can switch to by name.

In an agentic context, a well-defined persona means you do not re-explain the agent's role and constraints every time you start a session. The persona carries it. You will see this idea again in the field-craft module, where context files become the primary way to brief an agent.

!!! example "A Working Project Setup"
    You do a lot of document analysis. Your Claude Project has:

    - **Instructions:** "You are a plain-language editor supporting an analyst. Lead with the main finding. No jargon. Flag anything that requires verification before acting on it. Max 200 words per response unless asked for more."
    - **Documents:** Your organization's style guide, a glossary of domain terms, a one-page brief on the current project.

    Every analysis conversation starts with that context already loaded. You open the project and start working.

??? note "Instructor Note — Memory Feature Availability"
    Memory availability varies by subscription tier and has been rolled out at different times across regions. Verify current availability before teaching. The concept is stable; feature gating changes.

### Hands-On

1. If you use Claude: create a Project for one type of work you do repeatedly. Add instructions and at least one reference document.
2. If you use ChatGPT: review your current memory entries (Settings → Personalization → Memory). Delete anything that is outdated or wrong. Add a manual memory entry for something the model should always know.
3. Start a new conversation inside the Project or with memory active. Compare how quickly it orients to your work.

!!! question "Before You Continue"
    You create a Project for analysis work with detailed instructions. Three months later, your role changes. What do you need to update, and where?

<div class="quiz-block">
  <p class="quiz-question">You want the model to always reference your organization's style guide in every conversation. What is the most reliable way to set this up?</p>
  <ul class="quiz-options">
    <li data-correct="false">Paste the style guide at the start of every conversation</li>
    <li data-correct="false">Add the style guide content to your custom instructions</li>
    <li data-correct="true">Upload the style guide as a document inside a Project (Claude) or as a memory file, so it is available without consuming context each session</li>
    <li data-correct="false">Ask the model to remember the style guide at the end of each session</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I have set up at least one Project or named configuration for recurring work
- [ ] I know where to find and manage memory entries in my tool
- [ ] I understand the difference between custom instructions (proactive) and memory (reactive)
- [ ] My custom instructions and project documents contain no sensitive or controlled information

---

## Summary

| Concept | What it is | When to use it |
|---|---|---|
| Custom instructions | Persistent standing orders the model reads before every chat | Stable, always-true preferences: role, format, never-do behaviors |
| Projects (Claude) | A workspace with its own instructions and uploaded documents | Recurring work with the same context requirements every time |
| Memory (ChatGPT) | Reactive record of facts surfaced from your conversations | Things that evolve over time; supplements custom instructions |
| Personas | A named role/tone/constraint set you switch to by name | Agentic work where you do not want to re-brief the role each session |
| The data-handling line | The Module 1 bright line, applied to settings fields | Always — instructions reach the platform's servers on every request |

## End of Module

You have moved from re-briefing the model every session to posting standing orders it reads automatically. The same discipline that governs what you paste into a chat governs what you put in your instructions: the boundary set in Module 1 does not have an exception for a settings field. Next, you leave the chat window entirely and learn the terrain an agent operates on — the filesystem and the terminal.
