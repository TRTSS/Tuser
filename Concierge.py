import os.path
import requests


class Concierge:
    def __init__(self):
        if self.ConfigCheck():
            configs = open("configs.tuser")
            data = configs.readlines()
            self._login = data[0]
            self._pass = data[1]
            self._base = data[2]
        else:
            print("[CONCIERGE] Configs file does not exist. Use 'python tuser.py create' to create base and config "
                  "file.")

    def ConfigCheck(self) -> bool:
        return os.path.exists("./configs.tuser")

    def Register(self, username: str, password: str):
        if self.ConfigCheck():
            configs = open("configs.tuser")
            data = configs.readlines()
            res = requests.post("https://byed.ru/tuser/base/newuser", data={
                "login": data[0].replace("\n", ""),
                "password": data[1].replace("\n", ""),
                "table": data[2].replace("\n", ""),
                "username": username,
                "userPassword": password
            })
            # response = res.json()
            print (res.text)
            # return response[0]['res'] == "ok"
        else :
            print("[CONCIERGE] Configs file does not exist. Use 'python tuser.py create' to create base and config "
                  "file.")
