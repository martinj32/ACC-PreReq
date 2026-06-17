# Crossing the LD: Bridge to Advanced Agentics

**Who this is for:** An operator who has finished the proving ground and is about to step into the ACC main course — and wants a map of the terrain on the far side before crossing the line of departure.

**What you will leave with:** Recognition, not mastery. You will be able to *name* the patterns, components, and controls that the main course teaches you to *build* — grounding and retrieval, tools and MCP, permissions and guardrails, planning, the named workflow patterns, sub-agents, and agent evaluation — and you will know exactly which of these is deferred to the main course and why.

---

## How to Read This Module

**BLUF.** This is a recognition module: it gives you the vocabulary and the mental map for advanced agentics so the main course has something to build on, and it deliberately stops short of teaching you to build any of it.

This module is different from the eleven before it. Those taught you to *do* things — prompt, command an agent, verify, ship. This one teaches you to *recognize* things. When the main course says "wrap that tool in an MCP server" or "use an orchestrator-workers pattern," you will already know what those words point at. That is the entire job of a bridge: get you across the gap with your footing, not turn you into an expert on the far bank.

Everything here is built on the one primitive you already own. We recap that first, then walk the terrain.

!!! note "Recognition, Not Build"
    Throughout this module, watch for the **Deferred to the main course** markers. They are not gaps — they are the boundary of this course. You are meant to leave able to name these, not implement them.

??? note "Instructor Note — Hold the Altitude"
    The strongest temptation in this module is to start teaching. Don't. Every segment is a flyover. If students leave able to recognize the terms and say what is deferred, the module succeeded. Depth here steals time from the main course and overwhelms students who just finished a capstone.

---

## Segment 0 — Recap the Primitive

**BLUF.** Everything advanced is the same primitive you already command — an engine in a harness, supervised by an operator running a delegate-verify-own loop — repeated, connected, and scaled, so nothing ahead is genuinely new in kind.

### Why This Matters

The fear at this stage is that "advanced agentics" is a different, harder thing. It is not. It is the primitive you proved in the capstone, composed at larger scale. Anchoring everything ahead to what you already own is what keeps the main course from feeling like a wall.

### Concepts

You already hold the whole foundation:

- **Engine.** The model — predicts text, reasons in language, has no body of its own (Module 1).
- **Harness.** What gives the engine a body: tools, file access, the ability to act (Module 7).
- **Operator.** You — the accountable supervisor who delegates, verifies, and owns the result (Modules 7 and 9).
- **The loop.** Delegate, verify, own — the cycle you ran on a live build in the capstone (Module 11).

Every advanced topic in this module is one of these, extended. More tools on the harness. A plan you approve before action. One operator-agent directing several worker-agents. The primitive does not change; the composition does.

!!! tip "Map Every New Term Back to the Primitive"
    As each segment introduces a term, ask: is this a richer engine, a bigger harness, or a tighter operator loop? Almost everything sorts into one of those three. That sorting is the recognition skill this module builds.

<div class="quiz-block">
  <p class="quiz-question">What is the most accurate way to think about "advanced agentics" relative to what you already learned?</p>
  <ul class="quiz-options">
    <li data-correct="false">A different and fundamentally harder technology that replaces the basics</li>
    <li data-correct="true">The same engine-harness-operator primitive and delegate-verify-own loop, composed and scaled up</li>
    <li data-correct="false">A way to remove the human operator from the loop entirely</li>
    <li data-correct="false">A different model architecture that no longer predicts text</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## Segment 1 — Grounding and Retrieval

**BLUF.** The pattern you used by hand in Module 7 — pulling real source material into the context so the agent answers from retrieved fact instead of memory — has a name: retrieval-augmented generation, and grounded output is the cited, traceable kind you can verify.

### Why This Matters

You already did this. When you fed an agent a document and had it answer from that document rather than its training, you performed retrieval by hand. Naming the pattern lets you recognize it when the main course automates it — and lets you tell, every time, whether an answer is grounded in a real source or generated from the model's memory.

### Concepts

