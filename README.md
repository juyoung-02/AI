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

Install the Gemini client and set the API key before running:

```bash
pip install google-generativeai
export GEMINI_API_KEY=your-key-here
```

All modules attempt to use the Gemini 2.0 Flash model and only fall back to
simple heuristics when the model is unavailable.

```bash
python -m friend_ai.cli
```

Type messages and the AI will respond. Enter `exit` to quit.
