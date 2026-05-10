n = int(input())

word= {}

for i in range(n):
    text=input()
    
    if text in word:
        word[text] += 1 
    else:
        word[text] = 1 
        
print(len(word))
print(*word.values())