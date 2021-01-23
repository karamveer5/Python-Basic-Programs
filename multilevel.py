class Base:
    def k1(self,a):
    	return a

class Derived1(Base):
    def k2(self,a,b):
    	return a+b
    	
class Derived2(Derived1):
    def k3(self,a,b):
    	return a*b
    	
k=Derived2()

print(k.k1(5))
print(k.k2(5,6))
print(k.k3(5,6))