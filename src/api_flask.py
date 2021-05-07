from flask import Flask, jsonify
from src import manage_bd

app = Flask(__name__)

games = manage_bd.read_bd()


@app.route("/")
def index():
    return "Hello Kevin"


@app.route("/jeux")
def list_jeux():
    # print(games)
    return {"Liste jeux": games}


@app.route("/jeu/<int:jeu_id>")
def jeu_by_id(jeu_id):
    result = {}
    for jeu in games:
        if jeu["id"] == jeu_id:
            result = jsonify({"jeu": jeu})
    return result


@app.route("/deletejeu/<int:jeu_id>")
def delete_jeu_by_id(jeu_id):
    for game in games:
        if game["id"] == jeu_id:
            del game["id"]
    return jsonify({
        "Liste jeux": games
    })


@app.route("/addjeux")
def add_new_jeu():
    new_game = {"category": "combat", "description": "Sangoku doit vaincre les mechants", "editor": "Bandai", "id": 3,
                "name": "Dragon ball z", "number_player": "1-2 joueurs", "time": "200min", "year_published": "2011"}
    new_game_2 = {"category": "combat", "description": "Sangoku doit vaincre les mechants encore une fois",
                  "editor": "Bandai",
                  "id": 2,
                  "name": "Dragon ball z 2", "number_player": "1-2 joueurs", "time": "200min", "year_published": "2021"}
    games.append(new_game)
    games.append(new_game_2)
    return jsonify({
        "Nb jeux": len(games),
        "Liste de jeux": games
    })


@app.route("/put-jeux/<int:jeu_id>")
def put_jeu_by_id(jeu_id):
    result = {}
    for jeu in games:
        if jeu["id"] == jeu_id:
            jeu["editor"] = "Bandai"
            jeu["category"] = "combat"
            jeu["description"] = "Sangoku doit vaincre les mechants"
            jeu["name"] = "Dragon ball z"
            jeu["year_published"] = "2011"
            jeu["number_player"] = "1-2 joueurs"
            jeu["time"] = "200min"
            result = jsonify({"jeu": jeu})
    return result


app.run()
