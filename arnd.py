import tkinter as tk


class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self, item):
        self.canvas.delete(self.item)


class Game(tk.Frame):

    def __init__(self, master):
        super(Game, self).__init__(master)

        self.lives = 3
        self.width = 800
        self.height = 600

        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg='#aaaaff' )
        self.canvas.pack()
        self.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Arknd")

    game = Game(root)
    game.mainloop()

