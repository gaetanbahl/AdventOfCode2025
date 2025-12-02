with open("input", "r") as f:
    lines = f.readlines()

ids = [(int(a), int(b)) for a, b in (range.split("-") for range in lines[0].split(","))]

def split(n):
    n = str(n)
    return n[:len(n)//2]

def incr_split(n):
    s = split(n)
    s = str(int(s) +1)
    return int(s+s)

def is_repeat(n):
    n = str(n)
    if len(n) % 2 == 1:
        return False
    else:
        a, b = n[:len(n)//2], n[len(n)//2:]
        return a == b

def find_next_repeated(inf, sup):
    n = inf
    while n <= sup:
        if is_repeat(n):
            return n
        n += 1
    return -1

s = 0

for a, b in ids:
    n = find_next_repeated(a, b)
    if n != -1:
        s += n
    else:
        continue

    n = incr_split(n)
    while n <= b:
        s += n
        n = incr_split(n)


print(s)