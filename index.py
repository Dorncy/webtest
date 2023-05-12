import webbrowser
from aiohttp import request
from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "test"


def index():
    html_path = "firebase_update.html"
    return webbrowser.open(html_path)


if __name__ == "__main__":
    app.run()
