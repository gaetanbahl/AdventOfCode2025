with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

sp = lines.index("")

ranges, items = lines[:sp], lines[(sp+1):]

ranges = [r.split("-") for r in ranges]
ranges = [(int(a), int(b)) for a, b in ranges]

def ranges_overlap(a, b, c, d):
    return not (b < c or d < a)

def union(a, b, c, d):
    if ranges_overlap(a, b, c, d):
        return (min(a, c), max(b, d))
    return None

merged_ranges = []

for a,b in ranges:
    new_ranges = []
    while(merged_ranges):
        c,d = merged_ranges.pop()
        if ranges_overlap(a, b, c, d):
            a, b = union(a, b, c, d)
        else:
            new_ranges.append((c, d))
    new_ranges.append((a, b))
    merged_ranges = new_ranges

total = 0
for a, b in merged_ranges:
    total += b - a + 1

print(total)