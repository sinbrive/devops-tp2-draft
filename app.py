from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    # comment to remove !!!
    return "Hello, eKod!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
