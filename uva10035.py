while(True):
    data = input().split(' ')

    max_len = max(len(data[0]),len(data[1]))
    data = ['0'*(max_len-len(data[i]))+data[i] for i in range(2)]
    
    if(int(data[0])==0 and int(data[1])==0):
        break

    carry_out = 0
    last_carry = 0
    for i in range(1,max_len+1):
        if int(data[0][-i])+int(data[1][-i])+last_carry>9:
            carry_out += 1
            last_carry = 1
        else:
            last_carry = 0

    if carry_out==0:
        print('No carry operation.')
    elif carry_out==1:
        print('1 carry operation.')
    else:
        print(carry_out,'carry operations.')