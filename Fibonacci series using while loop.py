n=int(input("Enter a number:"))
a=0
b=1
c=0
count=1
print("Fibonacci series:",end=' ')
while(count<=n):
	count+=1
	print(c,end=' ')
	a=b
	b=c
	c=a+b