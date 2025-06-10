# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either a radius or a diameter")
        
import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either a radius or a diameter")

    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle with radius {self.radius} and diameter {self.diameter}"
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        raise TypeError("Can only add another Circle")
    def __gt__(self, other):
        return self.radius > other.radius  
    def __eq__(self, other):
        return self.radius == other.radius  
    def __lt__(self, other):
        return self.radius < other.radius
    
import turtle

def draw_circle(circle):
    turtle.penup()
    turtle.goto(0, -circle.radius)  # Move to correct position
    turtle.pendown()
    turtle.circle(circle.radius)

turtle.speed(0)
circles = [Circle(3), Circle(7), Circle(1)]
for c in sorted(circles):
    draw_circle(c)

turtle.done()