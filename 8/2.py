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

cur_nodes = [l_entry_nodes.index(x) for x in l_entry_nodes if x[-1] == "A"]
num_steps = 0
j = 0

steps_to_z = []

for ent_node in range(len(cur_nodes)):
    while l_entry_nodes[cur_nodes[ent_node]][-1] != "Z":
        cur_nodes[ent_node] = l_entry_nodes.index(l_exit_nodes[cur_nodes[ent_node]][0 if steps[j] == "L" else 1])
        j += 1
        num_steps += 1
        if j == len(steps):
            j = 0
    steps_to_z.append(num_steps)
    num_steps = 0

mult_res = 1
for k in steps_to_z:
    mult_res *= (k / len(steps))
mult_res *= len(steps)
print(mult_res)