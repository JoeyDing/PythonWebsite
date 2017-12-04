
import turtle

"""
turtle.color('green')

turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.right(90) """



"""
turtle.color('green')
for step in range(4):
    turtle.forward(100)
    #turtle.right(90)
#not indented, not a part of the loop
turtle.color('red')
#turtle.forward(300)
#turtle.right(500)
"""

# draw a "tian" in chiense
turtle.color('green')
for step in range(4):
    turtle.forward(100)
    turtle.right(90)
    for moresteps in range(4):
        turtle.forward(50)
        turtle.right(90)

turtle.forward(200)

# draw 五方
turtle.color('red')
for step in range(5):
    turtle.forward(100)
    turtle.right(360/5)
    for moresteps in range(5):
        turtle.forward(50)
        turtle.right(360/5)


turtle.left(90)
turtle.forward(200)


turtle.color('black')
for step in range(4):
    turtle.forward(10)
    turtle.right(360/4)
    for moresteps in range(4):
        turtle.forward(50)
        turtle.right(360/4)


#draw triangle
turtle.left(90)
turtle.forward(200)
turtle.color('purple')
for step in range(4):
    turtle.forward(100)
    turtle.right(360/3)
