import uuid

import schemas as db
import utils


def main():
    db.Event.delete().execute()

    data = utils.read_json_to_dict("WebScrapping/Kölnopendata.json")

    for event in data["items"]:
        topics = " ".join(event["thema"])
        location = f"{event['strasse']} {event['hausnummer']} {event['stadtteil']} {event['ort']}".strip()

        db.Event.create(
            id=uuid.uuid4(),
            title=event["title"],
            description=event["description"],
            link=event["link"],
            start_date=event["beginndatum"],
            end_date=event["endedatum"],
            price=event["preis"],
            topics=topics,
            location=location
        )


if __name__ == '__main__':
    main()
