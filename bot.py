import telebot
import json
import os
 
TOKEN = "8397745119:AAEM28_nkeJ_YmjwacbzCDCOxRLkTiUODCw"
bot = telebot.TeleBot(TOKEN)

def malumotni_oqi():
    if os.path.exists('zapravkalar.txt'):
        try:
            with open('zapravkalar.txt', 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []
    return []

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! Metan Yakkabog' botiga xush kelibsiz.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    data = malumotni_oqi()
    if not data:
        bot.send_message(message.chat.id, "Hozircha zapravkalar ma'lumoti topilmadi.")
        return
    
    javob = "⛽ Zapravkalar holati:\n\n"
    for z in data:
        status = "🟢 Ochiq" if z.get('status') == 'ochiq' else "🔴 Yopiq"
        nomi = z.get('nomi', 'Noma\'lum')
        narx = z.get('narx', '-')
        bosim = z.get('bosim', '-')
        javob += f"{status} {nomi}\n💰 Narx: {narx} so'm\n⚡ Bosim: {bosim} atm\n\n"
    
    bot.send_message(message.chat.id, javob)

print("Bot ishga tushdi...")
# Webhookni o'chirish va pollingni boshlash
bot.remove_webhook()
bot.polling(none_stop=True)
