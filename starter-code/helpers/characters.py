from helpers.mongoConnection import *
from helpers.checking import *
from bson import ObjectId

def insert_character(obj):
    if not check_params(obj,["name","personality","job"]):
        return {"response":400,"message":"Bad Request: 'name', 'personality' and 'job' are obligatory parameters"}
    q = {"name":obj["name"]}
    if check_exists(q,"characters"):
        return {"response":400,"message":"Bad Request: there is already a character with that name"}
    res = write_coll("characters",obj)
    return res.inserted_id

def list_characters():
    res = read_coll("characters",{})
    response = {c["name"]:str(c["_id"]) for c in res}
    return response

def get_character(obj):
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"characters"):
        return {"response":400,"message":"Bad Request: character with given id does not exist"}
    return read_coll("characters",q)

def delete_character(obj):
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"characters"):
        return {"response":400,"message":"Bad Request: character with given id does not exist"}
    delete_coll("characters",q)
    return {"response":200,"message":"character successfully deleted"}

def update_character(obj):
    if not check_params(obj,["id"],["name","personality","job"]):
        return {"response":400,"message":"Bad Request: 'id' and at least one of ['name', 'personality' , 'job'] are obligatory parameters"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"characters"):
        return {"response":400,"message":"Bad Request: character with given id does not exist"}
    obj.pop("id")
    update_coll("characters",q,obj)
    return {"response":200,"message":"character successfully updated"}

