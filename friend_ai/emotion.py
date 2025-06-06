class EmotionRegulator:
    def __init__(self):
        pass

    def profile(self, relation_level: int):
        if relation_level == 0:
            return {"온정도":0.4, "에너지":0.5, "격식":0.6, "공감":0.3}
        elif relation_level == 1:
            return {"온정도":0.5, "에너지":0.5, "격식":0.4, "공감":0.4}
        else:
            return {"온정도":0.7, "에너지":0.7, "격식":0.3, "공감":0.6}
