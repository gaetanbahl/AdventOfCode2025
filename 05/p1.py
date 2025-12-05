with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

sp = lines.index("")

ranges, items = lines[:sp], lines[(sp+1):]

ranges = [r.split("-") for r in ranges]
ranges = [(int(a), int(b)) for a, b in ranges]

items = [int(i) for i in items]

total = 0

for i in items:
    for a, b in ranges:
        if a <= i <= b:
            total += 1
            break

print(total)