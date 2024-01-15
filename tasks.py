# credit_approval/tasks.py

from celery import shared_task
from django.core.management import call_command

@shared_task
def initialize_system():
    call_command('init_system')
