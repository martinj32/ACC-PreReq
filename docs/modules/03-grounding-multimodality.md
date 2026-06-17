# Feeding the Machine: Grounding & Multimodality

**Who this is for:** Anyone who has internalized Module 1's "brain in a jar" — a model with no live access and a knowledge cutoff — and now needs to know how modern tools punch holes in that jar, and what new failure modes come with them.

**What you will leave with:** A clear model of what *grounding* is (web search, file upload, connectors), how to tell grounded output from generated output, and why this is the practical fix for the knowledge-cutoff and hallucination problems — plus how the model now takes in images, screenshots, PDFs, charts, and voice, and the failure mode each of those inputs brings.

---

## Grounding: Punching a Hole in the Jar

**BLUF.** A bare LLM is a brain in a jar with a knowledge cutoff and no live access — but grounding (web search, file upload, connectors) feeds it real, current, specific source material at request time, and that is the practical fix for both the knowledge-cutoff and hallucination problems you met in Module 1.

### Why This Matters

Module 1 gave you the correct baseline mental model: the LLM is an engine with no body, no memory between chats, and no live connection to the world. That model is still true of the *engine*. But the *tools wrapped around it* have changed, and if you keep treating every AI tool as a sealed jar, you will both miss what it can now do and — more dangerously — fail to check whether it actually did it. This section corrects and extends the mental model: the jar is still a jar, but grounding hands material in through a slot.

### Concepts

**Grounding means giving the model real source material to work from, at request time.** Instead of predicting from training data alone, a grounded model is handed actual text — a web page, your uploaded document, a record pulled from a connected system — and asked to answer *from that*. The prediction engine is unchanged; what changed is that you put real, specific, current information into its context window for this one request.

Three common grounding paths:

- **Web search.** The tool runs a live search, pulls back current pages, and the model answers from those results. This is the direct fix for the knowledge cutoff: the model is no longer limited to what it trained on.
- **File / document upload.** You attach a PDF, spreadsheet, or text file. The model reads it and answers from its actual contents instead of guessing what a document like that probably says.
- **Connectors.** The tool is wired into an external system — a document store, a wiki, a database, a drive — and can retrieve relevant records on demand. (Connecting tools and systems in depth, including the protocols that standardize it, is Module 12. Here, just know the category exists.)

**Why grounding fixes the two big problems.** Knowledge cutoff: web search and connectors bring in information from after the training date. Hallucination: when the model answers from a document actually in front of it, its claims can be traced back to a real source you can check — instead of being plausible completions from training. Grounding does not *guarantee* correctness, but it makes the output **traceable**, which is what makes verification possible.

!!! warning "Verify Before Teaching — Tool and Feature Specifics"
    Which tools have web search, how upload works, what connectors exist, and how each is enabled all change frequently as products update. Treat every specific feature claim in this module as a snapshot. Confirm the current behavior of the actual tool in front of you before relying on it or teaching it.

??? note "Instructor Note — Correct, Don't Contradict Module 1"
    Do not let students conclude Module 1 was wrong. The engine is still a brain in a jar — stateless, cutoff-bound, no native live access. Grounding is an external tool layer feeding the jar. Frame this as 'extend the model,' not 'replace it.' The distinction matters when they reach the harness in Module 7: grounding is a tool call, and tool calls are what make the jar useful.

### Hands-On

1. Ask your tool a question about something that clearly happened *after* its training cutoff. Note whether it refuses, guesses, or searches.
2. If it has web search, ask the same question again and require it to use search. Compare the two answers.
3. Upload a short document and ask a question whose answer is only in that document. Confirm the answer actually came from your file, not from general knowledge.
4. Ask: "Which parts of that answer came from the document, and which from your own knowledge?" See whether it can separate them.

!!! question "Before You Continue"
    Module 1 told you the model is a brain in a jar with no live access. You just watched it answer a question about a recent event. Did the engine change — or did something feed the jar? What is the difference, and why does it matter for trust?

<div class="quiz-block">
  <p class="quiz-question">What does "grounding" actually do to an LLM's behavior?</p>
  <ul class="quiz-options">
    <li data-correct="false">It retrains the model on new data in real time</li>
    <li data-correct="false">It removes the model's knowledge cutoff permanently</li>
    <li data-correct="true">It feeds real source material into the model's context at request time so it answers from that, not just from training</li>
    <li data-correct="false">It makes the model stop hallucinating entirely</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can explain grounding as feeding real source material into the model at request time
- [ ] I can name three grounding paths: web search, file upload, connectors
- [ ] I understand grounding is the practical fix for knowledge cutoff and hallucination
- [ ] I understand the engine is unchanged — grounding is an external tool layer feeding the jar

---

## Grounded vs. Generated: How to Tell the Difference

**BLUF.** A grounded answer and a generated answer look identical on the screen — confident either way — so before you trust an AI claim you have to confirm grounding actually happened and trace the claim to its source, because the tool will not always make that obvious.

### Why This Matters

Grounding only helps if it actually ran. Module 1 warned you that a model with stale data and a model that searched the web produce answers that look the same. The same trap applies here: a tool *capable* of grounding does not always *use* it, and an answer that reads like it came from your document may be half document, half training-data guess. The skill is telling the two apart.

