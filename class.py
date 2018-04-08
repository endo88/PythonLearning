class Orange:
    def __init__(self,w,c):
        """waga podawana jest w gramach"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Utworzono pomarańczę")

    def rot(self,days,temp):
        self.mold = days * temp

or1 = Orange(280,"zielona")
print(or1)
print(or1.weight)
print(or1.color)

or1.weight = 500
or1.color = 'czerwona'

print(or1)
print(or1.weight)
print(or1.color)

or1.rot(10,29)
print(or1.mold)
