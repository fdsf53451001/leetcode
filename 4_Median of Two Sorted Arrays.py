nums1 = [1,6]
nums2 = [4,5,7]
sum_arr = []

i,j = 0,0
m,n = len(nums1),len(nums2)
while(i<m and j<n):
    if(nums1[i]>nums2[j]):
        sum_arr.append(nums2[j])
        j+=1
    else:
        sum_arr.append(nums1[i])
        i+=1

for x in range(i,m):
    sum_arr.append(nums1[x])

for y in range(j,n):
    sum_arr.append(nums2[y])


len_sum = len(sum_arr)
if(len_sum%2==0):
    print((sum_arr[len_sum/2-1]+sum_arr[len_sum/2])/2.0)
else:
    print(sum_arr[int(len_sum/2)])