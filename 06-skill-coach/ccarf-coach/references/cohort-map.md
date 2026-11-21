# Cohort map

Every session of the 2-day cohort: its time, the points it covers (from the published
running order), the task statements it serves, and its lab. Use it for session recaps
and to send a weak task back to the session that teaches it.

## Day 1: Agents, Tools & MCP

### Day 1, session 1: The exam and how to pass it

- Time: 0:00 to 0:20 (20 min)
- Task statements: exam overview
- Slides: `01-slides/Day 1 Agents Tools and MCP.html`, the section that opens with this session's title

Covers:

- What a Claude architect decides, and what the exam rewards
- Quick win: preventing an unverified refund, and why a programmatic gate beats a stronger prompt
- Exam mechanics: format, scenarios, scaled scoring and domain weights

### Day 1, session 2: Tools that get selected

- Time: 0:20 to 1:05 (45 min)
- Task statements: 1.1, 2.1, 2.3, 2.5
- Slides: `01-slides/Day 1 Agents Tools and MCP.html`, the section that opens with this session's title

Covers:

- The tool definition: name, description and input schema
- The API is stateless: your code sends every `tool_use` and `tool_result` back in the
  messages array
- The tool-use loop: continue on `stop_reason: "tool_use"`, stop on `"end_turn"`, and return
  each `tool_result` with its `tool_use_id`
- Descriptions as the selection mechanism, diagnosing misrouting, and system-prompt keywords
  that override a good description
- Rename, split or consolidate: choosing the fix from the failure
- `tool_choice`: `auto`, `any` and forcing a named tool for the first call, then letting later
  turns choose; and why forcing a tool does not replace a gate
- Built-in tools: Grep versus Glob, Read and Write versus Edit, and Grep for entry points,
  then Read to trace imports through wrapper modules

### Day 1, session 3: Model Context Protocol in practice

- Time: 1:15 to 2:00 (45 min)
- Task statements: 2.2, 2.4
- Slides: `01-slides/Day 1 Agents Tools and MCP.html`, the section that opens with this session's title
- Lab: Lab 1, part A, `03-labs/lab_01/lab01_part_a.ipynb`

Covers:

- What MCP solves: clients, servers and hosts, with the tools of every configured server
  available at once
- Tools, resources and prompts, who controls each, and resources as content catalogues that
  save exploratory tool calls
- Structured error responses: `isError`, `errorCategory` and `isRetryable` across transient,
  validation, business and permission failures, and why a generic "Operation failed" blocks
  recovery
- Empty success versus a failure: never report a timeout as "no records found"
- Project versus personal servers: `.mcp.json`, `~/.claude.json` and environment variables
- Community servers versus custom ones, and MCP tool descriptions good enough that Claude
  stops reaching for Grep
- Demo: an MCP server with structured errors, used from Claude Code (Lab 1)

### Day 1, session 4: The agentic loop and the Agent SDK

- Time: 2:00 to 2:45 (45 min)
- Task statements: 1.1, 2.3
- Slides: `01-slides/Day 1 Agents Tools and MCP.html`, the section that opens with this session's title

Covers:

- The loop as a library: options, the message stream and how a run ends
- Model-driven decisions versus pre-configured decision trees
- Loop anti-patterns: parsing the reply text, checking for assistant text, or treating an
  iteration cap as the stopping rule; caps are safety nets, not control flow
- Built-in and custom tools, and `allowedTools` (`allowed_tools` in Python): it approves
  tools, it does not restrict them; real limits are `AgentDefinition.tools` and
  `disallowed_tools`
- Giving each agent only the tools its role needs: why 4 or 5 tools select better than 18,
  and permission modes
- The scoped cross-role tool: a narrow `verify_fact` instead of full search access, and a
  validated `load_document` instead of a general `fetch_url`

### Day 1, session 5: Multi-agent orchestration

- Time: 2:55 to 3:40 (45 min)
- Task statements: 1.2, 1.3, 5.3
- Slides: `01-slides/Day 1 Agents Tools and MCP.html`, the section that opens with this session's title
- Lab: Lab 2, `03-labs/lab_02/lab02.ipynb`

Covers:

- Coordinator and subagents: hub-and-spoke and why it is observable
- Defining subagents with `AgentDefinition` (description, prompt, tools, model) and the `Task`
  tool, which `allowedTools` must include (renamed `Agent` in current releases; the exam
  says `Task`)
- Subagents do not inherit the coordinator's conversation: passing findings explicitly, as
  claim-source mappings
- Parallel subagents: several spawns in one response
- Partitioning scope so that subagents do not duplicate each other's work
- Goal-based delegation, dynamic routing and the over-narrow decomposition trap
- The iterative refinement loop: the coordinator checks coverage and re-delegates the gaps
- Recover locally, then report what remains to the coordinator
- Demo: a research agent spawning four channel-partitioned searchers in one response, then
  chaining their findings into a formatter (Lab 2)

