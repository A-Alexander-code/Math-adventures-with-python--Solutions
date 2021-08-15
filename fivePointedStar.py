from turtle import *
import time

shape('turtle')

def draw_star(size):
    count = 0
    angle = 144
    while count <= 5:
        forward(size)
        right(angle)
        count += 1
    return

draw_star(100)
time.sleep(5)