- **Grounded vs. ungrounded.** An *ungrounded* answer comes from the model's trained weights — fluent, but with no source you can check, and subject to every failure mode from Module 1. A *grounded* answer is produced from real material retrieved into the context: a document, a search result, a database record. Grounded output can be cited and traced.
- **RAG — retrieval-augmented generation.** The general pattern: retrieve relevant real sources, put them in the context, and have the model answer from them. You did this manually in Module 7. The main course builds it into the harness so retrieval happens automatically.
- **Why it matters operationally.** Grounding is the practical fix for two Module 1 failures at once: the knowledge cutoff (retrieve current sources) and hallucination (answer from real text, not plausible completion). It does not eliminate the verify step — you still confirm the retrieved source is real and the answer reflects it.

!!! tip "Grounded Is Verifiable; Generated Is Not"
    The operator's question never changes: *where did this come from, and can I check it?* A grounded answer hands you the source. A generated one asks you to trust the model. Treat them differently.

!!! note "Deferred to the main course"
    Building a retrieval pipeline — embeddings, vector stores, automated chunking and ranking — is main-course material. Here you only need to recognize RAG as the named version of the by-hand grounding you already did.

<div class="quiz-block">
  <p class="quiz-question">You used "RAG by hand" in an earlier module without knowing the name. What did that consist of?</p>
  <ul class="quiz-options">
    <li data-correct="false">Asking the model to be more accurate</li>
    <li data-correct="true">Retrieving real source material into the context so the agent answered from it rather than from memory</li>
    <li data-correct="false">Running the same prompt several times and averaging</li>
    <li data-correct="false">Switching to a model with a larger context window</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## Segment 2 — Connecting Tools and MCP

**BLUF.** The harness is extensible — you can give an agent new tools and data sources — and the emerging standard way to do that is the Model Context Protocol (MCP), which exposes capabilities as Tools, Resources, and Prompts; the concept is stable, but the specifics change fast, so verify before you teach or rely on any detail.

### Why This Matters

In the capstone, your agent's harness had a fixed set of abilities. The main course shows you how to *add* abilities — connect the agent to a database, an internal system, a search index. MCP is the standardized connector for that. You need to recognize the term and the three things it exposes; you do not yet need to build a server.

### Concepts

- **The harness is extensible.** An agent's power comes from what its harness lets it touch. Adding a tool is how a general agent becomes useful for a specific job.
- **MCP — Model Context Protocol.** An open standard for connecting agents to external tools and data through a consistent interface, so a capability written once can be reused across different agents and applications rather than wired up bespoke each time.
- **Three things an MCP server exposes:**
    - **Tools** — actions the agent can invoke (query a database, send a request, run a search). The agent *does* something.
    - **Resources** — data the agent can read (files, records, documents). The agent *reads* something.
    - **Prompts** — reusable, pre-written prompt templates the server offers for common tasks. The agent *reuses* a known-good instruction.
- **The mental sort:** Tool = an action, Resource = readable data, Prompt = a canned instruction. That three-way distinction is the recognition target for this segment.

!!! danger "MCP Is Version-Sensitive — Verify Before Teaching or Relying"
    MCP is a fast-moving standard. The protocol details, transport mechanisms, available servers, security and governance model, and the exact Tool/Resource/Prompt semantics change between versions. **Do not teach any specific MCP detail, server name, or capability from memory.** Before any course run or operational use, verify the current state of the protocol at its official documentation and confirm what your organization has authorized. Treat anything specific in this segment as illustrative of the *concept*, not as current fact.

!!! warning "Connecting a Tool Expands the Attack and Disclosure Surface"
    Every tool or resource you connect is a new path data can flow out of — or untrusted input can flow in. The data-handling bright line from Module 1 and the permissions discipline in the next segment apply in full. An extensible harness is powerful and is exactly why guardrails exist.

??? note "Instructor Note — The MCP Trap"
    This is the highest verify-before-teaching risk in the entire prerequisite course. The protocol genuinely shifts between releases. Teach the *shape* — harness is extensible; MCP standardizes the connection; Tools/Resources/Prompts are the three exposed types — and explicitly tell students that any concrete detail must be checked against current docs. Do not let a confident-sounding specific become a taught fact.

!!! note "Deferred to the main course"
    Building MCP servers, configuring transports, and wiring real tools and data into an agent's harness are all main-course material. Recognition of the concept and the three exposed types is the bar here.

<div class="quiz-block">
  <p class="quiz-question">In MCP terms, what is the difference between a <em>Tool</em> and a <em>Resource</em>?</p>
  <ul class="quiz-options">
    <li data-correct="false">A Tool is free; a Resource costs tokens</li>
    <li data-correct="true">A Tool is an action the agent can invoke; a Resource is data the agent can read</li>
    <li data-correct="false">A Tool is for text; a Resource is for images</li>
    <li data-correct="false">There is no difference — they are two words for the same thing</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## Segment 3 — Permissions and Guardrails

