from smallblock.input import Input

inp = Input()

inp.press("W")
inp.press("SPACE")

print("Forward:", inp.down("W"))
print("Jump:", inp.down("SPACE"))

inp.move_mouse(320,240)

print("Mouse:", inp.mouse)

inp.click("LEFT")

print("Left Button:", inp.button_down("LEFT"))
