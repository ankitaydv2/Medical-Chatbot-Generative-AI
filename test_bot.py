from src.medical_chat_model import MedicalChatbot
print("Initializing MedicalChatbot (this may take a few seconds)...")
bot = MedicalChatbot()
q = "having pain in stomach"
print("User question:", q)
resp = bot.reply(q)
print("-----RESPONSE START-----")
print(resp)
print("-----RESPONSE END-----")
