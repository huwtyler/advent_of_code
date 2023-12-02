import re

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
str2num = {
    "one": "one",
    "two": "two",
    "three": "three",
    "four": "four",
    "five": "five",
    "six": "six",
    "seven": "seven",
    "eight": "eight",
    "nine": "nine",
}

with open("input.txt", "r") as x:
	values = x.readlines()

total = 0

def replace_alpha(string):
    indexes = []

    def find_positions(number_string, number):
        positions = [m.start() for m in re.finditer(number_string, string)]
        for position in positions:
            indexes.append([position, number])
    
    y = 1

    for x in words:
        find_positions(x, y)
        y += 1
    
    if len(indexes) > 0:
        first_index = str(sorted(indexes, key=lambda x: x[0], reverse= False).pop(0))
        last_index = str(sorted(indexes, key=lambda x: x[0], reverse= True).pop(0))
    
        if first_index[1] == 1:
            string = string.replace(words[0], first_index[1], 1)

        elif first_index[1] == 2:
            string = string.replace("two", first_index[1], 1)
        
        elif first_index[1] == 3:
            string = string.replace("three", first_index[1], 1)
        
        elif first_index[1] == 4:
            string = string.replace("four", first_index[1], 1)
        
        elif first_index[1] == 5:
            string = string.replace("five", first_index[1], 1)
        
        elif first_index[1] == 6:
            string = string.replace("six", first_index[1], 1)
        
        elif first_index[1] == 7:
            string = string.replace("seven", first_index[1], 1)
        
        elif first_index[1] == 8:
            string = string.replace("eight", first_index[1], 1)
        
        elif first_index[1] == 9:
            string = string.replace("nine", first_index[1], 1)
        
        if last_index[1] == 1:
            string = string.replace("one", last_index[1], -1)

        elif last_index[1] == 2:
            string = string.replace("two", last_index[1], -1)
        
        elif last_index[1] == 3:
            string = string.replace("three", last_index[1], -1)
        
        elif last_index[1] == 4:
            string = string.replace("four", last_index[1], -1)
        
        elif last_index[1] == 5:
            string = string.replace("five", last_index[1], -1)
        
        elif last_index[1] == 6:
            string = string.replace("six", last_index[1], -1)
        
        elif last_index[1] == 7:
            string = string.replace("seven", last_index[1], -1)
        
        elif last_index[1] == 8:
            string = string.replace("eight", last_index[1], -1)
        
        elif last_index[1] == 9:
            string = string.replace("nine", last_index[1], -1)

    return string

for cal_value in values:

    cal_value_list = list(replace_alpha(cal_value))

    for value in cal_value_list:
        if value.isnumeric():
            d1 = value
            break

    for value in reversed(cal_value_list):
        if value.isnumeric():
            d2 = value
            break

    output = str(d1) + str(d2)
    total += int(output)

print(total)