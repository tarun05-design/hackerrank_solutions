def count_substring(string, sub_string):
    count=0
    string_lenght=len(string)
    sub_lenght=len(sub_string)
    for i in range(string_lenght - sub_lenght + 1):
        if string[i:i + sub_lenght] == sub_string:
            count+= 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)