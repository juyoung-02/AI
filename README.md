# AI Friend Prototype

This repository contains a prototype of a conversational AI friend built around
multiple modules:

1. **Identity Module** – identifies users and tracks interaction counts.
2. **Context Memory** – stores structured conversation history.
3. **Emotion Regulation** – adapts tone based on relationship level.
4. **Response Generation** – integrates the Gemini 2.0 Flash model when an API
   key is provided.
5. **Meta Learner** – logs interactions for future analysis.

## Usage

Set the `GEMINI_API_KEY` environment variable with your API key. If omitted,
the system falls back to simple echo responses.

```bash
export GEMINI_API_KEY=your-key-here
python -m friend_ai.cli
```

Type messages and the AI will respond. Enter `exit` to quit.
