#!/bin/bash
# My first script

echo "Hello World!"
celery worker -l info -A queries

