with open("input", "r") as f:
    lines = f.readlines()
    
total = 0
position = 50

for line in lines:
    if line[0] == "L":
        prev_pos = position
        position -= int(line.strip()[1:])
        # position is always positive at the end of the loop, 
        # so, if it's negative we must have crossed 0 at least once
        if position < 0:
            total += abs(position // 100)
            # if we were already at zero before, 
            # this number is over valued by 1
            if prev_pos == 0:
                total -= 1
        # check if we're now stopped at zero
        position = position % 100
        if position == 0:
            total += 1
    elif line[0] == "R":
        position += int(line.strip()[1:])
        total += position // 100
        position = position % 100

print(total)