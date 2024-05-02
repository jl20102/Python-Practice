from turtle import*
import random


colors=['red', 'green', 'blue', 'orange', 'yellow', 'black']

def square(x,y,c):
    up()
    setpos(int(x),int(y))
    down()
    fillcolor(c)
    begin_fill()
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    end_fill()

square(0, 0, 'red')
square(100, 100, 'blue')

x=5
y=9
while True :
    x = random.randint(-500,500)
    y = random.randint(-500,500)
    f = random.randint(0,5)


    square(x,y,colors[f])

done()