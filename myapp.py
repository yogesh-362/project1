import requests
import json

URL = "http://127.0.0.1:8000/stuAPI/"

# Read Operation using get method
def get_data(id = None):
    data = { }
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    req = requests.get(url=URL, data=json_data)
    data = req.json()
    print(data)

get_data()


# To create/insert data using post method
def post_data():
    data = {
        'name':'Yohan',
        'roll':15,
        'city':'Tokyo'
    }
    json_data = json.dumps(data)
    req = requests.post(url=URL, data=json_data)
    data = req.json()
    print(data)

# post_data()

# Update data using put method
def update_data():
    data = {
        'id':5,
        'name':'Ketul',
        'city':'SK'
    }
    json_data = json.dumps(data)
    req = requests.put(url=URL, data=json_data)
    data = req.json()
    print(data)

# update_data()


def delete_data():
    data = {
        'id':5,
    }
    json_data = json.dumps(data)
    req = requests.delete(url=URL, data=json_data)
    data = req.json()
    print(data)

# delete_data()




