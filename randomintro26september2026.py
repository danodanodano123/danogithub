import random
length=int(input(("How many characters do you want in your password? (min. 6)")))
char="qwertyuiopasdfghjkllzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()"
p="".join(random.sample(char, length))
print (p)
