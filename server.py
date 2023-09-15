from flask import (
    render_template,
    request,
    redirect,
    Flask,
    jsonify,
    send_from_directory,
)

app = Flask(__name__, template_folder="frontend/dist", static_url_path="/", static_folder='frontend/dist/')


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
