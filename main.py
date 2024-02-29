import json
import requests
url='http://127.0.0.1:8000/quality_prediction'

input_data_for_model={
    'Size' : -3.970049,
    'Weight' : -2.512336,
    'Sweetness': 5.346330,
    'Crunchiness': -1.012009,
    'Juiciness' : 1.844900,
    'Ripeness': 0.329840,
    'Acidity': -0.491590483
}

input_json=json.dumps(input_data_for_model)
response=requests.post(url,data=input_json)
print(response.text)