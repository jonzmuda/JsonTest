import json


while True:
    with open('JSONfile.json') as f:
        data = json.load(f)
        name = input('Name: ')
        try:
            for key in data[name]:
                print(key + ': ' + data[name] [key])
        except KeyError:
            print('Thats not a name!')