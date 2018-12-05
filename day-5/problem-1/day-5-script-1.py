with open('input.txt', 'r') as inp: polymer = inp.read()
i, j, n = 0, 1, len(polymer)
while j < n:
    if polymer[i] == polymer[j] or polymer[i].upper() != polymer[j].upper(): i, j = j, j+1
    else: i, j, n, polymer = max(0, i-1), max(0, i-1)+1, n-2, polymer[:i] + polymer[j+1:]
print(n)