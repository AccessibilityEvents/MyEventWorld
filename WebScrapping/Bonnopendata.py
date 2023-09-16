import requests
from collections import defaultdict

url = 'https://www.bonn.de/citykey/events-json.php'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()


    events_by_title = defaultdict(list)

    for event in data:
        title = event["title"]
        start_date = event["startDate"]
        end_date = event["endDate"]

        events_by_title[title].append((start_date, end_date))

    for title, occurrences in events_by_title.items():
        latest_event = max(occurrences, key=lambda x: x[1])
        start_date, end_date = latest_event

        # Format the date strings
        formatted_start_date = f"Start datum: {start_date}"
        formatted_end_date = f"End Datum: {end_date}"

        print(formatted_start_date)
        print(formatted_end_date)
        print("title:", title)
        print("Ort:", 'Bonn')
        print("-----")
else:
    print("Failed to retrieve data from the URL.")
