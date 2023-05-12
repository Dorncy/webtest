from aiohttp import request
from flask import Flask, render_template
app = Flask(__name__)


# @app.route("/")
# def index():
#     return "test"

def index():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!'
    return render_template('firebase_update.html')


if __name__ == "__main__":
    app.run()
