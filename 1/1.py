import re
s = 0
with open("1/input.txt", "r") as f:
    strings = f.readlines()
for string in strings:
    digits = ''.join(re.findall('\d+', string))
    s += int(digits[0]) * 10 + int(digits[-1])
print(s)
