with open("input", "r") as f:
    lines = f.readlines()
total = 0
position = 50
for line in lines:
    if line[0] == "L":
        position -= int(line.strip()[1:])
    elif line[0] == "R":
        position += int(line.strip()[1:])
    position = position % 100 
    if position == 0:
        total += 1
print(total)