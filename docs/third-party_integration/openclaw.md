# Integration with OpenClaw

<img width="1342" height="1068" alt="Image" src="https://github.com/user-attachments/assets/bdfec840-fee9-40c8-aa3a-e502e6b98ae8" />

* Install `mcpporter` and enable it in OpenClaw's skills.

* Run `biblematemcpmini` in the background, e.g.:

> nohup biblematemcpmini -b googleai -p 33334 &

* Edit the file `~/.openclaw/workspace-main/config/mcporter.json`, to insert a new entry into the `mcpServers` object, for example:

```
{
  "mcpServers": {
    "biblemate": {
      "serverUrl": "http://127.0.0.1:33334/mcp/"
    }
  },
  "imports": []
}
```

If you have a token configured to the variable `BIBLEMATE_STATIC_TOKEN` in `~/agentmake/biblemate/biblemate.config`, use the following:

```
{
  "mcpServers": {
    "biblemate": {
      "serverUrl": "http://127.0.0.1:33334/mcp/",
      "headers": {
        "Authorization": "Bearer <BIBLEMATE_STATIC_TOKEN>"
      }
    }
  },
  "imports": []
}
```

Add BibleMate to the Agent's Skills:

Read https://github.com/eliranwong/biblematecli/blob/main/package/biblemate/skills/antigravity/README.md

## Optional - Bash Script

Add a bash script to run `biblematemcpmini` in the background:

```bash
## mcp mini server
start_bmmcpmini() {
  echo "Starting BibleMate MCP mini server ..."
  nohup biblematemcpmini -b googleai -p 33334 &
  echo "BibleMate AI MCP mini server started."
}
### Check if BibleMate MCP mini server is already running
if ! pgrep -f "/bin/biblematemcpmini" > /dev/null; then
  start_bmmcpmini
else
  echo "BibleMate AI MCP mini server is already running."
fi
```