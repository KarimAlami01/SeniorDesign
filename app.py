teams = {
    "Atlanta Hustle": "/static/teams/hustle.png",
    "Austin Sol": "/static/teams/sol.png",
    "Boston Glory": "/static/teams/glory.png",
    "Carolina Flyers": "/static/teams/flyers.png",
    "Chicago Union": "/static/teams/union.png",
    "Colorado Summit": "/static/teams/summit.png",
    "Dallas Legion": "/static/teams/legion.png",
    "DC Breeze": "/static/teams/breeze.png",
    "Detroit Mechanix": "/static/teams/mechanix.png",
    "Houston Havoc": "/static/teams/havoc.png",
    "Indianapolis AlleyCats": "/static/teams/cats.png",
    "Los Angeles Aviators": "/static/teams/aviators.png",
    "Madison Radicals": "/static/teams/radicals.png",
    "Minnesota Wind Chill": "/static/teams/windchill.png",
    "Montreal Royal": "/static/teams/royal.png",
    "New York Empire": "/static/teams/empire.png",
    "Oakland Spiders": "/static/teams/spiders.png",
    "Philadelphia Phoenix": "/static/teams/phoenix.png",
    "Pittsburgh Thunderbirds": "/static/teams/thunderbirds.png",
    "Portland Nitro": "/static/teams/nitro.png",
    "Salt Lake Shred": "/static/teams/shred.png",
    "San Diego Growlers": "/static/teams/growlers.png",
    "Seattle Cascades": "/static/teams/cascades.png",
    "Toronto Rush": "/static/teams/rush.png",
    "Not Real": "https://via.placeholder.com/300x300.png?text=Image"
}

import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        team = request.form["team"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(team),
            temperature=0.6,
            max_tokens=4040,  # increase max tokens to get longer output
            n=3,  
            stop=None,  # no stop sequence
        )
        result = ""
        for choice in response.choices:
            result += choice.text
        return redirect(url_for("report", result=result, team = team))

    result = request.args.get("result")
    return render_template("index.html")


def generate_prompt(team):
    return f"Here is a team in the AUDL. Generate a well-structured 2 paragraph sports article giving a brief description about the {team} and predicting how their upcoming 2023 season will go."

@app.route("/report")
def report():
    result = request.args.get("result")
    team = request.args.get('team')

    team_logo_url = None
    if team in teams:
        team_logo_url = teams[team]
    return render_template("report.html", result=result, team=team, team_logo_url=team_logo_url)

def test_prompt(data):
    return f"You are a very reputable sports reporter in the AUDL world, here is the box score and team stats for a match in the 2023 season of the AUDL {data}. Write a well-structured and detailed sports article including a title discussing the match."

@app.route("/match1")
def match1():
    with open('scraped_data_0.html', 'r') as file:
     data = file.read() 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = test_prompt(data),        
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=1,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match1.html", result=result)

@app.route("/match2")
def match2():
    with open('scraped_data_1.html', 'r') as file:
     data = file.read() 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = test_prompt(data),        
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=1,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match2.html", result=result)

@app.route("/match3")
def match3():
    with open('scraped_data_2.html', 'r') as file:
     data = file.read() 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = test_prompt(data),        
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=1,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match3.html", result=result)

@app.route("/match4")
def match4():
    with open('scraped_data_3.html', 'r') as file:
     data = file.read() 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = test_prompt(data),        
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=1,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match4.html", result=result)

@app.route("/match5")
def match5():
    with open('scraped_data_4.html', 'r') as file:
     data = file.read() 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = test_prompt(data),        
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=1,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match5.html", result=result)

@app.route("/match6")
def match6():
    with open('scraped_data_5.html', 'r') as file:
     data = file.read() 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = test_prompt(data),        
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=1,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match6.html", result=result)

@app.route("/match7")
def match7():
    with open('scraped_data_6.html', 'r') as file:
     data = file.read() 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = test_prompt(data),        
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=1,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match7.html", result=result)

@app.route("/match8")
def match8():
    with open('scraped_data_7.html', 'r') as file:
     data = file.read() 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = test_prompt(data),        
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=1,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match8.html", result=result)

@app.route("/match9")
def match9():
    with open('scraped_data_8.html', 'r') as file:
     data = file.read() 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = test_prompt(data),        
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=1,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match9.html", result=result)

@app.route("/match10")
def match10():
    with open('scraped_data_9.html', 'r') as file:
     data = file.read() 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = test_prompt(data),        
        temperature=0.6,
        max_tokens=1890,  # increase max tokens to get longer output
        n=1,  
        stop=None,  # no stop sequence
    )
    result = ""
    for choice in response.choices:
        result += choice.text
    return render_template("match10.html", result=result)