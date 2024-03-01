# import requests
# import json
#
# URL = "http://127.0.0.1:8000/stuapi/"
#
# # Read Operation using get method
# def get_data(id = None):
#     data = {}
#     if id is not None:
#         data = {'id':id}
#     headers = {'content-type': 'application/json'}
#     json_data = json.dumps(data)
#     req = requests.get(url=URL,headers=headers, data=json_data)
#     data = req.json()
#     print(data)
#
# # get_data()
#
#
# # To create/insert data using post method
# def post_data():
#     data = {
#         'name':'kenichi',
#         'roll':19,
#         'city':'Tokyo'
#     }
#     headers = {'content-type':'application/json'}
#     json_data = json.dumps(data)
#     req = requests.post(url=URL,headers=headers, data=json_data)
#     data = req.json()
#     print(data)
#
# # post_data()
#
# # Update data using put method
# def update_data():
#     data = {
#         'id':4,
#         'name':'Ketul',
#         'roll': 123,
#         'city':'SK'
#     }
#     headers = {'content-type': 'application/json'}
#     json_data = json.dumps(data)
#     req = requests.put(url=URL,headers=headers, data=json_data)
#     data = req.json()
#     print(data)
#
# # update_data()
#
#
# def delete_data():
#     data = {
#         'id':5,
#     }
#     headers = {'content-type': 'application/json'}
#     json_data = json.dumps(data)
#     req = requests.delete(url=URL,headers=headers, data=json_data)
#     data = req.json()
#     print(data)
#
# delete_data()
#
#
#
#
