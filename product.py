from itertools import product

n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

result = product(list_a, list_b)
for pair in result:
    print(pair, end=' ')