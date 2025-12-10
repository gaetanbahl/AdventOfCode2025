with open("input", "r") as f:
    lines = [(int(a), int(b)) for a, b in (line.split(",") for line in f.readlines())]

def area(x1, y1, x2, y2):
    return (abs(x1 - x2 ) + 1) * (abs(y1 - y2) + 1)

print(max([area(x1, y1, x2, y2) for (x1, y1) in lines for (x2, y2) in lines]))