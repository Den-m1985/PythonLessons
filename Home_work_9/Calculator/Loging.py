import codecs
import datetime

def log(message, answer = 'empty'):
    dtn = datetime.datetime.now()
    '''
    # логирование в 'log_calculator.txt'
    botlogfile = open('log_calculator.txt', 'a', encoding='utf-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' +
          message.from_user.first_name, message.from_user.id,
          'операция: ' + ' '.join(text), file=botlogfile)
    botlogfile.close()
    '''
    # логирование в 'log'
    with codecs.open('log', 'a', encoding='utf-8') as file:
        file.writelines(
            f'\n Chat {message.chat.id} User: {message.from_user.first_name} Data: {dtn} Message: {message.text} Answer: {answer}')
