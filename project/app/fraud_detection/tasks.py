import time

from celery import shared_task


@shared_task(name="async_workflow")
def async_workflow():
    time.sleep(10)
