import re
from datetime import datetime, timedelta

def parse_task_from_message(message: str):
    # Простой пример: "напомни позвонить маме завтра в 19:00"
    match = re.search(r"(напомни|нужно|надо)\s+(.*)\s+(сегодня|завтра)?\s*(в\s*\d{1,2}:\d{2})?", message.lower())
    if not match:
        return None, None

    task = match.group(2).strip()
    day = match.group(3)
    time_str = match.group(4)

    if not task:
        return None, None

    now = datetime.now()
    if day == "завтра":
        date = now + timedelta(days=1)
    else:
        date = now

    if time_str:
        hour, minute = map(int, re.findall(r'\d+', time_str))
        due_time = date.replace(hour=hour, minute=minute, second=0, microsecond=0)
    else:
        due_time = date + timedelta(minutes=5)

    return task, due_time
