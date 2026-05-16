---
name: talk-responses
description: Speak Codex responses aloud on macOS using the local `say` command. Use when the user asks Codex to talk, speak, read responses aloud, use voice, enable voice responses, narrate responses, or otherwise produce audible responses for the current prompt or session.
---

# Talk Responses

Use this skill to make Codex speak its own responses aloud when requested. This
is a best-effort local TTS workflow for macOS; it does not change Codex's native
transport or UI.

## Workflow

1. Compose the response text normally.
2. Before sending the visible response, run the bundled helper script:

```bash
python3 scripts/speak_response.py --stdin
```

Resolve `scripts/speak_response.py` relative to this `SKILL.md` file. If the
skill is installed in the default Codex directory, the absolute path is usually:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/talk-responses/scripts/speak_response.py" --stdin
```

Pass the exact response text on stdin.
3. Then send the same response text in the normal assistant response.

For long-running work, speak concise status updates only if the user explicitly
asked for ongoing voice narration. Otherwise, speak final answers and direct
answers.

## Safety

- Do not speak secrets, credentials, private keys, tokens, or large raw logs.
- If a response contains sensitive material, summarize safely before speaking
  and make clear in the visible response that sensitive text was not spoken.
- Do not speak huge files or generated artifacts verbatim. Summarize instead.
- If `say` is unavailable or audio execution is blocked, continue with text and
  tell the user that local speech failed.

## Options

Default voice and rate are configured by macOS. Override them only when useful:

```bash
python3 scripts/speak_response.py --stdin --voice Samantha --rate 190
```

Validate the helper without speaking:

```bash
python3 scripts/speak_response.py --text "voice check" --dry-run
```
