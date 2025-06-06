import json
from typing import Dict, List

from .gemini import generate, available

SYSTEM_PROMPT = (
    "시스템 역할: 당신은 대화 연속성 유지를 위한 맥락 기억 관리자입니다."
    " 관련 정보를 추출해 JSON 형식으로 반환합니다."
)


class ContextMemory:
    def __init__(self):
        self.memory: Dict[str, List[Dict]] = {}

    def update(self, user_id: str, message: str, timestamp: str) -> List[Dict]:
        log = self.memory.setdefault(user_id, [])

        if available():
            recent = "\n".join(r["message"] for r in log[-5:])
            prompt = (
                f"이전 메시지들:\n{recent}\n새 메시지: {message}\n시간: {timestamp}"
            )
            try:
                raw = generate(prompt, SYSTEM_PROMPT)
                record = json.loads(raw)
            except Exception:
                record = None
        else:
            record = None

        if record is None:
            record = {
                "기억_ID": f"m{len(log) + 1}",
                "사용자_ID": user_id,
                "message": message,
                "내용": message,
                "카테고리": "사실적",
                "프라이버시_수준": "공개",
                "관련성_점수": 0.5,
                "생성일시": timestamp,
                "최종접근일시": timestamp,
                "접근횟수": 1,
                "감정적_가중치": 0.5,
                "태그": [],
            }

        log.append(record)
        return log[-5:]
