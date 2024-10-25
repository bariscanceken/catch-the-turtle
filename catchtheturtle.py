#library
import turtle
import random

#
a = 0
xcrd = 0
ycrd = 0 

#options screen
drawboard = turtle.Screen()
drawboard.bgcolor("white")
drawboard.title("Turtle Game")

#options ti1
ti = turtle.Turtle("turtle")
ti.shapesize(3)
ti.color("blue")

#options ti2
ti2 = turtle.Turtle()
ti2.shapesize(3)
ti2.color("Red")


#random
def randomcoordinate(x,y):
    global xcrd
    global ycrd
    global a
    ti2.clear()
    if abs(x - xcrd) < 50 and abs(y - ycrd) < 50:
        a += 1
        ti2.teleport(-650,350)
        ti2.write(f"Skorunuz: {a}")
    else :
        ti2.teleport(-650,350)
        ti2.write(f"Skorunuz: {a}")

    print(f"Tıklanan: ({x}, {y}), Rastgele: ({xcrd}, {ycrd})")
    xcrd = random.randrange(-600,600)
    ycrd = random.randrange(-300,300)
    ti.teleport(xcrd,ycrd)

        
#Click func
drawboard.onscreenclick(randomcoordinate)

turtle.done()


