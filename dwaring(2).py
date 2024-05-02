from turtle import*

color = ['red' 'yellow' 'orange' 'blue' 'green' 'black' 'brown']

def square(x,y,):
    up()
    fillcolor('red')
    goto(x, y)
    down()
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

x = int(-100)
y = int(-100)
while True:
    x += 50
    y += 50
    square(x, y)


done()