**BLUF.** The supervisor mindset becomes concrete here: agents run inside scoped permissions, command allowlists, approval gates, and sandboxes — the technical "how" behind staying the accountable human in the loop.

### Why This Matters

You held the supervisor mindset by judgment in the capstone — reading diffs, marking files read-only. The main course makes that enforcement *technical*: the agent is structurally prevented from doing what it should not, not merely trusted to comply. Recognizing these controls tells you what to ask for when you scope an agent's authority.

### Concepts

- **Scoped permissions.** An agent is granted specific read, write, and execute rights — and nothing more. A read-only agent cannot modify; a sandboxed agent cannot reach outside its box. Least privilege, applied to agents.
- **Command allowlists.** Rather than letting an agent run anything, you permit a defined set of commands. Everything outside the list is blocked by default.
- **Approval gates.** For consequential actions — writing a file, running a command, sending a request — the agent pauses and asks for human approval before proceeding. The gate is where your judgment enters the loop.
- **Sandboxes.** The agent operates in an isolated environment where a mistake cannot damage anything real. This is what makes the deliberate-bad-edit drill from the capstone safe to do at scale.

!!! tip "Guardrails Are the Mechanism; You Are Still Accountable"
    Permissions and gates reduce how much damage a mistake can do — they do not transfer accountability. You still own the output (Module 9). Guardrails make supervision *enforceable*; they do not make it *unnecessary*.

!!! note "Deferred to the main course"
    Configuring permission scopes, writing allowlists, building approval workflows, and setting up sandboxes are main-course skills. Here you recognize them as the technical implementation of the supervisor mindset.

<div class="quiz-block">
  <p class="quiz-question">An <em>approval gate</em> in an agent workflow does what?</p>
  <ul class="quiz-options">
    <li data-correct="false">Speeds the agent up by skipping confirmation steps</li>
    <li data-correct="true">Pauses the agent before a consequential action so a human can approve it</li>
    <li data-correct="false">Removes the need for the operator to verify output</li>
    <li data-correct="false">Grants the agent broader permissions automatically</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## Segment 4 — Planning and Decomposition

**BLUF.** A capable agent can produce a plan and present it for your approval before it acts — and that plan is a supervision artifact: a checkpoint where you steer the work before any change is made.

### Why This Matters

In the capstone you decomposed the build yourself, then delegated pieces. The main course shows agents that decompose a large task into ordered steps *and surface the plan for review*. Recognizing the plan-then-act pattern tells you where to insert your judgment most cheaply — before action, not after.

### Concepts

- **Decomposition.** Breaking a large, ambiguous task into ordered, concrete sub-steps. You did this with pseudocode in Module 10; an agent can do it for a multi-step job.
- **Plan-then-act.** The agent proposes a plan, you review and approve (or correct) it, and only then does it execute. Catching a flawed approach in the plan is far cheaper than catching it in finished work.
- **The plan as a supervision artifact.** The plan is the earliest and cheapest place to apply oversight. It is the delegate step of the loop made visible: you see the agent's intended approach before any file is touched.

!!! tip "Steer at the Plan, Not the Wreckage"
    Correcting a plan costs a sentence. Correcting completed work costs a rebuild. When an agent offers a plan, that is your highest-leverage moment to redirect.

!!! note "Deferred to the main course"
    Building agents that plan, structuring multi-step decomposition, and managing plan-execution workflows are main-course material. Recognizing the plan as an approval checkpoint is the bar here.

<div class="quiz-block">
  <p class="quiz-question">Why is an agent's proposed plan described as a "supervision artifact"?</p>
  <ul class="quiz-options">
    <li data-correct="false">Because it replaces the need to verify the final output</li>
    <li data-correct="true">Because it is the earliest, cheapest checkpoint to apply your judgment — before any change is made</li>
    <li data-correct="false">Because the agent cannot act without writing one down</li>
    <li data-correct="false">Because it is automatically saved to version control</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## Segment 5 — Workflow Patterns, Named

**BLUF.** Advanced agentic systems are assembled from a small set of named, reusable patterns — prompt chaining, routing, orchestrator-workers, and evaluator-optimizer — and recognizing them by name is the goal here; you build them in the main course.

