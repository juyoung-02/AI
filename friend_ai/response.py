class ResponseGenerator:
    def __init__(self):
        # Placeholder for gemini-2.0-flash integration
        pass

    def generate(self, context, emotion_profile):
        last_message = context[-1]["message"] if context else ""
        return f"[AI 응답 - 온정도 {emotion_profile['온정도']}] {last_message}"
