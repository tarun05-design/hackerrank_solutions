total_student, subjects = map(int, input().split())

lst = []

for i in range(subjects):
    a = list(map(float, input().split()))
    lst.append(a)

column_wise = list(zip(*lst))

for i in column_wise:
    print(sum(i) / subjects)
