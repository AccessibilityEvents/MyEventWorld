from os import path
import mimetypes

from flask import (
    render_template,
    request,
    redirect,
    Flask,
    jsonify,
    send_from_directory,
)

app = Flask(__name__)

#For tests
@app.route("/")
def main():
    return redirect("/api/search", 302)


@app.route("/api/search")
def api():
    therm = request.args.get("therm")
    print("Starting Search")
    print(therm)
    return f"{therm} is the therm"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
