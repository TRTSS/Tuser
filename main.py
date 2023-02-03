import os
import random

from Concierge import Concierge

checkpoint = Concierge()

wallet = 0


def Regist():
    username = input("Regist Username: ")
    password = input("Regist Password: ")

    status = checkpoint.Register(username, password)
    if status.ok:
        print("You are registed! Now you can login.")
    else:
        print("Ops... something go wrong... try again or later")


def Login() -> bool:
    username = input("Login Username: ")
    password = input("Login Password: ")

    status = checkpoint.Login(username, password)
    if status.ok:
        print("Great! You logged in!")
        return True
    else:
        print("Ops... something go wrong... try again or later")
        return False


while True:
    print("Welcome to GUESS THE NUMBER game!\nGuess what you want to do:")
    print("1 - Play\n2 - Login\n3 - Regist")
    print(f"WALLET: {wallet}")
    cmd = input()
    os.system('cls')
    if cmd == "1":
        if checkpoint.user.id is None:
            c = input("Do you want to create an account to save your scores? (Y/N) ")
            if c.lower() == "y":
                os.system('cls')
                print("Alright! Choose 2 or 3!")
                continue
        guessTo = random.randint(1, 5)
        n = [int(x) for x in input("Enter 3 numbers: ").split()]
        bank = 300
        for i in range(3):
            if n[i] == guessTo:
                os.system('cls')
                print(f"You win with number {n[i]}! You get {bank} points")
                wallet += bank
                checkpoint.SetUserField("scores", wallet)
            else:
                bank -= 100
                if bank == 0:
                    os.system('cls')
                    print(f"You lose! The number was {guessTo}")
    if cmd == "2":
        if Login():
            status = checkpoint.GetUserField("scores")
            os.system('cls')
            if status.ok:
                wallet = int(status.data)
                print ("Your wallet is synced.")
            else:
                print("Troubles with wallet sync")
    if cmd == "3":
        Regist()
