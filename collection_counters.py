shoes_count = int(input())

size=list(map(int,input().split()))

cus_count = int(input())

total=[]

for i in range(cus_count):
    sizes, price = map(int, input().split())
    if sizes in size:
        total.append(price)
        size.remove(sizes)
        
print(sum(total))