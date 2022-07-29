from turtle import *
speed(0)
side = 6
size = 150
pensize(5)
for i in range(side):
    pencolor('green')
    forward(size)
    for i in range(6):
        pencolor('purple')
        forward(75)
        pencolor('red')
        circle(25)
        pencolor('blue')
        left(360/6)
        write(i, font=('Arial','4','normal'))
    left(360/side)

mainloop()
