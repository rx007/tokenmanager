from celery import Celery
from datetime import datetime, timedelta 
from tokenmaker.models import Token

app = Celery('tasks', broker="amqp://localhost")

@app.shared_task
def token_refresh():
    try:
        token = Token.objects.get_current_token()
        token.refresh()

        token_refresh.apply_async(
                eta=datetime.utcnow() + timedelta(seconds=3)
                )
    except:
        pass
    return
