
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

"""

"""
#draw custom shape
nbrsides = 20
turtle.color('green')
for steps in range(nbrsides):
    turtle.forward(50)
    turtle.right(360/nbrsides)
    for moresteps in range(nbrsides):
        turtle.forward(30)
        turtle.right(360/nbrsides)
"""

#print 0,1,2
for steps in range(3):
    print(steps)

#print 1,2,3 , never reach the higher number
for steps in range(1,4):
    print(steps)

#print 1,3,5,7,9 ,third parameter skip by 
for steps in range(1,10,2):
    print(steps)

# foreach loop
for steps in [1,2,3]:
    print(steps)

# foreach loop
for color in ['red','black','green','blue']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)

# while loop : do sth while a condition is true.
#this is where while loop shines, as long as they keep getting this answer we will stayhere until they get this right
answer = '0'

while answer != '4':
    #since input function will return string, so initilize the anser a string '0'. noy s number
    answer = input('What is 2+2 ? ')
print('Yes! 2+2 = 4')