import datetime
from typing import Dict, List


class MetaLearner:
    def __init__(self):
        self.log: List[Dict] = []

    def record(self, user_id: str, message: str, response: str) -> None:
        self.log.append(
            {
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "user_id": user_id,
                "message": message,
                "response": response,
            }
        )
