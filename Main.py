import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import constants
import time
import datetime

bot = telepot.Bot(constants.Token)


def handle(msg):
    print(msg)
    if telepot.flavor(msg) == "chat":
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            logic(msg['text'], chat_id, chat_type)
    elif telepot.flavor(msg) == "callback_query":
        callback_id, chat_id, data, msg_id = msg['id'], msg['from']['id'], msg['data'], msg["message"]["message_id"]

def logic(text, chat_id, chat_type):
    if chat_type == "group":
        for key in constants.key_words:
            if key in text.lower():
                keyboard = InlineKeyboardMarkup(inline_keyboard=[[{"text": "Узнать подробнее", "callback_data": "view"}]])
                bot.sendMessage(chat_id, constants.ans, reply_markup=keyboard)
                break
    elif chat_type == "privat":
        if text == "/start":
            keyboard = InlineKeyboardMarkup(inline_keyboard=[[{"text": "Написать разработчику", "callback_data": "write"}]
                                                             , [{"text": "Посмотреть портфолио", "callback_data": "check"}]])
            text = "Привет!\nМеня зовут Артём, и я занимаюсь разработкой мобильных приложений более 6 лет. Сотрудничая со мной, вы экономите ваше время и деньги, получая продукт, который не оставит вас равнодушным. Примеры моих работ можно увидеть ниже."+ "\nФото из [vk]" + "(" + constants.ava + ")"
            bot.sendMessage(chat_id, text, reply_markup=keyboard, disable_web_page_preview=False, parse_mode='markdown')



# Запускаем поток, который получает новые сообщения
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

while True:
    time.sleep(10)
