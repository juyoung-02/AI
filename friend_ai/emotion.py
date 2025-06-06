import json
from typing import Dict

from .gemini import generate, available

SYSTEM_PROMPT = (
    "시스템 역할: 당신은 적절한 감정 톤과 친밀도 수준을 결정하는 감정 반응"
    " 조정자입니다. 입력을 바탕으로 감정 프로필을 JSON으로 출력합니다."
)


class EmotionRegulator:
    def __init__(self):
        pass

    def profile(self, relation_level: int) -> Dict:
        if available():
            prompt = f"관계_레벨: {relation_level}"
            try:
                raw = generate(prompt, SYSTEM_PROMPT)
                return json.loads(raw)
            except Exception:
                pass

        if relation_level == 0:
            warmth, formality, energy = 0.4, 0.6, 0.5
        elif relation_level == 1:
            warmth, formality, energy = 0.5, 0.4, 0.5
        else:
            warmth, formality, energy = 0.7, 0.3, 0.7
        return {
            "온정도": warmth,
            "에너지": energy,
            "격식": formality,
            "공감": min(0.3 + relation_level * 0.1, 1.0),
        }
