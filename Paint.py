import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.draw_color = "black"
        self.line_width = 2

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.set_start_point)

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.color_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Colors", menu=self.color_menu)
        self.color_menu.add_command(label="Black", command=self.set_color_black)
        self.color_menu.add_command(label="Red", command=self.set_color_red)
        self.color_menu.add_command(label="Green", command=self.set_color_green)
        self.color_menu.add_command(label="Blue", command=self.set_color_blue)

        self.width_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Line Width", menu=self.width_menu)
        self.width_menu.add_command(label="1", command=lambda: self.set_line_width(1))
        self.width_menu.add_command(label="2", command=lambda: self.set_line_width(2))
        self.width_menu.add_command(label="3", command=lambda: self.set_line_width(3))
        self.width_menu.add_command(label="5", command=lambda: self.set_line_width(5))

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(x, y, x, y, fill=self.draw_color, width=self.line_width, capstyle=tk.ROUND, smooth=True)

    def set_start_point(self, event):
        self.start_x, self.start_y = event.x, event.y

    def set_color_black(self):
        self.draw_color = "black"

    def set_color_red(self):
        self.draw_color = "red"

    def set_color_green(self):
        self.draw_color = "green"

    def set_color_blue(self):
        self.draw_color = "blue"

    def set_line_width(self, width):
        self.line_width = width


if __name__ == "__main__":
    root = tk.Tk()
    paint_app = PaintApp(root)
    root.mainloop()
