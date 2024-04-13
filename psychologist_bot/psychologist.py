from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext


# Замените 'YOUR_TOKEN' на ваш токен бота
TOKEN = '7139295438:AAGiCObOWxNpx4iAKrpcULFe0wJI_nTjiIQ'

# ID психолога
PSYCHOLOGIST_ID = '5074965474'
STUDENT_ID = '507213521'

PSYCHOLOGIST_NAME = 'Наталья Николаева'
PSYCHOLOGIST_PHONE = '+1234567890'
PSYCHOLOGIST_SCHEDULE = 'Понедельник-пятница: 9:00-18:00'

def start(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    if user_id == STUDENT_ID:
        buttons = [
            [InlineKeyboardButton("Контакт психолога", callback_data='contact')],
            [InlineKeyboardButton("Мне нужна помощь", callback_data='help')]
        ]
        update.message.reply_text(
            'Выберите действие:',
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif user_id == PSYCHOLOGIST_ID:
        update.message.reply_text('Вы психолог. Ожидайте сообщений от студентов.')
    else:
        update.message.reply_text(
            'Привет! Я бот-психолог. Если у тебя есть проблемы, можешь написать мне.'
        )

def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = str(query.from_user.id)
    if query.data == 'contact':
        contact_text = (
            f'Контакт психолога: {PSYCHOLOGIST_NAME}\n'
            f'Телефон: {PSYCHOLOGIST_PHONE}\n'
            f'График работы: {PSYCHOLOGIST_SCHEDULE}'
        )
        query.answer()
        query.message.reply_text(contact_text)
    elif query.data == 'help' and user_id == STUDENT_ID:
        query.answer()
        query.message.reply_text('Напиши, что тебя тревожит, и я поддержу тебя.')

def handle_student_message(update: Update, context: CallbackContext) -> None:
    if str(update.message.from_user.id) == STUDENT_ID:
        context.bot.send_message(chat_id=PSYCHOLOGIST_ID, text=update.message.text)

def handle_psychologist_message(update: Update, context: CallbackContext) -> None:
    if str(update.message.from_user.id) == PSYCHOLOGIST_ID:
        context.bot.send_message(
            chat_id=STUDENT_ID,
            text=f'Ответ от {PSYCHOLOGIST_NAME}:\n\n{update.message.text}'
        )

def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_click))
    dispatcher.add_handler(MessageHandler(Filters.chat(int(STUDENT_ID)) & Filters.text, handle_student_message))
    dispatcher.add_handler(MessageHandler(Filters.chat(int(PSYCHOLOGIST_ID)) & Filters.text, handle_psychologist_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()