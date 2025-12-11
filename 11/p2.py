from functools import cache

with open("input", "r") as file:
    lines = [l.strip().split(" ") for l in file.readlines()]

neighbors = dict()
for line in lines:
    node = line[0][:-1]
    edges = line[1:]
    neighbors[node] = edges

neighbors["out"] = []

@cache
def dfs(node, output):

    if node == output:
        return 1
    
    total = 0
    for n in neighbors[node]:
        total += dfs(n, output)

    return total

print(dfs("svr", "fft")*dfs("fft", "dac")*dfs("dac", "out"))