### Day 1, session 6: Enforcement, handoff, decomposition & sessions

- Time: 3:40 to 4:25 (45 min)
- Task statements: 1.4, 1.5, 1.6, 1.7
- Slides: `01-slides/Day 1 Agents Tools and MCP.html`, the section that opens with this session's title
- Lab: Lab 3, parts A and B, `03-labs/lab_03/`

Covers:

- Prompts are probabilistic, hooks are code
- `PostToolUse` for normalising data, `PreToolUse` for policy and prerequisite gates,
  including denying a refund over $500 and redirecting it to `escalate_to_human`
- Structured handoff to a human who has no transcript: customer ID, root cause, amount and
  recommended action
- One customer request, several concerns: parallel investigation and shared case facts
- Fixed pipelines (prompt chaining) versus adaptive decomposition, and per-file passes plus a
  cross-file integration pass
- Sessions: `--resume <session-name>`, `fork_session` from a shared baseline, or a fresh
  session with a structured summary when old tool results are stale; and telling a resumed
  session which files changed
- Demo: an identity gate that blocks a refund until verification (Lab 3)

### Day 1, session 7: Scenario clinic

- Time: 4:25 to 4:55 (30 min)
- Task statements: Domains 1 and 2
- Slides: `01-slides/Day 1 Agents Tools and MCP.html`, the section that opens with this session's title

Covers:

- Exam-style items in two official scenario settings, answered live and taken apart
- Why each distractor is attractive, and the evidence in the stem that rules it out

## Day 2: Claude Code, Prompting & Reliability

### Day 2, session 1: Day 1 recap and homework review

- Time: 0:00 to 0:10 (10 min)
- Task statements: exam overview
- Slides: `01-slides/Day 2 Claude Code Prompting and Reliability.html`, the section that opens with this session's title

Covers:

- The items the cohort found hardest, and the decision behind each

### Day 2, session 2: Configuring Claude Code for a team

- Time: 0:10 to 0:50 (40 min)
- Task statements: 3.1, 3.2, 3.3
- Slides: `01-slides/Day 2 Claude Code Prompting and Reliability.html`, the section that opens with this session's title

Covers:

- The CLAUDE.md hierarchy: user, project and subdirectory, and diagnosing with `/memory`
- Writing rules Claude follows: specific, checkable and lean
- Modular organisation: `@path` imports and `.claude/rules/`
- Path-specific rules with `paths:` globs, and why a glob such as `**/*.test.tsx` beats
  subdirectory CLAUDE.md files for conventions spread across folders
- Custom slash commands and skills: `.claude/commands/` for the team versus
  `~/.claude/commands/` for you, personal variants under a different name, and `SKILL.md`
  frontmatter (`allowed-tools`, `argument-hint`, `context: fork`)
- Which surface owns which rule: CLAUDE.md, skill or hook

### Day 2, session 3: Working modes and CI/CD

- Time: 0:50 to 1:35 (45 min)
- Task statements: 3.4, 3.5, 3.6
- Slides: `01-slides/Day 2 Claude Code Prompting and Reliability.html`, the section that opens with this session's title
- Lab: Lab 4, `03-labs/lab_04/lab04_ci_review.ipynb`

Covers:

- Plan mode versus direct execution, plan then execute, and Explore for verbose discovery
- Permission modes, and which belongs in CI
- Iterative refinement: worked examples, tests first and the interview pattern; interacting
  issues in one message, independent ones one at a time
- Headless mode: `-p`, `--output-format json` and `--json-schema`; read `structured_output`
  rather than trusting the exit code
- CLAUDE.md as CI context: review criteria, standards and test fixtures
- Code review in CI with `anthropics/claude-code-action`; on a rerun, pass the prior findings
  in and report only new or still-unaddressed issues
- An independent reviewer: why the session that wrote the code reviews it worse
- Generating useful tests rather than duplicates
- Demo: Claude Code reviewing a pull request against explicit criteria (Lab 4)

### Day 2, session 4: Prompt precision and few-shot

- Time: 1:45 to 2:10 (25 min)
- Task statements: 4.1, 4.2
- Slides: `01-slides/Day 2 Claude Code Prompting and Reliability.html`, the section that opens with this session's title

Covers:

- Explicit criteria over "flag any issues" or "be conservative"
- Reducing false positives: temporarily disabling a noisy category, anchoring each severity
  level to a code example, and why noisy categories erode trust in accurate ones
- Few-shot examples for ambiguous decisions and consistent format
- Few-shot extraction across document layouts, and what examples cannot supply

### Day 2, session 5: Structured output, validation & scale

- Time: 2:10 to 3:00 (50 min)
- Task statements: 4.3, 4.4, 4.5, 4.6
- Slides: `01-slides/Day 2 Claude Code Prompting and Reliability.html`, the section that opens with this session's title
- Lab: Lab 5, `03-labs/lab_05/lab05_extraction.ipynb`

