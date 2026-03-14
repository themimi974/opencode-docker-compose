# OpenCode — Docker usage (Groq / Kimi K2)

Drop all three files at the root of any project you want to work on:
- `docker-compose.yml`
- `opencode.json`
- `.env`  ← you create this one

## Setup

```
GROQ_API_KEY=gsk_...
```

Docker Compose picks it up automatically.

## Run

```bash
docker compose run --rm opencode
```

> Always use `run`, not `up` — OpenCode is a TUI, not a daemon.

## What the container can see

Only `./**` — the directory where you placed the files.
Nothing from your home directory or the rest of your filesystem.

## Config explained

### What goes in env (`.env`)
- `GROQ_API_KEY` — your Groq secret key (sensitive, never commit this)

### What goes in `opencode.json` (safe to commit)
- Provider + model declaration
- Token limits: `context: 131072`, `output: 16384`
  These are NOT available as env vars — they must live in the config file.
  OpenCode uses them to display how much context you have left in the UI.

## Notes

- The container runs as uid 1000. Check yours with `id -u` and adjust
  `user:` in the yml if needed.
- Sessions are lost when the container exits. For persistent sessions:
  add `- opencode_sessions:/root/.local/share/opencode` under `volumes:`
  and declare the named volume at the bottom of the compose file.
