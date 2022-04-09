import tkinter as tk
from template import Template


class App(Template):
    def __init__(self):
        super(App, self).__init__()
        self.createWidgets()
        self.attachWidgets()

    def createWidgets(self):
        pass

    def attachWidgets(self):
        pass


if __name__ == "__main__":
    app = App()
    app.run()
