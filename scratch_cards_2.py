import re

with open("example.txt", "r") as x:
	input = x.readlines()

def process_scratchcard(line, j=1):
    print("    " * j, line.split(":")[0])
    winning_number_count=0

    scratchcard = line.strip().split(":")
    numbers = scratchcard[1].split("|")

    winning_numbers = []

    p = re.compile("\d+")
    for m in p.finditer(numbers[0]):
        winning_numbers.append(m.group())

    p = re.compile("\d+")
    for m in p.finditer(numbers[1]):
        if m.group() in winning_numbers:
            winning_number_count += 1

    for i in range(winning_number_count):
        # print("    " *j, "i:",i, "j:", j)
        process_scratchcard(input[i+j], j+1)
    
    global card_count
    card_count+=1

card_count = 0

for line in input:
    process_scratchcard(line)

print(card_count)