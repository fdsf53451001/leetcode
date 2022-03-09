count_table = {}

def algorithm(n):
    answer_list = []
    while n!=1:
        if n in count_table:
            answer_list.extend([0 for i in range(count_table[n])])
            break
        answer_list.append(n)
        n = n//2 if n%2==0 else 3*n+1
    # notice! 1 not in answer list

    for i in range(1,len(answer_list)+1):
        if answer_list[-i]!= 0:
            count_table[answer_list[-i]] = i
    return len(answer_list)+1

if __name__ == '__main__':
    while(True):
        try:
            nums = input().split(' ')
        except EOFError:
            break
        start,end = int(nums[0]),int(nums[1])
        max_length = 0
        for i in range(min(start,end),max(start,end)+1):
            length = algorithm(i)
            max_length = length if length>max_length else max_length
        print(start,end,max_length)

