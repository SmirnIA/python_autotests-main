import pytest
import requests

def test_status_code():
    url = "https://api.pokemonbattle.me:9104/trainers"
    response = requests.get(url)
    assert response.status_code ==200

def test_check_respons():
    url = "https://api.pokemonbattle.me:9104/trainers"
    response = requests.get(url, params = {"trainer_id": "2482"})
    assert response.text["trainer_name" == "Alisa"]