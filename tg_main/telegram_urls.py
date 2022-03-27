# Telegram api urls
# https://api.telegram.org/bot<token>/METHOD_NAME
from django.conf import settings


TGBOTAPIURL = f'https://api.telegram.org/bot{settings.TGBOTAPI_TOKEN}'


TGURL_SETWEBHOOK = f'{TGBOTAPIURL}/setWebhook'


# secure root of our api
API_ROOT = f'{settings.HOSTNAME}/{settings.TGBOTAPI_TOKEN}'