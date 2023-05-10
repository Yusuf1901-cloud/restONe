import requests

product_id = input("Which product you want to delete!\n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print("You entered invalid id for product!")

if product_id:
    endpoint = f'http://127.0.0.1:8000/api/products/{product_id}/delete/'
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204)