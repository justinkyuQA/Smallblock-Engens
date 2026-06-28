import time
import tkinter as tk


class Window:
    def __init__(self, width, height, title="SmallBlock"):
        self.width = width
        self.height = height
        self.title = title

        self.root = tk.Tk()
        self.root.title(title)
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=width,
            height=height,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack()

        self.back = []
        self.running = False
        self.last_time = time.time()
        self.fps = 0

    def begin(self):
        self.back = []

    def present(self):
        self.canvas.delete("all")

        for item in self.back:
            kind = item[0]
            args = item[1:]

            if kind == "pixel":
                x, y, color = args
                self.canvas.create_line(x, y, x + 1, y, fill=color)

            elif kind == "line":
                x1, y1, x2, y2, color = args
                self.canvas.create_line(x1, y1, x2, y2, fill=color)

            elif kind == "rect":
                x, y, w, h, color = args
                self.canvas.create_rectangle(x, y, x + w, y + h, outline=color)

            elif kind == "fill_rect":
                x, y, w, h, color = args
                self.canvas.create_rectangle(x, y, x + w, y + h, outline=color, fill=color)

            elif kind == "circle":
                x, y, r, color = args
                self.canvas.create_oval(x - r, y - r, x + r, y + r, outline=color)

            elif kind == "text":
                x, y, text, color = args
                self.canvas.create_text(x, y, text=text, fill=color, anchor="nw")

        now = time.time()
        dt = now - self.last_time
        self.last_time = now
        if dt > 0:
            self.fps = int(1 / dt)

        self.canvas.create_text(
            8,
            8,
            text=f"{self.fps} FPS",
            fill="white",
            anchor="nw"
        )

        self.root.update_idletasks()
        self.root.update()

    def pixel(self, x, y, color):
        self.back.append(("pixel", x, y, color))

    def line(self, x1, y1, x2, y2, color):
        self.back.append(("line", x1, y1, x2, y2, color))

    def rect(self, x, y, w, h, color):
        self.back.append(("rect", x, y, w, h, color))

    def fill_rect(self, x, y, w, h, color):
        self.back.append(("fill_rect", x, y, w, h, color))

    def circle(self, x, y, r, color):
        self.back.append(("circle", x, y, r, color))

    def text(self, x, y, text, color):
        self.back.append(("text", x, y, text, color))

    def run(self, draw=None, fps=60):
        self.running = True
        delay = 1 / fps

        while self.running:
            start = time.time()
            self.begin()

            if draw:
                draw(self)

            self.present()

            elapsed = time.time() - start
            sleep_time = max(0, delay - elapsed)
            time.sleep(sleep_time)

    def close(self):
        self.running = False
        self.root.destroy()
