import requests
url = 'https://wttr.in/Лондон?nTqmM&lang=ru'
response = requests.get(url)
response.raise_for_status()
print(response.text)

url = 'https://wttr.in/Шереметьево?nTqmM&lang=ru'
response = requests.get(url)
response.raise_for_status()
print(response.text)

url = 'https://wttr.in/Череповец?nTqmM&lang=ru'
response = requests.get(url)
response.raise_for_status()
print(response.text)