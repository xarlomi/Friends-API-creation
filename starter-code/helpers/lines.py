from helpers.mongoConnection import *
from helpers.checking import *
from bson import ObjectId

def insert_quote(obj):
    if not check_params(obj,["line","name", "episode"]):
        return {"response":400,"message":"Bad Request: 'line','name' and  'episode' are obligatory parameters"}
    q = {"line":obj["line"]}
    if check_exists(q,"lines"):
        return {"response":400,"message":"Bad Request: there is already a quote with that name"}
    res = write_coll("lines",obj)
    return res.inserted_id

def list_lines():
    res = read_coll("lines",{})
    response = {c["line"]:str(c["_id"]) for c in res}
    return response

def get_quote(obj):
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"lines"):
        return {"response":400,"message":"Bad Request: quote with given id does not exist"}
    return read_coll("lines",q)

def delete_quote(obj):
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"lines"):
        return {"response":400,"message":"Bad Request: quote with given id does not exist"}
    delete_coll("lines",q)
    return {"response":200,"message":"quote successfully deleted"}

def update_quote(obj):
    if not check_params(obj,["id"],["line","name", "episode"]):
        return {"response":400,"message":"Bad Request: 'id' and at least one of ['line','name','episode'] are obligatory parameters"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"lines"):
        return {"response":400,"message":"Bad Request: quote with given id does not exist"}
    obj.pop("id")
    update_coll("lines",q,obj)
    return {"response":200,"message":"quote successfully updated"}

