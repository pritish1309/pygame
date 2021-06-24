import turtle
import random
p=turtle.Turtle('classic')
window=turtle.Screen()
window.bgcolor('black')
p.color('Aqua')

def movingleft():
    p.setheading(180)
    p.forward(50)
def movingright():
    p.setheading(0)
    p.forward(50)
def movingup():
    p.setheading(90)
    p.forward(50)
def movingdown():
    p.setheading(270)
    p.forward(50)

window.onkeypress(movingleft,'Left')
window.onkeypress(movingright,'Right')
window.onkeypress(movingup,'Up')
window.onkeypress(movingdown,'Down')
window.listen()

a=turtle.Turtle('classic')
a.color('Yellow')
a.penup()
a.goto(random.randint(-150,150),random.randint(-150,150))

while True:
    g=p.xcor()
    h=p.ycor()
    print(g,h)
    a.setheading(a.towards(p))
    a.forward(1)
    if a.distance(p)<5:
        a.goto(random.randint(-100,100),random.randint(-100,100))
