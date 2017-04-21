import tkinter as tk


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

