#creat the grid (g)
with open('input.txt', 'r') as inp: g = [list(i) for i in inp.readlines()]

#create functions to turn the cart at intersections according to the problem
left, right = lambda x: (x+3)%4, lambda x: (x+1)%4

#tell the cart what to do based on current trajectory interger 0-3
dr, dc = [-1, 0, 1, 0], [0,1,0,-1]

class Cart():

    def __init__(self, r, c, curr, nxt=0):
        self.r = r #cart row
        self.c = c #cart column
        self.curr = curr #cart current trajectory
        self.nxt = nxt #what the cart should do at the next intersection ('+')
    
    def __repr__(self):
        return(str(self.c)+','+str(self.r)) #easier than typing similar a bunch of times
    
    def loc(self):
        return (self.c, self.r) #easier than typing similar a bunch of times

#lets us run the while loop later
running = True

#initialize an empty list to store the carts
carts = list()

#create the carts, add the carts to the list, replace the spots with rails
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == '>': 
            carts.append(Cart(i, j, 1))
            g[i][j]='-'
        elif g[i][j] in '<': 
            carts.append(Cart(i, j, 3))
            g[i][j]='-'
        elif g[i][j] == '^':
            carts.append(Cart(i, j, 0))
            g[i][j]='|'
        elif g[i][j]  == 'v':
            carts.append(Cart(i, j, 2))
            g[i][j]='|'

#function to easily create the set of possible collision points
def set_crash_sites(carts=carts): return set(cart.loc() for cart in carts)

while running:
    carts = sorted(carts, key=lambda cart:(cart.loc())) #sort by row then column
    for cart in carts:
        r2, c2 = cart.r+dr[cart.curr], cart.c+dc[cart.curr] #this will be the cart.r and cart.c after the move
        nxt = g[r2][c2] #lets us know if the cart will change trajectory this turn
        if nxt == '\\': cart.curr = {0: 3, 1:2, 2:1, 3:0}[cart.curr]
        elif nxt == '/': cart.curr = {0: 1, 1:0, 2:3, 3:2}[cart.curr]
        #if cart comes to intersection, change trajectory (maybe) and change what it should do next time
        elif nxt == '+': 
            if cart.nxt == 0: cart.curr = left(cart.curr)
            elif cart.nxt==2: cart.curr = right(cart.curr)
            cart.nxt = (cart.nxt+1) % 3

        crash_sites = set_crash_sites()
        cart.r, cart.c = r2, c2

        if cart.loc() in crash_sites:
            print(cart) #answer
            running = False
            break
