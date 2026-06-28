from smallblock.input import Input

inp = Input()

inp.bind("left", "A", "LEFT")
inp.bind("right", "D", "RIGHT")
inp.bind("jump", "SPACE")

inp.press("A")

print("Move Left :", inp.action("left"))
print("Move Right:", inp.action("right"))
print("Jump      :", inp.action("jump"))

inp.next_frame()

inp.release("A")
inp.press("SPACE")

print()

print("A Released :", inp.released("A"))
print("Jump Press :", inp.pressed("SPACE"))
