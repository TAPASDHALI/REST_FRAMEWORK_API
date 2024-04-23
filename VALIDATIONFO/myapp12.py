import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data) 

# get_data()

## this code is use to post any type od data
def post_data():
    data = {
        'name':'ramen',
        'roll':142,
        'city':'puruliya',
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data) 

post_data()


## this code is use to post any type od data
def update_data():
    data = {
        'id': 2,
        'name':'Ravi',
        'city':'DHUPGURI',
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data) 

# update_data()


## this code is use to delete any number id 
def delete_data():
    data = {
        'id': 2,
    }

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data) 

# delete_data()