import logging
from shop.celery import app

logger = logging.getLogger(__name__)

@app.task
def send_mail():
    logger.info('!!!!!!!!send mail!!!!!!!!!')