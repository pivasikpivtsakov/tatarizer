from rest_framework import viewsets


class TelegramController(viewsets.ViewSet):
    def post(self):
        return 'ok'

    def get(self):
        return 'hello this is api root'
