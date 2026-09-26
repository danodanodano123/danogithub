#def my_function(animal, name):
 # print("I have a", animal)
  #print("My",animal+"'s name is",name)
#my_function("Buddy","dog")
#What I Learned: python functions and arguments, including argument types (postional and keyword)

day=0
hunger=5
happiness=5
energy=5

def add_day():
    global day
    global hunger
    global happiness
    global energy
    print(f"\n--- Day {day} ---")
    print(f"Hunger: {hunger}/10")
    print(f"Happiness: {happiness}/10")
    print(f"Energy: {energy}/10")
    print(f"\nType 1 to play with Max, type 2 to feed Max, type 3 to let him sleep")
    playerDecision=int(input(f"\nInput your decision here: "))
    if playerDecision==1:
        if happiness<9:
            happiness=happiness+1
        elif happiness>9:
            happiness=10
        hunger=hunger-1
        energy=energy-1
    elif playerDecision==2:
        if hunger<9:
            hunger=hunger+1
        elif hunger>9:
            happiness=10
        happiness=happiness-1
        energy=energy-1
    elif playerDecision==3:
        if energy<9:
            energy=energy+1
        elif energy>9:
            energy=10
        happiness=happiness-1
        hunger=hunger-1
    else:
        print("Please choose a valid decision")
        day=day-1

while True:
    day=day+1
    if hunger==0 or happiness==0 or energy==0:
        print(f"\nGame over!")
        break
    add_day()