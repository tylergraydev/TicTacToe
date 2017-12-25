from graphics import *
from images import *

def main():
    winW = 1000
    winH = 600
    win = GraphWin("TicTacToe" , winW, winH)
    board = Board(winW, winH)
    board.setFill("Black")
    board.setWidth(20)
    board.draw(win)

    o = O(winW, winH, 70, 2)
    o1 = O(winW, winH, 70, 5)
    o2 = O(winW, winH, 70, 9)
    #o.setFill("Black")
    o.setOutline("Black")
    o.setWidth(20)
    o.draw(win)
    o1.setOutline("Black")
    o1.setWidth(20)
    o1.draw(win)
    o2.setOutline("Black")
    o2.setWidth(20)
    o2.draw(win)

    win.getMouse()
    win.close()

main()

