from collections import defaultdict


with open("input.txt", 'r') as f:
    lines = f.readlines()


grid = defaultdict(lambda : ".")

ncols = len(lines[0])
nrows = len(lines)

for i, line in enumerate(lines):
    for j, char in enumerate(line.rstrip('\n')):
        grid[(i, j)] = char

def neighbors(i, j):
    return [
        (i-1, j-1), (i-1, j), (i-1, j+1),
        (i, j-1),             (i, j+1),
        (i+1, j-1), (i+1, j), (i+1, j+1)
    ]

def is_accessible(i, j, grid):
    count = 0
    for ni, nj in neighbors(i, j):
        if grid[(ni, nj)] != ".":
            count += 1
            if count > 3:
                return False
    return True

def print_grid(grid, nrows, ncols):
    for i in range(nrows):
        for j in range(ncols):
            print(grid[(i, j)], end="")
        print()

s = 0
for i in range(nrows):
    for j in range(ncols):
        if grid[(i, j)] == "@" and is_accessible(i, j, grid):
            grid[(i, j)] = "x"
            s += 1

print(s)