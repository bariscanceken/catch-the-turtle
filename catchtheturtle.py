#Kütüphaneler
import turtle
import random
import time

#turtle options
drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("Catch The Turtle")
t_i = turtle.Turtle("turtle")
t_i.pencolor("blue")
t_i.shapesize(3)

#random coordinate settings
def play(xcrd, ycrd):
    global xdeger
    global ydeger
    t_i.penup()
    t_i.teleport(random.randrange(-600,600),random.randrange(-300,300))
    t_i.pendown()
    skorboard(xcrd,ycrd)
#1400 genişlik 700 yükseklik

a = 1

skor = 5

def skorboard(xcrd, ycrd):
    global skor
    print("deneme")
    x,y = t_i.position()
    if abs(x-xcrd) < 20 and abs(y-ycrd) < 20:
        skor += 1
    else:
        pass

t_i.teleport(-650,350)
t_i.write(f"SKOR:{skor}")

drawing_board.onscreenclick(play)

turtle.mainloop()

