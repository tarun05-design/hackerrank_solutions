from itertools import combinations

a,b = map(str, input().split())

lst = []

for i in a:
    lst.append(i)
lst.sort()
ss = ''

for x in lst:
    ss+=x
a=ss

size=int(b)

for i in range(1,size+1):
    comb = list(tuple(sorted(combinations(a,i))))

    for item in comb:
        remove_space=''.join(item)
        print(remove_space)
