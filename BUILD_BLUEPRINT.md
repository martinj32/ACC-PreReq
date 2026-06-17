# ACC Course Restructure — Build Blueprint

Single source of truth for the restructure. Every execution agent follows this exactly.

## The new linear spine (one pass, each concept taught ONCE)

| # | Slug | Title | Markdown file | Slide script | Deck output |
|---|---|---|---|---|---|
| 0 | orientation | Mission Brief: How This Course Runs | docs/overview.md | (none — web only) | — |
| 1 | ai-foundations | Know Your Weapon: How AI Actually Works | docs/modules/01-ai-foundations.md | slides/build_01_ai_foundations.py | 01-ai-foundations.pptx |
| 2 | prompting | Briefing the Machine: Prompting as a Mission Order | docs/modules/02-prompting.md | slides/build_02_prompting.py | 02-prompting.pptx |
| 3 | grounding | Feeding the Machine: Grounding & Multimodality | docs/modules/03-grounding-multimodality.md | slides/build_03_grounding.py | 03-grounding.pptx |
| 4 | personalizing | Standing Orders: Making the AI Know You | docs/modules/04-personalizing.md | slides/build_04_personalizing.py | 04-personalizing.pptx |
| 5 | terminal | Know the Terrain: Filesystem & Terminal | docs/modules/05-terminal.md | slides/build_05_terminal.py | 05-terminal.pptx |
| 6 | version-control | The Duty Logbook: Version Control with Git | docs/modules/06-version-control.md | slides/build_06_version_control.py | 06-version-control.pptx |
| 7 | commanding-agent | From Advisor to Operator: Commanding an Agent | docs/modules/07-commanding-an-agent.md | slides/build_07_commanding_agent.py | 07-commanding-agent.pptx |
| 8 | tokens-cost | Ammunition Discipline: Tokens, Context & Cost | docs/modules/08-tokens-context-cost.md | slides/build_08_tokens_cost.py | 08-tokens-cost.pptx |
| 9 | ethics | Rules of Engagement: Ethics & Responsible AI Use | docs/modules/09-ethics.md | slides/build_09_ethics.py | 09-ethics.pptx |
| 10 | field-craft | Field Craft: Markdown, Code, Tools & Context Files | docs/modules/10-field-craft.md | slides/build_10_field_craft.py | 10-field-craft.pptx |
| 11 | capstone | The Proving Ground: Capstone Build | docs/modules/11-capstone.md | slides/build_11_capstone.py | 11-capstone.pptx |
| 12 | bridge | Crossing the LD: Bridge to Advanced Agentics | docs/modules/12-bridge-advanced.md | slides/build_12_bridge.py | 12-bridge.pptx |
| — | glossary | Glossary & Quick Reference | docs/modules/glossary.md | (none — web only) | — |

Audience: U.S. military / intelligence unit. KEEP the military framing (SITREP, OPORD, grid coordinates, duty logbook, "motivated junior/PFC"). Titles and analogies stay military.

## Source content → destination (migration map)

Source files (READ-ONLY during the build; do NOT edit or delete them — the orchestrator removes old files at the end):
- AIL = docs/bedrock/ai-literacy.md
- PER = docs/bedrock/personalizing-your-ai.md
- MACH = docs/terminal-basics/the-machine.md
- TERM = docs/terminal-basics/the-terminal.md
- AGE = docs/agentic-ai/agent-concepts.md
- MM = docs/mental-models/core-content.md
- SUM = docs/prereq-course/module-summary.md
- DESIGN = docs/prereq-course/course-design.md (full M1-M8 detail — read for hands-on specifics)

