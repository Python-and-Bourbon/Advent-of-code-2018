# https://docs.python.org/3/library/collections.html#collections.deque
from collections import deque
with open('input.txt', 'r') as inp: lines = inp.read().split()[:7:6]
players, last = map(int, lines)
scores, circle = [0 for _ in range(players)], deque([0])
for marble in range(1, last+1):
    if marble % 23 == 0:
        circle.rotate(7)
        scores[marble % players] += marble + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(marble)
print(max(scores))