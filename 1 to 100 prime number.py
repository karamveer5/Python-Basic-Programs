a = 1

while a<= 100:
    b=0
    i = 2
    
    while(i <=a/2):
        if(a% i == 0):
            b+=1
            break
        i = i + 1

    if (b == 0 and a != 1):
    	print(a)
    a+=1