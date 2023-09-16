import requests

url = "https://www.stadt-koeln.de/externe-dienste/open-data/events-od.php"


response = requests.get(url)


if response.status_code == 200:

    data = response.json()


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
    print("Keine Daten")
