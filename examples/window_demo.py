from smallblock.graphics.window import Window

win=Window(640,480,"SmallBlock Graphics v1.0")

win.line(0,0,640,480,"red")
win.line(640,0,0,480,"green")

win.rect(40,40,140,80,"yellow")

win.fill_rect(240,60,120,120,"blue")

win.circle(500,120,50,"magenta")

win.text(
20,
430,
"SmallBlock Graphics Engine v1.0",
"white"
)

win.run()
