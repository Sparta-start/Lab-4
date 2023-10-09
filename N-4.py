numbers = input().split()
sete = set()
for num in numbers:
    if num in sete:
        print("YES")
    else:
        print("NO")
        sete.add(num)