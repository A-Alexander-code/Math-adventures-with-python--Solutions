from turtle import *

shape('turtle')

def spiral():
    lenght=50
    for i in range(75): 
        right(5)
        lenght += 5
        for i in range(4):
            forward(lenght)
            right(90)

spiral()