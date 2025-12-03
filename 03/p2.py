
import math

with open("input", 'r') as f:
    lines = f.readlines()

lines = [[int(i) for i in l.strip()] for l in lines]

def check_dp(line):
    N = len(line)
    prev, curr = [0] * N, [0] * N
    prev[-1] = int(line[-1])

    for j in range(N-2, -1, -1):
        prev[j] = max(int(line[j]), int(prev[j+1]))

    for i in range(10, -1, -1):
        for j in range(N-12+i, -1, -1):
            curr[j] = max(int(curr[j+1]), int(line[j])*(10**(int(math.log10(prev[j+1])+1))) + prev[j+1])
        prev = curr.copy()

    return max(curr)

def check_simple(line):
    curr_number = 0
    remain_line = line
    for i in range(12):
        if i != 11:
            candidates = remain_line[:-(12-i-1)]
        else:
            candidates = remain_line
        m = max(candidates)
        curr_number = curr_number * 10 + m
        idx = remain_line.index(m)
        remain_line = remain_line[(idx+1):]

    return curr_number

dp = list(map(int, map(check_dp, lines)))
# simple = list(map(int, map(check_simple, lines)))
print(sum(dp))
# print(sum(simple))