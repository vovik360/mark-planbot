import datetime
from utils import parse_task_from_message
from database import save_task

async def process_message(user_id: int, message: str, context):
    task_text, due_time = parse_task_from_message(message)
    
    if not task_text or not due_time:
        await context.bot.send_message(chat_id=user_id, text="Я не понял, что и когда делать. Попробуй переформулировать.")
        return

    task_id = save_task(user_id, task_text, due_time)
    await context.bot.send_message(chat_id=user_id, text=f"Задача сохранена:\n\n📌 {task_text}\n⏰ {due_time.strftime('%d.%m.%Y %H:%M')}")
