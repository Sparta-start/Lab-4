res = sorted(set(input().split()) & set(input().split()), key=int)
print(" ".join(res))