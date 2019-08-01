
import json

"""
a='{"name":"Sagar","age":"45","city":"Pune"}'
b=json.loads(a)
print(a)

"""
# fetching data from person.json file . It should be located at D:/Result
with open("D:/Result/person.json") as jsondata:
    data=json.load(jsondata)

print(data)
#print(data['name'])   Accessing single data from json file


for i in data:
    if data['name'] == i['name'] or data['name'] == i['name'] or data['name'] == i['name']:
        print("json catch correct name of user")
    else:
        print("wrong")
