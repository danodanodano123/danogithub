answer=input("Input a vowel to end the program: ").lower()

while answer not in ("a", "i", "u", "e", "o"):
    print("Not a vowel")
    answer=input("Input a vowel to end the program: ").lower()
print("Program ended")