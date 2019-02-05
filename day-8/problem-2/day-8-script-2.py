with open('input.txt', 'r') as inp: lines = [int(i) for i in inp.read().split()]

def recursive_tree(lines):
    children, metadata = [lines.pop(0) for _ in range(2)]
    scores, datapoints = [recursive_tree(lines) for _ in range(children)], [lines.pop(0) for _ in range(metadata)]
    if children == 0: return sum(datapoints)
    return sum(scores[i-1] for i in datapoints if i-1 in range(children))
print(recursive_tree(lines))