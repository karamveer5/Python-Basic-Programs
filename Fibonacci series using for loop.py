k=int(input("Enter a number: "))
a=0
b=1
print(a,end=' ')
print(b,end=' ')
for i in range(3,k+1):
	c=a+b
	print(c,end=' ')
	a=b
	b=c