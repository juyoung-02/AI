from .identity import IdentityModule
from .context import ContextMemory
from .emotion import EmotionRegulator
from .response import ResponseGenerator
from .meta import MetaLearner


class AIFriend:
    def __init__(self):
        self.identity = IdentityModule()
        self.context = ContextMemory()
        self.emotion = EmotionRegulator()
        self.response = ResponseGenerator()
        self.meta = MetaLearner()

    def interact(self, message: str, session_id: str, timestamp: str):
        identity_info = self.identity.identify(message, session_id, timestamp)
        user_id = identity_info["사용자_ID"]
        ctx = self.context.update(user_id, message, timestamp)
        emotion_profile = self.emotion.profile(identity_info["관계_레벨"])
        reply = self.response.generate(ctx, emotion_profile)
        self.meta.record(user_id, message, reply)
        return reply, identity_info
