from Concierge import Concierge
import tuser

checkpoint = Concierge()

tuser.CreateUsersBase()

username = input()
password = input()

res = checkpoint.Register(username, password)