with open("input", "r") as f:
    lines = [l[:-1] for l in f.readlines()]

ops = list(reversed(lines[-1].strip().split()))
ncol, nrow = len(lines[0]), len(lines) -1

nums = [[]]

for c in reversed(range(ncol)):
    
    n = "".join([lines[s][c] for s in range(nrow)])
    try:
        nums[-1].append(int(n))
    except ValueError:
        nums.append([])

init = {"*" : 1, "+" : 0}
funcs = {"*" : int.__mul__, "+" : int.__add__}

total = 0
for i,ns in enumerate(nums):
    
    res = init[ops[i]]

    for n in ns:
        res = funcs[ops[i]](n, res)
    total += res

print(total)