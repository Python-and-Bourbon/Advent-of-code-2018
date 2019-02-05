#read the input to create a list of strings for each line
with open('input.txt', 'r') as inp: lines = [line.rstrip('\n') for line in inp.readlines()]

#createa an empty dictionary and initial state with an empty pot on each side
gen_number, lookup, initial_state, d = 0, dict(), '.'+lines[0][15:]+'.', 1

#fill the lookup dictionary to store rules and results
for i in lines:
    temp = i.split(' => ')
    #use try/except block to kick out the empty line and initial state lines from input
    try: lookup[temp[0]] = temp[1]
    except Exception: continue

current_gen, next_gen = initial_state, str()

#create a .txt file to write each generation, look for errors or see if .'s are needed on either side
with open('output.txt', 'w') as outp:
    #write initial state as gen 0
    outp.write('0:  '+initial_state+'\n')
    while gen_number < 20:
        next_gen = str()
        #create a temporary string for each spot as 'LLCRR' per problem for lookup
        for i in range(len(current_gen)):
            #if statements for two on far left and 2 on far right to still work as intended
            if i == 0: temp = '..'+current_gen[:3]
            elif i == 1: temp = '.'+current_gen[:4]
            elif i == len(current_gen)-2: temp = current_gen[i-2:]+'.'
            elif i == len(current_gen)-1: temp = current_gen[i-2:]+'..'
            else: temp = current_gen[i-2:i+3]

            #take temporary value from above and add the pot's next gen output from lookup
            next_gen += lookup[temp]

        current_gen = next_gen

        #if the far right pot has a plant, look at the next pot in next generation
        if current_gen[-1] == '#': current_gen+='.'
        #if the pot at index 0 is full, look at the next pot over, increment d for use in last step 
        if current_gen[0] == '#': d, current_gen = d+1, '.'+current_gen
        gen_number += 1
        #write the current gen number and gen to the output file. use spacing to keep even
        outp.write(str(gen_number) + ':' + (' ' * (3 - len(str(gen_number)))) + current_gen + '\n')

out = 0
for i in range(len(current_gen)): 
    #d dots were added to the left of 0 index. subtract d from each index with plant to compensate
    if current_gen[i]=='#': out += i-d

print(out)
