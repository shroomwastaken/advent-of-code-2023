with open("./input.txt", "r") as f:
    fc = [x.strip() for x in f.readlines()]
    game = [[x[col] for x in fc] for col in range(len(fc[0]))]

s = 0
for col in range(len(game)):
    for symb in range(1, len(game[col])):
        if game[col][symb] == "O":
            new_ind = symb
            for i in range(len(game[col][:symb]))[::-1]:
                if game[col][i] != ".": break
                if game[col][i] == ".":
                    if i >= 1 and game[col][i - 1] != ".":
                        new_ind = i
                        break
                    elif i == 0:
                        new_ind = 0
                        break
            game[col][symb], game[col][new_ind] = game[col][new_ind], game[col][symb]
    for symb in range(len(game[col])):
        if game[col][symb] == "O":
            s += len(game[col]) - symb
print(s)