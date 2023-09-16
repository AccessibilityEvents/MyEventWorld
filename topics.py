# Ordnet allen Einträgen mithilfe von KI Topics zu
from copy import deepcopy
from os import environ
from functools import lru_cache

import openai
from json import loads, dumps


openai.api_key = environ.get("OPENAI_API_KEY")


def main():
    file_path = "WebScrapping/Kölnopendata.json"

    data = read_json_to_dict(file_path)
    length = len(data["items"])

    for i, value in enumerate(reversed(deepcopy(data["items"]))):
        if "thema" in value:
            continue

        text = value["title"] + value["description"]
        topic = [word.strip() for word in get_topic(text).split(",")]
        data["items"][i]["thema"] = topic

        print(f"{i}/{length} - {topic} - {value['title']}")

    write_dict_to_json(file_path, data)


def write_dict_to_json(file_path: str, data: dict):
    json_text = dumps(data, indent=2, ensure_ascii=False)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(json_text)


def read_json_to_dict(file_path: str) -> dict:
    with open(file_path, "r") as file:
        text = file.read()

        data = loads(text)

    return data


@lru_cache
def get_topic(text: str) -> str:
    messages = [
        {
            "role": "system",
            "content": """Task: Classify the following Text by one or more of the following topics. Don't make topics up on your own. 
 Topics:
 - MINT
 - Politik
 - Bürgerbeteiligung
 - Sprache
 - Handwerk
 - Informatik
 - Kunst/Kultur
 - Geschichte
 - Logikspiele/Spiele
 - Sport
 - Schule"""
        },
        {
            "role": "user",
            "content": "Bilderbuchgeschichten für Kinder ab 3 Jahren in der Stadtteilbibliothek Chorweiler"
        },
        {
            "role": "assistant",
            "content": "Sprache"
        },
        {
            "role": "user",
            "content": "Workshop Digitales Zeichnen"
        },
        {
            "role": "assistant",
            "content": "Informatik,Kunst/Kultur"
        },
        {
            "role": "user",
            "content": text
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    main()

