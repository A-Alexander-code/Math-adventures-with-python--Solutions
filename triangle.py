from turtle import *

shape('turtle')

def triangle(sidelenght):
    for i in range(3):
        forward(sidelenght)
        left(120)

sidelenght = 100

triangle(sidelenght)