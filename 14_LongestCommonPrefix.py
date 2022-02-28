strs = ["flower","flow","flight"]
if len(strs)==1:
    print(strs[0]) 

compare_string = strs[0]
max_len = -1

try:
    flag = True
    while(flag):
        max_len+=1
        for i in range(1,len(strs)):
            if strs[i][max_len]!=compare_string[max_len]:
                flag = False
                break
        
except IndexError:
    pass
        
print(compare_string[:max_len]) 


# solution 2
s = ""
for a in zip(*strs):
    if len(set(a))==1:
        s+=a[0]
    else:
        break
print(s)