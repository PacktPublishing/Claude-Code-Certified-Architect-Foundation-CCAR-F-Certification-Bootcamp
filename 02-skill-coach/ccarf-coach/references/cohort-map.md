# Cohort map

Every part of the 2-day cohort in the order it is taught: its time, what it covers (from the
chapter's own "What you will learn" slide), the task statements it serves, its slides and its
lab. Use it for recaps and to send a weak task back to the chapter that teaches it.

The cohort teaches nine chapters. Chapters A to D are the spines: they teach the current
product (the Messages API, MCP and the Agent SDK, Claude Code, Skills and plugins). Chapters E
to I are the exam chapters, one per exam domain: each names the spine slide that taught the
mechanism and goes straight to the decision the exam tests.

Slides: the instructor shares them as PDF, one file per chapter (for example
`Chapter E Agentic Architecture Patterns.pdf`) and one combined file per day. Ask the user
where they saved them before pointing to a path.

## Day 1: Agents, Tools and MCP

### Opening: the exam and how to pass it (Day 1)

- Time: 0:00 to 0:20 (20 min)

Covers:

- What a Claude architect decides, and what the exam rewards.
- The quick win: preventing an unverified refund, and why a programmatic gate beats a stronger prompt.
- Exam mechanics: format, scenarios, scaled scoring and domain weights.

### Day 1, Chapter A: The Messages API

- Time: 0:20 to 1:10 (50 min)
- Kind: spine chapter (how the product works)
- Exam chapters that build on it: E, F, H and I
- Slides: `Chapter A The Messages API.pdf`

Covers:

- One request, one response: Send a request with the Python SDK and read the typed blocks that come back.
- Tools & the agent loop: Define a tool, loop on the stop reason, or let the Tool Runner loop for you.
- Guardrails & server tools: Enforce rules in code before a tool runs, and know where each tool runs.
- Structured output & subagents: Get a validated object back, and delegate work to subagents your code calls.
- Tokens & cost: Count tokens before you send, and keep long loops affordable.
- Build it or reuse a harness?: Choose between a manual loop, the Tool Runner, the Agent SDK and Managed Agents.

### Day 1, Chapter B: MCP and the Agent SDK

- Time: 1:20 to 2:15 (55 min)
- Kind: spine chapter (how the product works)
- Exam chapters that build on it: E and F
- Slides: `Chapter B MCP and the Agent SDK.pdf`
- Lab: Lab 3, parts A and B, `01-labs/lab_03/`; or the quick-win gates, `01-labs/quickwin`

Covers:

- How MCP works: Hosts, clients and servers, the three primitives, and the two transports.
- Build an MCP server: Write a server in Python, ask the user with elicitation, and test it.
- Claude Agent SDK: Run the Claude Code harness with query() and configure it in code.
- Tools & MCP servers: Connect custom tools, local servers and remote servers.
- Permissions & hooks: Decide which tool calls run, and enforce rules before a tool runs.
- Subagents & sessions: Delegate to specialists, then resume or fork a session later.

### Day 1, Chapter E: Agentic Architecture Patterns

- Time: 2:25 to 3:20 (55 min)
- Kind: exam chapter for Domain 1
- Task statements: 1.1 to 1.7
- Builds on: Chapters A and B
- Slides: `Chapter E Agentic Architecture Patterns.pdf`
- Lab: Lab 2, `01-labs/lab_02/lab02.ipynb`

Covers:

- Agent architecture patterns: Six multi-agent patterns and the coordinator they all run on.
- Hooks & enforcement: Turn rules that must always hold into hooks, in the SDK and in Claude Code.
- Human handoff: Escalate with a record a person can act on without the transcript.
- Resume, fork or start fresh: Pick the session that still matches the code on disk.

### Day 1, Chapter F: Tool Design and MCP Patterns

- Time: 3:30 to 4:20 (50 min)
- Kind: exam chapter for Domain 2
- Task statements: 2.1 to 2.5
- Builds on: Chapters A and B
- Slides: `Chapter F Tool Design and MCP Patterns.pdf`
- Lab: Lab 1, part A, `01-labs/lab_01/lab01_part_a.ipynb`

Covers:

- Tools that get selected: Write descriptions that pick the right tool, and fix a tool that is picked wrongly.
- Errors an agent can recover from: Return errors that tell the agent whether to retry, fix the input or escalate.
- Who holds which tool: Give each agent only the tools its role needs, in the SDK and in Claude Code.
- MCP servers & built-in tools: Place each MCP server in the right scope and pick the right built-in tool.

### Scenario clinic: Customer Support and Multi-Agent Research (Day 1)

- Time: 4:20 to 4:50 (30 min)

Covers:

- Six exam-style items on the Customer Support and Multi-Agent Research scenarios, worked live.
- The items are in `clinic.html`. The coach never reproduces them.

### Day 1 close and homework (Day 1)

- Time: 4:50 to 5:00 (10 min)

Covers:

- The Day 1 decisions in one pass, and the homework set (`homework-day1.html`).

## Day 2: Claude Code, Prompting and Reliability

### Day 1 recap and homework review (Day 2)

- Time: 0:00 to 0:10 (10 min)

Covers:

- The Day 1 decisions again, and the homework items most people missed.

### Day 2, Chapter C: Claude Code

- Time: 0:10 to 1:00 (50 min)
- Kind: spine chapter (how the product works)
- Exam chapters that build on it: G
- Slides: `Chapter C Claude Code.pdf`

Covers:

- The config map: Find where every setting lives, and which file wins.
- What it knows: Write CLAUDE.md, imports and path rules: guidance Claude reads.
- What it may do: Set permission rules, modes and the sandbox.
- Which tools it reaches: Add MCP servers in the right scope, with secrets kept out of git.
- What always happens: Run hooks at fixed points, outside the model's control.
- Subagents & headless runs: Define specialists in files, and run Claude Code in CI.

### Day 2, Chapter D: Skills and Plugins

- Time: 1:00 to 1:25 (25 min)
- Kind: spine chapter (how the product works)
- Exam chapters that build on it: G
- Slides: `Chapter D Skills and Plugins.pdf`

Covers:

- Kinds of know-how: Choose between CLAUDE.md, a Skill, a hook and a plugin.
- Writing a Skill: Write a Skill that triggers, and know where it runs.
- Packaging a plugin: Ship Skills, subagents, hooks and MCP servers in one folder.
- Sharing & trust: Publish through a marketplace, and review a plugin before you install it.

### Day 2, Chapter G: Claude Code Workflow Patterns

- Time: 1:35 to 2:20 (45 min)
- Kind: exam chapter for Domain 3
- Task statements: 3.1 to 3.6
- Builds on: Chapters C and D
- Slides: `Chapter G Claude Code Workflow Patterns.pdf`
- Lab: Lab 4, `01-labs/lab_04/lab04_ci_review.ipynb`

Covers:

- Instructions Claude loads: Put each rule where it reaches the right people and loads at the right time.
- Skills & commands: Share procedures with the team, and fork verbose work into a subagent.
- Plan, then iterate: Plan a large change before editing, and steer each iteration with examples and tests.
- Claude Code in CI: Run a review without a person, with findings as JSON and the standards in CLAUDE.md.

### Day 2, Chapter H: Prompting and Structured Output Patterns

- Time: 2:20 to 3:10 (50 min)
- Kind: exam chapter for Domain 4
- Task statements: 4.1 to 4.6
- Builds on: Chapter A
- Slides: `Chapter H Prompting and Structured Output Patterns.pdf`
- Lab: Lab 5, `01-labs/lab_05/lab05_extraction.ipynb`

Covers:

- Criteria and examples: Write criteria that cut false positives, and add examples for what criteria cannot carry.
- Structured output: Get a record out of a document the exam's way and today's way, with honest fields.
- Validate and retry: Catch what a valid record still gets wrong, and retry only what a retry can fix.
- Scale and review: Run bulk work through batches, and have a different instance review the code.

### Day 2, Chapter I: Context and Reliability Patterns

- Time: 3:20 to 4:05 (45 min)
- Kind: exam chapter for Domain 5
- Task statements: 5.1 to 5.6
- Builds on: Chapter A
- Slides: `Chapter I Context and Reliability Patterns.pdf`
- Lab: Lab 6, parts A and B, `01-labs/lab_06/`

Covers:

- Context that stays exact: Keep amounts, dates and IDs exact, and put what matters where attention falls.
- Long sessions and large codebases: Explore without flooding the context, and keep findings when the history is summarised.
- Escalation and errors: Decide when to resolve, ask or escalate, and pass failures on with what was tried.
- Output you can trust: Measure accuracy where it fails, and keep sources and their conflicts visible.

### Simulated exam, worked together (Day 2)

- Time: 4:05 to 4:50 (45 min)

Covers:

- Four scenarios with four items each, mixed across the five domains as the exam weights them.
- The items are in `simulated-exam.html`. The coach never reproduces them.

### Your final week and exam day (Day 2)

- Time: 4:50 to 5:00 (10 min)

Covers:

- A plan for the final week: the practice exam, the weakest domain first, and exam-day logistics.

## Task statement to chapter

| Task | Chapter |
|---|---|
| 1.1 | Day 1, Chapter E (builds on Chapters A and B) |
| 1.2 | Day 1, Chapter E (builds on Chapters A and B) |
| 1.3 | Day 1, Chapter E (builds on Chapters A and B) |
| 1.4 | Day 1, Chapter E (builds on Chapters A and B) |
| 1.5 | Day 1, Chapter E (builds on Chapters A and B) |
| 1.6 | Day 1, Chapter E (builds on Chapters A and B) |
| 1.7 | Day 1, Chapter E (builds on Chapters A and B) |
| 2.1 | Day 1, Chapter F (builds on Chapters A and B) |
| 2.2 | Day 1, Chapter F (builds on Chapters A and B) |
| 2.3 | Day 1, Chapter F (builds on Chapters A and B) |
| 2.4 | Day 1, Chapter F (builds on Chapters A and B) |
| 2.5 | Day 1, Chapter F (builds on Chapters A and B) |
| 3.1 | Day 2, Chapter G (builds on Chapters C and D) |
| 3.2 | Day 2, Chapter G (builds on Chapters C and D) |
| 3.3 | Day 2, Chapter G (builds on Chapters C and D) |
| 3.4 | Day 2, Chapter G (builds on Chapters C and D) |
| 3.5 | Day 2, Chapter G (builds on Chapters C and D) |
| 3.6 | Day 2, Chapter G (builds on Chapters C and D) |
| 4.1 | Day 2, Chapter H (builds on Chapter A) |
| 4.2 | Day 2, Chapter H (builds on Chapter A) |
| 4.3 | Day 2, Chapter H (builds on Chapter A) |
| 4.4 | Day 2, Chapter H (builds on Chapter A) |
| 4.5 | Day 2, Chapter H (builds on Chapter A) |
| 4.6 | Day 2, Chapter H (builds on Chapter A) |
| 5.1 | Day 2, Chapter I (builds on Chapter A) |
| 5.2 | Day 2, Chapter I (builds on Chapter A) |
| 5.3 | Day 2, Chapter I (builds on Chapter A) |
| 5.4 | Day 2, Chapter I (builds on Chapter A) |
| 5.5 | Day 2, Chapter I (builds on Chapter A) |
| 5.6 | Day 2, Chapter I (builds on Chapter A) |
