# w.a.p.to perform a diffrent list operation

k=['a','e','p','q']
s=[23,56,14,9,10,23]
print("\nThe First List Is:",k)
print("\nThe Second List Is:",s)

print("\nTo Short The Line First:",end='')
k.sort(reverse=True)
print(k)

print("\nTo Count How Much Time 23 Appers In The List s.",end='')
a=s.count(23)
print("Count List Is:",a)

s.insert(2,-1)
print("\nInsert -1 In 2nd Position In 2nd List:",s)

print("\nTo Append The 4 In The 2nd List:",end="")
s.append(4)
print(s)

print("\nTo Extend The List Into 2nd List:",end='')
s.extend(k)
print(s)

print("\nTo Reverse The List s:",end='')
s.reverse()
print(s)