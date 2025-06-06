class MetaLearner:
    def __init__(self):
        self.log = []

    def record(self, user_id: str, message: str, response: str):
        self.log.append({
            "user_id": user_id,
            "message": message,
            "response": response,
        })
