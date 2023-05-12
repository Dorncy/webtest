from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "test"


@app.route('/')
def index():
    html_path = "firebase_update.html"
    return render_template(html_path)


if __name__ == "__main__":
    app.run()
