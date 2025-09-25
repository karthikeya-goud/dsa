
def f1(a):
    for i in a:
        c=0
        for j in a:
            if i==j:
                c+=1
        if c==1:
            return i
    return
 

def f2(a):
    A=min(a)
    B=max(a)
    c=[0]*(B-A+1)
    for i in a:
        c[i-A]+=1
    for i in range(B-A+1):
        if c[i]==1:
            return A+i
    print(c)
    return

def f3(a):
    hm={}
    for i in a:
        if i in hm:
            hm[i]+=1
        else:
            hm[i]=1
    
    for i in hm:
        if hm[i]==1:
            return i
    return

def f4(a):
    a.sort()

    curr=1
    while curr<len(a)-1:
        if a[curr]==a[curr+1] and a[curr]!=a[curr-1]:
            return a[curr-1]
        curr+=3
    return a[-1]

from checkbit import checkbit_1
def f5(a):
    ans=0
    for i in range(31):
        c=0
        for n in a:
            if checkbit_1(n,i):
                c+=1
        if c%3!=0:
            ans=ans+(1<<i) # ans= ans | (1<<i)
    
    return ans
if __name__=='__main__':

    a=[int(x) for x in input().split()]
    print(f1(a)) # N*N,1
    print(f2(a)) # N+N ,B-A+1
    print(f3(a)) # N+N,N
    print(f4(a)) # NlogN + N/2 , N
    print(f5(a)) # 31*N , 1