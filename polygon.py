from turtle import *

shape('turtle')

def polygon(numberOfSides, sidelenght):
    intAngle = 360/numberOfSides
    for i in range(numberOfSides):
        forward(sidelenght)
        left(intAngle)

number = int(input('How many sides has the polygon: '))
lenght = int(input('What is the lenght of the side: '))

polygon(number, lenght)