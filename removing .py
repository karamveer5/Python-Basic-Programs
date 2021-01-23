#,w.a.p.to print a specified list after removing 0th 2nd 4th 5th element

k=[1,2,3,4,5,6,7,8]
i=[0,2,4,5]
for i in sorted(i,reverse=True):
	del k[i]
print(k)	