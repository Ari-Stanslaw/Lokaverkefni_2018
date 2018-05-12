from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

with open("hero.json","r") as info:
    gogn = json.load(info)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/wiki.html/<int:hero_id>")
def wiki(hero_id):
    name = gogn["hero"][hero_id]["name"]
    realname = gogn["hero"][hero_id]["real_name"]
    description = gogn["hero"][hero_id]["description"]
    age = gogn["hero"][hero_id]["age"]
    height = gogn["hero"][hero_id]["height"]
    affiliation =  gogn["hero"][hero_id]["affiliation"]
    base_of_operations = gogn["hero"][hero_id]["base_of_operations"]
    difficulty = gogn["hero"][hero_id]["difficulty"]
    health = gogn["hero"][hero_id]["health"]
    armour = gogn["hero"][hero_id]["armour"]
    shield = gogn["hero"][hero_id]["shield"]
    role = gogn["hero"][hero_id]["role"]["name"]

    img = gogn["hero"][hero_id]["img"]

    return render_template('wiki.html',
                           name=name,
                           realname=realname,
                           description=description,
                           img=img, age=age,
                           height=height,
                           affiliation=affiliation,
                           base_of_operations=base_of_operations,
                           difficulty=difficulty,
                           health=health,
                           armour=armour,
                           shield=shield,
                           role=role)



if __name__ == '__main__':
    app.run(debug=True)
