import telebot
from telebot import types

TOKEN = '6610865586:AAHCkP7duffqFr34EXxvgXsYb2rBzbTyE_Y' # Token vzyat iz Telegram stranitsy BotFather
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    keyboard.add(types.KeyboardButton(text='/start'))
    bot.reply_to(message, 'Hello, my Dear!')

bot.polling()

# @bot.message_handler(commands=['pass'])
# def random_num(message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1)
#     keyboard.add(types.KeyboardButton(text='/pass'))
#     num = 8
#     num_user = message.text
#     if num == num_user:
#         bot.reply_to(message, 'ty ygadal')
#     else:
#         bot.reply_to(message, 'ty  ne ygadal')



# ----------------------------------------------------------------------------------
# For Linux-systemy:
# from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler


# # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
# TOKEN = '6919136856:AAHr00lbQvPMCUXMHK6P_1sswvU6X5Fog-M'
# SELECT_LANGUAGE, SELECT_OPTION = range(2)

# def start(update, context):
#     reply_keyboard = [['English','Русский']]
#     update.message.reply_text(
#         'Привет! Выберите язык:',
#         reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
#     )
#     return SELECT_LANGUAGE
# def select_language(update, context):
#     user = update.message.from_user
#     context.user_data['language'] = update.message.text.lower()

#     update.message.reply_text(f'Отлично, {user.first_name}! Теперь выберите опцию:',
#                               reply_markup=ReplyKeyboardMarkup([['Option 1', 'Option 2']], one_time_keyboard=True))
#     return SELECT_OPTION

# def select_option(update, context):
#     user = update.message.from_user
#     option_selected = update.message.text
#     language = context.user_data.get('language', 'English')

#     update.message.reply_text(f'Вы выбрали опцию "{option_selected}" на языке {language}.',
#                               reply_markup=ReplyKeyboardRemove())

    

#     return ConversationHandler.END

# def cancel(update, context):
#     user = update.message.from_user
#     update.message.reply_text(f'{user.first_name}, вы отменили операцию.', reply_markup=ReplyKeyboardRemove())
#     return ConversationHandler.END
# def info(update,context):
#     update.message.reply_text('Этот бот создан с использованием python-telegram-bot. '
#                               'Вы можете использовать команду /square <число>, чтобы возвести число в квадрат.'
#                               'Также есть команды /caps <text> что бы перевести в верхний регистр '
#                               ' /reverse <text> что бы развернуть текст')

# def square(update, context):
#     try:
#         number = int(context.args[0])
#         result = number ** 2
#         update.message.reply_text(f'Квадрат числа {number} равен {result}.')

#     except (IndexError,ValueError):
#         update.message.reply_text('Используйте команду в формате: /square <число>.')
# def caps(update, context):
#     try:
#         text = ' '.join(context.args).upper()
#         update.message.reply_text(f'Текст в верхнем регистре: {text}')
#     except IndexError:
#         update.message.reply_text('Используйте команду в формате: /caps <текст>.')

# def reverse(update, context):
#     try:
#         text = ' '.join(context.args)[::-1]
#         update.message.reply_text(f'Обратный текст: {text}')
#     except IndexError:
#         update.message.reply_text('Используйте команду в формате: /reverse <текст>.')

# def echo(update, context):
#     update.message.reply_text(update.message.text)

# def main():
#     # Создаем экземпляр класса Updater и передаем ему токен бота
#     updater = Updater(token=TOKEN, use_context=True)

#     # Получаем объект диспетчера для регистрации обработчиков
#     dp = updater.dispatcher

#     # Регистрируем обработчик команды /start
#     conv_handler = ConversationHandler(
#         entry_points=[CommandHandler('start', start)],
#         states={
#             SELECT_LANGUAGE: [MessageHandler(Filters.regex('^(English|Русский)$'), select_language)],
#             SELECT_OPTION: [MessageHandler(Filters.regex('^(Option 1|Option 2)$'), select_option)]
#         },
#         fallbacks=[CommandHandler('cancel', cancel)]
#     )

#     dp.add_handler(conv_handler)
#     dp.add_handler(CommandHandler("info", info))
#     dp.add_handler(CommandHandler("square", square, pass_args=True))
#     dp.add_handler(CommandHandler("reverse", reverse, pass_args=True))
#     dp.add_handler(CommandHandler("caps", caps, pass_args=True))
#     # Регистрируем обработчик для эхо-бота
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

#     # Запускаем бота
#     updater.start_polling()

#     # Останавливаем бота при нажатии Ctrl+C
#     updater.idle()

# if name == 'main':
#     main()

