'''
Author: Spencer Klinge
Date: 9-24-2015
Class: ISTA 130
Section Leader: Will Zandler

shape_chooser.py
Description:

This program promts the user to input the number of sides, color, and side length of a polygon

it then draws that polygon with the givin characteristics using the turtle class.
'''

import turtle


'''
def polygon(turtle, int, int):
    buddy-> turtle object
    sides_number-> number of sides for the polygon
    side_length-> length of each side of the polygon
    draws a polygon of the givin number of sides, and side length

'''
def polygon(buddy, sides_number, side_length):
    for i in range(sides_number):
        buddy.forward(side_length)
        buddy.left(360/sides_number)


'''
main handles the user input alog with turtle construction and the calling of polygon. it sets the requested
characteristics prior to calling polygon.
'''
def main():
    number=input('Enter the number of polygons:')
    polygons=input('Enter the number of sides:')
    headcolor=input('Enter the color:')
    side= input('Enter the side length for your polygon:')
    turtle_head= turtle.Turtle()
    turtle_head.color(headcolor)
    for i in range(int(number)):# number of polygons/ position reset for loop

        turtle_head.setheading(0)
        polygon(turtle_head, int(polygons), int(side))
        turtle_head.penup()
        turtle_head.setheading(270)
        turtle_head.forward(int(side))
        turtle_head.pendown()


    input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
