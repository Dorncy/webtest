from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "test"


@app.route('/')
def index():
    return render_template("firebase_update.html")


if __name__ == "__main__":
    app.run(debug=True)
