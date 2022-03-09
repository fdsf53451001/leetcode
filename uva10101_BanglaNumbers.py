
def algorithm(n):
    result = [0,0,0,0,0]
    result[0] = n//10000000
    n = n - result[0]*10000000
    result[1] = n//100000
    n = n - result[1]*100000
    result[2] = n//1000
    n = n- result[2]*1000
    result[3] = n//100
    n = n- result[3]*100 
    result[4] = n

    ans = ''
    if result[0]>=100:
        ans += (' '+algorithm(result[0])+' kuti')
    else:
        ans += (' '+str(result[0])+' kuti') if result[0]!=0 else ''
    ans += (' '+str(result[1])+' lakh') if result[1]!=0 else ''
    ans += (' '+str(result[2])+' hajar') if result[2]!=0 else ''
    ans += (' '+str(result[3])+' shata') if result[3]!=0 else ''
    ans += (' '+str(result[4])) if result[4]!=0 else ''
    
    return ans[1:]



if __name__ == '__main__':
    i = 0
    while(True):
        try:
            i += 1
            num = int(input())
            if num==0:
                print(str(i)+'. 0')
                continue
            print(str(i)+'.',algorithm(num))
        except EOFError:
            break