### Why This Matters

The main course will hand you these patterns as building blocks. Walking in able to recognize the four by name means you spend main-course time learning to *apply* them, not decoding the vocabulary. Each is just the primitive composed a particular way.

### Concepts

Four recognition targets:

- **Prompt chaining.** Break a task into a sequence of steps, where each step's output feeds the next. A pipeline: draft, then critique the draft, then revise from the critique. Order is the point.
- **Routing.** Classify the incoming request first, then send it to the handler best suited for it. A triage step that directs simple queries to a fast path and complex ones to a heavier one.
- **Orchestrator-workers.** One coordinating agent breaks a job into parts, hands each to a worker, and assembles the results. A team lead delegating to a section.
- **Evaluator-optimizer.** One agent produces output; another evaluates it against criteria and sends back corrections; the first revises. A generate-and-critique loop that runs until the output meets the bar.

!!! tip "Recognize the Shape, Defer the Build"
    You are learning to name these, not wire them. When the main course says "route this," you will know it means classify-then-dispatch. That recognition is the deliverable.

!!! note "Deferred to the main course"
    Implementing any of these patterns — chaining steps, building routers, orchestrating workers, running evaluator-optimizer loops — is main-course work. Naming the four on sight is the bar here.

<div class="quiz-block">
  <p class="quiz-question">A workflow classifies each incoming request and sends it to the handler best suited for it. Which named pattern is this?</p>
  <ul class="quiz-options">
    <li data-correct="false">Prompt chaining</li>
    <li data-correct="true">Routing</li>
    <li data-correct="false">Evaluator-optimizer</li>
    <li data-correct="false">Orchestrator-workers</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## Segment 6 — Sub-Agents and Multi-Agent Systems

**BLUF.** A single operator-agent can delegate to multiple worker-agents — one commander directing a team — and this preview is meant only to make the idea recognizable, not to teach you to orchestrate it.

### Why This Matters

The orchestrator-workers pattern points straight at this: systems where one agent commands others. It is where serious scale comes from, and where supervision gets genuinely harder, because now you are supervising a supervisor. You only need to recognize the shape now.

### Concepts

- **Sub-agents.** Worker-agents a coordinating agent spawns and directs, each handling a bounded piece of a larger job.
- **The commander analogy.** One agent acts as the commander — decomposing the mission, assigning tasks, integrating the results — while workers execute their slices. The same chain-of-command structure you already understand, expressed in agents.
- **Supervision gets harder, not optional.** With multiple agents, the accountable human is now overseeing a delegation chain. The loop still applies; it just has more surface to cover. Owning the output of a multi-agent system is a real challenge the main course addresses directly.

!!! warning "More Agents, More Surface to Verify"
    Multi-agent systems multiply both capability and the places things can go wrong. The delegate-verify-own loop does not disappear at scale — it becomes more demanding. Do not read "the agents handle it" as "I can stop verifying."

!!! note "Deferred to the main course"
    Designing, building, and orchestrating multi-agent systems is squarely main-course material. This segment is a preview so the term is familiar, nothing more.

<div class="quiz-block">
  <p class="quiz-question">What does adding sub-agents change about the operator's responsibility?</p>
  <ul class="quiz-options">
    <li data-correct="false">It removes the need to verify, since agents check each other</li>
    <li data-correct="true">It expands the surface the accountable human must supervise — the loop still applies, with more to cover</li>
    <li data-correct="false">It transfers accountability to the commander agent</li>
    <li data-correct="false">It makes verification optional for low-stakes tasks</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## Segment 7 — Evaluating an Agent

**BLUF.** Judging an agent means assessing its *whole* output, not a single answer — through spot-checks, regression testing against known-good results, and the evaluator-optimizer idea — a light preview of a discipline the main course develops fully.

### Why This Matters

The capstone graded one build with your own eyes. At scale, eyeballing every output stops working, and you need methods to judge an agent's performance systematically. Recognizing the basic ideas now sets up the main course's deeper treatment of evaluation.

### Concepts

- **Spot-checks.** Sample a subset of outputs and verify them closely. You cannot read everything at scale; you can check enough to calibrate trust.
- **Regression testing.** Keep a set of known-good results. When the agent or its setup changes, re-run them and confirm the outputs still match — catching when a change quietly breaks something that used to work.
- **Evaluator-optimizer, reused.** The same pattern from Segment 5, applied to evaluation: one agent (or a rubric) judges another's output against criteria and drives improvement. A scalable version of the verify step.

