a, b = [int(x) for x in input().split()]
day = set()
for i in range(b):
    begin, step = [int(x) for x in input().split()]
    day |= {x for x in range(begin, a+1, step) if x % 7 not in [0,6]}
print(len(day))