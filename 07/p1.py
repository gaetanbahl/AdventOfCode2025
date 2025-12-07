from collections import defaultdict

with open("input", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

nrows = len(lines)
ncols = len(lines[0])

queue = []
grid = defaultdict(lambda : ".")
for i in range(nrows):
    for j in range(ncols):
        grid[(i, j)] = lines[i][j]
        if grid[(i, j)] == "S":
            queue.append((i,j))

splits = 0

def check(p):
    global splits
    i, j = p

    if i == nrows:
        return

    if grid[i+1, j] == ".":
        if not (i+1,j) in queue: 
            queue.append((i+1,j))
    elif grid[i+1, j] == "^":
        if not (i+1,j+1) in queue:
            queue.append((i+1,j+1))
        if not (i+1,j-1) in queue:
            queue.append((i+1,j-1))
        splits += 1
    
    grid[(i, j)] = "|"

while queue:
    p = queue.pop()
    check(p)

print(splits)