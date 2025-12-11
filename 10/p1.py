with open("input", "r") as file:
    lines = [l.strip().split(" ") for l in file.readlines()]

lights = []
toggles = []

for line in lines:
    lights.append([c == "#" for c in line[0][1:-1]])
    tog = []
    for t in line[1:-1]:
        tog.append(tuple(int(x) for x in t[1:-1].split(",")))
    toggles.append(tog)

def step(l, toggle):
    new_l = l[:]
    for t in toggle:
        new_l[t] = not new_l[t]
    return new_l

total_steps = 0
for i, l in enumerate(lights):

    visited = set()
    visited.add(tuple([False,]*len(l)))
    queue = [(t, [False,]*len(l)) for t in toggles[i][:]]

    n_steps = 0
    found = False
    while True:
        new_queue = []
        while queue:
            toggle, l = queue.pop(0)
            new_l = step(l, toggle)
            t_new_l = tuple(new_l)
            # print(t_new_l, lights[i])
            if t_new_l not in visited:
                if t_new_l == tuple(lights[i]):
                    found = True
                    break
                visited.add(t_new_l)
                for tog in toggles[i]:
                    new_queue.append((tog, new_l))
        
        queue = new_queue
        n_steps += 1
        if found:
            break
    total_steps += n_steps

print(total_steps)