from flask import render_template, request, redirect, Flask, jsonify

app = Flask(__name__, template_folder="templates")

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")