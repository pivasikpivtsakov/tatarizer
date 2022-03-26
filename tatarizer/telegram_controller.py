from rest_framework.response import Response
from rest_framework.views import APIView


class TelegramController(APIView):
    def post(self, request):
        return Response('ok')

    def get(self, request):
        return Response('hello this is api root')
