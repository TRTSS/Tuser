import os.path
import requests


class OperationStatus:
    def __init__(self, ok, systemVerbose=None, errorCode=None):
        self.ok = ok
        self.systemVerbose = systemVerbose
        self.errorCode = errorCode


class Concierge:
    def __init__(self):
        if self.ConfigCheck():
            configs = open("configs.tuser")
            data = configs.readlines()
            self._login = data[0]
            self._pass = data[1]
            self._base = data[2]
        else:
            raise Exception(f"Tuser base error: There is no Tuser config file.")

    def ConfigCheck(self) -> bool:
        return os.path.exists("./configs.tuser")

    def Register(self, username: str, password: str) -> OperationStatus:
        if self.ConfigCheck():
            configs = open("configs.tuser")
            data = configs.readlines()
            res = requests.post("https://ziplit.online/tuser/base/newuser", data={
                "login": data[0].replace("\n", ""),
                "password": data[1].replace("\n", ""),
                "table": data[2].replace("\n", ""),
                "username": username,
                "userPassword": password
            })
            response = res.json()[0]

            return OperationStatus(ok=response.get("res"), systemVerbose=response.get("verbose"), errorCode=response.get("errorCode"))
        else:
            raise Exception(f"Tuser base error: There is no Tuser config file.")
