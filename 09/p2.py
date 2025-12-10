with open("input", "r") as f:
    points = [(int(a), int(b)) for a, b in (line.split(",") for line in f.readlines())]

def area(x1, y1, x2, y2):
    return (abs(x1 - x2 ) + 1) * (abs(y1 - y2) + 1)


vertical_edges = []
horizontal_edges = []
points = points + [points[0]]
for i, p in enumerate(points[:-1]):
    p2 = points[i+1]
    x1, y1 = p
    x2, y2 = p2
    if x1 == x2:
        vertical_edges.append((x1, min(y1, y2), max(y1, y2)))
    elif y1 == y2:
        horizontal_edges.append((y1, min(x1, x2), max(x1, x2)))
    
points = points[:-1]

def is_point_inside(p, vertical_edges):
    if p in points:
        return True  # On a known point
    n_on_left = 0
    xp, yp = p
    for y, x1, x2 in horizontal_edges:
        if yp == y and x1 <= xp <= x2:
            return True  # On edge
    for x, y1, y2 in vertical_edges:
        if xp == x and y1 <= yp <= y2:
            return True  # On edge
        elif xp > x and y1 < yp <= y2:
            n_on_left += 1

    return n_on_left % 2 == 1

def get_opposite_corners(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1, y2), (x2, y1)

areas = []

for i, p1 in enumerate(points):
    for j, p2 in enumerate(points[(i+1):]):
        o1, o2 = get_opposite_corners(p1, p2)
        if is_point_inside(o1, vertical_edges) and is_point_inside(o2, vertical_edges):
            areas.append(area(p1[0], p1[1], p2[0], p2[1]))

print(max(areas))