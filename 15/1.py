with open("./input.txt", "r") as f:
    strings = f.readline().split(",")

s = 0
total = 0
for string in strings:
    for char in string:
        s += ord(char)
        s *= 17
        s %= 256
    total += s
    s = 0
print(total)