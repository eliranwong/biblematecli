# Integration with Google Antigravity

<img width="839" height="990" alt="Image" src="https://github.com/user-attachments/assets/14fddc7e-e0dd-472d-8c53-d3879c2ba2cc" />

### Step-by-Step Configuration

1. **Open the MCP Settings:**
* In the **Agent View** (the panel you just reopened!), click the **three dots (...)** in the top right corner.
* Select **MCP Servers**.
* Click on **Manage MCP Servers**.


2. **Access the Raw Config:**
* In the Manage MCPs view, look for a button or link that says **"View raw config"**. This will open your `mcp_config.json` file (usually located at `~/.gemini/antigravity/mcp_config.json`).


3. **Add Your Bible Server:**

* Run `biblematemcpmini` in the background, e.g.:

> nohup biblematemcpmini -b googleai -p 33334 &

* Insert a new entry into the `mcpServers` object.

```
    "biblemate": {
      "serverUrl": "http://127.0.0.1:33334/mcp/"
    }
```

If you have a token configured to the variable `BIBLEMATE_STATIC_TOKEN` in `~/agentmake/biblemate/biblemate.config`, use the following:

```
    "biblemate": {
      "serverUrl": "http://127.0.0.1:33334/mcp/",
      "headers": {
        "Authorization": "Bearer <BIBLEMATE_STATIC_TOKEN>"
      }
    }
```

Remarks: This requires running the MCP server in the background, with the command `biblematemcpmini`. Do not run `biblematemcp`, as Antigravity does not support a single MCP server with more than 50 tools.

4. **Refresh and Verify:**
* Save the file and return to the **Manage MCP Servers** tab.
* Click **Refresh**. You should see "bible-server" appear with a green status indicator.

5. Add BibleMate to the Agent's Skills:

Read https://github.com/eliranwong/biblematecli/blob/main/package/biblemate/skills/antigravity/README.md


### Optional - Bash Script

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