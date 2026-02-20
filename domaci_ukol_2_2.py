import requests
import json

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

obchodni_jmeno = input("Zadej obchodní jméno subjektu: ")

data = {"obchodniJmeno": obchodni_jmeno}

response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, json=data)

response_data = response.json()

pocetCelkem = response_data.get('pocetCelkem', 0)
ekonomickeSubjekty = response_data.get('ekonomickeSubjekty', [])

print(f"Počet celkem: {pocetCelkem}")
if ekonomickeSubjekty:
    for subjekt in ekonomickeSubjekty:
        ico = subjekt.get('ico', 'N/A')
        obchodniJmeno = subjekt.get('obchodniJmeno', 'N/A')
        print(f"Název subjektu: {obchodniJmeno}, ICO: {ico}")
else:
    print("Žádné ekonomické subjekty nebyly nalezeny.")