### Concepts

**Confirm the grounding fired.** Capability is not the same as use. A tool with web search may answer a particular question straight from training without searching at all. Look for the signal that grounding happened: a search step, cited sources, a "based on the file you uploaded" reference, retrieved snippets. No signal means assume it answered from training until you check.

**Trace claims to sources.** When a tool cites sources or quotes a document, the value is that you can *follow* it. A grounded answer should let you ask "where did this specific claim come from?" and get a pointer you can verify. If a claim cannot be traced to the provided source, treat it as generated — the model may have blended in training-data filler.

**Watch for the mixed answer.** The most dangerous case is partial grounding: some of the answer is faithfully drawn from your source, and some is plausible completion bolted on. Because the tone is uniform, the seam is invisible. This is why "which parts came from the source?" is a question worth asking the model directly — and why a structured-output prompt (Module 2) that demands a source for every claim is so useful here.

!!! tip "Make It Cite, Then Check the Citation"
    Ask the tool to answer only from the provided sources and to mark any claim it cannot support. Then actually open a citation and confirm it says what the model says it says. A cited source the model invented or misread is still a hallucination — citation is a starting point for verification, not a substitute for it.

!!! danger "A Citation Is Not Proof"
    Grounding can still go wrong: the tool can retrieve the wrong document, quote a real source inaccurately, or cite a page that does not support the claim. Trace-ability lowers risk; it does not remove the operator. You still own the output. (The verification techniques from Module 1 — cite-and-check, cross-source, second-tool — are exactly the drills you run here.)

??? note "Instructor Note — This Is the Module 1 Reflex, Applied"
    Students may think grounding lets them stop verifying. It does the opposite: it gives them something checkable to verify against. Tie this section explicitly back to the five verification techniques from Module 1. Grounding makes those drills *possible*; it does not make them optional.

### Hands-On

1. Ask a grounded question and look for the signal that grounding fired (search step, citations, file reference). Is it there?
2. Pick one specific claim in the answer and ask the tool: "What is your source for that exact claim?"
3. Open that source and confirm it actually supports the claim. Did it?
4. Find one claim in the answer you *cannot* trace to a provided source. Treat it as generated — would you have caught it without checking?

!!! question "Before You Continue"
    Your tool gives you a confident, well-written answer with no visible sources, even though it has web search available. What is your safest assumption about where that answer came from — and what do you do next?

<div class="quiz-block">
  <p class="quiz-question">A tool that has web search gives you a confident answer with no citations and no visible search step. What should you assume?</p>
  <ul class="quiz-options">
    <li data-correct="false">It must have searched, because it has the capability</li>
    <li data-correct="true">Assume it answered from training data until you confirm grounding actually fired</li>
    <li data-correct="false">The answer is verified because it sounds confident</li>
    <li data-correct="false">Citations are unnecessary when a tool has search enabled</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I confirm grounding actually fired before trusting a "grounded" answer
- [ ] I can trace a grounded claim to its source and verify the source supports it
- [ ] I know the mixed answer (part grounded, part generated) is the dangerous case
- [ ] I treat a citation as a starting point for verification, not as proof

---

## Multimodality: More Ways In, More Ways to Misread

**BLUF.** Modern tools take input as images, screenshots, PDFs, charts, and voice — not just typed text — which is powerful for real work, but each input mode carries its own failure mode, and a model that misreads a blurry table or a noisy recording will do it with the same confidence as everything else.

### Why This Matters

You will not always have clean text to paste. You will have a photo of a whiteboard, a screenshot of an error, a scanned PDF, a chart in a slide, or a question you would rather speak than type. Multimodality lets the model take those directly. But every new input channel is a new place for the model to go confidently wrong — and the failures here are easy to miss because you assume "it can see the image, so it read it correctly." It often did not.

### Concepts

**The input modes you will actually use:**

- **Images and screenshots.** Photos of documents, whiteboards, equipment, or a screen; screenshots of errors or interfaces. The model describes, extracts text from, or reasons about the picture.
- **PDFs and documents.** Multi-page files read directly, including scanned ones. (This overlaps with file-upload grounding — a PDF is both a grounding source and a visual input.)
- **Charts and tables in images.** Graphs, data tables, diagrams embedded in a picture rather than as clean data.
- **Voice input.** You speak; the tool transcribes to text, then the model answers from the transcript.

**Each mode has its own failure mode — know them before you rely on them:**

- **Blurry or low-quality images:** the model fills in unreadable text with plausible guesses. A smudged digit becomes a confident wrong number.
- **Tables and charts:** the model misreads which value sits in which cell, swaps rows and columns, or misjudges a value from a graph's axis. Tabular structure is exactly where it slips.
- **Dense or handwritten documents:** transcription errors and skipped lines; the model may silently drop content it could not parse.
- **Voice:** the transcription step can mishear words — especially names, jargon, callsigns, and numbers — and the model then answers a subtly different question than the one you asked.
- **Across all modes:** the model rarely says "I couldn't read this." It produces a confident answer over an input it only partially understood.

