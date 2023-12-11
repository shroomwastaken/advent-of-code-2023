import itertools

with open("./input.txt", "r") as f:
    strings = [list(s.strip()) for s in f.readlines()] # char by char

# expanding the universe :0

# expanding rows
n_strings = []
for string in range(len(strings)):
    if strings[string] == ["." for _ in range(len(strings[string]))]:
        n_strings.append(strings[string])
    n_strings.append(strings[string])

# expanding columns
for col in range(len(n_strings[0])):
    if all([strings[i][col] == "." for i in range(len(strings))]):
        for i in range(len(n_strings)):
            n_strings[i][col] = ".."

for s in range(len(n_strings)):
    n_strings[s] = ''.join(n_strings[s])

# x1, y1 - coords of first galaxy in the pair; x2, y2 - coords of second galaxy in pair
def calculate_steps(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


galaxies = []
for row in range(len(n_strings)):
    for char in range(len(n_strings[row])):
        if n_strings[row][char] == "#":
            galaxies.append([row, char])

pairs = list(itertools.combinations(galaxies,2))

s = 0
for i in pairs:
    s += calculate_steps(i[0][0], i[0][1], i[1][0], i[1][1])
print(s)