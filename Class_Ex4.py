import turtle as t

turtle1 = t.Turtle()
window = turtle1.getscreen()

# Let's draw a triangle
turtle1.penup()             # This command helps us to not draw when we want to change the turtles position
turtle1.goto(200, 200)      # This command helps us to change the turtle1's default position
turtle1.pendown()           # This command helps us to put our pen down to continue drawing
t.begin_fill()              # Starts filling the turtles
turtle1.fd(100)             # This command goes forward so: fd() == forward() and also its parameter is our step
turtle1.left(120)           # This command takes an angle as parameter and then turns that angle left
turtle1.fd(100)
turtle1.goto((200, 200))    # This command helps us to go to the home, here our home is 200, 200 as we have changed it in the line 8
t.end_fill()                # Ends filling the turtle

# Let's draw square
turtle1.penup()             # This command helps us to not draw when we want to change the turtles position
turtle1.goto(-200, 200)     # This command helps us to change the turtle1's default position
turtle1.pendown()           # This command helps us to put our pen down to continue drawing
t.begin_fill()              # Starts filling the turtles
turtle1.rt(30)              # This command helps us to turn 30 degrees to right
turtle1.fd(100)             # This command goes forward so: fd() == forward() and also its parameter is our step
turtle1.left(90)            # This command takes an angle as parameter and then turns that angle left
turtle1.fd(100)
turtle1.left(90)
turtle1.fd(100)
turtle1.goto((-200, 200))   # This command helps us to go to the home, here our home is -200, 200 as we have changed it in the line 18
t.end_fill()                # Ends filling the turtle


# Let's draw hexagon
turtle1.penup()             # This command helps us to not draw when we want to change the turtles position
turtle1.goto(-200, -200)    # This command helps us to change the turtle1's default position
turtle1.pendown()           # This command helps us to put our pen down to continue drawing
turtle1.rt(90)              # This command helps us to turn 90 degrees to right
turtle1.fd(100)             # This command goes forward so: fd() == forward() and also its parameter is our step
turtle1.left(60)            # This command takes an angle as parameter and then turns that angle left
turtle1.fd(100)
turtle1.left(60)
turtle1.fd(100)
turtle1.left(60)
turtle1.fd(100)
turtle1.left(60)
turtle1.fd(100)
turtle1.goto((-200, -200))  # This command helps us to go to the home, here our home is -200, -200 as we have changed it in the line 31


# Let's draw octaagon
turtle1.penup()             # This command helps us to not draw when we want to change the turtles position
turtle1.goto(200, -200)     # This command helps us to change the turtle1's default position
turtle1.pendown()           # This command helps us to put our pen down to continue drawing
turtle1.rt(60)              # This command helps us to turn 90 degrees to right
turtle1.fd(70)             # This command goes forward so: fd() == forward() and also its parameter is our step
turtle1.rt(45)            # This command takes an angle as parameter and then turns that angle left
turtle1.fd(70)
turtle1.rt(45)
turtle1.fd(70)
turtle1.rt(45)
turtle1.fd(70)
turtle1.rt(45)
turtle1.fd(70)
turtle1.rt(45)
turtle1.fd(70)
turtle1.rt(45)
turtle1.fd(70)
turtle1.goto((200, -200))  # This command helps us to go to the home, here our home is 200, -200 as we have changed it in the line 31

window.exitonclick()