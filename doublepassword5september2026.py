password1="reza727"
password2="well"

while True:
    userinp1=(input("Enter the first passkey: "))
    userinp2=(input("Enter the second passkey: "))
    if userinp1==password1 and userinp2==password2:
        print("Access granted!")
        break
    else:
        print("Access denied!")