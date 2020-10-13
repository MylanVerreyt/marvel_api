"""Nodige imports"""
import hashlib
import requests
import time

"""Variabelen"""
ts = time.time()
public_key = 'private'
private_key = 'public'
name = input("Character name: ")


def hash_params():
    """ Functie voor md5 hash voor api key + tijdstip """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{ts}{private_key}{public_key}'.encode('utf-8'))
    hash_params = hash_md5.hexdigest()

    return hash_params


params = {'ts': ts, 'apikey': public_key, 'hash': hash_params()}
"""Zoeken naar een character via de naam van het karakter"""
result = requests.get('https://gateway.marvel.com:443/v1/public/characters?name='+ name ,
                   params=params)


"""Uitvoer van de code met error handeling"""
json_data = result.json()
json_status = json_data["code"]
json_info = json_data["data"]
json_this = json_info["results"]

if json_status == 200: 
    for x in json_this[0:1]:
        print(x) 
elif json_status == 409:
    print("API key, hash of tijdstip is niet opgegeven")
elif json_status == 401:
    print("tijdstip of de referer is verkeerd ingevuld")
elif json_status == 405:
    print("Deze methode is niet toegelaten!")
elif json_status == 403:
    print("Geen toegang!")
else:
    print("Er is spijtig genoeg iets mis gegaan probeer opnieuw of contacteer de eigenaar")