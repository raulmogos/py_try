'''
    ramdon journey
'''

import turtle
from random import randint as rd


tu = turtle.Turtle()

tu.speed(50000)

def run_1():
    while True:
        tu.forward(rd(40,100))
        turn = rd(0,1)
        if turn:
            tu.left(rd(0,360))
        else:
            tu.right(rd(0,360))
        tu.dot()

def run_2():
    while True:
        tu.setx(rd(-400,400))
        tu.sety(rd(-400,400))
        tu.dot()


run_1()
