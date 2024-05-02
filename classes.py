from turtle import *
class bee:
    health = 100

    def draw(x, y) :
        up()
        goto(x, y)
        down()
        circle(100)
        right(90)
        circle(50)

    def attack():
        print("sttsck")
        
beeOne = bee                                                                                        
beeTwo = bee

beeOne.draw(0, 0)
beeTwo.draw(-200, 100)

done()