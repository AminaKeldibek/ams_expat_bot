import json
import requests

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings


@require_POST
@csrf_exempt
def webhook(request):
    telegram_url = "https://api.telegram.org"
    data = json.loads(request.body)
    print (data)
    r = requests.post(
        telegram_url + "/bot" + settings.TELEGRAM_TOKEN + "/sendMessage",
        data={"chat_id": data['message']['chat']['id'],
              "text": "Hi back"}
    )
    print (r)

    return HttpResponse("")
