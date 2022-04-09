import tkinter as tk
from template import Template


class App(Template):
    def __init__(self):
        super(App, self).__init__()
        self.createWidgets()
        self.attachWidgets()

    def createWidgets(self):
        self.canvas = tk.Canvas(self, width=300, height=300, bg="white")

    def attachWidgets(self):
        self.canvas.place(x=0, y=0)


if __name__ == "__main__":
    app = App()
    app.run()
