with open("./input.txt", "r") as f:
    strings = f.readlines()

units = []
cur_unit = []
for i in range(len(strings)):
    if strings[i] != "\n":
        cur_unit.append(strings[i].strip())
        continue
    units.append(cur_unit)
    cur_unit = []
units.append(cur_unit)


def check_rows(arr):
    for row in range(len(arr) // 2):
        if arr[:row + 1] == arr[row + 1:(row + 1) * 2][::-1]: return row + 1
    for row in range(len(arr) // 2, len(arr) - 1):
        if arr[row - (len(arr) - row - 2):row + 1] == arr[row + 1:len(arr)][::-1]: return row + 1


def check_columns(arr):
    cols = [''.join([x[col] for x in arr]) for col in range(len(arr[0]))]
    for row in range(len(cols) // 2):
        if cols[:row + 1] == cols[row + 1:(row + 1) * 2][::-1]: return row + 1
    for row in range(len(cols) // 2, len(cols) - 1):
        if cols[row - (len(cols) - row - 2):row + 1] == cols[row + 1:len(cols)][::-1]: return row + 1


s = 0
for unit in units: s += res * 100 if (res := check_rows(unit)) != None else check_columns(unit)
print(s)