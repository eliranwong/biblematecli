import os
from biblemate import BIBLEMATE_PACKAGE_DIR
from pathlib import Path
import argparse
import shutil

parser = argparse.ArgumentParser(description = f"""Install/Update BibleMate AI MCP SKILLs CLI options""")
parser.add_argument("-a", "--antigravity", action="store_true", dest="antigravity", help="Install/Update Antigravity skill.")
parser.add_argument("-c", "--claude", action="store_true", dest="claude", help="Install/Update Claude Code skill.")
parser.add_argument("-g", "--gemini", action="store_true", dest="gemini", help="Install/Update Gemini CLI skill.")
parser.add_argument("-o", "--openclaw", action="store_true", dest="openclaw", help="Install/Update OpenClaw skill.")
args = parser.parse_args()

def install_skill():
    print("Installing BibleMate skill...")
    if args.antigravity:
        print("Installing Antigravity skill...")
        antigravity_skill_dir = os.path.expanduser("~/.gemini/antigravity/skills/bible-study")
        if not os.path.isdir(antigravity_skill_dir):
            Path(antigravity_skill_dir).mkdir(parents=True, exist_ok=True)
        shutil.copy(os.path.join(BIBLEMATE_PACKAGE_DIR, "skills", "antigravity", "SKILL.md"), antigravity_skill_dir)
    if args.claude:
        print("Installing Claude Code skill...")
        claude_skill_dir = os.path.expanduser("~/.claude/skills/bible-study")
        if not os.path.isdir(claude_skill_dir):
            Path(claude_skill_dir).mkdir(parents=True, exist_ok=True)
        shutil.copy(os.path.join(BIBLEMATE_PACKAGE_DIR, "skills", "antigravity", "SKILL.md"), claude_skill_dir)
    if args.gemini:
        print("Installing Gemini CLI skill...")
        gemini_skill_dir = os.path.expanduser("~/.gemini/skills/bible-study")
        if not os.path.isdir(gemini_skill_dir):
            Path(gemini_skill_dir).mkdir(parents=True, exist_ok=True)
        shutil.copy(os.path.join(BIBLEMATE_PACKAGE_DIR, "skills", "antigravity", "SKILL.md"), gemini_skill_dir)
    if args.openclaw:
        print("Installing OpenClaw skill...")
        openclaw_skill_dir = os.path.expanduser("~/.openclaw/skills/bible-study")
        if not os.path.isdir(openclaw_skill_dir):
            Path(openclaw_skill_dir).mkdir(parents=True, exist_ok=True)
        shutil.copy(os.path.join(BIBLEMATE_PACKAGE_DIR, "skills", "openclaw", "SKILL.md"), openclaw_skill_dir)

if __name__ == "__main__":
    install_skill()
    