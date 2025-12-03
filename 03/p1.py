from collections import deque

with open("input", 'r') as f:
    lines = f.readlines()

lines = [[int(i) for i in l.strip()] for l in lines]


def check(line):
    largest_tens_so_far = 0
    max_joltage = 0
    for i, n in enumerate(line):
        if n >= largest_tens_so_far:
            largest_tens_so_far = n
        for j, m in enumerate(line[(i+1):]):
            joltage = n * 10 + m
            if joltage > max_joltage:
                max_joltage = joltage

    return max_joltage

total = sum(map(check, lines))

print(total)