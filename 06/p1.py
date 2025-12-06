with open("input", "r") as f:
    lines = [l for l in f.readlines()]

ops = lines[-1].strip().split()
ncol, nrow = len(lines[0]), len(lines) -1

init = {"*" : 1, "+" : 0}
funcs = {"*" : int.__mul__, "+" : int.__add__}

total = 0
for i in range(ncol):
    
    res = init[ops[i]]

    for j in range(nrow):
        res = funcs[ops[i]](int(lines[j][i]), res)
    total += res

print(total)