import requests

url = "https://www.stadt-koeln.de/externe-dienste/open-data/events-od.php"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Extract and print the desired information for each item
    for item in data["items"]:
        beginndatum = item["beginndatum"]
        endedatum = item["endedatum"]
        title = item["title"]
        preis = item["preis"]
        if preis:
            preis_cleaned = preis.replace('<br>', ' ').replace('<br />', ' ').strip()
        else:
            print("Preis nicht angegeben")
        print("Beginndatum:", beginndatum)
        print("Endedatum:", endedatum)
        print("Title:", title)
        print("Preis:", preis_cleaned)
        print("-----")
else:
    print("Failed to retrieve data from the URL.")
