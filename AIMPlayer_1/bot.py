import telebot
import threading
import time

bot_token = "6491778406:AAF2CjOcwnEfsGfiCy4daz6TlvKKPthkwwM"  # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot(token=bot_token)

chat_id = 2109538484
signal = True
@bot.message_handler(commands=['start'])
def send_hello_message(a=""):
    global chat_id, signal  # Здесь вы можете использовать любой способ хранения chat_id
    file_path = "content/report.txt"
    if signal:
        with open(file_path, "r", encoding="utf-8") as file:
            bot.send_message(chat_id, file.readline())
        signal = False


def warning():
    global signal
    signal = True
# Функция для периодической отправки сообщений раз в минуту
def schedule_messages():
    while True:
        send_hello_message()
        time.sleep(60)  # Пауза в 60 секунд



# Запускаем поток для отправки сообщений раз в минуту
thread = threading.Thread(target=schedule_messages)
thread.start()

# Запускаем polling
bot.infinity_polling()