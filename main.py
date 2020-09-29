"""
    tic tac toe
    sgrecha10@gmail.com
"""

from tkinter import *
import random

SIZE = 3
WIDTH = 400
HEIGHT = 400
HUMAN = 'zero'
BOT = 'cross'


class Game:
    def __init__(self, root):
        self.field = Field(root)
        self.ai = Ai()


class Field:
    def __init__(self, root):
        self.arrField = {}
        self.root = root
        self.periodX = WIDTH / SIZE
        self.periodY = HEIGHT / SIZE
        self.c = Canvas(self.root, width=WIDTH, height=HEIGHT, bg='white')
        self.c.pack()
        self.draw_field()

    def draw_field(self):
        self.root.title('Крестики - нолики')
        self.root.geometry(str(WIDTH) + str('x') + str(HEIGHT))
        for i in range(1, SIZE):
            self.c.create_line(self.periodX * i, 10, self.periodX * i, HEIGHT - 10, fill='gray')
        for i in range(1, SIZE):
            self.c.create_line(10, self.periodY * i, WIDTH - 10, self.periodY * i, fill='gray')
        tmp = []
        for i in range(SIZE):
            for k in range(SIZE):
                wid = self.c.create_rectangle(self.periodX * k + 1,
                                         self.periodY * i + 1,
                                         self.periodX * (k + 1) - 1,
                                         self.periodY * (i + 1) - 1,
                                         fill='white', outline='white')
                self.c.tag_bind(wid, "<Button-1>", lambda event, wid=wid, i=i, k=k: self.mark_cell(wid, i, k, 'human'))
                tmp.append((i,k))
        self.arrField = dict.fromkeys(tmp)

    def mark_cell(self, wid, i, k, player):
        # self.c.delete(wid)
        if player == 'human':
            form = HUMAN
        else:
            form = BOT
        # Записываем в массив поля
        self.arrField[i, k] = player
        if form == 'zero':
            self.c.create_oval(self.periodX * k + 10,
                          self.periodY * i + 10,
                          self.periodX * (k + 1) - 10,
                          self.periodY * (i + 1) - 10,
                          fill='white', outline='black', width=3)
        elif form == 'cross':
            self.c.create_line(self.periodX * k + 10,
                          self.periodY * i + 10,
                          self.periodX * (k + 1) - 10,
                          self.periodY * (i + 1) - 10,
                          fill='black', width=3)

            self.c.create_line(self.periodX * (k + 1) - 10,
                          self.periodY * i + 10,
                          self.periodX * k + 10,
                          self.periodY * (i + 1) - 10,
                          fill='black', width=3)
        if player == 'human':
            a.ai.step(i, k)

    def draw_line(self, *args):
        start, finish = args[0], args[1]
        x1, y1 = self.periodX * start[1] + 1, self.periodY * start[0] + 1
        x2, y2 = self.periodX * (start[1] + 1) - 1, self.periodY * (start[0] + 1) - 1
        xs, ys = ((x2-x1) / 2) + x1, ((y2-y1) / 2) + y1
        x1, y1 = self.periodX * finish[1] + 1, self.periodY * finish[0] + 1
        x2, y2 = self.periodX * (finish[1] + 1) - 1, self.periodY * (finish[0] + 1) - 1
        xf, yf = ((x2-x1) / 2) + x1, ((y2-y1) / 2) + y1
        self.c.create_line(xs, ys, xf, yf, fill='red', width=3)


class Ai:
    def step(self, i, k):
        # находим случайное значение поля для хода, проверяем что бы было свободно
        i, k = random.choice([key for key in a.field.arrField if a.field.arrField[key] == None])
        # перечеркиваем выигравшие клеточки
        a.field.draw_line((0,1), (2,1))
        # ai ходит
        a.field.mark_cell(0, i, k, 'bot')


if __name__ == '__main__':
    root = Tk()
    a = Game(root)
    root.mainloop()
