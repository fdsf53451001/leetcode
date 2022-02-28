data = [0,1,0,1,1,0,0,1,1]

max_len = 0
for i in range(len(data)):  # start point
    for j in range(i+1,len(data)):    # end point
        len0 = 0
        len1 = 0
        for index in range(i,j+1):
            if(data[index]==0):
                len0 += 1
            else:
                len1 += 1
        if(len0==len1 and len0*2>max_len):
            max_len = len0*2
print(max_len)
        
# TLE, NOT WORK