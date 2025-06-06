# AI Friend Prototype

This repository contains a minimal prototype of a conversational AI friend. It
implements the basic pipeline described in the architecture:

1. **Identity Module** – identifies users based on session.
2. **Context Memory** – stores recent messages.
3. **Emotion Regulation** – adjusts response tone.
4. **Response Generation** – placeholder for Gemini 2.0 Flash integration.
5. **Meta Learner** – records interactions for future learning.

## Running a Test Conversation

```bash
python -m friend_ai.cli
```

Type messages and the AI will respond. Enter `exit` to quit. The response
generation is currently a placeholder to be replaced with the actual Gemini
model.
