import random

userscore=0
aiscore=0
wincondition=3
aichoices = ["rock", "paper", "scissors"]

print("Rock, paper, scissors! The first to reach 3 wins will win the whole game!")


def userwins():
    print(f"The AI's choice was {finalaichoice}")
    print("You won this round!")
    global userscore
    userscore += 1

def userloses():
    print(f"The AI's choice was {finalaichoice}")
    print("You lost this round!")
    global aiscore 
    aiscore += 1

def tie():
    print(f"The AI's choice was {finalaichoice}")
    print("It's a tie this round!")

while userscore<wincondition and aiscore<wincondition:
    userchoice = input(f"\nShoot! (input rock/paper/scissors) ")
    finalaichoice = random.choice(aichoices)
    if userchoice=="rock":
        if finalaichoice=="paper":
            userloses()
        elif finalaichoice=="scissors":
            userwins()
        else:
            tie()
    elif userchoice=="paper":
        if finalaichoice=="rock":
            userwins()
        elif finalaichoice=="scissors":
            userloses()
        else:
            tie()
    elif userchoice=="scissors":
        if finalaichoice=="rock":
            userloses()
        elif finalaichoice=="paper":
            userwins()
        else:
            tie()
    else:
        print("Not a valid choice")

    if userscore==wincondition:
        print(f"\nYou have won the game!")
    if aiscore==wincondition:
        print(f"\nThe AI has won the game!")