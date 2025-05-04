import openai
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Получаем токен Telegram бота из переменной окружения
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

async def start(update: Update, context):
    await update.message.reply_text("Привет! Я готов работать.")

async def handle_message(update: Update, context):
    user_message = update.message.text
    response = openai.Completion.create(
        model="text-davinci-003",  # Можно поменять модель в зависимости от нужд
        prompt=user_message,
        max_tokens=150
    )
    await update.message.reply_text(response.choices[0].text.strip())

def main():
    application = Application.builder().token(TELEGRAM_API_KEY).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
