from datetime import datetime, timezone
from .pipeline import AIFriend
from .gemini import available


def run():
    if not available():
        print("Warning: Gemini model unavailable. Using fallback heuristics.")
    ai = AIFriend()
    session_id = "session"
    print("AI 친구와 대화를 시작합니다. 종료하려면 'exit'를 입력하세요.")
    while True:
        user_input = input("당신: ")
        if user_input.strip().lower() == "exit":
            break
        timestamp = datetime.now(timezone.utc).isoformat()
        reply, info = ai.interact(user_input, session_id, timestamp)
        print(f"AI: {reply}")


if __name__ == "__main__":
    run()
