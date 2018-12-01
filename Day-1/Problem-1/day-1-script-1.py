frequency, answer_file = 0, open('day-1-answer-1.txt', 'w')
with open('input.txt') as inp:
    lines = [line.rstrip('\n') for line in inp.readlines()]
for val in lines:
    if val[0] =='+': frequency += int(val[1:])
    if val[0] == '-': frequency -= int(val[1:])
    answer_file.write(val + ' ' + str(frequency) + '\n')
answer_file.close(), print(frequency)
