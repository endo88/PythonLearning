class Rectangle():
    recs = []

    def __init__(self,w,l):
        self.width = w
        self.length = l
        self.recs.append((self.width,self.length))

    def print_size(self):
        print("""{} na {}""".format(self.width,self.length))

r1 = Rectangle(10,24)
r2 = Rectangle(100,200)
r3 = Rectangle(50,20)

print(Rectangle.recs)
