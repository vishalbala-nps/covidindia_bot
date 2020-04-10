from flask import *
from flask_assistant import Assistant, ask, tell


app = Flask(__name__)
assist = Assistant(app, route='/')

@app.route("/")
def root():
    return "<h1>Hi!</h1>"

@assist.action('greeting')
def greet_and_start():
    return ask("Hello there! Welcome!")

if __name__ == "__main__":
    app.run(port=8080)