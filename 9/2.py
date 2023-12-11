with open("9/input.txt", "r") as f:
    strings = f.readlines()

histories = []
for string in strings:
    f = [int(x) for x in string.split()]
    f.reverse()
    histories.append(f)

s = 0
for history in histories:
    diffs = [[x for x in history]]
    y = 0
    while not all(v == 0 for v in diffs[y]):
        diffs.append([diffs[y][x + 1] - diffs[y][x] for x in range(0, len(diffs[y]) - 1)])
        y += 1
    
    s += sum([x[-1] for x in diffs if x != []])

print(s)