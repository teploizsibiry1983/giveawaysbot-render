import json
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Загружаем конфиг
with open("config.json") as f:
    config = json.load(f)

BOT_TOKEN = config["BOT_TOKEN"]
DRAWINGS = config["DRAWINGS"]

bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

# Хранение участников по розыгрышам
participants = {drawing["NAME"]: set() for drawing in DRAWINGS}

# Команда для публикации тестового поста с кнопкой
def start_drawing(update: Update, context: CallbackContext):
    drawing_name = DRAWINGS[0]["NAME"]  # берем первый розыгрыш
    keyboard = [
        [InlineKeyboardButton(f"Участвую (0)", callback_data=f"join|{drawing_name}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f"Розыгрыш: {drawing_name}\nНажми кнопку, чтобы участвовать!", reply_markup=reply_markup)

# Обработка нажатий кнопки
def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    data = query.data.split("|")
    action = data[0]
    drawing_name = data[1]

    if action == "join":
        user_id = query.from_user.id
        participants[drawing_name].add(user_id)
        count = len(participants[drawing_name])
        # Обновляем кнопку с числом участников
        keyboard = [
            [InlineKeyboardButton(f"Участвую ({count})", callback_data=f"join|{drawing_name}")]
        ]
        query.edit_message_reply_markup(InlineKeyboardMarkup(keyboard))
        query.message.reply_text(f"{query.from_user.first_name}, вы участник розыгрыша!")

dispatcher.add_handler(CommandHandler("start_drawing", start_drawing))
dispatcher.add_handler(CallbackQueryHandler(button_handler))

updater.start_polling()
updater.idle()
