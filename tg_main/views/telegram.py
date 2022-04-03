from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import httpx as http

from tg_main.telegram_urls import TGURL_ANSWERINLINEQUERY


class TelegramWebhook(APIView):
    async def post(self, request):
        print('request: ')
        print(request.data)
        async with http.AsyncClient() as client:
            response = await client.post(TGURL_ANSWERINLINEQUERY, data={
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
            print(response.json())
        return Response('ok', status=status.HTTP_200_OK)

    def get(self, request):
        return Response('hello this is api root', status=status.HTTP_200_OK)
