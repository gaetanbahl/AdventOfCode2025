with open("input", "r") as f:
    lines = f.readlines()

ids = [(int(a), int(b)) for a, b in (range.split("-") for range in lines[0].split(","))]
    
def is_repeat(n):
    n = str(n)
    for num_repeated_digits in range(1, len(n)):
        if len(n) % num_repeated_digits == 0:
            parts = [n[j*num_repeated_digits:(j+1)*num_repeated_digits] for j in range(len(n)//num_repeated_digits)]
            if len(set(parts)) == 1:
                return parts[0], len(n)//num_repeated_digits
            
    return False

def find_next_repeated(inf, sup):
    n = inf
    while n <= sup:
        if parts := is_repeat(n):
            return parts
        n += 1
    return -1, -1

s = 0

for a, b in ids:
    print("processing ", a, b)
    part, repeats = find_next_repeated(a, b)
    while part != -1:
        print(part, "repeated", repeats, "times")
        n = int(part * repeats)
        s += n
        part, repeats = find_next_repeated(n+1, b)

print(s)