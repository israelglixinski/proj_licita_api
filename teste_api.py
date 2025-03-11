import requests


response = requests.get('http://localhost:5000/lista_final')



print(response.text)