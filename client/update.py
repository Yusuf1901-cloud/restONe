import requests

id = int(input("Which product you would like to update"))
 
endpoint = f'http://127.0.0.1:8000/api/products/{id}/update/'

data = {
    'title': 'Solo update view for anyone you meet!'
}

get_response = requests.patch(endpoint, json=data)
print(get_response.json())