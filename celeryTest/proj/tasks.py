
from __future__ import absolute_import

from proj.celery import celery


@celery.task
def add(x, y):
    return x + y


@celery.task
def mul(x, y):
    mul.delay(1,3)
    return x * y


@celery.task
def xsum(numbers):
    return sum(numbers)
