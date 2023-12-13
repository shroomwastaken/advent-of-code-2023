from copy import deepcopy

with open("./input.txt", "r") as f:
    strings = f.readlines()


def all_possible_unit_variations(arr):
    res = [deepcopy(arr)]
    for row in range(len(arr)):
        for symb in range(len(arr[row])):
            if arr[row][symb] == "#":
                arr[row][symb] = "."
                res.append(deepcopy(arr))
                arr[row][symb] = "#"
            else:
                arr[row][symb] = "#"
                res.append(deepcopy(arr))
                arr[row][symb] = "."
    return res


units = []
cur_unit = []
for i in range(len(strings)):
    if strings[i] != "\n":
        cur_unit.append(list(strings[i].strip()))
        continue
    units.append(all_possible_unit_variations(cur_unit))
    cur_unit = []
units.append(all_possible_unit_variations(cur_unit))


def check_rows(arr, got_row):
    for row in range(len(arr) // 2):
        if arr[:row + 1] == arr[row + 1:(row + 1) * 2][::-1] and row + 1 != got_row: return row + 1
    for row in range(len(arr) // 2, len(arr) - 1):
        if arr[row - (len(arr) - row - 2):row + 1] == arr[row + 1:len(arr)][::-1] and row + 1 != got_row: return row + 1


def check_columns(arr, got_col):
    cols = [''.join([x[col] for x in arr]) for col in range(len(arr[0]))]
    for row in range(len(cols) // 2):
        if cols[:row + 1] == cols[row + 1:(row + 1) * 2][::-1] and row + 1 != got_col: return row + 1
    for row in range(len(cols) // 2, len(cols) - 1):
        if cols[row - (len(cols) - row - 2):row + 1] == cols[row + 1:len(cols)][::-1] and row + 1 != got_col: return row + 1


# s = 0
# for unit in units: s += res * 100 if (res := check_rows(unit)) != None else check_columns(unit)
# print(s)

s = 0
for vars in units:
    a = check_rows(vars[0], None)
    b = check_columns(vars[0], None)
    for i in range(1, len(vars)):
        na = check_rows(vars[i], a)
        nb = check_columns(vars[i], b)
        if na != None:
            a = na
            break
        if nb != None:
            b = nb
            break
    s += 100 * a if a != None else b
print(s)