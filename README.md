# Talk Responses Codex Skill

A tiny Codex skill that speaks assistant responses aloud on macOS using the
built-in `say` command.

The skill is intentionally simple: install the `talk-responses/` folder into
your Codex skills directory, then ask Codex to "talk in your responses", "use
voice responses", or "read this aloud".

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R talk-responses "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex or start a new session so the skill is discovered.

## Use

Example prompts:

```text
Talk in your responses for this session.
Use voice responses.
Read your answer aloud.
Speak this response.
```

The skill uses macOS `say`, so it is primarily for local macOS Codex sessions.
If `say` is unavailable or audio is blocked, Codex will keep responding in text.

## Contents

```text
talk-responses/
├── SKILL.md
├── agents/openai.yaml
└── scripts/speak_response.py
```

## License

MIT
