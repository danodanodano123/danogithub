items = []
while True:
    print(f"\nItems: {items}")
    print(f"You have woke up locked in a wizard's tower, and you need the Golden Key to escape... What shall you do?\n1) Search around (adds an item)\n2) Throw away an item (removes an item)\n3) Try to open the exit door\n4) Just give up (ends the game)")
    choice=int(input("Input a choice number (1-4): "))
    if choice == 1:
        playerinput=input("What did you find? ")
        items.append(playerinput)
    elif choice == 2:
         playerinput=input("What will you remove? ")
         if playerinput not in items:
              print("Not a valid move")
         else:
              items.remove(playerinput)
    elif choice == 3:
        if "Golden Key" in items:
              print("You escaped the wizard's tower!")
              break
        else:
            print("The door is locked, and you don't have the key.")
    elif choice == 4:
         break
    else:
            print("Not a valid choice")