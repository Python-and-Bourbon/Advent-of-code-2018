from string import ascii_lowercase, ascii_uppercase
with open('input.txt', 'r') as inp: polymer, m = list(inp.read()), 50000 # input is 50000 characters long 
for letter_tuple in list(zip([i for i in ascii_lowercase], [i for i in ascii_uppercase])):
    s = ''.join([i for i in polymer if i not in letter_tuple])
    n, i, j = len(s), 0, 1
    while j < n:
        if s[i] == s[j] or s[i].upper() != s[j].upper(): i, j = j, j+1
        else: i, j, n, s = max(0, i-1), max(0, i-1)+1, n-2, s[:i] + s[j+1:]
    m = min(n, m)
print(m)
