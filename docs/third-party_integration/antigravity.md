# Configure BibleMate MCP Server in Google Antigravity

<img width="839" height="990" alt="Image" src="https://github.com/user-attachments/assets/14fddc7e-e0dd-472d-8c53-d3879c2ba2cc" />

### Step-by-Step Configuration

1. **Open the MCP Settings:**
* In the **Agent View** (the panel you just reopened!), click the **three dots (...)** in the top right corner.
* Select **MCP Servers**.
* Click on **Manage MCP Servers**.


2. **Access the Raw Config:**
* In the Manage MCPs view, look for a button or link that says **"View raw config"**. This will open your `mcp_config.json` file (usually located at `~/.gemini/antigravity/mcp_config.json`).


3. **Add Your Bible Server:**
* Insert a new entry into the `mcpServers` object.

#### Option A: Connection via Command (Recommended)

```json
    "biblemate": {
      "command": "python",
      "args": [
        "/home/username/agentmake/biblemate/bible_study_mcp.py"
      ]
    }
```

#### Option B: Connection via URL

Alternately, run command `biblematemcp`, and configure like:

```
    "biblemate": {
      "serverUrl": "http://127.0.0.1:33333/mcp/"
    }
```

If token is configured:

```
    "biblemate": {
      "serverUrl": "http://127.0.0.1:33333/mcp/",
      "headers": {
        "Authorization": "Bearer <TOKEN>"
      }
    }
```

Remarks: Option B requires running the MCP server in the background, with the command `biblematemcpmini`. Do not run `biblematemcp` for this option, as Antigravity does not support more than 50 tools.

4. **Refresh and Verify:**
* Save the file and return to the **Manage MCP Servers** tab.
* Click **Refresh**. You should see "bible-server" appear with a green status indicator.

