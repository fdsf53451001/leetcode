country_table = {}

if __name__ == '__main__':
    count = int(input())
    for i in range(count):
        data = input().split(' ')
        if data[0] in country_table:
            country_table[data[0]]+=1   # exist, add one
        else:
            country_table[data[0]]=1    # not exist
    
    sort_keys = list(country_table.keys())
    sort_keys.sort()
    for key in sort_keys:
        print(key,country_table[key])