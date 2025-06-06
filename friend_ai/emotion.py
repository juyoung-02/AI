from typing import Dict


class EmotionRegulator:
    def __init__(self):
        pass

    def profile(self, relation_level: int) -> Dict:
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
