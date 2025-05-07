
import turtle
import time
import random

turtle.shape('circle')
#turtle.color('blue')
turtle.shapesize(5)
turtle.bgcolor('black') 
#turtle.pensize(5)
turtle.speed('fastest')  
turtle.goto(0,-470)

colors = ['snow', 'linen','light grey','light steel blue','light blue','silver']
clr = ['red','blue','green','white']

def square():
         for i in range(70):
           turtle.color(random.choice(clr)) 
           turtle.right(-35+2)
           turtle.circle(500,130,5) # circle cmd has 3 parameters(radius, arc, step)
           turtle.left(45+5)
         #i = i + 200
           turtle.right(3.1415)

# arc = 360 circle, 180 half circle, 90 quarter of a circle
def circle():
     for i in range(30):
          turtle.color(random.choice(colors))
          turtle.left(90+2)
          turtle.circle(120,130,2)
          turtle.right(-92+5)
          turtle.right(45)
         
square()
time.sleep(2)
turtle.penup()
turtle.hideturtle()
turtle.goto(-43,-110)
turtle.pendown()
circle()
turtle.mainloop()