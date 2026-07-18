Height=float(input("Enter your height in cm..."))
Weight=float(input("Enter your weight in kg..."))
Height=Height/100
BMI=Weight/(Height*Height)
print(BMI)
if BMI>0:
    if BMI<18.5:
        print("You are underweight!")
    if BMI>=18.5 and BMI<23:
        print("You are healthy!")
    if BMI>=23 and BMI<25:
        print("You are overweight!")
    if BMI>=25 and BMI<30:
        print("You are type 1 obese!")
    if BMI>=30:
        print("You are type 2 obese!")
