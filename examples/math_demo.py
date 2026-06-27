from smallblock.math import *

a=Vector2(3,4)
b=Vector2(2,1)

print("a =",a)
print("b =",b)
print("a+b =",a+b)
print("a-b =",a-b)
print("length =",a.length())
print("normalized =",a.normalized())

print("clamp =",clamp(15,0,10))
print("lerp =",lerp(0,100,0.25))
