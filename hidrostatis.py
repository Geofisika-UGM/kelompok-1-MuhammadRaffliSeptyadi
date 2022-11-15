
import turtle
   
def hdr(r,h,hmax):
    """Menghitung Tekanan hidrostatis (massa jenis zat cair,kedalaman) """
    t=turtle.Turtle()
    t.penup()
    t.goto(-100,-50)
    t.pendown()
    c=9.8
    hdr = r*h*c
    z= hmax-h
    if h < 51:
        h1=h*2
    elif h < 100:
            h1=h
    elif h == 100:
            h1=h
    if z < 51:
            z1=z*2
    elif z == 100:
        z1=z
    elif z < 100:
        z1=z
    for i in range(1,11):
        if h > 10*10**i:
            h1=h/10**i
        if z > 10*10**i:
            z1=z/10**i 
        

    x=6
    t.pensize(2)
    t.pencolor('black')
    t.fillcolor('cyan')
    t.begin_fill()
    t.forward((h1+x+z1)/2)
    t.left(90)
    t.forward(z1/2)
    t.write(" "+ str(z) + "m")
    t.forward(z1/2)
    t.right(90)
    t.forward(x)
    t.penup()

    for i in range(90):
        t.forward(1)
        t.right(1)

    t.forward(1)
    t.forward(z1/2)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(z1/2)
    t.forward(x)


    for i in range(90):
        t.forward(1)
        t.left(1)
    
    t.forward(1)
    t.forward(x)
    t.pendown()
    t.forward(x)
    t.right(90)
    t.forward(h1/2)
    t.write(" "+ str(h) + "m")
    t.forward(h1/2)
    t.left(90)
    t.penup()
    t.forward((h1+x+z1)/2)
    t.left(90)
    t.pendown()
    t.forward((h1+x+z1)/2)
    t.write(" "+ str(h+z) + "m")
    t.forward((h1+x+z1)/2)
    t.end_fill()
    t.penup()
    t.goto(-100,-70)
    t.write("Tekanan Hidrosatis :"+ str(hdr) + "N/m^2")
    
    turtle.done()
    turtle.mainloop()
