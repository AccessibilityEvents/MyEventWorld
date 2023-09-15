from flask import render_template, request, redirect, Flask, jsonify, send_from_directory

app = Flask(__name__, template_folder="frontend/dist")

@app.route("/<path:path>")
def send_report(path):
    return send_from_directory('frontend/dist', path)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")