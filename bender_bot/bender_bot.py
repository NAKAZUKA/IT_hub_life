import telebot
from telebot import types
from question_to_answer import get_gpt_response
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Мероприятия')
    btn2 = types.KeyboardButton('Связь с профкомом')
    btn3 = types.KeyboardButton('Мой клуб')
    btn4 = types.KeyboardButton('GPT')
    btn5 = types.KeyboardButton('Помощь')
    markup.add(btn1, btn2, btn3, btn4, btn5)

    bot.send_message(message.chat.id,
                     "**Привет!** Меня зовут Bender. Я твой **помощник**.\n\n"
                     "Я здесь, чтобы помочь тебе добиться **успеха** в твоих академических начинаниях.\n\n"
                     "Не стесняйся обращаться ко мне с любыми **вопросами** или **проблемами**, с которыми ты сталкиваешься.",
                     parse_mode='Markdown',
                     reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo(message):
    if message.text == 'Мероприятия':
        formatted_text = "**Мероприятия на сегодня:**\n\n" \
                         "- ТАЙНАЯ КАРТА - Студенты получают загадочную карту с непонятными символами. Их задача - расшифровать карту и найти сокровище.\n\n" \
                         "- АКАДЕМИЧЕСКИЙ КОНКУРС - Участники соревнуются в знаниях по различным областям: от истории и литературы до науки и искусства."
        bot.send_message(message.chat.id, formatted_text, parse_mode='Markdown')
    elif message.text == 'Связь с профкомом':
        formatted_text = "[Ссылка на профком](https://t.me/profkom_IThub-life)"
        bot.send_message(message.chat.id, formatted_text, parse_mode='Markdown')
    elif message.text == 'Мой клуб':
        formatted_text = "**Наши клубы:**\n\n" \
                        "- МЫСЛИШКА - клуб шахматистов\n" \
                        "- СЛОВО - литературный клуб\n" \
                        "- ЛЮБИМЫЙ ФИЛЬМ - клуб киноманов\n" \
                        "- ОБЪЕКТИВ - клуб фотографов\n" \
                        "- ЭНЕРГИЯ - клуб активного отдыха"
        bot.send_message(message.chat.id, formatted_text, parse_mode='Markdown')

    elif message.text == 'GPT':
        bot.send_message(message.chat.id, 'Можешь задать мне любой вопрос я постараюсь ответить')
        bot.register_next_step_handler(message, get_response)

    elif message.text == 'Помощь':
        formatted_text = "**Помощь**\n\n" \
                        "Вот ссылка на бота-психолога, к которому ты можешь обратиться анонимно: https://t.me/psychologist_ithub_bot"
        bot.send_message(message.chat.id, formatted_text, parse_mode='Markdown')


def get_response(message):
    # Получаем вопрос пользователя
    user_question = message.text

    # Вызываем функцию для получения ответа
    gpt_response = get_gpt_response(user_question)

    # Отправляем ответ пользователю
    bot.send_message(message.chat.id, gpt_response, parse_mode='Markdown')
        
        
bot.polling()
