with open('input.txt', 'r') as inp: lines = [line.rstrip('\n') for line in inp.readlines()]
def find_condition(lines):
    for i in range(len(lines[0])):
        visited = set()
        for line in lines:
            word = line[:i] + line[i+1:]
            if word in visited: return word
            visited.add(word)
print(find_condition(lines))