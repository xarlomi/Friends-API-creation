from helpers.mongoConnection import *
from helpers.checking import *
from bson import ObjectId

def insert_episode(obj):
    if not check_params(obj,["episode","name"]):
        return {"response":400,"message":"Bad Request: 'episode'and 'name' are obligatory parameters"}
    q = {"episode":obj["episode"]}
    if check_exists(q,"episodes"):
        return {"response":400,"message":"Bad Request: that episode already exists"}
    res = write_coll("episodes",obj)
    return res.inserted_id

def list_episodes():
    res = read_coll("episodes",{})
    response = {c["episode"]:str(c["_id"]) for c in res}
    return response

def get_episode(obj):
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"episodes"):
        return {"response":400,"message":"Bad Request: episode with given id does not exist"}
    return read_coll("episodes",q)

def delete_episode(obj):
    if not check_params(obj,["id"]):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"episodes"):
        return {"response":400,"message":"Bad Request: episode with given id does not exist"}
    delete_coll("episodes",q)
    return {"response":200,"message":"episode successfully deleted"}

def update_episode(obj):
    if not check_params(obj,["id"],["episode","name"]):
        return {"response":400,"message":"Bad Request: 'id' and at least one of ['episode','name'] are obligatory parameters"}
    q = {"_id":ObjectId(obj["id"])}
    if not check_exists(q,"episodes"):
        return {"response":400,"message":"Bad Request: episode with given id does not exist"}
    obj.pop("id")
    update_coll("episodes",q,obj)
    return {"response":200,"message":"episode successfully updated"}



