import datetime
import requests
import json


def funk():
    url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=PLN&amount=1"

    payload = {}
    headers = {
      "apikey": "kx4ivlz0zmOuRSz53WqiIoHyAF1cNbeF"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text
    result = json.loads(result)['info']
    return result['rate']


a = funk()
print(a, type(a))





# info = {
#     "success": true,
#     "query": {
#         "from": "PLN",
#         "to": "USD",
#         "amount": 1
#     },
#     "info": {
#         "timestamp": 1675105743,
#         "rate": 0.230294
#     },
#     "date": "2023-01-30",
#     "result": 0.230294
# }
