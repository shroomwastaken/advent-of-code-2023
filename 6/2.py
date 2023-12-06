with open("6/input.txt", "r") as f:
    strings = f.readlines()

times = int(''.join(strings[0][11:].split(" "))[:-1])
distances = int(''.join(strings[1][11:].split(" ")))
res = 0
for i in range(0, times):
    if (times - i) * i > distances:
        res += 1
print(res)
