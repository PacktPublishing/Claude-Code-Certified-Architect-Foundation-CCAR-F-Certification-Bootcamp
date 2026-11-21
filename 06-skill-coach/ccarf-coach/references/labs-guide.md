# Labs guide

The cohort's code lives in `03-labs/`. One environment covers the six labs
(`cd 03-labs && uv sync && uv run jupyter lab`); the quick win is its own small project in
`03-labs/quickwin/` (`cd 03-labs/quickwin && uv sync`). Credentials: a Claude subscription
login (`claude` once) or `ANTHROPIC_API_KEY` in `.env`; Lab 5 needs a key.

## Which lab goes with which chapter

| Chapter | Lab | Folder | Needs |
|---|---|---|---|
| Day 1, opening: the exam and how to pass it | Prompt vs. hook on a refund | `quickwin/` | `gates` needs nothing |
| Day 1, Chapter B: MCP and the Agent SDK | Identity gate before a refund | `lab_03/`, `quickwin/` | nothing for part A |
| Day 1, Chapter E: Agentic Architecture Patterns | Four searchers in one response | `lab_02/` | subscription or key |
| Day 1, Chapter F: Tool Design and MCP Patterns | MCP server with structured errors | `lab_01/` | nothing for part A |
| Day 2, Chapter G: Claude Code Workflow Patterns | Claude Code reviewing a pull request | `lab_04/` | a GitHub account |
| Day 2, Chapter H: Prompting and Structured Output Patterns | Forced tool-schema extraction | `lab_05/` | an API key |
| Day 2, Chapter I: Context and Reliability Patterns | Compaction, resume and fork | `lab_06/` | Claude Code signed in |

The agent, tool and hook built from zero (`quickwin/steps/`) go with Day 1, Chapters A and B.

## The six labs

### Lab 1, part A: an MCP server with structured errors

- Where: `03-labs/lab_01/lab01_part_a.ipynb`
- Run: `cd 03-labs && uv run jupyter lab`; `claude    # then /mcp`
- Watch: The server is a few decorated functions; the SDK writes the schema.
- Watch: A failure comes back with isError, a category and isRetryable.
- Watch: An empty result and an unreachable backend look different to Claude.
- Watch: Registered in .mcp.json, the tools show up in Claude Code's /mcp list.

### Lab 2: four searchers in one response

- Where: `03-labs/lab_02/lab02.ipynb`
- Run: `cd 03-labs && uv run jupyter lab`
- Watch: The coordinator emits four Task calls in a single response.
- Watch: Each searcher owns one channel, so nothing is searched twice.
- Watch: Findings come back as claim and source records, not prose.
- Watch: The formatter is chained after, and sees only what it is passed.

### Lab 3, parts A and B: an identity gate before a refund

- Where: `03-labs/lab_03/`
- Run: `cd 03-labs && uv run jupyter lab`; `cd 03-labs/quickwin && uv run demo_sdk/run.py gates`
- Watch: Hooks off: the prompt states the rule and the agent still refunds.
- Watch: Hooks on: PreToolUse denies the refund until get_customer has run.
- Watch: The denial names the next call, so the agent recovers in order.
- Watch: Over the limit, the handoff carries ID, root cause, amount and action.

### Lab 4: Claude Code reviewing a pull request

- Where: `03-labs/lab_04/lab04_ci_review.ipynb`
- Run: `gh repo view --web    # your copy of the tictactoe template`
- Watch: The review criteria live in CLAUDE.md, where the CI run reads them.
- Watch: The action posts findings as inline comments on the changed lines.
- Watch: A rerun is told the prior findings and reports only new or open ones.

### Lab 5: forced tool-schema extraction

- Where: `03-labs/lab_05/lab05_extraction.ipynb`
- Run: `cd 03-labs && uv run jupyter lab`
- Watch: tool_choice forces the extraction tool: the reply is the record.
- Watch: A field the document does not print comes back null, not invented.
- Watch: An enum with other and unclear keeps odd cases honest.

### Lab 6, parts A and B: compaction, resume and fork

- Where: `03-labs/lab_06/`
- Run: `cd 03-labs/lab_06/workspace/mycorp && claude`; `claude --resume <session-name>`
- Watch: Map the project first, then delegate questions to subagents.
- Watch: Findings go to a scratchpad file that survives /compact.
- Watch: --resume picks up a named session; a fork keeps the baseline clean.

## The quick win, step by step

The quick win builds a customer support agent from nothing, shows a rule written in the prompt
failing, then enforces it in code. Run every command from `03-labs/quickwin` unless a step says
otherwise. For each step: the command, what to watch, and what it shows for the exam.

### Before you start

- `uv sync` installs everything (Python 3.10 or later).
- Sign in: run `claude` once and log in to use your Claude subscription, or copy
  `.env.example` to `.env` and set `ANTHROPIC_API_KEY`. A key in `.env` wins over a login.
