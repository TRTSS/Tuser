import sys
import requests


def CreateUsersBase():
    BaseName = input('Base name: ')

    res = requests.post("https://ziplit.online/tuser/base/create", data={"name": BaseName})
    data = res.json()

    keys = data.keys()
    if data['res']:
        configFile = open("configs.tuser", 'w')
        for i in keys:
            if (i != "res"):
                configFile.write(data[i] + "\n")
        print (f"Base {BaseName} created. Config file created, DO NOT change it and KEEP IT SAFE.")
    else:
        print (f"Error appears: {data['verbose']}")


if sys.argv[1] == "create":
    CreateUsersBase()