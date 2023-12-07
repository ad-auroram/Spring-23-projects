#roadwork ahead? uh, yeah, I sure hope it does

import turtle as ttl

def main ():
    #orange diamond
    ttl.speed(0)
    ttl.left(45)
    ttl.goto(0,-200)
    ttl.color("#FF6600")
    ttl.begin_fill()
    ttl.forward(300)
    ttl.left(90)
    ttl.forward(300)
    ttl.left(90)
    ttl.forward(300)
    ttl.left(90)
    ttl.forward(300)
    ttl.left(90)
    ttl.end_fill()

    #outline
    ttl.color("black")
    ttl.pensize(10)
    ttl.forward(300)
    ttl.left(90)
    ttl.forward(300)
    ttl.left(90)
    ttl.forward(300)
    ttl.left(90)
    ttl.forward(300)
    ttl.left(90)

    #text
    ttl.penup()
    ttl.goto(-85,45)
    ttl.pendown()
    ttl.write("ROAD", font=("Calibri", 55, "normal"))
    ttl.penup()
    ttl.goto(-95,-20)
    ttl.pendown()
    ttl.write("WORK", font=("Calibri",55,"normal"))
    ttl.penup()
    ttl.goto(-100, -85)
    ttl.pendown()
    ttl.write("AHEAD", font=("Calibri",55,"normal"))

    ttl.done()

main()