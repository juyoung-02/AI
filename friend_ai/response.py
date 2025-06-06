import logging
from typing import List, Dict

from .gemini import generate, available


class ResponseGenerator:
    """Generate responses using Gemini 2.0 Flash when available."""

    def __init__(self):
        pass

    def generate(self, context: List[Dict], emotion_profile: Dict) -> str:
        prompt = self._build_prompt(context, emotion_profile)
        if available():
            try:
                return generate(prompt)
            except Exception as exc:
                logging.error("Gemini API call failed: %s", exc)

        last_message = context[-1]["message"] if context else ""
        return f"[AI 응답 - 온정도 {emotion_profile['온정도']}] {last_message}"

    def _build_prompt(self, context: List[Dict], emotion_profile: Dict) -> str:
        history = "\n".join(f"User: {item['message']}" for item in context)
        prompt = (
            f"Emotion Warmth: {emotion_profile['온정도']}\n"
            f"Conversation:\n{history}\nAI:"
        )
        return prompt
