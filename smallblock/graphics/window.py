import tkinter as tk

class Window:

    def __init__(self,width,height,title="SmallBlock"):
        self.width=width
        self.height=height

        self.root=tk.Tk()
        self.root.title(title)

        self.canvas=tk.Canvas(
            self.root,
            width=width,
            height=height,
            bg="black",
            highlightthickness=0
        )

        self.canvas.pack()

    def pixel(self,x,y,color):
        self.canvas.create_line(
            x,y,
            x+1,y,
            fill=color
        )

    def line(self,x1,y1,x2,y2,color):
        self.canvas.create_line(
            x1,y1,
            x2,y2,
            fill=color
        )

    def rect(self,x,y,w,h,color):
        self.canvas.create_rectangle(
            x,
            y,
            x+w,
            y+h,
            outline=color
        )

    def fill_rect(self,x,y,w,h,color):
        self.canvas.create_rectangle(
            x,
            y,
            x+w,
            y+h,
            outline=color,
            fill=color
        )

    def circle(self,x,y,r,color):
        self.canvas.create_oval(
            x-r,
            y-r,
            x+r,
            y+r,
            outline=color
        )

    def text(self,x,y,text,color):
        self.canvas.create_text(
            x,
            y,
            text=text,
            fill=color,
            anchor="nw"
        )

    def run(self):
        self.root.mainloop()
