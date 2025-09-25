a='1010'
b='1011'
def getVal(s,idx):
    if idx<len(s):
        return int(s[-1*(idx+1)])
    return 0
print(getVal(a,1),getVal(b,1))
c=0
ans=''
for i in range(max(len(a),len(b))):
    res=getVal(a,i)+getVal(b,i)+c
    if res==3:
        c=1
        ans='1'+ans
    elif res==2:
        c=1
        ans='0'+ans
    elif res==1:
        c=0
        ans='1'+ans
    else:
        c=0
        ans='0'+ans
    print(f"{i} : {ans} , {c}")
if c==1:
    ans='1'+ans

print(ans)