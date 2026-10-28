# DecodeClip MCP Server

A [Model Context Protocol](https://modelcontextprotocol.io) server for
[DecodeClip](https://decodeclip.com) — turn long-form videos (YouTube links or
direct URLs) into short, vertical, subtitled viral clips from any MCP client
(Claude Desktop, Claude Code, Cursor, etc.).

By default it talks to the **official hosted DecodeClip API** at
`https://api.decodeclip.com`. Point it at your own deployment by setting
`DECODECLIP_API_URL`.

## What it can do

| Tool | Auth | Description |
|------|:----:|-------------|
| `decodeclip_health` | – | API status + how this server is configured |
| `decodeclip_list_caption_templates` | – | Available caption styles (default, hormozi, mrbeast, …) |
| `decodeclip_list_transitions` | – | Available transition effects |
| `decodeclip_broll_status` | – | Whether B-roll overlays are configured |
| `decodeclip_list_fonts` | ✓ | Subtitle fonts available to your account |
| `decodeclip_billing_summary` | ✓ | Plan, usage and remaining quota |
| `decodeclip_create_clip_task` | ✓ | Start clipping a video → returns a `task_id` |
| `decodeclip_list_tasks` | ✓ | List your tasks |
| `decodeclip_get_task` | ✓ | Task status, progress and clips |
| `decodeclip_wait_for_task` | ✓ | Poll until a task finishes |
| `decodeclip_list_clips` | ✓ | List a task's generated clips |
| `decodeclip_download_clip` | ✓ | Save a clip's MP4 to disk |
| `decodeclip_export_clip` | ✓ | Re-encode + save with a platform preset (tiktok/reels/shorts) |
| `decodeclip_cancel_task` / `decodeclip_resume_task` / `decodeclip_delete_task` | ✓ | Manage tasks |

Tools marked ✓ require an API key (or self-host credentials, see below).

## Getting an API key

1. Sign in at [decodeclip.com](https://decodeclip.com).
2. Go to **Settings → API Keys**.
3. Create a key and copy it (it's shown only once). It looks like `sk_…`.

## Configuration

All configuration is via environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `DECODECLIP_API_KEY` | – | Your API key (recommended auth). |
| `DECODECLIP_API_URL` | `https://api.decodeclip.com` | Backend base URL. Set for self-hosting. |
| `DECODECLIP_DOWNLOAD_DIR` | `./decodeclip-downloads` | Where downloaded/exported clips are written. |
| `DECODECLIP_TIMEOUT` | `60` | HTTP timeout (seconds) for non-download requests. |
| `DECODECLIP_USER_ID` | – | Self-host only: authenticate by user id (see below). |
| `DECODECLIP_AUTH_SECRET` | – | Self-host only: backend `BACKEND_AUTH_SECRET` for HMAC signing. |

### Self-hosting auth

If you run your own backend you have three options:

- **API key** (same as hosted): create a key and set `DECODECLIP_API_KEY`.
- **Signed headers**: set `DECODECLIP_USER_ID` + `DECODECLIP_AUTH_SECRET` (your
  backend's `BACKEND_AUTH_SECRET`).
- **Unsigned**: if the backend runs with `ALLOW_UNSIGNED_BACKEND_AUTH=true`,
  just set `DECODECLIP_USER_ID`.

Auth precedence is: API key → signed headers → unsigned user id.

## Install & run

Requires Python 3.10+. With [uv](https://docs.astral.sh/uv/):

```bash
cd mcp
uv run decodeclip-mcp        # runs the stdio server
```

Or install into the current environment:

```bash
pip install -e .
decodeclip-mcp
```

## Hosted SSE server

For clients that add a remote MCP URL, run the server over SSE and require a
DecodeClip API key as the client Bearer token:

```bash
DECODECLIP_API_URL=https://api.decodeclip.com \
DECODECLIP_MCP_TRANSPORT=sse \
DECODECLIP_MCP_HOST=0.0.0.0 \
DECODECLIP_MCP_PORT=9100 \
DECODECLIP_MCP_PUBLIC_URL=https://mcp.decodeclip.com \
DECODECLIP_MCP_REQUIRE_BEARER_AUTH=true \
decodeclip-mcp
```

Then configure the MCP client with:

```text
Server URL: https://mcp.decodeclip.com/sse
Transport: SSE
Authentication: Bearer Token
Token: sk_your_decodeclip_api_key
```

With Docker Compose, the `mcp` service runs this mode by default and binds to
`127.0.0.1:9100` for a reverse proxy.

## Use with Claude Desktop / Claude Code

Add to your MCP client config (e.g. `claude_desktop_config.json`, or via
`claude mcp add`). Example using `uv` to run from a checkout:

```json
{
  "mcpServers": {
    "decodeclip": {
      "command": "uv",
      "args": ["--directory", "/absolute/path/to/decodeclip/mcp", "run", "decodeclip-mcp"],
      "env": {
        "DECODECLIP_API_KEY": "sk_your_key_here"
      }
    }
  }
}
```

For a self-hosted backend, add `"DECODECLIP_API_URL": "http://localhost:8000"` to `env`.

With Claude Code:

```bash
claude mcp add decodeclip -e DECODECLIP_API_KEY=sk_your_key_here \
  -- uv --directory /absolute/path/to/decodeclip/mcp run decodeclip-mcp
```

## Example prompts

- "Use decodeclip to make clips from https://youtu.be/… with the hormozi caption template, then wait for it and download the top clip."
- "List my recent decodeclip tasks and show the virality scores of the latest one's clips."
- "Export clip <id> from task <id> as a TikTok preset."

## License

AGPL-3.0-or-later, matching the DecodeClip project.

### Clip length

`decodeclip_create_clip_task` accepts `clip_length`: `auto` (default, 15–60s),
`short` (15–30s), `medium` (30–60s), or `long` (1–2 min). This controls the
selection range and rendering limit. Removing pauses and filler words can
shorten the finished clips.
