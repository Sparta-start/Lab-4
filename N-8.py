a = int(input())
nums = set(range(1, a + 1))
tru = nums
while True:
    inp = input()
    if inp == 'HELP':
        break
    inp = {int(x) for x in inp.split()}
    if len(tru&inp) > len(tru)/2:
        print('YES')
        tru &= inp
    else:
        print('NO')
        tru &= nums - inp
        
print(' '.join([str(x) for x in sorted(tru)]))