!!! tip "Evaluation Is the Verify Step at Scale"
    Everything here is the capstone's verify step, grown up. Spot-checks, regression sets, and evaluator loops are how you keep verifying when there is too much output to read by hand.

!!! note "Deferred to the main course"
    Building production evaluation harnesses, regression suites, and automated evaluator pipelines is main-course material. Recognizing that whole-output evaluation is a discipline — and naming spot-checks, regression, and the evaluator-optimizer idea — is the bar here.

<div class="quiz-block">
  <p class="quiz-question">Why is whole-output evaluation necessary instead of just reading every answer at scale?</p>
  <ul class="quiz-options">
    <li data-correct="false">Because agents are always correct, so reading is wasted effort</li>
    <li data-correct="true">Because at scale you cannot read everything — you need spot-checks and regression tests to judge performance systematically</li>
    <li data-correct="false">Because evaluation transfers accountability away from the operator</li>
    <li data-correct="false">Because the model evaluates itself perfectly</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

---

## What's Deferred — and What You Carry Across

**BLUF.** You cross the line of departure with the vocabulary and the map; the main course is where you build. Carry the primitive and the loop — they are what everything ahead is made of.

The boundary of this course, stated plainly. The main course teaches you to *build* all of these:

| Topic | You can now recognize | The main course teaches you to build |
|---|---|---|
| Grounding / Retrieval | RAG as named, traceable grounding | Retrieval pipelines (embeddings, vector stores) |
| Tools & MCP | Harness is extensible; Tool/Resource/Prompt | MCP servers and real tool/data connections |
| Permissions & Guardrails | Scopes, allowlists, gates, sandboxes | Configuring enforceable agent permissions |
| Planning | Plan-then-act as a supervision checkpoint | Agents that decompose and plan |
| Workflow Patterns | The four patterns by name | Implementing chaining, routing, orchestration, eval loops |
| Sub-Agents | One commander directing workers | Designing multi-agent systems |
| Evaluation | Spot-checks, regression, evaluator-optimizer | Production evaluation harnesses |

!!! danger "One Last Verify-Before-Teaching Reminder"
    Model names, tiers, context-window sizes, MCP protocol details, and any DoD AI policy specifics all change between course runs. Nothing version-sensitive in this module — most of all MCP — should be delivered from memory. Verify against current official sources before you teach or rely on it.

### Readiness Check

- [ ] I can state that advanced agentics is the same engine-harness-operator primitive, scaled
- [ ] I can name RAG as the grounding pattern I already used by hand
- [ ] I can describe MCP as the standard for extending the harness and name Tool / Resource / Prompt — and I know it is version-sensitive and must be verified
- [ ] I can name the permission and guardrail controls behind the supervisor mindset
- [ ] I can explain why an agent's plan is a supervision checkpoint
- [ ] I can name the four workflow patterns: prompt chaining, routing, orchestrator-workers, evaluator-optimizer
- [ ] I recognize the sub-agent / multi-agent idea and that it expands, not removes, supervision
- [ ] I can name spot-checks, regression, and evaluator-optimizer as agent-evaluation ideas
- [ ] I know which of these is deferred to the main course

---

## Summary

| Segment | Recognition Target | Deferred to Main Course |
|---|---|---|
| 0 Primitive | Engine-harness-operator + the loop, scaled | — (you already own it) |
| 1 Grounding | RAG = named, traceable grounding | Retrieval pipelines |
| 2 Tools & MCP | Extensible harness; Tool/Resource/Prompt | Building MCP servers (verify details) |
| 3 Guardrails | Scopes, allowlists, gates, sandboxes | Configuring permissions |
| 4 Planning | Plan-then-act as a checkpoint | Building planning agents |
| 5 Patterns | Chaining, routing, orchestrator-workers, evaluator-optimizer | Implementing them |
| 6 Sub-Agents | One commander, many workers | Multi-agent design |
| 7 Evaluation | Spot-checks, regression, evaluator-optimizer | Production eval harnesses |

!!! note "End of Module — and End of the Prerequisite Course"
    You have crossed the line of departure with your footing. You command an agent, you verify and own its work, you recover from its mistakes, and you can now name the terrain ahead. The primitive and the loop are what every advanced topic is built from — carry them across. The main course is where you build.
