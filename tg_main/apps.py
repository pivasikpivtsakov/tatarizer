import os

import httpx as http
from django.apps import AppConfig

from .telegram_urls import TGURL_SETWEBHOOK, API_ROOT


class TgMainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tg_main'

    # startup hook
    def ready(self):
        if os.environ.get('RUN_MAIN') != 'true':
            with http.Client() as client:
                response = client.post(TGURL_SETWEBHOOK, data={'url': API_ROOT})
                print('setWebhook result: ', response.json())
