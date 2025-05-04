from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

import os

# Хранилище задач (пока просто в памяти)
user_tasks = {}

TOKEN = os.getenv("TELEGRAM_TOKEN")


# /start — приветствие
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    user_tasks[user_id] = []  # создаём список задач для нового юзера
    await update.message.reply_text(
        "Привет! Я Марк — твой ИИ-помощник. Просто напиши мне, что нужно сделать, и я всё запомню 😉"
    )


# Обычные сообщения — добавление задач
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    message = update.message.text

    # Если пользователь ещё не запускал /start
    if user_id not in user_tasks:
        user_tasks[user_id] = []

    # Добавляем задачу
    user_tasks[user_id].append(message)

    await update.message.reply_text(f"Запомнил: «{message}». Не забуду!")

    
# Команда /tasks — показать сохранённые задачи
async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    tasks = user_tasks.get(user_id, [])

    if not tasks:
        await update.message.reply_text("Ты пока ничего не просил.")
    else:
        task_list = "\n".join(f"{i+1}. {task}" for i, task in enumerate(tasks))
        await update.message.reply_text(f"Вот что ты мне уже поручил:\n{task_list}")


# Запуск бота
def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("tasks", list_tasks))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


if __name__ == '__main__':
    main()
