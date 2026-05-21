total_integers = int(input())
s = set(map(int, input().split()))
total_commands = int(input())

for i in range(total_commands):
    command = input().split()
    
    if len(command) == 1:
        s.pop()
    else:
        if command[0] == 'remove':
            s.remove(int(command[1]))
        else:
            s.discard(int(command[1]))
            
print(sum(s))