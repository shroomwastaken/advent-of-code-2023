with open("./input.txt", "r") as f:
    strings = f.readlines()

steps = strings[0][:-1]
l_entry_nodes = []
l_exit_nodes = []
step_cycles = 0
for i in range(2, len(strings)):
    split_str = strings[i].split(" = ")
    entry_node = split_str[0]
    exit_nodes = (split_str[1].split(", ")[0][1:], split_str[1].split(", ")[1][:-2])
    l_entry_nodes.append(entry_node)
    l_exit_nodes.append(exit_nodes)

cur_node = l_entry_nodes.index("AAA")
num_steps = 0
j = 0

while cur_node != l_entry_nodes.index("ZZZ"):
    cur_node = l_entry_nodes.index(l_exit_nodes[cur_node][0 if steps[j] == "L" else 1])
    num_steps += 1
    j += 1
    if j == len(steps):
        j = 0

print(num_steps)