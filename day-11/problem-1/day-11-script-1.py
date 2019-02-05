import numpy as np
const , m, g = 7989, (0, 0, 0), np.zeros((300, 300))

#function to calculate the power level of a given coordinate
def power_level(x, y, c=const):
    x, y, rack = x+1, y+1, x+11
    return ((rack * y + c) * rack) // 100 % 10 - 5

#calculate the power level at each coordinate and strore in numpy array
for i in range(300):
    for j in range(300):
        g[i, j] = int(power_level(i, j))

#find the largest 3X3 grid of power levels in the numpy array
for i in range(297):
    for j in range(297):
        t_m = np.sum(g[i:i+3, j:j+3])
        g[i,j]=t_m
        #value m is a tuple with the x,y coordinate of the top-left cell in best grid and its sum
        if t_m > m[2]: m = (i, j, t_m) 
with open('output.txt', 'w') as out: 
    for i in range(300): out.write(' '.join([' '*(4-len(str(int(x))))+str(int(x)) for x in g[i]])+'\n')
print(m[0]+1, m[1]+1)