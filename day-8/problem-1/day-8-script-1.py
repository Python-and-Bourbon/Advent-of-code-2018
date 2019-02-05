with open('input.txt', 'r') as inp: lines = [int(i) for i in inp.read().split()]

def recursive_tree(lines):
    children, metadata = [lines.pop(0) for _ in range(2)]
    return sum(recursive_tree(lines) for _ in range(children)) + sum(lines.pop(0) for _ in range(metadata))
print(recursive_tree(lines))