from celery import shared_task
import requests

from config.settings import TG_BOT_API
from habits.models import Habit


@shared_task
def send_telegram_reminder(habit_id):
    habit = Habit.objects.get(id=habit_id)

    chat_id = habit.user.chat_id

    message = f"Не забудьте {habit.action} в {habit.time} в {habit.place}!"

    bot_token = TG_BOT_API
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=data)

    if response.status_code != 200:
        raise Exception("Не удалось отправить сообщение в Telegram")
