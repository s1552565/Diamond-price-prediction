# input from user
n = int(input("enter the number of stars to print"))
boolean = bool(int(input("n")))

if boolean == True:
    for i in range(n):
        print("*"*i)
elif boolean == False:
    for i in range(n):
        print("*"*(n-i))