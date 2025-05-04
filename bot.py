import logging
import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Настройки логов
logging.basicConfig(level=logging.INFO)

# API-ключи
TELEGRAM_TOKEN = "8014948500:AAEnxkOjDNenrZ-8NViSaCYt1U2sD1yPRDU"
openai.api_key = "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"

# Асинхронная функция общения с OpenAI
async def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ты бот-планировщик по имени Марк. Пиши коротко, по-человечески, дружелюбно и с ответственностью. Запоминай, что тебе говорит Вова, и формируй из этого задачи и напоминания."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Ошибка OpenAI: {e}"

# Главный обработчик сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    reply = await ask_openai(user_input)
    await update.message.reply_text(reply)

# Запуск бота
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
