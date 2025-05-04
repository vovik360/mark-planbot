# scheduler.py
import time
import os
from telegram import Bot
from database import get_due_tasks, mark_task_notified

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

def check_and_notify():
    tasks = get_due_tasks()
    for task_id, user_id, text in tasks:
        bot.send_message(chat_id=user_id, text=f"⏰ Напоминание:\n{ text }")
        mark_task_notified(task_id)

if __name__ == "__main__":
    while True:
        check_and_notify()
        time.sleep(60)