Covers:

- Structured outputs (`output_config.format`, `messages.parse` with Pydantic) and tool use
  with a JSON schema, versus "please return JSON": when each fits, and why the exam's "most
  reliable" means tool use
- `tool_choice: "any"` when the document type is unknown, and forcing `extract_metadata`
  before enrichment
- Schema design for real documents: nullable fields, `enum` with "other", and "unclear"
- Schema-valid is not correct: `calculated_total` against `stated_total`, and
  `conflict_detected`
- Validation, retry and feedback loops: a repair request carries the document, the failed
  output and the errors; when a retry is futile; `detected_pattern` for dismissed findings
- Confidence that means something: calibrated, per field, routed to review
- The Message Batches API: 50% cost, up to 24 hours with no latency SLA, `custom_id`, and no
  multi-turn tool use inside a request; resubmitting only the failed ids, refining the prompt
  on a sample first, and setting the submission cadence from the SLA
- Multi-pass and multi-instance review: per-file passes plus a cross-file integration pass,
  and why an independent instance finds more
- Demo: forced tool-schema extraction from three short supplier documents: null for an
  unprinted field, `unclear` and `other` (Lab 5)

### Day 2, session 6: Context and reliability

- Time: 3:10 to 4:05 (55 min)
- Task statements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6
- Slides: `01-slides/Day 2 Claude Code Prompting and Reliability.html`, the section that opens with this session's title
- Lab: Lab 6, parts A and B, `03-labs/lab_06/`

Covers:

- Context as a budget: what summaries lose, and the persistent case-facts block
- Lost in the middle: key findings first and explicit section headers; trimming tool output
  and directing compaction
- Large codebase exploration: map first, delegate questions to subagents, keep a findings
  scratchpad and run `/compact` along the way
- Crash recovery with structured agent state
- Escalation triggers: honour an explicit request for a human at once; sentiment and
  self-rated confidence are poor proxies; ask for another identifier when a lookup returns
  several matches
- Error propagation across agents: partial results and coverage gaps
- Human review: a 97% aggregate can hide a failing document type; validating by type and
  field, stratified sampling of high-confidence extractions, and calibration
- Provenance and conflicting sources: established, contested and gaps; publication versus
  collection dates; rendering each content type in its natural format
- Demo: compaction, resume and fork in a real project (Lab 6)

### Day 2, session 7: Simulated exam, worked together

- Time: 4:05 to 4:50 (45 min)
- Task statements: all five domains
- Slides: `01-slides/Day 2 Claude Code Prompting and Reliability.html`, the section that opens with this session's title

Covers:

- A simulated exam case: 4 scenarios with 4 items each, the same structure as the real exam
- Unlike Day 1's clinic, every domain is mixed, weighted as the exam weights them
- Each scenario's 4 items answered together in 5 minutes, then analysed together: why the
  right answer wins and why each other option fails
- Single-answer and multiple-response items, all original and written against the official
  objectives

### Day 2, session 8: Your final week and exam day

- Time: 4:50 to 5:00 (10 min)
- Task statements: exam overview
- Slides: `01-slides/Day 2 Claude Code Prompting and Reliability.html`, the section that opens with this session's title

Covers:

- Your take-home full-length practice exam, and how to read your weak domains from it
- Registration, booking and exam-day rules

---

## Task statement to session

| Task | Session |
|---|---|
| 1.1 | Day 1, session 4 |
| 1.2 | Day 1, session 5 |
| 1.3 | Day 1, session 5 |
| 1.4 | Day 1, session 6 |
| 1.5 | Day 1, session 6 |
| 1.6 | Day 1, session 6 |
| 1.7 | Day 1, session 6 |
| 2.1 | Day 1, session 2 |
| 2.2 | Day 1, session 3 |
| 2.3 | Day 1, sessions 2 and 4 |
| 2.4 | Day 1, session 3 |
| 2.5 | Day 1, session 2 |
| 3.1 | Day 2, session 2 |
| 3.2 | Day 2, session 2 |
| 3.3 | Day 2, session 2 |
| 3.4 | Day 2, session 3 |
| 3.5 | Day 2, session 3 |
| 3.6 | Day 2, session 3 |
| 4.1 | Day 2, session 4 |
| 4.2 | Day 2, session 4 |
| 4.3 | Day 2, session 5 |
| 4.4 | Day 2, session 5 |
| 4.5 | Day 2, session 5 |
| 4.6 | Day 2, session 5 |
| 5.1 | Day 2, session 6 |
| 5.2 | Day 2, session 6 |
| 5.3 | Day 2, session 6 |
| 5.4 | Day 2, session 6 |
| 5.5 | Day 2, session 6 |
| 5.6 | Day 2, session 6 |
