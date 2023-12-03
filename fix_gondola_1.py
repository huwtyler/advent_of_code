import re

with open("p3_1_input.txt", "r") as x:
	input = x.readlines()

symbol_positions = []
output = []

for line in input:
    x = []

    p = re.compile("[!,@,£,$,%,^,&,*,(,),\,/,\-,_,=,+,#]")
    for m in p.finditer(line):
          x.append(m.start())
    
    symbol_positions.append(x)

for i, line in enumerate(input):
    p = re.compile("\d+")
    for m in p.finditer(line):
        if i == 0:
            if m.start() -1 in symbol_positions[i] or m.end() in symbol_positions[i] or m.start() -1 in symbol_positions[i+1] or m.end() in symbol_positions[i+1]:
                output.append(int(m.group()))
            for j, digit in enumerate(m.group()):
                 if m.start() +j in symbol_positions[i+1]:
                      output.append(int(m.group()))
                      break
        elif i == len(symbol_positions)-1:
            if m.start() -1 in symbol_positions[i] or m.end() in symbol_positions[i] or m.start() -1 in symbol_positions[i-1] or m.end() in symbol_positions[i-1]:
                output.append(int(m.group()))
            for j, digit in enumerate(m.group()):
                if m.start() +j in symbol_positions[i-1]:
                    output.append(int(m.group()))
                    break
        else:
            if m.start() -1 in symbol_positions[i] or m.end() in symbol_positions[i] or m.start() -1 in symbol_positions[i-1] or m.end() in symbol_positions[i-1] or m.start() -1 in symbol_positions[i+1] or m.end() in symbol_positions[i+1]:
                output.append(int(m.group()))
            for j, digit in enumerate(m.group()):
                if m.start() +j in symbol_positions[i-1] or m.start() +j in symbol_positions[i+1]:
                    output.append(int(m.group()))
                    break

print(sum(output))