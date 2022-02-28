x=101
num_str = str(x)[::-1]
num = 0
try:
    num = int(num_str)
except ValueError:
    pass

if x!=num or num==-1:
    print('F')
else:
    print('T')
