s = "cbbd"

long_string = ''
long_size = 0

def evaluate(s,size,front,end):
    while front-1>=0 and end+1<len(s):
        front,end = front-1,end+1
        if s[front]!=s[end]:
            break
        size+=2
    return size

for i in range(len(s)):
    s1 = evaluate(s,1,i,i)
    s2 = 0
    if i+1<len(s) and s[i]==s[i+1]:
        s2 = evaluate(s,2,i,i+1)
    
    if s1>long_size:
        long_size = s1
        long_string = s[(i-(s1-1)//2):(i+(s1-1)//2)+1]
    if s2>long_size:
        long_size = s2
        long_string = s[(i-(s2-2)//2):(i+(s2-2)//2)+2]
print(long_string)

    
