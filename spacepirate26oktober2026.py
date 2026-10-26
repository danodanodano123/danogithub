armory=["Dagger", "Longsword", "Mace", "Longbow", "Crossbow", "Hand Cannon", "Trebuchet", "Battering Ram"]
taken=[]
dhealth=100
choice=0

while choice!=1 and choice!=2 and choice!=3:
    choice=int(input("There are three types of weapons in the King's armory: Melee, ranged, and massive siege weapons. Pick one type to take under your command: (1/2/3) "))
    if choice==1:
        taken=armory[0:3]
    elif choice==2:
        taken=armory[3:6]
    elif choice==3:
        taken=armory[6:]
    else:
        print("Not a valid choice")

print(f"\nA dragon has attacked the kingdom! Use your weapons to eliminate it!")
while dhealth>0:
    print(f"\nDragon Health: {dhealth}")
    print(f"Your weapons: {taken}")
    choice1=input("Which weapon shall you use? ")
    if choice1 in taken:
        if choice1=="Dagger":
            dhealth-=5
            print("The dragon has taken 5 damage!")
        if choice1=="Longsword":
            dhealth-=10
            print("The dragon has taken 10 damage!")
        if choice1=="Mace":
            dhealth-=15
            print("The dragon has taken 15 damage!")
        if choice1=="Longbow":
            dhealth-=25
            print("The dragon has taken 25 damage!")
        if choice1=="Crossbow":
            dhealth-=20
            print("The dragon has taken 20 damage!")
        if choice1=="Hand Cannon":
            dhealth-=30
            print("The dragon has taken 30 damage!")
        if choice1=="Battering Ram":
            dhealth-=35
            print("The dragon has taken 35 damage!")
        if choice1=="Trebuchet":
            dhealth-=45
            print("The dragon has taken 45 damage!")
    else:
        print("Not a valid choice")

    if dhealth<=0:
        print(f"\nDragon Health: 0\nYou have eliminated the dragon!")