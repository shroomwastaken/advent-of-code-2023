def get_sets(string: str) -> list[int]:
    nums = [0, 0, 0] # r, g, b
    nums_red = []
    nums_green = []
    nums_blue = []
    l = string.split(";")
    for i in l:
        chunk = i.split(" ")
        if '' in chunk: chunk.remove('')
        for elem in range(len(chunk)):
            if chunk[elem].isdigit():
                if 'd' in chunk[elem + 1]: nums_red.append(int(chunk[elem]))
                elif 'n' in chunk[elem + 1]: nums_green.append(int(chunk[elem]))
                else: nums_blue.append(int(chunk[elem]))
    return [max(nums_red), max(nums_green), max(nums_blue)]

with open("2\input.txt", "r") as f:
    strings = f.readlines()

games = []
sum_of_powers = 0
for string in strings:
    string = string[5:len(string) ] # trim "game: "
    game = []
    id = int(string[0:string.index(":")])
    game.append(id)
    string = string[string.index(":") + 2:]
    game.append(get_sets(string))
    games.append(game)
for game in games:
    sum_of_powers += game[1][0] * game[1][1] * game[1][2]
print(sum_of_powers)
