#target is the starting index for final output
with open('input.txt', 'r') as f: target = int(f.readline())

#problem wants the 10 
target_end = target+10

#set scoreboard initial state and each elf's starting index
scoreboard, elf_one, elf_two = [3, 7], 0, 1

#use target_end for desired length to make sure we have enough scores to print the solution
while len(scoreboard) < target_end:

    #create new score based on the sum of each elf's recipe
    new_score = scoreboard[elf_one]+scoreboard[elf_two]

    #because the scores can only be 1 digit, we can append 1 and then mod of score 
    #and 10 (second digit)
    if new_score > 9: scoreboard += [1, new_score % 10]
    else: scoreboard.append(new_score)
    
    #set new elf indexes by incrementing and looping (mod) as described in problem
    elf_one = (elf_one + 1 + scoreboard[elf_one]) % len(scoreboard)
    elf_two = (elf_two + 1 + scoreboard[elf_two]) % len(scoreboard)

#use [target:target_end] instead of [-10:] in case the final scoreboard 
#has 1 more score than needed
print(''.join([str(i) for i in scoreboard[target:target_end]]))
