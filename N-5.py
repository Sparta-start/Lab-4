a, b = map(int, input().split())

an = set(int(input()) for _ in range(a))
bor = set(int(input()) for _ in range(b))

col = an.intersection(bor)
uniq = an - col
borya = bor - col

print(len(col))
print(*sorted(col))

print(len(uniq))
print(*sorted(uniq))

print(len(borya))
print(*sorted(borya))
