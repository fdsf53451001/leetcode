
def algorithm(n):
    sum1 = 0
    str1 = str(n)[::2]
    for ch in str1:
        sum1 += int(ch)
    sum2=0
    str2 = str(n)[1::2]
    for ch in str2:
        sum2 += int(ch)
    return True if abs(sum2-sum1)%11==0 else False

if __name__ == '__main__':
    while True:
        num = int(input())
        if num==0:
            break

        if algorithm(num):
            print(num,'is a multiple of 11.')
        else:
            print(num,'is not a multiple of 11.')
