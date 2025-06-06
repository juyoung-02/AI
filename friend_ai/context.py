from typing import Dict, List


class ContextMemory:
    def __init__(self):
        self.memory: Dict[str, List[Dict]] = {}

    def update(self, user_id: str, message: str, timestamp: str) -> List[Dict]:
        record = {
            "기억_ID": f"m{len(self.memory.get(user_id, [])) + 1}",
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
        log = self.memory.setdefault(user_id, [])
        log.append(record)
        return log[-5:]
