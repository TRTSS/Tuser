from Concierge import Concierge

checkpoint = Concierge()

username = input("login: ")
password = input("password: ")

res = checkpoint.Register(username, password)

if res.ok:
    print (f"You are registed, {username}!")
else:
    print (f"Ooops... some troubles appear, {username}. {res.ok} {res.errorCode} {res.systemVerbose}")