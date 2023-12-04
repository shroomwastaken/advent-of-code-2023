with open("3\input.txt", "r") as f:
    strings = f.readlines()

sum = 0


# you can tell i didnt care about efficiency
def check_gears_and_get_sum_of_ratios(s_inf: list, n_inf: list) -> int:
    sum = 0
    valid_symbs = []
    for num in n_inf:
        symbs = [x for x in s_inf if -1 <= x[0] - num[0] <= 1 and -1 <= x[1] - num[1] <= len(str(num[2]))]
        for symb in symbs:
            if not symb in valid_symbs:
                valid_symbs.append(symb)
                valid_symbs.append(num[2])
            else:
                sum += num[2] * valid_symbs[valid_symbs.index(symb) + 1]
    return sum


# transform the strings into list of lists of symbols
# with extra layer around the array to avoid bounds checking stuff
strings.insert(0, '.' * len(strings[1]))
strings.append('.' * len(strings[2]))
for i in range(len(strings)):
    strings[i] = list('.' + strings[i][:-1] + '.')

# get positions of all symbols
symbol_info = [] # list of coords
for i in range(len(strings)):
    for j in range(len(strings[i])):
        if strings[i][j] != '.' and not strings[i][j].isdigit():
            symbol_info.append([i, j])

# get positions and lengths of all numbers
num_info = [] # list of coords of start and the num
for i in range(len(strings)):
    cur_num = []
    start_j = 0
    for j in range(len(strings[i])):
        if strings[i][j].isdigit():
            start_j = j if start_j == 0 else start_j
            cur_num.append(strings[i][j])
        else:
            if cur_num != []:
                num_info.append([i, start_j, int(''.join(cur_num))])
                start_j = 0
                cur_num = []

print(check_gears_and_get_sum_of_ratios(s_inf=symbol_info, n_inf=num_info))
