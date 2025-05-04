from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

# Обработчик стартовой команды
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I'm your bot.")

# Запуск приложения
application = ApplicationBuilder().token(TOKEN).build()

# Регистрируем обработчики
application.add_handler(CommandHandler("start", start))

# Запускаем бота
if __name__ == '__main__':
    application.run_polling()
