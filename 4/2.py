with open("4/input.txt") as f:
    strings = f.readlines()
total_won = 0
win_s = []
for i in range(len(strings)):
    strings[i] = strings[i][strings[i].index(":") + 1:-1]
for string in strings:
    s = 0
    split_str = string.split(" | ")
    winning_nums = [int(x) for x in str(split_str[0]).split(" ") if x != "" and x != "'"]
    got_nums = [int(x) for x in str(split_str[1]).split(" ") if x != "" and x != "'"]
    for num in got_nums:
        if num in winning_nums:
            s += 1
    win_s.append([s, 1])
total_won = len(win_s)
for i in range(len(win_s)):
    for j in range(i + 1, i + win_s[i][0] + 1):
        win_s[j][1] += win_s[i][1]
print(sum([x[1] for x in win_s]))
