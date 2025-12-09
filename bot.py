from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN

# создаём приложение
app = ApplicationBuilder().token(BOT_TOKEN).build()

# сюда добавляем обработчики
# app.add_handler(CommandHandler("start_drawing", start_drawing_function))
# app.add_handler(CallbackQueryHandler(button_click_function))

# запуск бота
app.run_polling()
