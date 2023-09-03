from flask import Flask
import os

app = Flask(__name__)

@app.route("/hostname")
def get_hostname():
    return os.uname()[1]

@app.route("/author")
def get_author():
    return os.environ["AUTHOR"]

@app.route("/id")
def get_id():
    return os.environ["UUID"]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
