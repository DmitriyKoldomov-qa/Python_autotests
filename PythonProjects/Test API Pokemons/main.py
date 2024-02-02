"""
Kolorado DmitryK test 4 api
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token':'aa5ea0c2fa130125d74192c54f8c8c08'}

body = {"name": "generate","photo": "generate"}
response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER,timeout=5)
print(f'Статус код: {response.status_code}). Сообщение: {response.text}')

body1 = {"pokemon_id": "29606","name": "deDDDDD","photo": "https://dolnikov.ru/pokemons/albums/008.png"}
response = requests.put(url=f'{URL}/pokemons', json=body1, headers=HEADER,timeout=5)
print(f'Статус код: {response.status_code}). Сообщение: {response.text}')

body2 = {"pokemon_id": "29606",}
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body2, headers=HEADER,timeout=5)
print(f'Статус код: {response.status_code}). Сообщение: {response.text}')

response = requests.get(url=f'{URL}/pokemons', params={'trainer_id': '4716'})
print(f'Статус код: {response.status_code}). Сообщение: {response.text}')

json_data = response.json()