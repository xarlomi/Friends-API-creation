from flask import Flask, request
from helpers.mongoConnection import  insert, read
from bson import json_util, ObjectId
from helpers.checking import check_mandatory

app = Flask("friendsapi")

@app.route("/characters")
def characters():
    # An empty dictionary as query will return all documents in collection
    data = read({},"characters", project={"name":1})
    # Because our data contains ObjectId's, that are not automatically converted to 
    # data types compatible with json, we use `json_util.dumps` to do so.
    return json_util.dumps(data)

# To fetch argument from endpoint, enclose in < > and add to function signature
@app.route("/characters/details/<characters_id>")
def characters_details(characters_id):
    try:
        id_ = ObjectId(characters_id)
    except:
        # Returning an int after json response will set it to the HTTP response code
        # Default is 200 OK.
        return {"Error":"characters_id not valid!"},400
        # Error code 400 means Bad Request.
    q = {"_id":id_}
    data = read(q,"characters")
    if len(data) == 0:
        return {"Error":"No friends character with given id!"}
    return json_util.dumps(data)


@app.route("/characters/new")
def characters_new():
    # All the query parameters (The parameters following the ? on the url or the params in `requests.get`)
    # are recognized by flask on a dictionary and stored in `request.args`
    # This, however, is an InmutableDictionary object. We convert it to a regular dictionary.
    args = dict(request.args)
    # Checking if all necessary parameters were given
    if not check_mandatory(args,["name", "personality", "job"]):
        return {"Error":"missing obligatory parameter"}
    
    q = {"name":args["name"]}
    # We try to find a celebrity with the same name
    data = read(q,"characters")
    # If there is any response, data will contain an element
    if len(data)>0:
        return {"Error":"Friends character already exists"}
    res = insert(args,"characters")
    return json_util.dumps({"_id":res})

@app.route("/characters/remove")
def characters_remove():
    # All the query parameters (The parameters following the ? on the url or the params in `requests.get`)
    # are recognized by flask on a dictionary and stored in `request.args`
    # This, however, is an InmutableDictionary object. We convert it to a regular dictionary.
    args = dict(requests.args)
    # Checking if all necessary parameters were given
    if not check_mandatory(args,"name"):
        return {"Error":"missing obligatory parameter"}
    
    q = {"name":args["name"]}
    # We try to find a celebrity with the same name
    data = read(q,"characters")
    # If there is any response, data will contain an element
    if len(data)<0:
        return {"Error":"Friends character not in our database"}
    res = delete(args,"characters")
    return json_util.dumps({"_id":res})

@app.route("/lines")
def lines():
    # An empty dictionary as query will return all documents in collection
    data = read({},"lines", project={"line":1})
    # Because our data contains ObjectId's, that are not automatically converted to 
    # data types compatible with json, we use `json_util.dumps` to do so.
    return json_util.dumps(data)

# To fetch argument from endpoint, enclose in < > and add to function signature
@app.route("/lines/details/<lines_id>")
def lines_details(lines_id):
    try:
        id_ = ObjectId(lines_id)
    except:
        # Returning an int after json response will set it to the HTTP response code
        # Default is 200 OK.
        return {"Error":"lines_id not valid!"},400
        # Error code 400 means Bad Request.
    q = {"_id":id_}
    data = read(q,"lines")
    if len(data) == 0:
        return {"Error":"No characters´ lines with given id!"}
    return json_util.dumps(data)

@app.route("/lines/<name>")
def names_details(name):
    nombre =  (name)
    q = {"name":nombre}
    data = read(q,"lines")
    if len(data) == 0:
        return {"Error":"No characters´ lines with given name!"}
    return json_util.dumps(data)



@app.route("/lines/new")
def lines_new():
    # All the query parameters (The parameters following the ? on the url or the params in `requests.get`)
    # are recognized by flask on a dictionary and stored in `request.args`
    # This, however, is an InmutableDictionary object. We convert it to a regular dictionary.
    args = dict(request.args)
    # Checking if all necessary parameters were given
    if not check_mandatory(args,["line", "name", "episode"]):
        return {"Error":"missing obligatory parameter"}
    
    q = {"line":args["line"]}
    # We try to find a celebrity with the same name
    data = read(q,"lines")
    # If there is any response, data will contain an element
    if len(data)>0:
        return {"Error":"That line already exists"}
    res = insert(args,"lines")
    return json_util.dumps({"_id":res})    

app.run(debug=True) 