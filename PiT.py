#PiT
import random
import turtle
turtle.setup(900,600,0,0)
t = eval(input())
Q = t
C = 0
turtle.goto(300,0)
turtle.goto(0,0)
turtle.goto(0,300)
turtle.goto(0,290)
turtle.pencolor("red")
turtle.circle(-290,90)
turtle.pencolor("blue")
turtle.pensize(2)
turtle.penup()
for i in range(t):
    x,y = random.randint(0,290),random.randint(0,290)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x,y)
    turtle.penup()
    if pow(x,2) + pow(y,2) <= 290 * 290:
        C = C + 1
    p = ((i + 1)/t) * 100
    print("\r{:.2f}%".format(p),end = "")
Pi = 4 * (C / Q)
turtle.goto(0,0)
print("")
print("Pi={:.100f}".format(Pi))
input("Press Enter to Continue")
