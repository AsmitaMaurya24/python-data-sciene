class Calculation1:
    def Summation(self,a,b):
        return a+b

class Calculation2:
    def Multiplication(self,a,b):
            return a*b
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
            return a/b
d = Derived()
print(Summation(10,20))
print(Multiplication(10,20))
print(Divide(10,20))