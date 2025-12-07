from collections import defaultdict
from functools import cache

with open("input", 'r') as f:
    lines = [l.strip() for l in f.readlines()]

nrows = len(lines)
ncols = len(lines[0])

grid = defaultdict(lambda : ".")
for i in range(nrows):
    for j in range(ncols):
        grid[(i, j)] = lines[i][j]
        if grid[(i, j)] == "S":
            start_pos = (i,j)

@cache
def check(i, j):

    if i == nrows:
        return 1

    if grid[i+1, j] == ".":
        return check(i+1, j)
    elif grid[i+1, j] == "^":
        a = check(i+1, j+1)
        b = check(i+1, j-1)
        return a+b

print(check(*start_pos))