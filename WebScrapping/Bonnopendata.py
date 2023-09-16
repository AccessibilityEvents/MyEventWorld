import requests

url = 'https://www.bonn.de/citykey/events-json.php'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    for event in data[:5]:
        print(event)
        print("-----")
else:
    print("Failed to retrieve data from the URL.")
