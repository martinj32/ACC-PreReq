# Briefing the Machine: Prompting as a Mission Order

**Who this is for:** Anyone who can talk to an AI tool and now wants to brief it the way you would brief a capable junior — deliberately, so it does not fill the gaps with guesses.

**What you will leave with:** The four-element framework for a deliberate prompt, the habit of iterating instead of one-shotting, and a set of intermediate structures — few-shot, chain-of-thought, decomposition, structured output, and the system-vs-user distinction — that extend clarity rather than chase tricks. You will produce five structured prompts of your own.

---

## Prompting as a Mission Order

**BLUF.** Converting prompting-by-feel into method means telling the model who to be, giving it the context it needs, showing it an example, and saying what good output looks like — the same as briefing a person, not typing into a search box.

### Why This Matters

A vague prompt is a vague order, and a vague order gets a vague result from a junior who fills the gaps with assumptions. You have already seen in Module 1 what the model does when it guesses wrong. Deliberate prompting is how you reduce that surface area. Think of it as the difference between "go handle the comms" and a proper five-paragraph order: the second one does not leave the outcome to chance.

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

The iterative habit matters more than the perfect prompt. A rough ask the model can build on beats silence. Read the output, tighten the next ask based on what missed, repeat.

!!! tip "If You Are Stuck, Ask the Model to Interview You"
    Type: "I need help with [task]. Ask me the questions you need answered before you start."

    The model surfaces what context it is missing. Answer the questions, then ask it to proceed.

!!! warning "The Template Trap"
    The four elements are a structure, not a script to recite. The durable skill is clarity — giving the model what it needs to not guess. How you deliver that varies by task.

!!! danger "Scrub Before You Brief"
    Everything in Module 1's data-handling rule applies to every prompt you write. Real names, units, locations, grids, dates tied to operations, and credentials do not go into an unauthorized tool — not even inside a "good" structured prompt. Use bracketed placeholders like [UNIT], [LOCATION], [NCO]; the model reasons about structure, not identity, and a scrubbed prompt works just as well.

??? note "Instructor Note — Prompt Engineering Creep"
    Resist turning this into a "prompt engineering tricks" hour. Magic phrases are not the lesson. The lesson is clarity. Students who focus on tricks over structure will hit a ceiling fast. The intermediate techniques below are extensions of clarity, not incantations — frame them that way every time.

### Hands-On

1. Pick a real task you need help with.
2. Write a one-line version of the request. Submit it. Save the output.
3. Add role, context, an example of what good looks like, and an output spec. Submit again.
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

- [ ] I can name the four elements of a deliberate prompt
- [ ] I have run a before/after comparison with my own real task
- [ ] I treat prompting as a conversation, not a one-shot command
- [ ] I scrub real identifiers out of every prompt before sending it

---

## Intermediate Prompting: Structure That Extends Clarity

**BLUF.** Five intermediate moves — few-shot, chain-of-thought, decomposition, structured output, and the system-vs-user distinction — each give the model more of what it needs to stop guessing; none of them is a trick, and all of them are just clarity at the next level.

### Why This Matters

The four elements get you a clear order. The intermediate techniques are what you reach for when the task is harder than one clear order can carry: when the format matters exactly, when the reasoning needs to be visible and checkable, or when one ask is really five asks stacked together. These are the difference between a junior who executes a simple order and one you can hand a complex mission.

### Concepts

**Few-shot prompting.** Instead of describing what you want, *show* it — with two, three, or more worked examples. The single example from the four-element framework is "one-shot"; adding several is "few-shot." More examples pin down the pattern more tightly: the model sees the shape of input-to-output you want and matches it. Use it when the task has a consistent format and one example leaves too much room to drift.

!!! example "Few-Shot in Action"
    **Task:** classify incoming reports by urgency.

    ```
    Report: "Routine resupply completed on schedule." -> Priority: LOW
    Report: "Comms link to outstation intermittent for 20 min." -> Priority: MEDIUM
    Report: "Unidentified vehicle breached the perimeter wire." -> Priority: HIGH

    Report: "Generator fuel at 15%, refuel not scheduled until tomorrow." -> Priority:
    ```

    Three examples teach the pattern far more reliably than the sentence "classify these by how urgent they are."

**Chain-of-thought.** Ask the model to show its reasoning before its answer: "Work through this step by step, then give your conclusion." Two payoffs. First, on multi-step problems the visible reasoning often improves the answer, because the model commits to intermediate steps instead of jumping to a guess. Second — and more important for you — the reasoning is now *auditable*. You can see where it went wrong instead of just accepting a bare answer. That makes chain-of-thought a verification aid, not just a quality aid.

!!! tip "Reasoning You Can Check Beats an Answer You Can't"
    A bare answer you cannot trace is a black box. "Show your work, then answer" turns the output into something you can inspect against the steps. For anything consequential, ask for the reasoning so you can supervise it.

**Decomposition.** When the ask is big, break it into an ordered sequence of smaller asks rather than demanding the whole thing at once. Either drive the steps yourself ("First, list the sections. Now draft section one. Now section two.") or tell the model to lay out a plan and proceed step by step with your approval. Decomposition keeps each step verifiable and keeps the model from collapsing a complex job into a shallow single pass.

**Structured output.** Tell the model the exact shape you want the answer in — a JSON object with named fields, a Markdown table with set columns, a numbered list, a fixed schema. This does two things: it makes the output predictable and easy to drop into a template or another tool, and it forces the model to fill specific slots, which surfaces gaps. If you ask for a table with a "Source" column, an empty cell tells you the model has no source — a gap a free-text paragraph would have hidden.

