import re

with open("p3_1_input.txt", "r") as x:
	input = x.readlines()

symbol_positions = []
gear_adj = []

for line in input:
    x = []

    p = re.compile("[*]")
    for m in p.finditer(line):
          x.append(m.start())
    
    symbol_positions.append(x)

for i, line in enumerate(input):
    p = re.compile("\d+")
    for m in p.finditer(line):
        if i == 0:
            if m.start() -1 in symbol_positions[i]: #W
                gear_adj.append([int(m.group()), [i, m.start() -1]])
            if m.start() -1 in symbol_positions[i+1]: #SW
                gear_adj.append([int(m.group()), [i+1, m.start() -1]])
            if m.end() in symbol_positions[i]: #E
                gear_adj.append([int(m.group()), [i, m.end()]])
            if m.end() in symbol_positions[i+1]: #SE
                gear_adj.append([int(m.group()), [i+1, m.end()]])
            for j, digit in enumerate(m.group()):
                 if m.start() +j in symbol_positions[i+1]: #S
                      gear_adj.append([int(m.group()), [i+1, m.start() +j]])
        elif i == len(symbol_positions)-1:
            if m.start() -1 in symbol_positions[i]: #W
                gear_adj.append([int(m.group()), [i, m.start() -1]])
            if m.start() -1 in symbol_positions[i-1]: #NW
                gear_adj.append([int(m.group()), [i-1, m.start() -1]])
            if m.end() in symbol_positions[i]: #E
                gear_adj.append([int(m.group()), [i, m.end()]])
            if m.end() in symbol_positions[i-1]: #NE
                gear_adj.append([int(m.group()), [i-1, m.end()]])
            for j, digit in enumerate(m.group()):
                 if m.start() +j in symbol_positions[i-1]: #N
                      gear_adj.append([int(m.group()), [i-1, m.start() +j]])
        else:
            if m.start() -1 in symbol_positions[i]: #W
                gear_adj.append([int(m.group()), [i, m.start() -1]])
            if m.start() -1 in symbol_positions[i-1]: #NW
                gear_adj.append([int(m.group()), [i-1, m.start() -1]])
            if m.end() in symbol_positions[i]: #E
                gear_adj.append([int(m.group()), [i, m.end()]])
            if m.end() in symbol_positions[i-1]: #NE
                gear_adj.append([int(m.group()), [i-1, m.end()]])
            if m.start() -1 in symbol_positions[i+1]: #SW
                gear_adj.append([int(m.group()), [i+1, m.start() -1]])
            if m.end() in symbol_positions[i+1]: #SE
                gear_adj.append([int(m.group()), [i+1, m.end()]])
            for j, digit in enumerate(m.group()):
                if m.start() +j in symbol_positions[i-1]: #N
                    gear_adj.append([int(m.group()), [i-1, m.start() +j]])
                if m.start() +j in symbol_positions[i+1]: #S
                    gear_adj.append([int(m.group()), [i+1, m.start() +j]])

def find_matching_pairs(pair_list):
    matching_pairs = []

    for i in range(len(pair_list)):
        current_pair = pair_list[i]
        current_address = current_pair[1]

        for j in range(i + 1, len(pair_list)):
            compare_pair = pair_list[j]
            compare_address = compare_pair[1]

            if current_address == compare_address:
                matching_pairs.append(current_pair[0] * compare_pair[0])

    return matching_pairs

matching_pairs = find_matching_pairs(gear_adj)

# print(matching_pairs)
print(sum(matching_pairs))