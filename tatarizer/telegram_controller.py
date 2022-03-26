from rest_framework.views import APIView


class TelegramController(APIView):
    def post(self):
        return 'ok'

    def get(self):
        return 'hello this is api root'
