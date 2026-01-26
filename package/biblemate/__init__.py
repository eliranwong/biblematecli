from __future__ import annotations

import os
import shutil
import pprint
import warnings
from pathlib import Path
from typing import Dict, List

from agentmake import USER_OS, AGENTMAKE_USER_DIR, readTextFile, writeTextFile
from biblemate import config
from biblemate.ui.selection_dialog import TerminalModeDialogs

# ------------------------------------------------------------------------------
# Warnings
# ------------------------------------------------------------------------------

warnings.filterwarnings(
    "ignore",
    message="coroutine '.*' was never awaited",
    category=RuntimeWarning,
    module="agentmake",
)

# ------------------------------------------------------------------------------
# Paths
# ------------------------------------------------------------------------------

USER_DIR = Path(AGENTMAKE_USER_DIR)
BIBLEMATE_USER_DIR = USER_DIR / "biblemate"
BIBLEMATE_USER_DIR.mkdir(parents=True, exist_ok=True)

CONFIG_FILE_BACKUP = BIBLEMATE_USER_DIR / "biblemate.config"

BASE_DIR = Path(__file__).resolve().parent
VERSION_FILE = BASE_DIR / "version.txt"
TEMP_DIR = BASE_DIR / "temp"
TEMP_DIR.mkdir(exist_ok=True)

VECTORSTORE_DIR = Path.home() / "biblemate" / "data" / "vectors"
VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------------------
# Config persistence
# ------------------------------------------------------------------------------

def write_user_config() -> None:
    """Persist current config values to disk."""
    content = f"""
config.banner_title="{config.banner_title}"
config.agent_mode={config.agent_mode}
config.prompt_engineering={config.prompt_engineering}
config.auto_suggestions={config.auto_suggestions}
config.auto_tool_selection={config.auto_tool_selection}
config.max_steps={config.max_steps}
config.light={config.light}
config.web_browser={config.web_browser}
config.hide_tools_order={config.hide_tools_order}
config.skip_connection_check={config.skip_connection_check}
config.default_bible="{config.default_bible}"
config.default_commentary="{config.default_commentary}"
config.default_encyclopedia="{config.default_encyclopedia}"
config.default_lexicon="{config.default_lexicon}"
config.max_semantic_matches={config.max_semantic_matches}
config.max_log_lines={config.max_log_lines}
config.mcp_port={config.mcp_port}
config.mcp_timeout={config.mcp_timeout}
config.color_agent_mode="{config.color_agent_mode}"
config.color_partner_mode="{config.color_partner_mode}"
config.color_info_border="{config.color_info_border}"
config.embedding_model="{config.embedding_model}"
config.custom_input_suggestions={pprint.pformat(config.custom_input_suggestions)}
config.disabled_tools={pprint.pformat(config.disabled_tools)}
""".strip()

    writeTextFile(str(CONFIG_FILE_BACKUP), content)


DEFAULT_CONFIG = """
config.banner_title=""
config.agent_mode=False
config.prompt_engineering=False
config.auto_suggestions=True
config.auto_tool_selection=False
config.max_steps=50
config.light=True
config.web_browser=False
config.hide_tools_order=True
config.skip_connection_check=False
config.default_bible="NET"
config.default_commentary="CBSC"
config.default_encyclopedia="ISB"
config.default_lexicon="Morphology"
config.max_semantic_matches=15
config.max_log_lines=2000
config.mcp_port=33333
config.mcp_timeout=9999999999
config.color_agent_mode="#FF8800"
config.color_partner_mode="#8000AA"
config.color_info_border="bright_blue"
config.embedding_model="paraphrase-multilingual"
config.custom_input_suggestions=[]
config.disabled_tools=[]
""".strip()


def load_config() -> None:
    """Load user configuration, apply defaults for new fields."""
    if not CONFIG_FILE_BACKUP.exists():
        exec(DEFAULT_CONFIG, globals())
        write_user_config()
    else:
        exec(readTextFile(str(CONFIG_FILE_BACKUP)), globals())

    changed = False
    for line in DEFAULT_CONFIG.splitlines():
        if not line.startswith("config."):
            continue
        key = line.split("=", 1)[0].replace("config.", "")
        if not hasattr(config, key):
            exec(line, globals())
            changed = True

    if changed:
        write_user_config()


# ------------------------------------------------------------------------------
# Startup
# ------------------------------------------------------------------------------

load_config()

# ------------------------------------------------------------------------------
# Runtime State (Non-persistent)
# ------------------------------------------------------------------------------

config.current_prompt = ""
config.cancelled = False
config.last_multi_bible_selection = [config.default_bible]
config.last_bible_reference = ""
config.last_book = 43
config.last_chapter = 3
config.last_verse = 16
config.backup_required = False
config.export_item = ""

# ------------------------------------------------------------------------------
# Command Registry
# ------------------------------------------------------------------------------

config.action_list: Dict[str, str] = {
    ".ideas": "generate ideas for prompts",
    ".exit": "exit current prompt",
    ".new": "new conversation",
    ".trim": "trim conversation",
    ".edit": "edit conversation",
    ".reload": "reload conversation",
    ".import": "import conversation",
    ".export": "export conversation",
    ".backup": "backup conversation",
    ".find": "search conversation",
    ".bible": "open bible verse",
    ".chapter": "open bible chapter",
    ".compare": "compare bible verse",
    ".search": "search bible",
    ".dictionary": "search dictionary",
    ".encyclopedia": "search encyclopedia",
    ".lexicon": "search lexicon",
    ".help": "help page",
}

# ------------------------------------------------------------------------------
# Plugin Copy (idempotent)
# ------------------------------------------------------------------------------

ETEXTEDIT_PLUGIN_DIR = Path.home() / "etextedit" / "plugins"
ETEXTEDIT_PLUGIN_DIR.mkdir(parents=True, exist_ok=True)

SOURCE_PLUGIN_DIR = BASE_DIR / "etextedit" / "plugins"

for plugin in SOURCE_PLUGIN_DIR.glob("*.py"):
    target = ETEXTEDIT_PLUGIN_DIR / plugin.name
    if not target.exists():
        shutil.copy(plugin, target)

# ------------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------------

AGENTMAKE_CONFIG = {
    "stream": True,
    "print_on_terminal": False,
    "word_wrap": False,
}

OLLAMA_NOT_FOUND = (
    "`Ollama` is not found! BibleMate AI uses it for embeddings.\n"
    "Install from https://ollama.com/"
)

BIBLEMATE_VERSION = readTextFile(str(VERSION_FILE)).strip()

DIALOGS = TerminalModeDialogs()

# ------------------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------------------

def fix_string(text: str) -> str:
    return text.replace(" ", " ").replace("-", "-")


def list_dir_content(directory: str = ".") -> str:
    path = Path(directory.replace("%2F", "/")).expanduser()

    if not path.is_dir():
        return "Invalid path!"

    folders: List[str] = []
    files: List[str] = []

    for item in sorted(path.iterdir()):
        if item.is_dir():
            folders.append(f"📁 {item.name}")
        else:
            files.append(f"📄 {item.name}")

    return " ".join(folders) + ("\n\n" if folders and files else "") + " ".join(files)
