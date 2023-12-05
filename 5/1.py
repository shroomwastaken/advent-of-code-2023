with open("5/input.txt") as f:
    strings = f.readlines()

seeds = [int(x) for x in strings[0].split(": ")[1][6:-1].split(" ")]
lists = [[] for _ in range(7)]
lists.insert(0, seeds)
ranges = {}
i = 3
for x in range(len(lists)):
    try:
        while i != len(strings) and strings[i] != '\n':
            source_start, dest_start, length = [int(x) for x in strings[i].split()]
            ranges[range(dest_start, dest_start + length)] = range(source_start, source_start + length)
            i += 1
    except:
        pass
    i += 2
    for elem in lists[x]:
        state = [False, 0]
        for r in ranges.keys():
            if elem in r:
                state = [True, r]
                break
        if x + 1 != len(lists):
            lists[x + 1].append(elem if not state[0] else ranges[state[1]][state[1].index(elem)])
    ranges = {}
print(min(lists[-1]))
