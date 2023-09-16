import requests

url = "https://www.stadt-koeln.de/externe-dienste/open-data/events-od.php"


response = requests.get(url)


if response.status_code == 200:

    data = response.json()


    for item in data["items"]:
        startdate = item["beginndatum"]
        enddate = item["endedatum"]
        title = item["title"]


        print("Start Datum:", startdate)
        print("End datum:", enddate)
        print("Title:", title)

        print("Ort:", 'köln')
        print("-----")
else:
    print("Keine Daten")
