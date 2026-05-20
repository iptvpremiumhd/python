import telebot
import json
import os

TOKEN = "8397745119:AAEM28_nkeJ_YmjwacbzCDCOxRLkTiUODCw"
bot = telebot.TeleBot(TOKEN)

def ma'lumotni_oqi():
    if os.path.exists('zapravkalar.txt'):
        with open('zapravkalar.txt', 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Metan Yakkabog' botiga xush kelibsiz.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    data = ma'lumotni_oqi()
    javob = "⛽ Zapravkalar holati:\n\n"
    for z in data:
        status = "🟢 Ochiq" if z['status'] == 'ochiq' else "🔴 Yopiq"
        javob += f"{status} {z['nomi']}\n💰 Narx: {z['narx']}\n⚡ Bosim: {z['bosim']}\n\n"
    bot.send_message(message.chat.id, javob)

# Render uchun muhim: bot doimiy ishlashi kerak
print("Bot ishga tushdi...")
bot.polling(none_stop=True)
