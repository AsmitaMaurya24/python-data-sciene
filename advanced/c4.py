class Calculation1:
    def Summation(self, a, b):
        return a + b

class Calculation2:
    def Multiplication(self, a, b):
        return a * b
class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a / b
d = Derived()
print(d.Summation(10,30))
print(d.Multiplication(10,30))
print(d.Divide(10,30))