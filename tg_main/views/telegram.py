from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import httpx as http

from tg_main.telegram_urls import TGURL_ANSWERINLINEQUERY


class TelegramWebhook(APIView):
    def post(self, request):
        print('request: ')
        print(request.data)
        with http.Client() as client:
            response = client.post(TGURL_ANSWERINLINEQUERY, json={
                "results": [
                    {
                        "type": "article",
                        "id": "1",
                        "title": "Title",
                        "description": "Description",
                        "input_message_content": {"message_text": "hello I can respond to messages"}
                    }
                ]
            }
                                         )
            print('response: ')
            print(response.json())
        return Response('ok', status=status.HTTP_200_OK)

    def get(self, request):
        return Response('hello this is api root', status=status.HTTP_200_OK)
