from rest_framework.views import APIView


class TelegramController(APIView):
    def post(self, request):
        return 'ok'

    def get(self, request):
        return 'hello this is api root'
