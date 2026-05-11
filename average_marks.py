n = int(input())
headers = input().split()
marks_index = headers.index("MARKS")
total = 0

for i in range(n):
    row=input().split()
    total+=int(row[marks_index]) 
    
avg = total / n
print(avg)
