from smallblock.graphics import *

canvas = Canvas(256,256)

canvas.clear((15,15,25))

line(canvas,0,0,255,255,(255,0,0))
line(canvas,255,0,0,255,(0,255,0))

rectangle(canvas,20,20,80,60,(255,255,0))
fill_rect(canvas,30,30,60,40,(60,60,255))

circle(canvas,180,70,40,(255,0,255))
circle(canvas,180,70,20,(0,255,255))

triangle(canvas,50,180,20,240,80,240,(255,255,255))
triangle(canvas,170,160,230,230,120,220,(255,180,0))

canvas.save("exports/graphics_v03.ppm")

print("Graphics Engine v0.3")
print("Created exports/graphics_v03.ppm")
