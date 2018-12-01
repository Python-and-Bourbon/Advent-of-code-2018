from collections import defaultdict
frequency, answer_file, still_trying, dd = 0, open('day-1-answer-2.txt', 'w'), True, defaultdict(bool)
dd[0] = True
with open('input.txt') as inp:
    lines = [line.rstrip('\n') for line in inp.readlines()]
while still_trying:
    for val in lines:
        if val[0] =='+': frequency += int(val[1:])
        if val[0] == '-': frequency -= int(val[1:])
        answer_file.write(val + ' ' + str(frequency) + '\n')
        if dd[frequency] == True: 
            still_trying = False
            break
        dd[frequency] = True
answer_file.close(), print(frequency)