n1= int(input())
set1= set(map(int,input().split()))
n2= int(input())
set2= set(map(int,input().split()))

sub = set1.intersection(set2)
print(len(sub))