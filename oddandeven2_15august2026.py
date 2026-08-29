a=int(input("Enter the lower limit: "))
b=int(input("Enter the upper limit: "))
#value=0
for i in range(a,b):
    #value=value+1
    #num=value%2
    if i%2==0:
        #print(f"{value} --> Even")
        print(f"{i} --> Even")
    else:
        print(f"{i}")
        