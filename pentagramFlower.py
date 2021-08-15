from turtle import *
import time

shape('turtle')

def draw_star(sideLenght):
    count = 0
    angle = 216
    while count <= 5:
        right(angle)
        forward(sideLenght)
        count += 1
    return    
        
def spiral():
    lenght=100
    for i in range(80): 
        lenght += 5
        draw_star(lenght)
        right(5)

spiral()
time.sleep(3)