#!/bin/bash
# My first script

echo "Hello World!"
celery worker -l info -A proj &
celery worker -l info -A tasks &
python tasks_wrapper.py
