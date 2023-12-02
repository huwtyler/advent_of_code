with open("p2_1_input.txt", "r") as x:
	input = x.readlines()

output = []

for game in input:
    game = game.strip().split(":")
    game[0] = int(game[0].replace("Game ", ""))
    game[1] = game[1].split(";")

    min_red = 0
    min_blue = 0
    min_green = 0

    for set in game[1]:
        set = set.strip().split(", ")

        for cubes in set:
            if cubes.find("red") != -1:
                if int(cubes.replace(" red", "")) > min_red:
                     min_red = int(cubes.replace(" red", ""))
            elif cubes.find("green") != -1:
                if int(cubes.replace(" green", "")) > min_green:
                     min_green = int(cubes.replace(" green", ""))
            elif cubes.find("blue") != -1:
                if int(cubes.replace(" blue", "")) > min_blue:
                     min_blue = int(cubes.replace(" blue", ""))

    output.append(min_red*min_green*min_blue)

print(sum(output))