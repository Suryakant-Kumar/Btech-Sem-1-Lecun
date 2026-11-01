import turtle

sides = int(input())
t = turtle.Turtle()
t.speed(1)

angle = 360/sides
count = 0
while count < sides:
    t.forward(90)
    t.left(angle)
    count+=1

turtle.done()