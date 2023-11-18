import turtle


turtle.speed(10)
def setare (x,n,m):
    if x<20 :
        return
    # turtle.fillcolor("green")
    # turtle.begin_fill()
    for i in range (n):
        turtle.forward(x)
        turtle.right(180-180/n)

    # turtle.end_fill()



def chandi (x,n):
    for i in range (n):
        turtle.forward(x)
        turtle.right(180-((n-2)/n)*180)



def saat(r,l,p):
    for _ in range (12) :
        turtle.forward(r)
        turtle.pendown()
        setare(l,p,m)
        turtle.penup()
        turtle.backward(r)
        turtle.right(30)



def starf (x,n,m):
    if x<20 :
        return
    # turtle.fillcolor("green")
    # turtle.begin_fill()
    for i in range (n):
        turtle.forward(x)
        starf(x*m,n,m)
        turtle.right(180-180/n)

    # turtle.end_fill()

