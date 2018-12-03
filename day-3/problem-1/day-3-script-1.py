import numpy as np
def parse(data):
    num, _, top_left_corner, size = data.split(' ')
    top, left = top_left_corner.split(',')
    x, y = size.split('x')
    return list(map(int, [num[1:], top, left[:-1], x, y]))
with open('input.txt', 'r') as inp: lines = [parse(line.rstrip('\n')) for line in inp.readlines()]
# Commented code below whows max size for x and y are 1000 and 999
# print(max([i[1] + i[3] for i in lines]), max(i[2] + i[4] for i in lines), sep='\n')
field = np.zeros((1000, 1000))
for line in lines: field[line[1]:line[1]+line[3], line[2]:line[2]+line[4]] += 1
print(np.sum(field>=2))
