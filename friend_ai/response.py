import logging
from typing import List, Dict

from .config import GEMINI_API_KEY

try:
    import google.generativeai as genai
except ImportError as e:
    genai = None
    logging.warning("google-generativeai package is not installed: %s", e)


class ResponseGenerator:
    """Generate responses using Gemini 2.0 Flash when available."""

    def __init__(self):
        if genai and GEMINI_API_KEY:
            genai.configure(api_key=GEMINI_API_KEY)
            self.model = genai.GenerativeModel("gemini-2.0-flash")
        else:
            self.model = None

    def generate(self, context: List[Dict], emotion_profile: Dict) -> str:
        prompt = self._build_prompt(context, emotion_profile)
        if self.model:
            try:
                response = self.model.generate_content(prompt)
                return response.text
            except Exception as exc:
                logging.error("Gemini API call failed: %s", exc)
        # Fallback echo response
        last_message = context[-1]["message"] if context else ""
        return f"[AI 응답 - 온정도 {emotion_profile['온정도']}] {last_message}"

    def _build_prompt(self, context: List[Dict], emotion_profile: Dict) -> str:
        history = "\n".join(f"User: {item['message']}" for item in context)
        prompt = (
            f"Emotion Warmth: {emotion_profile['온정도']}\n"
            f"Conversation:\n{history}\nAI:"
        )
        return prompt
