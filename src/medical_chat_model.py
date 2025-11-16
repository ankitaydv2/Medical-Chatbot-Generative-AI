from src.prompt import SYSTEM_PROMPT
from src.helper import ChatModel

class MedicalChatbot:
    def __init__(self):
        self.model = ChatModel()

    def reply(self, user_msg):
        prompt = f"{SYSTEM_PROMPT}\nUser: {user_msg}\nAssistant:"
        return self.model.generate(prompt)
