from flask import Flask, request
from bson import json_util
from helpers.characters import *
from helpers.lines import *
from helpers.episodes import *

app = Flask(__name__)

#characters.py

@app.route("/characters/new")
def  characters_new():
    args = dict(request.args)
    id = insert_character(args)
    return json_util.dumps({"_id":id})

@app.route("/characters")
def characters():
    return json_util.dumps(list_characters())

@app.route("/characters/details")
def characters_details():
    args = dict(request.args)
    return json_util.dumps(get_character(args))

@app.route("/characters/delete")
def characters_delete():
    args = dict(request.args)
    return json_util.dumps(delete_character(args))

@app.route("/characters/edit")
def characters_edit():
    args = dict(request.args)
    return json_util.dumps(update_character(args))

# lines.py

@app.route("/lines/new")
def  lines_new():
    args = dict(request.args)
    id = insert_quote(args)
    return json_util.dumps({"_id":id})

@app.route("/lines")
def lines():
    return json_util.dumps(list_lines())

@app.route("/lines/details")
def lines_details():
    args = dict(request.args)
    return json_util.dumps(get_quote(args))

@app.route("/lines/delete")
def lines_delete():
    args = dict(request.args)
    return json_util.dumps(delete_quote(args))

@app.route("/lines/edit")
def lines_edit():
    args = dict(request.args)
    return json_util.dumps(update_quote(args))


@app.route("/characters/quotes")
def characters_quotes():
    args = dict(request.args)
    return json_util.dumps(get_quotes(args))

#episodes.py

@app.route("/episodes/new")
def  episodes_new():
    args = dict(request.args)
    id = insert_episode(args)
    return json_util.dumps({"_id":id})

@app.route("/episodes")
def episodes():
    return json_util.dumps(list_episodes())

@app.route("/episodes/details")
def episodes_details():
    args = dict(request.args)
    return json_util.dumps(get_episode(args))

@app.route("/episodes/delete")
def episodes_delete():
    args = dict(request.args)
    return json_util.dumps(delete_episode(args))

@app.route("/lines/edit")
def episodes_edit():
    args = dict(request.args)
    return json_util.dumps(update_episode(args))


app.run(debug=True)