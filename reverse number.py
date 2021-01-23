num=int(input("Enter a number:"))
sum=0
while num!=0:
    rem=num%10
    sum=10*sum+rem
    num=num//10
print("The number is:",sum)