!!! example "Asking for Structured Output"
    "Return your answer as a Markdown table with exactly these columns: Claim, Source, Confidence (High/Med/Low). One row per claim. If you cannot identify a source for a claim, write 'NONE' — do not omit the row."

    The schema does the supervising for you: any "NONE" in the Source column is an unverified claim you now know to chase.

**System vs. user prompt.** The **system prompt** sets standing instructions — who the model is, the rules, the constraints — and is loaded by the platform before the conversation begins. The **user prompt** is each turn you type. The distinction: the system prompt is the standing order that persists for the whole session; the user prompt is the individual task. Typing "You are a [role]" in your message is persona injection — it works and you will see the behavioral effect, but it lives in the visible chat and is not the same as a true platform-level system prompt. This matters later in the course when you start configuring context files that act as durable standing orders for an agent.

!!! note "Standing Order vs. Task Order"
    System prompt = standing order for the whole mission. User prompt = the specific task you hand off right now. When you reach Module 4 (Standing Orders) and Module 10 (context files), you are writing durable standing orders in file form — the same idea, made persistent.

!!! warning "Still Not Tricks"
    Every technique here adds clarity the model would otherwise have to guess. Few-shot shows the pattern; chain-of-thought exposes the reasoning; decomposition orders the work; structured output fixes the shape; system-vs-user separates standing rules from the task at hand. If a "technique" you read about online does not add clarity, it is folklore — skip it.

??? note "Instructor Note — Keep Chain-of-Thought Tied to Verification"
    Students will treat chain-of-thought as a magic quality boost. Anchor it to supervision instead: the reason an operator asks for visible reasoning is to *check* it. That framing carries straight into the supervisor mindset in Module 7.

??? note "Instructor Note — Structured Output as a Gap Detector"
    The strongest selling point of structured output for this audience is not tidiness — it is that a named-field schema forces missing information into the open (an empty 'Source' cell, a 'NONE'). Demo that explicitly; it connects prompting to the verification reflex from Module 1.

### Hands-On

Build your five structured prompts as you go — one per technique. Keep them; they are your deliverable.

1. **Few-shot:** Pick a small classification or formatting task. Write a prompt with three worked examples, then a fourth unsolved item. Run it.
2. **Chain-of-thought:** Take a multi-step problem. Ask the model to show its reasoning step by step, then give the answer. Read the steps — could you catch an error in them?
3. **Decomposition:** Take one big ask you would normally dump in a single prompt. Break it into an ordered sequence of smaller prompts and run them in turn.
4. **Structured output:** Ask for an answer as a JSON object or a Markdown table with named columns, including one column the model may have to mark "NONE." See what gaps the schema exposes.
5. **System vs. user:** In one chat, set a standing instruction first ("For this whole session, you are a plain-language editor; never use jargon"), then send several task prompts. Notice the standing order persisting across turns.

!!! question "Before You Continue"
    For your own most common AI task, which intermediate technique would help most — and is the help about output *quality* or about your ability to *verify* the output?

<div class="quiz-block">
  <p class="quiz-question">Why is asking the model to "show its reasoning step by step" valuable to an operator who must defend the output?</p>
  <ul class="quiz-options">
    <li data-correct="false">It guarantees the answer is correct</li>
    <li data-correct="false">It makes the model run faster</li>
    <li data-correct="true">It makes the reasoning auditable, so you can inspect where it went wrong instead of accepting a bare answer</li>
    <li data-correct="false">It removes the need to verify the output</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-block">
  <p class="quiz-question">You ask for output as a table with a required "Source" column, and one cell comes back "NONE." What has the structured-output technique just done for you?</p>
  <ul class="quiz-options">
    <li data-correct="false">Broken the model — it should never return NONE</li>
    <li data-correct="true">Surfaced a gap: that claim has no source, which a free-text paragraph would have hidden</li>
    <li data-correct="false">Confirmed the entire answer is verified</li>
    <li data-correct="false">Forced you to switch to a more powerful model</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can use few-shot examples to pin down a pattern
- [ ] I can ask for chain-of-thought reasoning and use it to verify, not just to improve quality
- [ ] I can decompose a big ask into an ordered sequence of verifiable steps
- [ ] I can request structured output and use the schema to surface gaps
- [ ] I can explain the difference between a system prompt and a user prompt
- [ ] I have built five structured prompts, one per technique

---

## Summary

| Concept | Core Idea | Why It Matters |
|---|---|---|
| **Four Elements** | Role, Context, Example, Output Spec | A vague prompt is a vague order. Structure stops the model from guessing. |
| **Iterate, Don't One-Shot** | Read, tighten the next ask, repeat | The iterative habit beats hunting for one perfect prompt. |
| **Few-Shot** | Show several worked examples | Pins down a pattern one example leaves too loose. |
| **Chain-of-Thought** | "Show your reasoning, then answer" | Makes the reasoning auditable — a verification aid, not just quality. |
| **Decomposition** | Break a big ask into ordered steps | Keeps each step verifiable; prevents a shallow single pass. |
| **Structured Output** | Ask for JSON / table / schema | Predictable shape, and named fields surface missing information. |
| **System vs. User** | Standing order vs. the task at hand | Sets up context files as durable standing orders later in the course. |

## End of Module

You can now brief the machine like a mission order: clear, structured, and scrubbed — and you have five intermediate moves for when the task is harder than one order can carry. None of them is a trick; all of them are clarity. Next steps:

1. Keep your five structured prompts — they are your deliverable for this module.
2. Pick the one technique that helped most and make it a default habit on your real work.
3. Carry the chain-of-thought / structured-output instinct forward: both are how you set up the output to be verified (Module 1) and supervised (Module 7).
4. Note where you used a standing instruction — that is the seed of the context files you will write in Module 10.
