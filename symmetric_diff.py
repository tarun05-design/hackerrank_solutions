n=int(input())
set_a=set(map(int,input().split()))
m=int(input())
set_b=set(map(int,input().split()))

def symmetric_diff(a,b):
    a=set_a
    b=set_b
    result= a.symmetric_difference(b)
    lst=list(result)
    lst.sort()
    for i in lst:
        print(i)

symmetric_diff(set_a,set_b)
        
