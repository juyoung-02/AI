import logging
from typing import Optional

from .config import GEMINI_API_KEY

try:
    import google.generativeai as genai
    genai.configure(api_key=GEMINI_API_KEY)
    _MODEL = genai.GenerativeModel("gemini-2.0-flash") if GEMINI_API_KEY else None
except Exception as exc:
    logging.warning("Gemini API unavailable: %s", exc)
    _MODEL = None


def available() -> bool:
    return _MODEL is not None


def generate(prompt: str, system: Optional[str] = None) -> str:
    """Generate text using Gemini. Returns fallback echo if unavailable."""
    if not _MODEL:
        return f"[no gemini] {prompt}"
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    try:
        resp = _MODEL.generate_content(messages)
        return resp.text
    except Exception as exc:
        logging.error("Gemini request failed: %s", exc)
        return f"[error] {prompt}"
