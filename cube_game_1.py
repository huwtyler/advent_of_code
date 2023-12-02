with open("p2_1_input.txt", "r") as x:
	input = x.readlines()
	
max_red = 12
max_blue = 14
max_green = 13

output = 0
game_failed = False

failed_games = []

for game in input:
    game = game.strip().split(":")
    game[0] = int(game[0].replace("Game ", ""))
    game[1] = game[1].split(";")

    red_count = 0
    green_count = 0
    blue_count = 0

    for set in game[1]:
        set = set.strip().split(", ")

        for cubes in set:
            if cubes.find("red") != -1:
                if int(cubes.replace(" red", "")) > max_red:
                     game_failed = True
                     break
            elif cubes.find("green") != -1:
                if int(cubes.replace(" green", "")) > max_green:
                     game_failed = True
                     break
            elif cubes.find("blue") != -1:
                if int(cubes.replace(" blue", "")) > max_blue:
                     game_failed = True
                     break
            
    if game_failed:
        failed_games.append(game[0])
    
    game_failed = False

output = sum(range(101)) - sum(failed_games)

print(output)