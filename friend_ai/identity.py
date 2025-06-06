import json
from typing import Dict

from .gemini import generate, available


SYSTEM_PROMPT = (
    "시스템 역할: 당신은 커뮤니티 AI의 사용자 신원 식별 담당자입니다. "
    "주요 임무: 입력된 메시지를 분석하여 사용자를 식별하고 관계 그래프를 유지관리합니다. "
    "출력은 JSON 형식으로 작성합니다."
)


class IdentityModule:
    def __init__(self):
        self.sessions: Dict[str, str] = {}
        self.profiles: Dict[str, Dict] = {}
        self.next_id = 1

    def identify(self, message: str, session_id: str, timestamp: str) -> Dict:
        if available():
            prompt = (
                f"메시지 내용: {message}\n시간 정보: {timestamp}\n세션 ID: {session_id}"
            )
            try:
                raw = generate(prompt, SYSTEM_PROMPT)
                data = json.loads(raw)
                return data
            except Exception:
                pass  # fallback below

        user_id = self.sessions.get(session_id)
        if user_id is None:
            user_id = f"user_{self.next_id}"
            self.next_id += 1
            self.sessions[session_id] = user_id
            self.profiles[user_id] = {"count": 0}
        profile = self.profiles[user_id]
        profile["count"] += 1

        count = profile["count"]
        trust = min(0.5 + count * 0.05, 0.95)
        if count < 5:
            level = 0
        elif count < 20:
            level = 1
        else:
            level = 3
        new_user = count == 1
        return {
            "사용자_ID": user_id,
            "신뢰도_점수": trust,
            "관계_레벨": level,
            "핵심_식별자": [session_id],
            "검증_필요": new_user,
            "검증_질문": [
                "안녕하세요! 자주 뵙지 못한 것 같은데, 어떻게 찾아오셨나요?"
            ] if new_user else [],
        }
