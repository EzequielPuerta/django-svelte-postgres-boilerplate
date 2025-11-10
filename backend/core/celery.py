import os
from celery import Celery
from dotenv import load_dotenv


load_dotenv()
CELERY_BROKER_URL = f"redis://redis:{os.getenv('REDIS_PORT')}/0"


app = Celery('tasks', broker=CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
