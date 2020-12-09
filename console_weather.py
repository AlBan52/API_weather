import requests

locations = ['Лондон', 'Шереметьево', 'Череповец']
payload = {'mnTq': '', 'lang': 'ru'}

for location in locations:
    response = requests.get(f'http://wttr.in/{location}', params=payload)
    response.raise_for_status()
    print(response.text)
