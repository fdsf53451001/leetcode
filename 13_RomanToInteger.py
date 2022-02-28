s = 'XIVIIVV'

normal_case = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

## slow way, match each two word, then split the string
# special_case = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
# num = 0
# index=0
# while index<len(s):
#     wd = s[index:index+2]
#     if wd in special_case:
#         num += special_case[wd]
#         index += 2
#         continue
#     num += normal_case[s[index:index+1]]
#     index += 1
# print(num) 

## fast way, compare two adjacent word, >= then add, < then sub
num = 0
prev = 0
s = s[::-1]
for ch in s:
    ch_num = normal_case[ch]
    if ch_num>=prev:
        num += ch_num
    else:
        num -= ch_num
    prev = ch_num
print(num)

