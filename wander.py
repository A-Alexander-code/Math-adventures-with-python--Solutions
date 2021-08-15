from turtle import *
from random import randint
import time

speed(0)

def wander():
    while True:
        fd(3)
        if xcor()>=200 or xcor()<=-200 or ycor()<=-200 or ycor()>=200:
            lt(randint(90,189))
    time.sleep(3)

wander()