def split_and_join(line):
    n=line.split()
    d="-".join(n)
    return d

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)