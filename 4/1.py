with open("4/input.txt") as f:
    strings = f.readlines()
total = 0

for i in range(len(strings)):
    strings[i] = strings[i][strings[i].index(":") + 1:-1]
for string in strings:
    sum = 0
    split_str = string.split(" | ")
    winning_nums = [int(x) for x in str(split_str[0]).split(" ") if x != "" and x != "'"]
    got_nums = [int(x) for x in str(split_str[1]).split(" ") if x != "" and x != "'"]
    for num in got_nums:
        if num in winning_nums:
            if sum == 0:
                sum = 1
            else:
                sum *= 2
    total += sum

print(total)
