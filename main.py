"""
    tic tac toe
    sgrecha10@gmail.com
"""

from tkinter import *

SIZE = 5
WIDTH = 400
HEIGHT = 400


"""class Game:
    def __init__(self):
        window.title('Крестики - нолики')
        window.geometry(str(WIDTH) + str('x') + str(HEIGHT))
        self.field = Field()


class Field():
    def __init__(self):
        self.c = Canvas(window, width=WIDTH, height=HEIGHT, bg='white')
        self.c.pack()

    def draw(self):
        self.periodX = WIDTH / SIZE
        self.periodY = HEIGHT / SIZE
        for i in range(1, SIZE):
            self.c.create_line(self.periodX * i, 10, self.periodX * i, HEIGHT - 10, fill='gray')
"""

if __name__ == '__main__':
    """window = Tk()
    window.configure(background='white')
    a = Game()
    a.field.draw()
    window.mainloop()
    """
    window = Tk()

    # рисуем поле
    window.title('Крестики - нолики')
    window.geometry(str(WIDTH) + str('x') + str(HEIGHT))

    c = Canvas(window, width=WIDTH, height=HEIGHT, bg='white')
    c.pack()

    periodX = WIDTH/SIZE
    periodY = HEIGHT/SIZE

    for i in range(1, SIZE):
        c.create_line(periodX*i, 10, periodX*i, HEIGHT-10, fill='gray')

    for i in range(1, SIZE):
        c.create_line(10, periodY*i, WIDTH-10, periodY*i, fill='gray')

    def clickCell(wid, i, k):
        c.delete(wid)

        c.create_oval(periodX * k + 10,
                      periodY * i + 10,
                      periodX * (k + 1) - 10,
                      periodY * (i + 1) - 10,
                      fill='white', outline='black', width=3)

        c.create_line(periodX * k + 10,
                      periodY * i + 10,
                      periodX * (k + 1) - 10,
                      periodY * (i + 1) - 10,
                      fill='black', width=3)

        c.create_line(periodX * (k+1) - 10,
                      periodY * i + 10,
                      periodX * k + 10,
                      periodY * (i + 1) - 10,
                      fill='black', width=3)
        

    for i in range(SIZE):
        for k in range(SIZE):
            wid = c.create_rectangle(periodX*k + 1,
                               periodY*i + 1,
                               periodX*(k+1) - 1,
                               periodY*(i+1) - 1,
                               fill='white', outline='white')
            c.tag_bind(wid, "<Button-1>", lambda event, wid=wid, i=i, k=k: clickCell(wid, i, k))



    window.mainloop()
    
