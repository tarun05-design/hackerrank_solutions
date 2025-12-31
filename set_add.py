n=int(input())
a=list()

for i in range(n):
    string=str(input())
    a.append(string)
    
remove_dup=set(a)
print(len(remove_dup))