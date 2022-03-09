from statistics import median_low

count = int(input())
for i in range(count):
    data = input().split(' ')
    data = [int(d) for d in data]
    data = data[1:]
    data.sort()
    
    mid = median_low(data)

    dis = 0
    for address in data:
        dis += abs(mid-address)
    print(dis)