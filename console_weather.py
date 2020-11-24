import requests

locations = ['Лондон', 'Шереметьево', 'Череповец']
url_template = 'http://wttr.in/{}?m&lang=ru'

for location in locations:
    url = url_template.format(location)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
