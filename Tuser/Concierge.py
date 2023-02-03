import os.path
import requests

LIB_FOLDER = os.path.dirname(os.path.realpath(__file__))

class OperationStatus:
    def __init__(self, ok, systemVerbose=None, errorCode=None, data=None):
        self.ok = ok
        self.systemVerbose = systemVerbose
        self.errorCode = errorCode
        self.data = data
        print (LIB_FOLDER)


class User:
    def __init__(self, userId=None, username=None):
        self.id = userId
        self.username = username


class Concierge:
    def ConfigCheck(func):
        def newFunc(*args):
            if os.path.exists("../configs.tuser"):
                return func(*args)
            else:
                raise Exception(f"Tuser base error: There is no Tuser config file.")

        return newFunc

    def GetConfigs (self):
        configs = open("../configs.tuser")
        data = configs.readlines()
        data = [x.replace("\n", "") for x in data]
        return {"login": data[0], "password": data[1], "table": data[2]}

    def __init__(self):
        try:
            data = self.GetConfigs()
            self.user = User()
            self._login = data["login"]
            self._pass = data["password"]
            self._base = data["table"]
        except:
            raise Exception(f"Tuser base error: There is no Tuser config file.")

    @ConfigCheck
    def Register(self, username: str, password: str) -> OperationStatus:
        """
        Method for registering a new user. If there is no configuration file, Tuser will throw an exception.
        Takes 2 arguments username and password. Returns the operation status object.
        :param username:
        :param password:
        :return: OperationStatus
        """
        res = requests.post("https://ziplit.online/tuser/base/newuser", data={
            "login": self._login,
            "password": self._pass,
            "table": self._base,
            "username": username,
            "userPassword": password
        })
        response = res.json()[0]

        return OperationStatus(ok=response.get("res"), systemVerbose=response.get("verbose"),
                               errorCode=response.get("errorCode"))

    @ConfigCheck
    def Login(self, username: str, password: str) -> OperationStatus:
        """
        Method for user authentication. If there is no configuration file, Tuser will throw an exception. Takes 2
        arguments: username and password. Returns the operation status object. In case of successful authorization,
        the Concierge object will contain the user object in the 'user' field.
        :param username:
        :param password:
        :return: OperationStatus
        """
        res = requests.post("https://ziplit.online/tuser/base/login", data={
            "login": self._login,
            "password": self._pass,
            "table": self._base,
            "username": username,
            "userPassword": password
        })
        response = res.json()[0]
        print (response)
        status = OperationStatus(ok=response.get("res"), systemVerbose=response.get("verbose"),
                                 errorCode=response.get("errorCode"))

        if status.ok:
            userObj = User(userId=response['data']['id'], username=response['data']['username'])
            self.user = userObj
            status.data = userObj

        return status

    @ConfigCheck
    def SetUserField (self, fieldName: str, fieldValue, userId = None) -> OperationStatus:
        """
        A method for setting a new value to an authorized user's field. If there is no configuration file,
        Tuser will throw an exception. Takes 2 required arguments: field name and value. Takes 1 optional
        argument - User ID. If the user ID is not set, the current authorized user from the Concierge object is taken
        as the ID. Returns the operation status object.
        :param fieldName:
        :param fieldValue:
        :param userId:
        :return: OperationStatus
        """
        if userId is None:
            userId = self.user.id
        res = requests.post("https://ziplit.online/tuser/base/setfield", data={
            "login": self._login,
            "password": self._pass,
            "table": self._base,
            "field": fieldName,
            "value": fieldValue,
            "tuserId": userId
        })
        response = res.json()[0]
        status = OperationStatus(ok=response.get("res"), systemVerbose=response.get("verbose"),
                                 errorCode=response.get("errorCode"))

        return status

    @ConfigCheck
    def GetUserField(self, fieldName: str, userId = None) -> OperationStatus:
        """
        A method for getting the value of an authorized user's field. If there is no configuration file, Tuser will
        throw an exception. Takes 1 required argument - the name of the field. Takes 1 optional argument - User
        ID. If the user ID is not set, the current authorized user from the Concierge object is taken as the ID.
        Returns the operation status object.
        :param fieldName:
        :param userId:
        :return: OperationStatus
        """
        if userId is None:
            userId = self.user.id
        res = requests.post("https://ziplit.online/tuser/base/getfield", data={
            "login": self._login,
            "password": self._pass,
            "table": self._base,
            "field": fieldName,
            "tuserId": userId
        })
        response = res.json()[0]
        status = OperationStatus(ok=response.get("res"), systemVerbose=response.get("verbose"),
                                 errorCode=response.get("errorCode"), data=response.get("data"))
        return status
