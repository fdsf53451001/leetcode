s1 = 'ab'
s2 = 'ajfovacakgf'

exist = False
start_point = 0
size = len(s1)
for index in range(len(s2)):
    if exist:
        if index-start_point>=size:
            break
        elif s2[index]!=s1[index-start_point]:
            exist = False
    else:
        if s2[index]==s1[0]:
            exist = True
            start_point = index
print(exist)