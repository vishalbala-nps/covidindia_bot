from flask import *

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Hi!</h1>"

if __name__ == "__main__":
    app.run(port=8080)