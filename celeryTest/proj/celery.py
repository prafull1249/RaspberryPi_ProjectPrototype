
from __future__ import absolute_import

from celery import Celery

celery = Celery('proj.celery',
                broker='amqp://Prafulla:praf1249@localhost/py_env',
                backend='amqp://',
                include=['proj.tasks'])

# Optional configuration, see the application user guide.
celery.conf.update(
    CELERY_TASK_RESULT_EXPIRES=86400,
)
if __name__ == '__main__':
    celery.start()
