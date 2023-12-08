import requests
 
"""response = requests.post(url="https://api.pokemonbattle.me:9104/pokemons", 
            json={
    "name": "generate",
    "photo": "generate"
},
        headers={'trainer_token': 'e45e4a9808d6cd72cb90eeae5c9c4488', 'Content-Type': 'application/json'})
print(response.text)

response = requests.put(url="https://api.pokemonbattle.me:9104/pokemons", 
            json={
    "pokemon_id": "19808",
    "name": "Marusya",
    "photo": "https://dolnikov.ru/pokemons/albums/118.png"
},
        headers={'trainer_token': 'e45e4a9808d6cd72cb90eeae5c9c4488', 'Content-Type': 'application/json'})
print(response.text)

response = requests.post(url="https://api.pokemonbattle.me:9104/trainers/add_pokeball", 
            json={
    "pokemon_id": "19808"
},
        headers={'trainer_token': 'e45e4a9808d6cd72cb90eeae5c9c4488', 'Content-Type': 'application/json'})
print(response.text)"""

"""response = requests.get(url="https://api.pokemonbattle.me:9104/trainers", 
            json={
    "pokemon_id": "19808"
},
        headers={'trainer_token': 'e45e4a9808d6cd72cb90eeae5c9c4488', 'Content-Type': 'application/json'})
print(response.text)"""

response = requests.get(url="https://api.pokemonbattle.me:9104/trainers", 
                        params={"trainer_id": "2482"},
                        headers={'trainer_token': 'e45e4a9808d6cd72cb90eeae5c9c4488', 'Content-Type': 'application/json'})
print(response.text)

