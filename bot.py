import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --------------------------
# ЧИТАЕМ config.json
# --------------------------
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

BOT_TOKEN = config["BOT_TOKEN"]

# --------------------------
# Команда /start
# --------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот запущен и работает!")

# --------------------------
# Запуск бота
# --------------------------
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    # Обработчик команды /start
    app.add_handler(CommandHandler("start", start))
    print("Bot started...")
    app.run_polling()

# --------------------------
# Точка входа
# --------------------------
if name == "main":
    main()
