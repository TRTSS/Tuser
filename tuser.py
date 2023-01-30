import sys
import requests


def CreateUsersBase():
    BaseName = input('Base name: ')

    res = requests.post("http://77.222.52.155:7777/zuvs.ru/tuser/base/create", data={"name": BaseName})
    data = res.json()

    keys = data.keys()
    if data['res']:
        configFile = open("configs.tuser", 'w')
        for i in keys:
            configFile.write(data[i] + "\n")
        print (f"Base {BaseName} created. Config file created, DO NOT change it and KEEP IT SAFE.")
    else:
        print (f"Error appears: {data['verbose']}")


if sys.argv[1] == "create":
    CreateUsersBase()