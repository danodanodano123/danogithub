Numberone=float(input("First number:"))
Numbertwo=float(input("Second number:"))
Operation=int(input("Choose the operation! Type 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for finding the remainder, and 6 for powers. "))

if Operation==1:
    Result1=Numberone+Numbertwo
    print(Result1)
if Operation==2:
    Result2=Numberone-Numbertwo
    print(Result2)
if Operation==3:
    Result3=Numberone*Numbertwo
    print(Result3)
if Operation==4:
    Result4=Numberone/Numbertwo
    print(Result4)
if Operation==5:
    Result5=Numberone%Numbertwo
    print(Result5)
if Operation==6:
    Result6=Numberone**Numbertwo
    print(Result6)
