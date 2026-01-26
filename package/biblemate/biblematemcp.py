from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

from biblemate import config, BIBLEMATE_VERSION
from agentmake import AGENTMAKE_USER_DIR, readTextFile

# ------------------------------------------------------------------------------
# Argument Parsing
# ------------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=f"BibleMate AI MCP Server {BIBLEMATE_VERSION} CLI options"
    )

    parser.add_argument(
        "-b", "--backend",
        dest="backend",
        help="AI backend; overrides the default backend temporarily."
    )

    parser.add_argument(
        "-lm", "--model",
        dest="model",
        help="AI model; overrides the default model temporarily."
    )

    parser.add_argument(
        "-p", "--port",
        dest="port",
        type=int,
        help=f"Specify MCP server port (default: {config.mcp_port}). "
             "Applicable to `biblematemcp` only."
    )

    return parser.parse_args()


ARGS = parse_args()

# ------------------------------------------------------------------------------
# Apply temporary config overrides
# ------------------------------------------------------------------------------

if ARGS.backend:
    config.backend = ARGS.backend

if ARGS.model:
    config.model = ARGS.model

# ------------------------------------------------------------------------------
# MCP Server Runner
# ------------------------------------------------------------------------------

def mcp() -> None:
    base_dir = Path(__file__).resolve().parent

    builtin_mcp_server = base_dir / "bible_study_mcp.py"
    user_mcp_server = (
        Path(AGENTMAKE_USER_DIR)
        / "biblemate"
        / "bible_study_mcp.py"
    )

    # User version overrides builtin if present
    mcp_path = user_mcp_server if user_mcp_server.is_file() else builtin_mcp_server

    mcp_script = readTextFile(str(mcp_path))

    port = ARGS.port if ARGS.port is not None else config.mcp_port

    mcp_script = mcp_script.replace(
        "mcp.run(show_banner=False)",
        (
            'mcp.run('
            'show_banner=False, '
            'transport="http", '
            'host="0.0.0.0", '
            f'port={port}'
            ')'
        ),
    )

    exec(mcp_script, globals())


# ------------------------------------------------------------------------------
# Entrypoint
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    mcp()
