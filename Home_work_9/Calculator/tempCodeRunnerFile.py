dler(commands=['start', 'help'])
def answer(message):
    bot.send_message(chat_id=message.from_user.id,
                     text