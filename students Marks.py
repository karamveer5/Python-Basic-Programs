a=float(input("Enter Python subject marks:"))
b=float(input("Enter Data Structure subject marks:"))
c=int(input("Enter Math subject marks:"))
d=float(input("Enter Computer Network subject marks:"))
e=float(input("Enter Data Base Management System subject marks:"))
t=a+b+c+d+e
k=t*100/500
#print(k)
if k>=75:
	print("You have O grade")
elif 60<=k<=74:
	print("You have A grade")
elif 50<=k<=59:
	print("You have B grade")
elif 40<=k<=49:
	print("You have C grade")
else:
	print("You have Fail")