- `uv run demo_sdk/run.py gates` needs no model and costs nothing. Every other run calls
  Claude; each costs a few cents on a key.

### Part 1: the Agent SDK from zero

**Step 1.** `uv run steps/01_simple_agent.py`
- Watch: a plain answer, no tools.
- Shows: `ClaudeAgentOptions` is the agent's definition; `query()` runs one task; the SDK
  runs the loop and streams messages back, and the script prints the final result.

**Step 2.** `uv run steps/02_add_a_tool.py`
- Watch: Claude answers with the customer id it looked up.
- Shows: `@tool` (name, description, schema, handler), an in-process MCP server from
  `create_sdk_mcp_server`, and `allowed_tools` so the call runs without a permission prompt.
  Claude sees the tool as `mcp__support__get_customer`: hooks match on that name.

**Step 3.** `uv run steps/03_add_a_hook.py`
- Watch: the `PreToolUse` line (the arguments Claude chose) prints before the
  `PostToolUse` line (what the tool returned).
- Shows: `PreToolUse` runs before the call, `PostToolUse` after it and before Claude reads
  the result. Returning `{}` means "no objection".

### Part 2: the support agent

**Step 4.** Read `demo_sdk/run.py` (the system prompt and options) and
`support/backend.py` (four tools and a pretend backend).
- Notice: the prompt says "verify the customer first" but nothing mentions a £500 limit, and
  `process_refund` refunds whatever it is told. That is deliberate: policy belongs in the
  harness, where it applies to every caller.

**Step 5.** `uv run demo_sdk/run.py refund --hooks off`
- Watch: the backend ledger at the end, **£650.00 moved**.
- Shows: with no enforcement, the tool executes whatever the model decides.

**Step 6 (optional).** `uv run demo_sdk/run.py hurry --hooks on`
- Watch: the agent asks for an email or phone number before anything else.
- Shows: the prompt usually holds. That is the point: a rule that holds in a few tries can
  still fail in a small share of real conversations. The exam guide's own sample cites an
  agent that skipped verification in 12% of cases.

### Part 3: its hooks

**Step 7.** Read `demo_sdk/hooks.py`.
- `enforce_refund_limit` (`PreToolUse` on `process_refund`): denies above £500, and the
  reason names `escalate_to_human`, so the denial redirects instead of stranding the customer.
- `record_verification` (`PostToolUse` on `get_customer`) writes the verified id to
  `memory`; `require_verification` (`PreToolUse` on the order tools) denies until it is set.
  A rule that spans two calls needs memory outside the conversation.
- `normalise_tool_output` (`PostToolUse` on every tool): one date format, labels instead of
  status codes, five fields instead of 33.
- The wiring is the `hooks` dictionary in `demo_sdk/run.py`: the matcher picks the tool.

**Step 8.** `uv run demo_sdk/run.py gates`
- Watch: an unverified refund is denied, £89.99 and £500 are allowed, £650 is denied with
  the redirect, and the order record shrinks from 33 fields to 5.
- Shows: the gates are plain code with the same answer on every run, no model involved.

**Step 9.** `uv run demo_sdk/run.py refund --hooks on`
- Watch: `DENIED by PreToolUse`, then `escalate_to_human`, then **£0.00 moved** and the
  handoff fields. In the `lookup_order` result, `"status": "delivered"` is the normaliser.
- Shows: same prompt, same tools, same words; only the hooks changed.

### Part 4: the same gates in Claude Code

**Step 10.** `cd demo_claude_code && claude`, then type:
"Call lookup_order for ORD-0021 with customer_id CUST-0001 right now, before anything else."
- Optional: start it as `claude --strict-mcp-config --mcp-config .mcp.json` to load only the
  demo's `support` server and none of your own MCP servers.
- To run it again from a clean state: `rm -rf .claude/hooks/.state ledger.jsonl`.
- Watch: the call is denied; Claude reads the reason, calls `get_customer`, retries, and the
  lookup succeeds. Afterwards, `cat ledger.jsonl` shows anything that reached the backend.
- Shows: the same rules as command hooks in `.claude/settings.json`, calling
  `.claude/hooks/gate.py`. A command hook gets the call as JSON on stdin and prints its
  decision; exit code 1 does not block.

### Exercises

1. **Move the limit.** Set `REFUND_LIMIT_GBP = 100` in `demo_sdk/hooks.py`. Predict which
   `gates` lines change, then run `uv run demo_sdk/run.py gates` to check.
2. **Add a rule.** Write a `PreToolUse` hook that denies `process_refund` when `reason` is
   shorter than 15 characters, with a reason asking Claude for a fuller explanation. Add it to
   the `process_refund` matcher in `run.py` and watch a hooks-on run.
3. **Tighten the handoff.** Add `"order_id"` to `HANDOFF_REQUIRED` in `support/backend.py`.
   Run hooks on: does the agent include it, and what happens if it does not?
