#target is the sequence we're looking for
with open('input.txt', 'r') as f: target = f.readline()

#now we don't have to type len(target) a bunch of times
l = len(target)

#set scoreboard initial state and each elf's starting index
scoreboard, elf_one, elf_two = [3, 7], 0, 1

#need at least l scores to start
while len(scoreboard) < l:
    #create new score based on the sum of each elf's recipe
    new_score = scoreboard[elf_one]+scoreboard[elf_two]

    #because the scores can only be 1 digit, we can append 1 and then mod of 
    # score and 10 (second digit)
    if new_score > 9: scoreboard += [1, new_score % 10]
    else: scoreboard.append(new_score)
    
    #set new elf indexes by incrementing and looping (mod) as described in problem
    elf_one = (elf_one + 1 + scoreboard[elf_one]) % len(scoreboard)
    elf_two = (elf_two + 1 + scoreboard[elf_two]) % len(scoreboard)

#create a set for lookups and an empty value for the output
combos, ans = set(), 0

#add the current scoreboard to the set as a string
combos.add(''.join([str(i) for i in scoreboard]))

#use combos set as the while loop condition
while target not in combos:

    #create new score based on the sum of each elf's recipe
    new_score = scoreboard[elf_one]+scoreboard[elf_two]

    #because the scores can only be 1 digit, we can append 1 and then mod of score and 
    # 10 (second digit)
    if new_score > 9: 
        scoreboard.append(1)
        combos.add(''.join([str(i) for i in scoreboard[-l:]]))
        ans += 1
        if target in combos: break
        scoreboard.append(new_score%10)
        combos.add(''.join([str(i) for i in scoreboard[-l:]]))
        ans += 1

    else: 
        scoreboard.append(new_score)
        combos.add(''.join([str(i) for i in scoreboard[-l:]]))
        ans += 1
    
    
    #set new elf indexes by incrementing and looping (mod) as described in problem
    elf_one = (elf_one + 1 + scoreboard[elf_one]) % len(scoreboard)
    elf_two = (elf_two + 1 + scoreboard[elf_two]) % len(scoreboard)
print(ans)