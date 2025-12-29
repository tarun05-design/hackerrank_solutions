from itertools import permutations

a, b = map(str,input().split())
split_size=int(b)

per=list(permutations(a,split_size))
sorted_list=per.sort()

for item in per:
    no_space="".join(item)
    print(no_space)