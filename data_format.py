import copy
import json

DEFULT_DICT = {
    "iter": 0,
    "dtype":"none",
    "o_place":"none",
    "user_name":"none",
    "status":"none"
    #"cotent":"none"
}


def raw_gen():
    return copy.deepcopy(DEFULT_DICT)

def j2d(data:str):
    return json.loads(data)

def d2j(data:dict):
    return json.dumps(data)

def user2web_format(place,name,status,content = ""):
    u2w_dict = raw_gen()
    
    u2w_dict['dtype'] = "u2w"
    u2w_dict['o_place'] = place
    u2w_dict['user_name'] = name
    u2w_dict['status'] = status
    #u2w_dict['content'] = content

    return u2w_dict