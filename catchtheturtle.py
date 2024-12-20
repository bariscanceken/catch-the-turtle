#library
import turtle
import random
import time

#options screen
drawboard = turtle.Screen()
drawboard.bgcolor("light blue")
drawboard.title("Turtle Game")

#options ti1
ti = turtle.Turtle("turtle")
ti.shapesize(3)
ti.color("green")


#options ti2
ti2 = turtle.Turtle()
ti2.shapesize(3)
ti2.color("Red")

#
score = 0
xcrd = 0
ycrd = 0

#Yazacak Turtle'ı Gizle
ti2.hideturtle()

#Ne kadar saniye istiyorsanız 5/3 katını giriniz.
t = 60

#random
def randomcoordinate(x,y):
    global xcrd
    global ycrd
    global score
    global t
    if abs(x - xcrd) < 50 and abs(y - ycrd) < 50:
        score += 1
        ti2.teleport(-650,350)
    else :
        ti2.teleport(-650,350)

    print(f"Tıklanan: ({x}, {y}), Rastgele: ({xcrd}, {ycrd})")
    xcrd = random.randrange(-600,600)
    ycrd = random.randrange(-300,300)
    ti.teleport(xcrd,ycrd)   

#Click Çalışması
drawboard.onscreenclick(randomcoordinate) 

#Zaman Döngüsü
while t > 0 :
    ti2.clear()
    t -= 1
    ti2.teleport(0,350)
    ti2.write(f"Kalan Süre : {t}", align="center", font=("Arial", 32, "bold"))
    ti2.teleport(-650,350)
    ti2.write(f"Skorunuz: {score}", align="center", font=("Arial", 32, "bold"))
    time.sleep(0.1)

print("Toplam Skorunuz: ",score)
exit()
turtle.done()
