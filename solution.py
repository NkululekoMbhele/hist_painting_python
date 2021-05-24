import turtle as t 
import random 


t.colormode(255)
tur = t.Turtle()

color_list = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41)]


tur.pu()
tur.setheading(225)
tur.fd(300)
tur.setheading(0)
tur.pd()

dots_number = 100

for i in range(1, dots_number):        
    tur.dot(20, random.choice(color_list))
    tur.pu()
    tur.fd(50)
    
    if i % 10 == 0:
        tur.setheading(90)
        tur.fd(50)
        tur.setheading(180)
        tur.fd(500)
        tur.setheading(0)
        




screen = t.Screen()
screen.exitonclick()