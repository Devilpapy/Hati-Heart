import turtle
  
pen = turtle.Turtle()

turtle.bgcolor("black")
  
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
  
def heart():
    pen.color('white')
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
  
def txt():
    pen.up()
    pen.setpos(0,80)
    pen.down()
    pen.color('white')
    pen.write("I like You", align='center', font=("Verdana", 20, "bold"))

  
heart()
txt()

turtle.hideturtle()
pen.hideturtle()

turtle.done()
