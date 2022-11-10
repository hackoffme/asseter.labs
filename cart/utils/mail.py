import logging

from cart import task
from shop.celery import app

logger = logging.getLogger(__name__)

# редис на минималках :)
user_tasks = {}


def notification_task(user):
    logger.info('tada')
    if user in user_tasks:
        # не уверен что лучшее решение
        # задача отменится по истечении времени
        app.control.revoke(user_tasks[user])
    current_task = task.send_mail.apply_async(countdown=5*60)
    user_tasks[user] = current_task.id

