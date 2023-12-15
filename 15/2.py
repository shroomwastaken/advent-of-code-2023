with open("./input.txt", "r") as f:
    strings = f.readline().split(",")
info = []

for string in strings:
    if "=" in string:
        info.append([string.split("=")[0], int(string.split("=")[1])])
    elif "-" in string:
        info.append([string[:-1], "-"])


def hash(str: str) -> int:
    s = 0
    for char in str:
        s += ord(char)
        s *= 17
        s %= 256
    return s


def is_elem_in_list(arr, str: str) -> int:
    return farr.index(str) if str in (farr := [x[0] for x in arr]) else -1


def remove_elem(arr, rem):
    return [i for i in arr if i[0] != rem]


boxes = [[] for _ in range(256)]
for elem in info:
    box_label = hash(elem[0])
    if elem[1] == "-":
        boxes[box_label] = remove_elem(boxes[box_label], elem[0])
    else:
        if (idx := is_elem_in_list(boxes[box_label], elem[0])) == -1:
            boxes[box_label].append(elem)
        else:
            boxes[box_label][idx] = elem
res = 0
for box in range(len(boxes)):
    if boxes[box] == []: continue
    for lens in range(len(boxes[box])):
        res += (box + 1) * (lens + 1) * boxes[box][lens][1]
print(res)