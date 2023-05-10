import requests

endpoint = 'http://127.0.0.1:8000/api/products/'
headers = {'Authorization': 'Bearer b06fe88e4381ddef170741bb1d75ee0fda9103e7'}
data = {
    'title': 'JIkkillamayo hoy bolakay!!!!!!!!!!!',
    'price': 45.99
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())