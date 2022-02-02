import telebot

from dto.telegram_dto import TelegramUserCreate, TelegramMessageCreate
from model.database import SessionLocal
from repository import telegram_user_repository, telegram_message_repository

token = "bot token"
bot = telebot.TeleBot(token)


def get_db():
    return SessionLocal()


@bot.message_handler(commands=['start'])
def start_conversation(message):
    from_user = message.from_user
    if telegram_user_repository.is_username_exist(from_user.username, get_db()):
        bot.send_message(chat_id=from_user.id, text="You're already exist!")
    else:
        t_user = TelegramUserCreate(username=from_user.username, telegram_id=from_user.id)
        telegram_user_repository.add_telegram_user(t_user, get_db())
        bot.send_message(chat_id=from_user.id, text="Hi!")


@bot.message_handler(content_types=['text'])
def get_messages(message):
    user_id = telegram_user_repository.get_id_by_username(message.from_user.username, get_db())
    telegram_message_repository.add_telegram_message(TelegramMessageCreate(user_id=user_id, text=message.text), get_db())
    bot.send_message(chat_id=message.from_user.id, text="OK")


bot.infinity_polling()
