'''
Author: Spencer Klinge
Date: 9-24-2015
Class: ISTA 130
Section Leader: Will Zandler

Description:
This program runs a series of functions outlined in part one of the homework 3 outline it imports python math libray.
'''


import math

'''
def print_word(int, string)
    num-> number of times the word is printed
    word->the word being printed
    prints the string parameter int amount of times, each on a new line. tests for invalid parameter
    such as negative number
'''
def print_word(num, word):
    if num >= 0:
        for i in range(num):
            p= i+1  
            print(p,'-->', word)
    return None

'''
def bacteria(int, int)

    time-> number of minutes it takes for bacterium to split into two new bacteria.
    generations->number of generations to include in the output
    this function begins with a single bacterium and multiplies by two each subsequent
    generation.
'''
def bacteria(time, generations):
    time_interval=time
    initial=1
    for i in range(generations):
        print('after', time_interval,'minutes: ', initial * 2, 'bacteria')
        time_interval+= time
        initial*=2
    return None

'''
def convert_to_copper(int, int , int):
gold-> amount of gold pieces
silver->amout of silver peices
copper-> amount of copper peices

this function takes the given amout of coins and outputs their total in the form of coppper peices.
'''
def convert_to_copper(gold, silver, copper):
    print(gold,'gp,',silver,'sp,',copper,'cp','converted to copper is:', ((gold*10)*5)+(silver*5)+copper, 'cp')

'''
def convert_from_copper(int)
copper-> amount of copper pieces

this function takes a total amount of copper and returns optimized change, giving the user
the max amount of gold, then silver, then copper.
'''
def convert_from_copper(copper):
    copper_temp=copper
    gold= copper_temp/50
    copper_temp= copper_temp % 50
    silver= copper_temp/5
    copper_temp= copper_temp % 5
    print(copper, 'copper pieces is:', int(gold), 'gp,', int(silver),'sp,',int(copper_temp),'cp')

'''
def repeat_word(string, int int)
word-> the word that is going to be printed
rows-> the number of rows down that will be printed
cols->the number of times the word will be printed on a single line

this function prints the word in a 2d grid with the demensions of the givin rows and colums
'''
def repeat_word(word, rows, cols):
    for i in range(rows):
        print(word * cols)

'''
def text_triangle(int)
side-> height of the triange, number of rows

this function takes an int and prints x's into a triangle shape according to the number
of rows.
'''
def text_triangle(side):
    if side <0:
        print()
        return None
    else:
        for i in range(side):
            print('x' * (i+1))

'''
def surface_area_of_cylinder(float, float)
float_radius-> radius of the cylinder
float_height-> height of the cylinder

this function, given the height and raidus, calculates the surface of a cylinder
using pythons math library.
'''

def surface_area_of_cylinder(float_radius, float_height):
    A= ((2 * math.pi * float_radius * float_radius) + (2 * math.pi * float_radius * float_height))
    print('The surface area of a cylinder with radius', float_radius, 'and height', float_height, 'is', A)

'''
def tree_height(float, float)
base_distance-> distance from the person to the tree
string_length-> length of the kite string_length

this function represets a person with a kite caught in a tree. th object is to measure the height
of the tree if the distance from the tree and the string length are both known.

'''
def tree_height(base_distance, string_length):
    tree=(string_length * string_length) - (base_distance * base_distance)
    tree= math.sqrt(tree)
    print('Kite string:', string_length)
    print('Distance:', base_distance)
    print('Height:', tree)
    
'main does some basic tests'
def main():
    print("this")
    print_word(-1, 'banana')
    bacteria(3,3)
    convert_to_copper(5, 10, 7)
    convert_from_copper(3242)
    repeat_word('kobold', 5, 3)
    surface_area_of_cylinder(10.0,10.0)
    text_triangle(-1)
    tree_height(300,500)

if __name__ == '__main__':
    main()
