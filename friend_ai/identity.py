class IdentityModule:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def identify(self, message: str, session_id: str, timestamp: str):
        user_id = self.users.get(session_id)
        if user_id is None:
            user_id = f"user_{self.next_id}"
            self.next_id += 1
            self.users[session_id] = user_id
            trust = 0.5
            level = 0
            new_user = True
        else:
            trust = 0.9
            level = 1
            new_user = False
        return {
            "사용자_ID": user_id,
            "신뢰도_점수": trust,
            "관계_레벨": level,
            "핵심_식별자": [session_id],
            "검증_필요": new_user,
            "검증_질문": [
                "안녕하세요! 자주 뵙지 못한 것 같은데, 어떻게 찾아오셨나요?"
            ] if new_user else []
        }
