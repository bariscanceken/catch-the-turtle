#library
import turtle
import random

#options
drawboard = turtle.Screen()
drawboard.bgcolor("white")
drawboard.title("Turtle Game")
ti = turtle.Turtle("turtle")
ti.shapesize(3)
ti.color("blue")

ti.teleport(-650,350)
skor = 0
ti.write(f"Skorunuz: {skor}")

#random
def randomcoordinate(x,y):
    global xcrd
    global ycrd
    xcrd = random.randrange(-600,600)
    ycrd = random.randrange(-300,300)
    ti.teleport(xcrd,ycrd)
    if abs(x-xcrd) < 50 or abs(y-ycrd) < 50:
         updateskor()

#skor
def updateskor():   
    global skor
    skor += 1


drawboard.onscreenclick(randomcoordinate)

turtle.done()


