from scipy.optimize import linprog
import numpy as np

with open("input", "r") as file:
    lines = [l.strip().split(" ") for l in file.readlines()]

joltage = []
toggles = []

for line in lines:
    joltage.append(tuple(int(x) for x in line[-1][1:-1].split(",")))
    tog = []
    for t in line[1:-1]:
        tog.append(tuple(int(x) for x in t[1:-1].split(",")))
    tog.sort(key=lambda x: len(x))
    toggles.append(tog)

total_steps = 0

for i, l in enumerate(joltage):

    c = np.ones(len(toggles[i]))
    A = np.zeros((len(l), len(toggles[i])))

    for j, tog in enumerate(toggles[i]):
        for idx in tog:
            A[idx][j] = 1

    b = np.array(l)

    res = linprog(c, A_eq=A, b_eq=b, bounds=(0, max(l)), method='highs', integrality=np.ones(len(toggles[i])))
    total_steps += int(res.fun)

print(total_steps)