!!! warning "Misreads Inherit the Confident Tone"
    A model that misread a chart axis or transcribed a number wrong does not flag it. The wrong value comes out with the same fluent confidence as a correct one — the Module 1 confident-wrong failure mode, now riding in on a new input channel. Always sanity-check extracted numbers, names, and table values against the original.

!!! danger "OPSEC Crosses Modes — The Module 1 Rule Still Holds"
    A screenshot, a photo of a document, or a scanned PDF can carry exactly the sensitive content you would never paste as text — names, grids, unit designations, markings, faces. Uploading an image is a disclosure decision, identical to pasting text. Everything in Module 1's data-handling rule applies to every image, PDF, and voice clip you feed an unauthorized tool.

!!! tip "Verify the Read Before You Trust the Reasoning"
    When the model extracts data from an image or chart, separate two questions: did it read the input correctly, and did it reason correctly from what it read? Check the read first. Good reasoning over a misread table is still wrong.

??? note "Instructor Note — Demo a Misread Live"
    Hand the model a slightly blurry table or a chart and ask it to read specific cells/values. It will usually get at least one wrong with full confidence. Doing this once makes 'verify the read' stick far better than asserting it. Use a fabricated, non-sensitive image.

### Hands-On

1. Screenshot a small table (fabricated, non-sensitive) and ask the model to read specific cells back to you. Check every value against the original.
2. Give it a chart image and ask for a specific value off the graph. Was it right, or confidently close-but-wrong?
3. If your tool supports voice, speak a sentence containing a name, a callsign, and a number. Check the transcription for errors before judging the answer.
4. Upload a multi-page PDF and ask about content on a later page. Confirm it actually read that far rather than guessing.
5. For each test, ask yourself: did the model flag any uncertainty about what it read? (It probably did not.)

!!! question "Before You Continue"
    You upload a screenshot of a data table and the model gives you a clean analysis. Two different things could be wrong: how it *read* the table, and how it *reasoned* from it. Which do you check first, and why?

<div class="quiz-block">
  <p class="quiz-question">You give the model a photo of a slightly blurry data table and it returns specific numbers with full confidence. What is the right posture?</p>
  <ul class="quiz-options">
    <li data-correct="false">Trust the numbers — the model can see the image clearly</li>
    <li data-correct="false">Assume it flagged anything it could not read</li>
    <li data-correct="true">Verify the extracted values against the original; misreads come out with the same confident tone as correct reads</li>
    <li data-correct="false">Re-upload the image until the answer changes</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-block">
  <p class="quiz-question">You want to ask about a document marked with a unit designation and a grid coordinate. Does uploading it as a screenshot instead of pasting the text change the data-handling rule?</p>
  <ul class="quiz-options">
    <li data-correct="false">Yes — an image is not text, so the rule does not apply</li>
    <li data-correct="true">No — uploading the image is a disclosure decision identical to pasting the text; the Module 1 rule still holds</li>
    <li data-correct="false">Yes — the model cannot extract sensitive details from images</li>
    <li data-correct="false">No, but only if you blur part of the image first</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>

### Readiness Check

- [ ] I can name the input modes: images/screenshots, PDFs, charts/tables, voice
- [ ] I can name the characteristic failure mode of each input mode
- [ ] I check the model's *read* of an input separately from its *reasoning*
- [ ] I apply the Module 1 data-handling rule to images, PDFs, and voice — not just typed text

---

## Summary

| Concept | Core Idea | Why It Matters |
|---|---|---|
| **Grounding** | Feed real source material into context at request time | The practical fix for knowledge cutoff and hallucination — output becomes traceable. |
| **Three Paths** | Web search, file upload, connectors | Three ways to hand the jar real, current, specific information. |
| **Grounded vs. Generated** | Confirm grounding fired; trace claims to sources | Capability is not use. The mixed answer (part grounded, part generated) is the dangerous case. |
| **A Citation Is Not Proof** | Trace-ability lowers risk, does not remove the operator | Run the Module 1 verification drills against the cited source. |
| **Multimodality** | Images, screenshots, PDFs, charts, voice as input | More ways in for real work — and more ways to misread. |
| **Per-Mode Failures** | Blurry text, swapped cells, misheard names/numbers | Misreads inherit the confident tone. Verify the read before the reasoning. |
| **OPSEC Crosses Modes** | An image/PDF/voice clip is a disclosure decision | The Module 1 data-handling rule applies to every input channel. |

## End of Module

You have corrected the "sealed jar" picture without throwing it away: the engine is still a brain in a jar, but grounding feeds it real source material and multimodality opens new slots to feed through. Both make the tool dramatically more useful for real work — and both add new places to go confidently wrong. Next steps:

1. On your next real task, deliberately ground the model (search or upload) and trace one claim back to its source.
2. Run a "verify the read" check on an image or chart before trusting any number it extracts.
3. Carry the grounding idea forward: in Module 7 you will see it as a tool call, and in Module 12 it gets a name — retrieval — alongside the connectors that standardize it.
4. Apply your Module 1 bright line to images, PDFs, and voice, not just text. The disclosure decision is the same.
