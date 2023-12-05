import re

with open("scratchcards.txt", "r") as x:
    input = x.readlines()

def process_scratchcard(line, line_number, previous_padding):
    global card_count
    card_count+=1

    padding = previous_padding + "    "

    print(padding, line.split(":")[0])

    p = re.compile("\d+")

    scratchcard = line.strip().split(":")
    numbers = scratchcard[1].split("|")
    prize_numbers = p.findall(numbers[0])
    card_numbers = p.findall(numbers[1])

    winning_numbers_count = len([x for x in prize_numbers if x in card_numbers])

    for i in range(winning_numbers_count):
        card_number = i + line_number + 1
        process_scratchcard(input[card_number], card_number, padding)

card_count = 0

for l_no, line in enumerate(input):
    process_scratchcard(line, l_no, "")

print(card_count)