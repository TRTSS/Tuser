import os
import sys
import requests


def QuikBaseCreate():
    if os.path.exists("./configs.tuser"):
        d = input("You already have quik Tuser base connected to your project. Do you want to create another? [y/n]: ")
        if d.lower() != "y":
            print("New Tuser base creation is stopped.")
            return
    BaseName = input('Base name: ')

    res = requests.post("https://ziplit.online/tuser/base/create", data={"name": BaseName})
    data = res.json()

    keys = data.keys()
    if data['res']:
        configFile = open("configs.tuser", 'w')
        for i in keys:
            if i != "res":
                configFile.write(data[i] + "\n")
        print(f"Base {BaseName} created. Config file created, DO NOT change it and KEEP IT SAFE.")
    else:
        print(f"Error appears: {data['verbose']}")


def BaseAddCol(name: str, type: str, defaultValue):
    pass


if sys.argv[1] == "quik":
    QuikBaseCreate()
