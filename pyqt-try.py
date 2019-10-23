from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from copy import deepcopy
from random import randint


def whichButton():
    a = QMainWindow.sender()
    print(a.text())

def part(btn,a,b):
    pass
    

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(30*16,30*16,30*16,30*16)
    win.setWindowTitle("hello there")

    l = [[0 for i in range(16)] for j in range(16)]

    for row in l:
        print(row)

    litsButtons = []
    for i in range(16):
        y = i*30
        row = [0 for i in range(16)]
        for j in range(16):
            x = j*30
            row[j] = QtWidgets.QPushButton(win)
            row[j].resize(30,30)
            row[j].move(x,y)
            row[j].setText(str(randint(1,55)))
        litsButtons.append(row)
        
    f = lambda aa,bb : print(aa,bb)
    i=0
    for it in litsButtons:
        j= 0 
        for bt in it:
            bt.setObjectName('_'+str(i)+'_'+str(j))
            print(bt.objectName())
            bt.clicked.connect(whichButton)
            j+=1
        i+=1
    '''
    b = QtWidgets.QPushButton(win)
    b.resize(35,35)
    t = QtWidgets.QPushButton(win)
    t.resize(35,35)
    t.move(35,0)
    '''
    win.show()
    sys.exit(app.exec_())






window()





















