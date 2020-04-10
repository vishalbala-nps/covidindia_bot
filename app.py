from flask import *
from flask_assistant import Assistant, ask, tell
import requests
import datetime
app = Flask(__name__)
assist = Assistant(app, route='/')

@app.route("/")
def root():
    return "<h1>Hi!</h1>"

@assist.action('greeting')
def greet_and_start():
    return ask("Hello there! Welcome to Covidstate India! What can I do for you?")

@assist.action('statistics_intent')
def statsfetcher():
    req = requests.get("http://covidstate.in/api/v1/data?type=latest")
    if req.status_code != 200:
        return tell("I'm sorry. An error occured. Please try again soon")
    rjson = req.json()
    ijson = rjson["data"]["India"]
    return ask("As of "+datetime.datetime.strptime(rjson["timestamp"]["updated_time"],"%Y-%m-%d %I:%M %p").strftime("%A	%d %I:%M %p")+" The number of infected people are "+ijson["total"]+", The number of deaths are "+ijson["deaths"]+" and the number of cured people are "+ijson["cured"])
if __name__ == "__main__":
    app.run(port=8080)