import re
with open("1/input.txt", "r") as f:
    strings = f.readlines()
n_strings = []

# trim the \n
for s in strings:
    if '\n' in s: s = s[:-1]
    n_strings.append(s.lower())

nums = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
nn_strings = []

for string in n_strings:
    interm = ""
    for char in range(len(string)):
        if (a := string[char:char + 3]) in ["one", "two", "six"]:
            interm += nums[a]
        elif (a := string[char:char + 4]) in ["four", "five", "nine"]:
            interm += nums[a]
        elif (a := string[char:char + 5]) in ["three", "seven", "eight"]:
            interm += nums[a]
        else:
            interm += string[char]
    nn_strings.append(interm)
summ = 0
for string in nn_strings:
    digits = ''.join(re.findall('\d+', string))
    summ += int(digits[0]) * 10 + int(digits[-1])
print(summ)