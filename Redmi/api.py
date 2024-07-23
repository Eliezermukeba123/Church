import requests

endpoint = "https://app.chmeetings.com/F17B18D8A37CEFD0/Core/Dashboard"
response = requests.get(endpoint)
print(response.text)