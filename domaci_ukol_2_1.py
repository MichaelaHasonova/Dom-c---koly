
import requests
import json


ico = input("Zadej IČO subjektu: ")

response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
data = response.json()
obchodni_jmeno = data['obchodniJmeno']
adresa = data['sidlo']['textovaAdresa']

print(obchodni_jmeno)
print(adresa)
