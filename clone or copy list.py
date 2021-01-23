num = int(input("Enter the Number: "))

for i in range(0, num):
    for j in range(0, i):
        print(" ", end="")
    for j in range(i*2, num*2-1):
        print("*", end="")
    print()
