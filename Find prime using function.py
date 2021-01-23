def prime():
	a=int(input("Enter a number "))
	b=0
	i=1
	for i in range(1,a+1):
		if a%i==0:
			b+=1
	if b==2:
		print("it is prime number")
	else:
		print("it is not a prime number")
		
prime()