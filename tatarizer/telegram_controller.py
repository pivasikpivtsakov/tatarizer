from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class TelegramController(APIView):
    def post(self, request):
        print(request.data)

        return Response('ok', status=status.HTTP_200_OK)

    def get(self, request):
        return Response('hello this is api root', status=status.HTTP_200_OK)
