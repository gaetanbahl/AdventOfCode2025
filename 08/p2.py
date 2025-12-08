import heapq
from collections import defaultdict

with open("input", "r") as file:
    lines = [tuple([int(n) for n in l.strip().split(",")]) for l in file.readlines()]

def eclidean_distance(a, b):
    return sum([(a[i] - b[i]) ** 2 for i in range(len(a))]) ** 0.5

print(f"Read {len(lines)} lines")

distances = []
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        distances.append((eclidean_distance(lines[i], lines[j]), (i, j)))

heapq.heapify(distances)

group_ids = defaultdict(lambda: None)
groups = []
n_groups = 0

while distances:
    dist, (a, b) = heapq.heappop(distances)
    #print(f"Distance between {a} and {b}: {dist}")

    if group_ids[a] is None and group_ids[b] is None:
        group_ids[a] = n_groups
        group_ids[b] = n_groups
        s = set()
        s.add(a)
        s.add(b)
        groups.append(s)
        n_groups += 1
    elif group_ids[a] is not None and group_ids[b] is None:
        group_id = group_ids[a]
        group_ids[b] = group_id
        groups[group_id].add(b)
    elif group_ids[a] is None and group_ids[b] is not None:
        group_id = group_ids[b]
        group_ids[a] = group_id
        groups[group_id].add(a)
    else:
        group_id_a = group_ids[a]
        group_id_b = group_ids[b]
        if group_id_a != group_id_b:
            for item in groups[group_id_b]:
                group_ids[item] = group_id_a
                groups[group_id_a].add(item)
            groups[group_id_b] = set()

    if len(groups[group_ids[a]]) >= 1000:
        print(f"Group {group_ids[a]} reached size 1000")
        print("Junction box a", lines[a])
        print("Junction box b", lines[b])
        print("Result", lines[a][0] * lines[b][0])
        break