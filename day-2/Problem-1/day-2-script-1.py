twos, threes, answer_file = 0, 0, open('day-2-answer-1', 'w')
with open('input.txt', 'r') as inp: lines = [line.rstrip('\n') for line in inp.readlines()]
val_len = len(lines[0])
for val in lines:
    short_twos, short_threes = False, False
    for i in set(val):
        if short_twos and short_threes: break
        if not short_twos and val.count(i) == 2: short_twos = True 
        elif not short_threes and val.count(i) == 3: short_threes = True
    if short_twos: twos += 1
    if short_threes: threes += 1
    answer_file.write('2s: {0}, 3s: {1}\n'.format(twos, threes))
answer_file.write('Answer: ' + str(twos*threes))
answer_file.close(), print(twos * threes)