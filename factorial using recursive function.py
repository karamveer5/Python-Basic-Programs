def Recursive(n):
    if n==0:
        return 1
    else:
        return n*Recursive(n-1)
num=int(input("Enter a number:"))
print("The factorial is:",Recursive(num))