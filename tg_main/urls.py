from django.conf import settings
from django.urls import path
from .views.telegram import TelegramWebhook


urlpatterns = [
    path(f'{settings.TGBOTAPI_TOKEN}', TelegramWebhook.as_view()),
]