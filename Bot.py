import telebot
import os

token = os.environ.get("Token")
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text", 'document', 'audio', 'sticker', 'voice', 'video'])
def text_message(message):
    bot.forward_message(-372766094, message.chat.id, message.message_id)

bot.polling()