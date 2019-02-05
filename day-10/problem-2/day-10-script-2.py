# regex logic found in this stack overflow post: https://stackoverflow.com/questions/4289331/python-extract-numbers-from-a-string

import re

with open('input.txt', 'r') as inp: 
    lines=[tuple(map(int, re.findall(r"[-\d]+",line))) for line in inp.readlines()]

def get_height(lines):
    low_y, high_y = min([pt[1] for pt in lines]), max([pt[1] for pt in lines])
    return (high_y-low_y)

def get_width(lines):
    low_x, high_x = min([pt[0] for pt in lines]), max([pt[0] for pt in lines])
    return (high_x-low_x)

def iterate(x):
    return [(p[0] + p[2], p[1] + p[3], p[2], p[3]) for p in x]

time, old_height, lines = 0, get_height(lines), iterate(lines)
current_height = get_height(lines)

while current_height < old_height:
    old_height = current_height
    lines = iterate(lines)
    current_height = get_height(lines)
    time += 1

print(time)