if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    lst=list(arr)
    unique=list(set(lst))
    unique.sort()
    
    print(unique[-2])
    