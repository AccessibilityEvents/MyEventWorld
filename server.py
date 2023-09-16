from os import path
from flask_cors import CORS

import suche

from flask import (
    render_template,
    request,
    redirect,
    Flask,
    jsonify,
    send_from_directory,
)

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def main():
    return redirect("/api/all", 304)

@app.route("/api/all")
def api_all():
    data = suche.read_data()
    titles = []
    times_start = []
    times_end = []
    descriptions = []
    links = []
    costs = []
    addresses = []
    for count in range(len(data)):
        if count == 2:
            titles = data[2]
            print(titles)
        elif count == 1:
            times_end = data[1]
            print(times_end)
        elif count == 0:
            times_start = data[0]
            print(times_start)
        elif count == 3:
            descriptions = data[3]
            print(descriptions)
        elif count == 4:
            costs = data[4]
            print(costs)
        elif count == 5:
            links = data[5]
            print(links)
        elif count == 6:
            addresses = data[6]
            print(addresses)


    res = []
    for num in range(len(titles)):
        try:
            res.append(
                {"Titel": titles[num], "Start": times_start[num], "Ende": times_end[num], "Beschreibung": descriptions[num],
                 "Preis": costs[num], "Link": links[num], "Ort": addresses[num]})
        except:
            continue

    return jsonify(res)

@app.route("/api/search")
def api():
    therm = request.args.get("therm")

    return jsonify({
        "Response": therm,
        "Code": 200
    })




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
