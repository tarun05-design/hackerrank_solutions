n=int(input())

aa=[]
bb=[]

for i in range(n):
    a,b=map(str,input().split())
    aa.append(a)
    bb.append(b)
    
for j in range(n):
    try:
        print(int(aa[j])//int(bb[j]))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as k:
        print("Error Code:",k)
    