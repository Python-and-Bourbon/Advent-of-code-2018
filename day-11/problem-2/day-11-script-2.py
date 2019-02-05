import numpy as np
const , m, g = 7989, (0, 0, 0, 0), np.zeros((300, 300))

#function to calculate the power level of a given coordinate
def power_level(x, y, c=const):
    x, y, rack = x+1, y+1, x+11
    return ((rack * y + c) * rack) // 100 % 10 - 5

#calculate the power level at each coordinate and strore in numpy array
for i in range(300):
    for j in range(300):
        g[i, j] = int(power_level(i, j))

#for s in range(1, 301):

#checking only through 20x20 windows at first. Comment out line 17 and uncomment line 18 if this doesn't work
for s in range(1, 21):
#for s in range(1, 301):
    #find the largest grid for each window size of power levels in the numpy array
    for i in range(300-s):
        for j in range(300-s):
            t_m = np.sum(g[i:i+s, j:j+s])
            #value m is a tuple with the x,y coordinate of the top-left cell in best grid and its sum
            if t_m > m[2]: m = (i, j, t_m, s) 
with open('output.txt', 'w') as out: 
    for i in range(300): out.write(' '.join([' '*(4-len(str(int(x))))+str(int(x)) for x in g[i]])+'\n')
print(m[0]+1, m[1]+1, m[3], sep=',')