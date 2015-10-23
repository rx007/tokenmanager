from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    # Executes every Monday morning at 7:30 A.M
    'every-3-seconds': {
        'task': 'tasks.add',
        'schedule': crontab(second='*/3'),
        'args': (16, 16),
    },
}
