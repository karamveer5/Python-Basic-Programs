def fact():
	a=int(input("Enter a number "))
	fact=1
	if a<0:
		print("factorial is does not exist")
	elif a==0:
		print(a," factorial is 0")
	else:
		for i in range(1,a+1):
			fact=fact*i
		print(f"{a} factorial is {fact}")
		
fact()