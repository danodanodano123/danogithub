credits=30
oxygen=12
food=12
daysSurvived=0

while True:
    daysSurvived=daysSurvived+1
    oxygen=oxygen-2
    food=food-2
    if daysSurvived==11:
        print(f"\nCongratulations, you survived 10 days!")
        break
    elif credits==0 or oxygen==0 or food==0:
        print(f"\nGame over!")
        break
    print(f"\n--- Day {daysSurvived} ---")
    print(f"Credits: {credits}")
    print(f"Oxygen: {oxygen}")
    print(f"Food: {food}")
    print(f"\nType 1 to spend 10 credits for 5 oxygen, type 2 to spend 10 credits for 5 food, type 3 to save credits")
    playerDecision=int(input(f"\nInput your decision for the day: "))
    if playerDecision==1:
        credits=credits-10
        oxygen=oxygen+5
    elif playerDecision==2:
        credits=credits-10
        food=food+5
    elif playerDecision==3:
        credits=credits+5