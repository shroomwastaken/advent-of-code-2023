with open("./input.txt", "r") as f:
    strings = f.readlines()

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# make a border around the array to not worry abt bounds checking
strings.insert(0, ''.join(["." for _ in range(len(strings[1]) + 1)]))
for f in range(1, len(strings)):
    strings[f] = "." + strings[f].strip() + "."
strings.append(''.join(["." for _ in range(len(strings[1]))]))

loop_vis = [[" " for _ in range(len(a))] for a in strings]

start_idx = [0, 0] # row, column
# scan through and find S
for i in range(len(strings)):
    if "S" in strings[i]:
        start_idx = [i, strings[i].index("S")]
        break

loop_vis[start_idx[0]][start_idx[1]] = "S"
corners = []
idx = [start_idx[0] + 1, start_idx[1]] # can just start by going down in both the example and my input
facing = DOWN
# traverse the entire loop
while idx != start_idx:
    cur_char = strings[idx[0]][idx[1]]
    loop_vis[idx[0]][idx[1]] = cur_char
    if cur_char == "|":
        idx[0] += 1 if facing == DOWN else -1
    elif cur_char == "-":
        idx[1] += 1 if facing == RIGHT else -1
    elif cur_char == "L":
        if facing == DOWN:
            idx[1] += 1
            facing = RIGHT
        elif facing == LEFT:
            idx[0] -= 1
            facing = UP
    elif cur_char == "J":
        if facing == DOWN:
            idx[1] -= 1
            facing = LEFT
        elif facing == RIGHT:
            idx[0] -= 1
            facing = UP
    elif cur_char == "7":
        if facing == UP:
            idx[1] -= 1
            facing = LEFT
        elif facing == RIGHT:
            idx[0] += 1
            facing = DOWN
    elif cur_char == "F":
        if facing == UP:
            idx[1] += 1
            facing = RIGHT
        elif facing == LEFT:
            idx[0] += 1
            facing = DOWN
    elif cur_char == "S":
        break
    else:
        raise ValueError("what")
