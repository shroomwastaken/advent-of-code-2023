with open("6/input.txt", "r") as f:
    strings = f.readlines()

times = [int(x) for x in strings[0][11:].split(" ") if x.isnumeric()]
times.append(int(strings[0][11:].split(" ")[-1][:-1])) # fuckin '\n'
distances = [int(x) for x in strings[1][11:].split(" ") if x.isnumeric()]
res = 1
for time in range(len(times)):
    interm = 0
    for i in range(0, times[time]):
        if (times[time] - i) * i > distances[time]:
            interm += 1
    res *= interm if interm > 0 else 1
print(res)