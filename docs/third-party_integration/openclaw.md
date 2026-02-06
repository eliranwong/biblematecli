# Integration with OpenClaw

Install `mcpporter` and enable it in OpenClaw's skills.

For example, assume `biblemate` is installed in a venv `~/ai`

Send the following message to the main agent:

```
Is `mcpporter` enabled in your skills? I want you to configure a custom mcp server and test it: 
command: /home/username/ai/bin/python3
args: /home/username/ai/lib/python3.12/site-packages/biblemate/bible_study_mcp.py
```