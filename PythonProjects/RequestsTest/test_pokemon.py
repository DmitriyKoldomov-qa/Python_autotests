import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json','trainer_token':'aa5ea0c2fa130125d74192c54f8c8c08'}

def test_get_trainer_by_code():
    """
    KTI-1. Get trainer by code
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': '4716'})
    assert response.status_code == 200, 'Unexpected status code'
    
def test_get_trainer_by_name():
    """
    KTI-2. Get trainer by name
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 4716},timeout=3)
    assert response.json() ['trainer_name'] == 'ДмитрийК', ''
    assert response.json() ['city'] == 'Санкт-Петербург', ''