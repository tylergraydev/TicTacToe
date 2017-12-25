from graphics import *

class Board():
    def __init__(self, width, height):
        self.board = []
        self.board.append(Line(Point(width * 2 / 3, height - 30),Point(width * 2 / 3, 30)))
        self.board.append(Line(Point(width * 1 / 3, height - 30),Point(width * 1 / 3, 30)))
        self.board.append(Line(Point(width - 30, height * 2 / 3),Point(30, height * 2 / 3)))
        self.board.append(Line(Point(width - 30, height * 1 / 3),Point(30, height * 1 / 3)))
    def draw(self, win):
        for self.each in self.board:
            self.each.draw(win)
    def setFill(self, color):
        for self.each in self.board:
            self.each.setFill(color)
    def setWidth(self, width):
        for self.each in self.board:
            self.each.setWidth(width)

class O():
    def __init__(self,winW, winH, radius, pos):
        x = winW /2
        y = winH / 2
        if(pos == 1):
            self.cir = Circle(Point(x / 6 * 2 , y / 3) ,radius)
        elif(pos == 2):
            self.cir = Circle(Point(x , y  / 3), radius)
        elif (pos == 3):
            self.cir = Circle(Point(x + x / 5 * 3, y / 3), radius)
        elif (pos == 4):
            self.cir = Circle(Point(x / 6 * 2, y), radius)
        elif (pos == 5):
            self.cir = Circle(Point(x , y), radius)
        elif (pos == 6):
            self.cir = Circle(Point(x + x / 5 * 3, y), radius)
        elif (pos == 7):
            self.cir = Circle(Point(x / 6 * 2, y + y*2/3), radius)
        elif (pos == 8):
            self.cir = Circle(Point(x, y + y*2/3), radius)
        elif (pos == 9):
            self.cir = Circle(Point(x + x / 5 * 3, y + y*2/3) , radius)



    def draw(self,win):
        self.cir.draw(win)
    def setFill(self, color):
        self.cir.setFill(color)
    def setOutline(self, color):
        self.cir.setOutline(color)
    def setWidth(self, width):
        self.cir.setWidth(width)


