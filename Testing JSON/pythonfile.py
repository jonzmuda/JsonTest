import json

with open('C:\\Users\\jonzm\\Desktop\\Projects\\Testing JSON\\JSONfile.json') as f:
    data = json.load(f)
    name = input('Name: ')
    for key in data[name]:
        print(key + ': ' + data[name][key])