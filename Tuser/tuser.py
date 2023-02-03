import os
import sys
import requests
from prettytable import PrettyTable

LIB_FOLDER = os.path.dirname(os.path.realpath(__file__))

def QuikBaseCreate():
    if os.path.exists("../configs.tuser"):
        d = input("You already have quik Tuser base connected to your project. Do you want to create another? [y/n]: ")
        if d.lower() != "y":
            print("New Tuser base creation is stopped.")
            return
    BaseName = input('Base name: ')

    res = requests.post("https://ziplit.online/tuser/base/create", data={"name": BaseName})
    data = res.json()

    keys = data.keys()
    if data['res']:
        configFile = open("../configs.tuser", 'w')
        for i in keys:
            if i != "res":
                configFile.write(data[i] + "\n")
        print(f"Base {BaseName} created. Config file created, DO NOT change it and KEEP IT SAFE.")
    else:
        print(f"Error appears: {data['verbose']}")


def GetBaseStruct():
    if os.path.exists("../configs.tuser"):
        configs = open("../configs.tuser")
        data = configs.readlines()
        res = requests.post("https://ziplit.online/tuser/base/cols", data={
            "login": data[0].replace("\n", ""),
            "password": data[1].replace("\n", ""),
            "table": data[2].replace("\n", "")
        })
        response = res.json()[0]
        colsTable = PrettyTable()
        colsTable.field_names = ["#", "Field name", "Field type"]
        i = 1
        for col in response['content']:
            colsTable.add_row([i, col['Field'], col['Type']])
            i += 1
        print (colsTable)
    else:
        raise Exception(f"Tuser base error: There is no Tuser config file.")


def AddBaseCol (colName, colType):
    if os.path.exists("../configs.tuser"):
        configs = open("../configs.tuser")
        data = configs.readlines()
        res = requests.post("https://ziplit.online/tuser/base/addcol", data={
            "login": data[0].replace("\n", ""),
            "password": data[1].replace("\n", ""),
            "table": data[2].replace("\n", ""),
            "colName": colName,
            "colType": colType
        })
        response = res.json()[0]
        if response['res']:
            print ("Field added to Tuser base.")
        else:
            print (response['verbose'])
    else:
        raise Exception(f"Tuser base error: There is no Tuser config file.")

def main ():
    if sys.argv[1] == "quick":
        QuikBaseCreate()
    if sys.argv[1] == "struct":
        GetBaseStruct()
    if sys.argv[1] == "add-field":
        AddBaseCol(sys.argv[2], sys.argv[3])
    if sys.argv[1] == "libpath":
        print (LIB_FOLDER)