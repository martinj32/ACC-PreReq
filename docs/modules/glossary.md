# Glossary & Quick Reference

**Who this is for:** Anyone in the course who hits a term they don't know yet and wants a fast, plain answer. Start here on day one; come back any time.

**What you will leave with:** A one-stop reference for the core vocabulary of the course — each term in one or two plain sentences, no prior technical knowledge assumed.

---

!!! tip "How to Use This Page"
    These are quick-reference definitions, not the full lesson. Each term is taught in depth in the module that owns it — the cross-references point you there. If a term feels thin here, that is by design: the module gives you the mental model; this page just keeps the words straight.

!!! note "A Word on the Definitions"
    Plain over precise. Where a one-sentence version sacrifices a little technical nuance for clarity, that is a deliberate trade — the goal is a working understanding a busy operator can hold in their head, not a textbook.

---

## How AI Works (the engine)

**Model**
: The trained AI system itself — the "engine" that takes text in and produces text out. It learned patterns from a huge body of text; it was *trained, not programmed*, so there is no rulebook inside it to look up. *(Module 1)*

**Parameter**
: One of the billions of internal numbers a model adjusts during training to capture patterns. You almost never touch these directly; the count ("a 70-billion-parameter model") is a rough proxy for how big and capable a model is. *(Module 1 / Module 8)*

**Inference**
: The act of running a trained model to get an answer — i.e., every time you send a prompt and it generates a response. Training is building the engine; inference is driving it. *(Module 1)*

**Token**
: The chunk of text a model actually reads and writes — roughly three-quarters of an English word each. Models count work in tokens, not words, which is why tokens are the unit of both context limits and cost. *(Module 1 / Module 8)*

**Context window**
: The fixed maximum number of tokens a model can hold in one conversation at a time — like a whiteboard with finite space. Fill it and the earliest content gets crowded out, which is why very long chats start to degrade. *(Module 1)*

**Temperature**
: A setting that controls how much randomness the model uses when choosing its next token. Low temperature = more focused and repetitive; high temperature = more varied and creative — and it is one reason the same prompt can give different answers. *(Module 1 / Glossary cross-ref: nondeterminism)*

**Hallucination**
: When a model states something false with full confidence, because it generates statistically likely text and has no built-in truth-check. Expected behavior of the system, not a rare bug — which is why everything that matters gets verified before you act on it. *(Module 1; ethical duty in Module 9)*

**Multimodal**
: A model that can take in or produce more than just text — images, screenshots, PDFs, charts, or voice, in addition to writing. Each extra mode brings its own failure modes (e.g., misreading a blurry table). *(Module 3)*

---

## Talking to the Model (prompting & grounding)

**Prompt**
: The instruction or question you give the model — your mission order to the machine. A clear prompt that says who to be, what's needed, and what good looks like gets a far better result than a vague one. *(Module 2)*

**System prompt vs. user prompt**
: The *system prompt* is the standing background instruction that sets the model's role and rules for the whole conversation; the *user prompt* is each specific request you type in. Think standing orders (system) versus the task of the moment (user). *(Module 2 / Module 4)*

**Grounding (retrieval / RAG)**
: Giving the model real, external source material — a web search result, an uploaded file, a document — so its answer is anchored to actual sources instead of generated from memory alone. **RAG** (Retrieval-Augmented Generation) is the formal name for the retrieve-then-answer pattern; grounded output can be cited and traced, ungrounded output cannot. *(Module 3; named again in Module 12)*

---

## Agents & the Operator (taking action)

**Agent vs. chatbot**
: A *chatbot* gives advice — it tells you the command; an *agent* takes action — it runs the command on your real files and terminal. The entire difference is access: read, write, and execute. *(Module 7)*

**The harness**
: The software wrapped around the model that gives it hands — the tools, file access, and terminal connection it needs to actually *do* things rather than just talk. Engine (model) + harness (tools) + operator (you) is the core primitive of agentic work. *(Module 7)*

**Tool call**
: A single action the agent takes through its harness — reading a file, running a command, searching the web. Watching the tool calls is how you see what the agent actually did, not just what it says it did. *(Module 7)*

**Operator posture**
: Your stance as the human in charge: you delegate clearly, verify the work, and own the outcome — the commander, not the typist. Capability does not transfer accountability; you sign for the result. *(Module 7; accountability in Module 9)*

**MCP (Model Context Protocol)**
: A standard way to plug new tools, data sources, and capabilities into an agent's harness — "the harness is extensible." Conceptually it offers Tools, Resources, and Prompts; the details are version-sensitive, so verify before relying on specifics. *(Module 12 — recognition only)*

---

## The Logbook (version control)

**Version control**
: A system that records a snapshot of your files every time they change — what changed, when, and why — with the ability to rewind to any earlier state. The duty logbook for your work, and essential once an agent can edit your files. *(Module 6)*

**Commit**
: One saved snapshot in version control — a recorded entry in the logbook, with a short note on what changed and why. You can always return to any commit later. *(Module 6)*

**Branch**
: A separate line of work in version control where you can make changes without touching the main version, then merge them back when ready. It lets you try something risky without endangering known-good work. *(Module 6)*

---

## Quick Reference Table

| Term | One-line meaning | Owning module |
|---|---|---|
| Model | The trained AI engine — text in, text out | M1 |
| Parameter | An internal number tuned in training; count ≈ model size | M1 / M8 |
| Inference | Running the model to get an answer | M1 |
| Token | ~¾ of a word; the unit of context and cost | M1 / M8 |
| Context window | Fixed token limit per conversation | M1 |
| Temperature | Randomness setting for the next token | M1 |
| Hallucination | Confident false output; expected, not a bug | M1 / M9 |
| Multimodal | Handles images, PDFs, audio — not just text | M3 |
| Prompt | Your instruction to the model | M2 |
| System vs. user prompt | Standing role/rules vs. the request of the moment | M2 / M4 |
| Grounding / RAG | Anchoring answers to real retrieved sources | M3 / M12 |
| Agent vs. chatbot | Takes action vs. gives advice | M7 |
| The harness | The tools/access that give the model hands | M7 |
| Tool call | A single action the agent takes | M7 |
| Operator posture | Delegate, verify, own — commander not typist | M7 / M9 |
| MCP | Standard way to add tools/data to an agent | M12 |
| Version control | Logbook of file changes you can rewind | M6 |
| Commit | One saved snapshot in the logbook | M6 |
| Branch | A separate line of work you can merge back | M6 |

---

!!! note "Verify-Before-Teaching Reminder"
    Model names, tiers, pricing, and context-window sizes change with releases, and MCP details are version-sensitive. Treat any specific number you hear as something to confirm against current provider documentation before relying on it.
