import json


def read_data():
    data_koeln = r"WebScrapping\Kölnopendata.json"

    with open(data_koeln, "r", encoding="utf-8") as data_r:
        read_data = data_r.read()
    data = json.loads(read_data)

    count = 0
    try:
        while True:
            title = data['items'][count]['title']
            count += 1
    except:
        pass
    titles = []
    times_start = []
    times_end = []
    descriptions = []
    links = []
    costs = []
    addresses = []
    num = 0

    while True:
        try:
            title = data['items'][num]['title']
            time_start = data['items'][num]['beginndatum']
            time_end = data['items'][num]["endedatum"]
            description = data['items'][num]["description"]
            link = data['items'][num]['link']
            cost = data['items'][num]['preis']
            plz = data['items'][num]['plz']
            ort = data['items'][num]['ort']
            street = data['items'][num]['strasse']
            number = data['items'][num]['hausnummer']

            descriptions.append(description)
            costs.append(cost)
            links.append(link)
            addresses.append(f"{street} {number}, {plz} {ort}")
            times_start.append(time_start)
            times_end.append(time_end)
            titles.append(title)
            num += 1
        except:
            return [times_start, times_end, titles, descriptions, costs, links, addresses]


## searching function
def search_element(arr, n, element):
    ## iterating through the array
    for i in range(n):

        ## checking the current element with required element
        if arr[i] == element:
            ## returning True on match
            return True

            event = arr[i]
            for j in range(len(event)):

                ## checking the current element with required element
                if str(event[j]).find(element):
                    ## returning True on match
                    return True

    ## element is not found hence the execution comes here
    return False


if __name__ == '__main__':
    ## initializing the array, length, and element to be searched
    arr = read_data()
    n = len(arr)
    element_to_be_searched = "Zauberwürfel"
    # element_to_be_searched = 11

    if search_element(arr, n, element_to_be_searched):
        print(element_to_be_searched, "is found")
    else:
        print(element_to_be_searched, "is not found")
