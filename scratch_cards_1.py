import re

with open("scratchcards.txt", "r") as x:
	input = x.readlines()
    
scores = []

for line in input:

    card_value=0

    scratchcard = line.strip().split(":")
    numbers = scratchcard[1].split("|")

    winning_numbers = []

    p = re.compile("\d+")
    for m in p.finditer(numbers[0]):
        winning_numbers.append(m.group())

    p = re.compile("\d+")
    for m in p.finditer(numbers[1]):
        number = m.group()
        if m.group() in winning_numbers:
            card_value = 1 if card_value == 0 else card_value * 2
    scores.append(card_value)
    print(scratchcard[0], card_value)

# print(sum(scores))
