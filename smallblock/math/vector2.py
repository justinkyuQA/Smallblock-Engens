import math

class Vector2:

    def __init__(self,x=0.0,y=0.0):
        self.x=float(x)
        self.y=float(y)

    def __add__(self,other):
        return Vector2(self.x+other.x,self.y+other.y)

    def __sub__(self,other):
        return Vector2(self.x-other.x,self.y-other.y)

    def __mul__(self,value):
        return Vector2(self.x*value,self.y*value)

    def length(self):
        return math.sqrt(self.x*self.x+self.y*self.y)

    def normalized(self):
        l=self.length()
        if l==0:
            return Vector2()
        return Vector2(self.x/l,self.y/l)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"
