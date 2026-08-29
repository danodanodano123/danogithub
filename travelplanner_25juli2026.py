Destination=(input("What's your destination? (beach/mountain) "))
Weather=(input("What's the weather like? (sunny/rainy) "))
Budget=int(input("How much is your budget in Rp? "))

if Destination==("beach"):
    if Weather==("sunny"):
        if Budget>=1000000:
            print("Enjoy your sunny day out, splurge your money a little bit!")
        if Budget<100000:
            print("Enjoy your sunny day out! Make sure you're careful with your food spending!")
    if Weather==("rainy"):
        if Budget>=1000000:
            print("Stay indoors, enjoy a seaside cafe!")
        if Budget<1000000:
            print("Stay indoors, maybe try some of the food stalls!")
if Destination==("mountain"):
    if Weather==("sunny"):
        if Budget>=1000000:
            print("Enjoy your hike, make sure to be safe and try some of the tourist attractions there!")
        if Budget<1000000:
            print("Enjoy your hike, make sure to be safe and enjoy the scenery!")
    if Weather==("rainy"):
        if Budget>=1000000:
            print("Make sure to bring a raincoat, and enjoy the scenery from a sky-high cafe!")
        if Budget<1000000:
            print("Make sure to bring a raincoat, stay indoors and enjoy the mountain scenery!")
if (Destination!=("mountain") and Destination!=("beach")) or (Weather!=("sunny") and Weather!=("rainy")) :
    print("Well, just make sure you stay within budget and have a nice stay!")