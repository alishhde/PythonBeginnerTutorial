import turtle as t

# In the next line we are initializing our turtle as name square
square = t.Turtle()

# Next line code makes our turtle to be drawn faster
square.speed(6)

# In the next line we want to initialize the window
window = t.getscreen()

# In the next line we want to change the background color
window.bgcolor("Green")

# Next two line code changes square size
square.resizemode("user")
square.shapesize(5, 5, 12)

size = 10
# Here we have determined a loop with range 15 because we have 15 square in the question
for i in range(15):

    """ In the next we want to draw our squre.
    In the Next loop we have initialized 
    some condition to change the color for each side"""
    for j in range(4):
        square.fd(70+size)
        if j == 0:    
            square.color("blue", "blue")
        elif j == 1:    
            square.color("orange", "orange")
        elif j == 2:    
            square.color("yellow", "yellow")
        else:
            square.color("red", "red")
        square.left(90)

    # Here we change the size to draw the next squar bigger
    size += 10

    square.fd(20)
    square.right(18)

# Next code helps us to wait for clock and then Stop the program's running
window.exitonclick()




# import turtle as t


# pen = t.Turtle()

# window = pen.getscreen()

# size = 10
# for i in range(50):
    
#     # Square
#     for i in range(4):
#         pen.forward(50+size)
#         pen.left(90)
    
#     pen.forward(20)
#     pen.right(18)
    
#     size += 10

# window.exitonclick()
