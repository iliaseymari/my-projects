import turtle as t
p = t.Pen()
s = t.Screen()
s.bgcolor('black')
p.speed(0)
p.pensize(2)
p.hideturtle()
for i in range(90):
    p.color("red")
    p.circle(i)
    p.color("cyan")
    p.circle(i*1.5)
    p.right(5)
    p.forward(3)
    
t.done()
