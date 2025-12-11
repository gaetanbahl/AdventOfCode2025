with open("input", "r") as file:
    lines = [l.strip().split(" ") for l in file.readlines()]

neighbors = dict()
for line in lines:
    node = line[0][:-1]
    edges = line[1:]
    neighbors[node] = edges

def dfs(node):

    if node == "out":
        return 1
    
    total = 0
    for n in neighbors[node]:
        total += dfs(n)

    return total

print(dfs("you"))