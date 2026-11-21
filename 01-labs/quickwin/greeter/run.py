"""Quick win: an agent that writes, tests and runs a small program, using only built-in tools.

No custom tools and no MCP server: Read, Write, Edit, Glob and Bash ship with the Agent SDK,
which runs the same engine as Claude Code. Its working folder is greeter/out/, cleared at the
start of every run. It may run python3 there and nothing else. When it finishes, the script
plays what it built.

    uv run greeter/run.py                    # build greet.py, then play it
    uv run greeter/run.py --no-play          # build only
    uv run greeter/run.py --model sonnet     # a bigger model, a fancier animation

Credentials: ANTHROPIC_API_KEY or CLAUDE_CODE_OAUTH_TOKEN from .env if set, otherwise your
`claude` login (a Pro/Max/Team subscription). The run is capped at 20 turns and $1.00 of
API-equivalent cost, and uses Haiku unless DEMO_MODEL or --model says otherwise.
    python3 greeter/out/greet.py             # play the last result again
"""
import argparse
import asyncio
import os
import shutil
import subprocess
import sys
from pathlib import Path

from claude_agent_sdk import (AssistantMessage, ClaudeAgentOptions, ResultError,
                              ResultMessage, TextBlock, ToolResultBlock, ToolUseBlock,
                              UserMessage, query)
from dotenv import load_dotenv

HERE = Path(__file__).resolve().parent
KIT = HERE.parent
OUT = HERE / "out"

BOLD, DIM, RESET = "\033[1m", "\033[2m", "\033[0m"
CYAN, GREEN, YELLOW, MAGENTA = "\033[36m", "\033[32m", "\033[33m", "\033[35m"

SYSTEM_PROMPT = f"""You are a Python developer working in {OUT}.
Create and change files only in that folder. Use only the Python standard library.
The shell runs commands that start with `python3` and denies everything else, so run
one plain python3 command at a time: no pipes, redirection, `&&` or other programs."""

TASK = """Create a small CLI application, greet.py, that draws a cool text animation
in the terminal to greet the students of {audience}. Think animated ASCII art: big
letters, colour, movement.

- It runs with `python3 greet.py` and ends by itself in under 10 seconds.
- `python3 greet.py --fast` plays the same animation with no delays, so you can test it.
- Hide the cursor while it plays and always restore it, even on Ctrl+C.

Test it once with --fast, fix anything that fails, then tell me in two sentences what it does."""

# The whole tool set: built-ins only. Bash may run python3 and nothing else.
TOOLS = ["Read", "Write", "Edit", "Glob", "Bash"]
ALLOWED = ["Read", "Write", "Edit", "Glob", "Bash(python3 *)"]


def describe(name, args):
    """One line per tool call, short enough for a projector."""
    if name in ("Write", "Edit", "Read"):
        path = Path(args.get("file_path", "")).name
        if name == "Write":
            lines = args.get("content", "").count("\n") + 1
            return f"{path} ({lines} lines)"
        return path
    if name == "Bash":
        return args.get("command", "")
    return str(args.get("pattern", args))[:70]


async def build(audience, model):
    options = ClaudeAgentOptions(
        model=model,
        system_prompt=SYSTEM_PROMPT,
        cwd=str(OUT),
        tools=TOOLS,                  # the built-in tools this session has at all
        allowed_tools=ALLOWED,        # which of them run without asking
        permission_mode="dontAsk",    # anything else is denied, never prompted
        setting_sources=[],           # ignore local CLAUDE.md and settings
        max_turns=20,
        max_budget_usd=1.00,          # API-equivalent cost; on a subscription nothing is billed
    )

    print(f"\n{BOLD}Task:{RESET} {TASK.format(audience=audience).splitlines()[0]} ...\n")
    try:
        await stream(query(prompt=TASK.format(audience=audience), options=options))
    except ResultError as error:
        # The run hit a cap (budget or turns): whatever greet.py it wrote so far is still there.
        reason = "; ".join(error.errors) or error.subtype or str(error)
        print(f"{YELLOW}{BOLD}Run stopped early:{RESET}{YELLOW} {reason}{RESET}\n")


async def stream(messages):
    """Print each tool call as it happens, the agent's words, and what the run cost."""
    async for message in messages:
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, ToolUseBlock):
                    print(f"  {CYAN}{block.name:6s}{RESET} {DIM}{describe(block.name, block.input)}{RESET}")
                elif isinstance(block, TextBlock) and block.text.strip():
                    print(f"\n{BOLD}Agent:{RESET} {block.text.strip()}\n")
        elif isinstance(message, UserMessage) and isinstance(message.content, list):
            for block in message.content:
                if isinstance(block, ToolResultBlock) and block.is_error:
                    text = block.content if isinstance(block.content, str) else str(block.content)
                    label = "denied by the permission rules" if "permission" in text.lower() \
                        else "error"
                    print(f"         {YELLOW}{label}, the agent reads it and adapts{RESET}")
        elif isinstance(message, ResultMessage):
            cost = message.total_cost_usd or 0.0
            models = ", ".join(message.model_usage or {}) or "default model"
            print(f"{DIM}run ended: {message.subtype}, {message.num_turns} turns, "
                  f"{message.duration_ms / 1000:.0f} s, ${cost:.4f}, {models}{RESET}\n")


def load_credentials():
    """A key, a setup-token or neither (then the saved `claude` login is used)."""
    load_dotenv(os.environ.get("DEMO_ENV_FILE") or KIT / ".env")
    for name in ("ANTHROPIC_API_KEY", "CLAUDE_CODE_OAUTH_TOKEN"):
        if not os.environ.get(name):
            os.environ.pop(name, None)   # a blank key fails instead of falling back


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--audience", default="the CCAR-F cohort")
    parser.add_argument("--model", help="model alias or id (default: DEMO_MODEL, else haiku)")
    parser.add_argument("--no-play", action="store_true", help="build only, do not play it")
    args = parser.parse_args()

    load_credentials()
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir(parents=True)
    asyncio.run(build(args.audience, args.model or os.environ.get("DEMO_MODEL") or "haiku"))

    script = OUT / "greet.py"
    if not script.exists():
        print(f"{YELLOW}No greet.py was written. Check the sign-in, then run again.{RESET}")
        sys.exit(1)
    if not args.no_play:
        input(f"{MAGENTA}{BOLD}Press Enter to play what it built ...{RESET}")
        subprocess.run([sys.executable, str(script)], cwd=OUT)


if __name__ == "__main__":
    main()
