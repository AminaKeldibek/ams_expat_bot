import json
import requests

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings


@require_POST
@csrf_exempt
def webhook(request):
    # responces
    responce = "How can I help you?"

    bureaucracy_resp = """/residence_permit\n/BSN\n/DigiD\n/registration\n/driverLicence"""
    residence_permit_resp = "https://www.iamexpat.nl/expat-info/official-issues/residence-permit-netherlands"
    telegram_url = "https://api.telegram.org"

    data = json.loads(request.body)
    print (data)

    text = data['message']['text']
    if text == "/Bureaucracy":
        responce = bureaucracy_resp
    if text == "/residence_permit":
        responce = residence_permit_resp

    r = requests.post(
        telegram_url + "/bot" + settings.TELEGRAM_TOKEN + "/sendMessage",
        data={"chat_id": data['message']['chat']['id'],
              "text": responce}
    )
    print (r)

    return HttpResponse("")
