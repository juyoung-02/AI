import datetime

class ContextMemory:
    def __init__(self):
        self.memory = {}

    def update(self, user_id: str, message: str):
        now = datetime.datetime.utcnow().isoformat()
        log = self.memory.setdefault(user_id, [])
        log.append({"timestamp": now, "message": message})
        return log[-5:]
