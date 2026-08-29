import random
score = 0
for i in range(10):
    a = random.randint(1,10)
    b = random.randint(1,10)
    answer=int(input(f"What is {a} + {b}? "))
    if answer==a+b:
        score=score+10
        print("Correct answer!")
        print(f"Score: {score}/100")
    if answer!=a+b:
        print("Wrong answer!")
        print(f"Score: {score}/100")
print(f"Test done! Your score is {score}/100")