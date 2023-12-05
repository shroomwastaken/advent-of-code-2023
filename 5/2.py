# this script took 6 hours and 15 minutes to finish
# it gave the right answer though so its fine

with open("5/input.txt") as f:
    strings = f.readlines()

i = 3
seed_ranges = []
ranges_all = []
ranges = {}
res = []
first_str = strings[0].split(": ")[1][:-1].split(" ")
for g in range(0, len(first_str), 2):
    seeds = range(int(first_str[g]), int(first_str[g]) + int(first_str[g + 1]))
    seed_ranges.append(seeds)

while i < len(strings) and strings[i] != '\n':
    source_start, dest_start, length = [int(x) for x in strings[i].split()]
    ranges[range(dest_start, dest_start + length)] = range(source_start, source_start + length)
    i += 1
    if i >= len(strings):
        ranges_all.append(ranges)
        ranges = {}
        break
    elif strings[i] == '\n':
        i += 2
        ranges_all.append(ranges)
        ranges = {}

for rs in range(len(seed_ranges)):
    print(f"doing seed range {rs}")
    values = list(seed_ranges[rs])
    for v_idx in range(len(values)):
        for ranges in range(len(ranges_all)):
            for r in ranges_all[ranges].keys():
                if values[v_idx] in r:
                    values[v_idx] = ranges_all[ranges][r][r.index(values[v_idx])]
                    break
    res.append(min(values))
print(min(res))
