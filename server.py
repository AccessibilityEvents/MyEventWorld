from flask_cors import CORS
from flask import (
    request,
    redirect,
    Flask,
    jsonify,
)

import schemas as db


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/")
def main():
    return redirect("/api/all", 304)


@app.route("/api/all", methods=["GET"])
def search_all():
    return jsonify(list(db.Event.select().dicts())), 200


@app.route("/api/search", methods=["GET"])
def search():
    therm = request.args.get("therm", "")
    category = request.args.get("category", "")

    result = db.Event.select().where(
        (
            (db.Event.title ** f"{therm}%") |
            (db.Event.description ** f"%{therm}%")
        ) & (
            db.Event.topics ** f"%{category}%"
        )
    )

    return jsonify(list(result.dicts()))


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
