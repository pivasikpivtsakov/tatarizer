from django.apps import AppConfig
import http3 as http

from telegram_urls import TGURL_SETWEBHOOK, API_ROOT


class TatarizerAppConfig(AppConfig):
    name = 'tatarizer'
    verbose_name = "татаризатор"

    # startup hook
    def ready(self):
        response = http.post(TGURL_SETWEBHOOK, data={'url': API_ROOT})
        response.json()