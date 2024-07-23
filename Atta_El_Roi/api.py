import requests

def get_country_codes():
    # Récupérer les données depuis l'API
    response = requests.get('https://restcountries.com/v3.1/all')
    data = response.json()

    # Extraire les informations nécessaires
    country_codes = []
    for country in data:
        country_info = {
            'name': country['name']['common'],
            'code': country['callingCodes'][0]
        }
        country_codes.append(country_info)

    # Afficher la liste des pays et leurs codes
    for country in country_codes:
        print(f"{country['name']} (+{country['code']})")

if __name__ == '__main__':
    get_country_codes()