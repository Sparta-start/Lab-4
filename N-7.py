a = int(input())
nums = set(range(1, a + 1))
tru = nums
while True:
    inp = input()
    if inp == 'HELP':
        break
    inp = {int(x) for x in inp.split()}
    ans = input()
    if ans == 'YES':
        tru &= inp
    else:
        tru &= nums - inp

print(' '.join([str(x) for x in sorted(tru)]))