| Module | Pulls from | Net-new to write |
|---|---|---|
| 1 ai-foundations | AIL "What an LLM Is", "Tokens and Context" (intro only), "How LLMs Fail", "Data Handling"; MM §1.6 doctrinal/intel framing | NEW sections: Conversation Mechanics & Statelessness; Verifying AI Output (a method); When to Use AI (and When Not To); extend failure modes with Bias-Spotting (literacy, not policy) |
| 2 prompting | AIL "Prompt Engineering"; SUM/DESIGN M1 prompt exercises (5 structured prompts deliverable) | NEW: Intermediate Prompting — few-shot, chain-of-thought, decomposition, structured output, system-vs-user prompt |
| 3 grounding | (mostly new) seed from AIL knowledge-cutoff/"brain in a jar" | NEW MODULE: web search / file upload / retrieval (grounded vs generated output, how to tell); Multimodality (images, screenshots, PDFs, charts, voice) + input-specific failure modes |
| 4 personalizing | PER (both sections, near-unchanged) | Light edit: "what to keep out" becomes back-ref to Module 1 data-handling, not a re-teach |
| 5 terminal | MACH (all), TERM (all EXCEPT "Why Version Control Exists"); SUM/DESIGN M2 (6-exercise transcript) | None conceptual; consolidate. Drop TERM's VC page (moves to Module 6) |
| 6 version-control | The canonical "Why Version Control Exists" concept (use AGE's "duty logbook" framing; the TERM copy is a duplicate — collapse to one); SUM/DESIGN M3 (git hands-on, repo + 5 commits, .gitignore-before-first-commit OPSEC warning) | None conceptual |
| 7 commanding-agent | AGE "Chatbot vs Agent", "Supervisor Mindset"; MM §1 (harness), §4 (tool calls), §5 (operator posture), §7 (worked examples — intel/SITREP/grid; BEST assets, reuse as exercises), §8 (identify-the-models exercise) | Light stitching only. Use ONE clean harness + ONE clean operator treatment (merge the duplicates). Name "context files as the primary agent-steering lever" as a forward-pointer to Module 10 |
| 8 tokens-cost | MM §1.5 (model families/tiers), §2 (context operational depth), §3 (tokens as currency), §6 (cost-consciousness); AIL "How AI Is Delivered and Paid For" | NEW: model-selection decision heuristic (fast vs reasoning vs big-context). Write as a SPIRAL on Module 1 ("you know what a token IS — here's how to spend them"), never re-define a token |
| 9 ethics | Seeds: AIL Data Handling (connect, don't duplicate), AGE supervisor "you own the output", AIL "trained not programmed → inherited bias" | NEW MODULE — see Ethics spec below |
| 10 field-craft | SUM/DESIGN M4 (Markdown), M5 (Programming Concepts), M6 (Developer Tools), M7 (Context Files) | None conceptual; consolidate 4 clean modules into one phase. M7 back-references Module 4 (personalizing) and Module 8 (context mgmt) |
| 11 capstone | SUM/DESIGN M8 | NEW: capstone now REQUIRES an agentic deliverable — a CLAUDE.md that actually constrains a real agent run, one full delegate-verify-own loop, and a deliberate git rewind of a bad agent edit. Rubric grades the loop + data-handling discipline, not just the artifact |
| 12 bridge | (new) scaffold from Module 7 (engine-harness-operator) and Module 8 (cost) | NEW MODULE — see Bridge spec below |

DELETE-as-duplicate (orchestrator handles file removal; agents simply do not re-teach): MM §1.6 (dup of AIL failure modes — harvest intel examples only); AGE "Why Version Control Exists" (dup of TERM's); the "rename folder project→project-v1" hands-on (appears twice — keep ONE, in Module 7); MM §1/§2/§3 concept re-teaches that duplicate Bedrock.

## NEW MODULE SPEC — Module 9 Ethics (Rules of Engagement)

Distinct from OPSEC/data-handling (that is security — what flows IN; ethics is what you do with output and whether use is right/lawful/accountable). Sections, in order:
1. Accountability & Authorship: You Sign for It — capability does not transfer accountability; no "the model said so" defense. Hands-on: "sign" an AI-drafted analytic paragraph only after vouching for every claim; reveal a planted false claim.
2. Hallucination as an Ethical Failure — reframes Module 1's technical fact as authored harm in consequential products; duty to verify scales with stakes.
3. Over-Reliance, Automation Bias & Deskilling — judge first, consult second. Hands-on: form your own assessment, write it down, THEN see the AI's.
4. Bias & Fairness in AI-Assisted Analysis — spotting stereotype-matching vs evidence-based output. (Coordinates with Module 1 bias-spotting: Module 1 = "spot skewed output" literacy; Module 9 = the ethical duty.)
5. Disclosure & Attribution: Provenance of Your Product — when AI assistance must be disclosed; anchor to DoD public-affairs guidance (DoDI 5400.19). Default to traceability when no policy stated.
6. Dual-Use & Misuse Awareness — generation can fabricate deception/synthetic media; awareness + lawful-use boundary, not a how-to.
7. Privacy & Collection Ethics Beyond OPSEC — third-party/incidental data, consent, aggregation; "technically collectible" ≠ "ethically/lawfully appropriate."
8. DoD AI Ethical Principles & Lawful-Use Close — the five principles (Responsible, Equitable, Traceable, Reliable, Governable) mapped back to each section; "not legal advice — follow unit policy, ask chain/legal when unsure."

If trimmed, the 4 must-haves are sections 1, 2, 3, 8. Build all 8 (full build approved).
EXCLUDE: environmental/energy cost; alignment/existential-risk theory; academic ethics philosophy; specific statute walkthroughs; vendor-TOS comparisons.
Anchor frameworks (flag "verify currency before delivery" on each): DoD 5 AI Ethical Principles; DoD CDAO Responsible AI / generative-AI guardrails; DoDI 5400.19; NIST AI RMF (Govern/Map/Measure/Manage) as a light secondary reference.

## NEW MODULE SPEC — Module 12 Bridge to Advanced Agentics

Conceptual on-ramp to the ACC main course. Recognition depth, NOT build depth. Segments:
0. Recap the primitive (engine-harness-operator + delegate-verify-own).
1. Grounding / Retrieval — NAME the pattern students saw in Module 7 (RAG-by-hand): answers from retrieved real sources, cited/traceable. Grounded vs ungrounded.
2. Connecting Tools & MCP (Model Context Protocol) — "the harness is extensible"; MCP as the standard way to give an agent new tools/data; Tool vs Resource vs Prompt. Conceptual only; defer building servers. FLAG version-sensitivity.
3. Permissions & Guardrails — scoped read/write/execute, command allowlists, approval gates, sandboxes. The "how" behind the supervisor mindset.
4. Planning & Decomposition — agent produces a plan you approve before it acts; plan as a supervision artifact.
5. Workflow Patterns, Named (recognition) — prompt chaining, routing, orchestrator-workers, evaluator-optimizer. "You'll build these in the main course."
6. Sub-Agents / Multi-Agent (preview only) — one commander agent delegating to workers.
7. Evaluating an Agent (light) — judging whole output: spot-checks, regression, evaluator-optimizer idea.
Defer wholesale to main course: building MCP servers, implementing multi-agent orchestration, production eval harnesses, low-supervision autonomous agents.

## NEW SECTIONS for existing modules (condensed specs)

- M1 Verifying AI Output (method): cite-and-check, cross-source, re-run for consistency, second-tool check, lateral reading. Turns the mandated reflex into technique.
- M1 When to Use AI / When Not To: wrong-tool cases (precise math, real-time facts, authoritative citation, anything sensitive); a one-page decision checklist.
- M1 Conversation Mechanics & Statelessness: model re-reads the whole thread each turn; no cross-chat memory by default; edit vs continue vs new chat.
- M1 Bias-Spotting (extends failure modes): outputs can be skewed by training data; how to notice. Keep it literacy, route policy to M9.
- M2 Intermediate Prompting: few-shot (multiple examples), chain-of-thought ("show your reasoning"), decomposition (break a big ask into ordered steps), structured output (ask for JSON/table/schema), system vs user prompt. Frame as clarity-extending structure, not "tricks."
- M3 (whole module) Grounding: web search, file/document upload, connectors; how to tell grounded from generated; this is the practical fix for knowledge-cutoff + hallucination. Multimodality: images/screenshots, PDFs, charts, voice input; each mode's failure modes (misread tables, hallucinate from blurry text).
- M8 Model-selection heuristic: fast vs reasoning vs big-context; a simple decision rule a junior can apply.

## VERIFY-BEFORE-TEACHING flags (put these as `!!! warning` / `??? note` in the markdown AND a NOTE callout on the relevant slide)

- Model names, tiers, pricing, context-window sizes — change with releases; verify at the provider's docs before any course run.
- MCP details (governance, server counts, transport) — version-sensitive; verify before teaching.
- DoD AI policy specifics (the five principles, CDAO guidance, DoDI 5400.19, NIST AI RMF) — in active revision; verify currency before delivery; "not legal advice."

## MARKDOWN PAGE CONVENTIONS (match the existing house style exactly)

Each module markdown follows this structure (see docs/bedrock/ai-literacy.md as the reference exemplar):
- `# Title`
- Bold lead: **Who this is for:** / **What you will leave with:**
- `---`
- Per section: `## Section Name`, then `**BLUF.**` one-liner, `### Why This Matters`, `### Concepts`, MkDocs admonitions (`!!! note/tip/warning/example/danger/question`), instructor notes as `??? note "Instructor Note — ..."`, `### Hands-On` numbered steps, `!!! question "Before You Continue"`, an interactive quiz block (HTML below), `### Readiness Check` with `- [ ]` items.
- End with a `## Summary` table and an `## End of Module` note where the exemplar has one.

Interactive quiz block format (the site already wires javascripts/quiz.js + stylesheets/quiz.css):
```
<div class="quiz-block">
  <p class="quiz-question">Question text?</p>
  <ul class="quiz-options">
    <li data-correct="false">Wrong option</li>
    <li data-correct="true">Correct option</li>
    <li data-correct="false">Wrong option</li>
  </ul>
  <div class="quiz-feedback"></div>
</div>
```
Include at least one quiz block per major section, matching the density of the exemplar.

## SLIDE SCRIPT CONVENTIONS

- `from acc_theme import *` (the shared theme lives at slides/acc_theme.py — do NOT redefine palette/primitives).
- Build with the documented builders: new_deck, add_title_slide, add_overview_slide, add_section_header, add_concept_slide, add_example_slide, add_check_on_learning, add_hands_on, add_section_summary, add_summary_table, add_readiness_check, add_end_slide, save_deck.
- Deck flow mirrors the markdown: Title → Overview → for each section [Section Header → Concept(s) → Example (if any) → Check on Learning → Hands-On → Section Summary] → Module Summary Table → Readiness Check → End.
- Title-slide subtitle: "PREREQUISITE MODULE  |  SELF-PACED" (or "INSTRUCTOR-LED" / "2-3 DAY BLOCK" where appropriate).
- Image placeholders: keep them, military-flavored, format `"[IMAGE: <description>]"`.
- End every script with `if __name__ == "__main__": build()` and have build() call `save_deck(prs, __file__, "<NN-slug>.pptx")`.
- DO NOT RUN the script (python is blocked for you). The orchestrator runs all builds. Just write correct code.

## HARD RULES FOR ALL AGENTS

1. Stay in your assigned files only. Never edit another agent's module or the source files.
2. Do not delete anything. The orchestrator handles old-file cleanup and the nav.
3. Each concept is taught ONCE in its canonical home (see migration map). If your module touches a concept owned by another module, reference it in one line, do not re-teach it. The ONE deliberate exception: the "verify after acting" habit may spiral (intro in M5 terminal, reinforce in M7, grade in M11).
4. Preserve the military framing and the house markdown style. Match the depth/length of docs/bedrock/ai-literacy.md.
5. Put verify-before-teaching flags wherever model names/pricing/MCP/DoD-policy appear.
6. Keep markdown and slides in sync — same sections, same key points.
7. Do not run python, git, or mkdocs. Report what you wrote and any cross-module dependencies you noticed.
