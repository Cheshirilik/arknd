import tkinter as tk
import time

# Abstract game object
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

# Ball. Move only diagonally.
class TheBall(GameObject):
    def __init__(self, canvas, x, y):
        self.radius = 10
        self.direction = [-1, 1]
        self.speed = 10

        item = canvas.create_oval(x-self.radius, y-self.radius,
                                  x+self.radius, y+self.radius,
                                  fill="white")

        super(TheBall, self).__init__(canvas, item)


# Paddle. Move only horizontally
class ThePaddle(GameObject):
    def __init__(self, canvas, x, y):
        self.width = 80
        self.height = 10
        self.ball = None

        item = canvas.create_rectangle(x-self.width/2, y-self.height/2,
                                  x+self.width/2, y+self.height/2,
                                  fill="blue")

        super(ThePaddle, self).__init__(canvas, item)

    def set_ball(self, ball):
        self.ball = ball

    def move(self, offset):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super(ThePaddle, self).move(offset, 0)
            if self.ball is not None:
                self.ball.move(offset, 0)



# main loop.
class Game(tk.Frame):

    def __init__(self, master):
        super(Game, self).__init__(master)

        self.lives = 3
        self.width = 800
        self.height = 600

        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg='#aaaaff' )

        self.item = self.canvas.create_rectangle(10, 10, 100, 80, fill='green')

        #time.sleep(5)
        obj = GameObject(self.canvas, self.item)
        obj.move(50, 50)

        self.canvas.pack()
        self.pack()



if __name__ == '__main__':
    root = tk.Tk()
    root.title("Arknd")



    game = Game(root)
    game.mainloop()

