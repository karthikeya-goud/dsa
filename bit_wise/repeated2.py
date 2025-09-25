
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
    return

def f3(a):
    hs=set()

    for i in a:
        if i in hs:
            hs.remove(i)
        else:
            hs.add(i)
    if len(hs)==1:
        return hs.pop()
    return

def f4(a):
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
def f5(a):
    ans=a[0]
    for i in range(1,len(a)):
        ans=ans^a[i]
    return ans

def f6(a):
    a.sort()

    curr=0
    while curr<len(a):
        if a[curr]!=a[curr+1]:
            return a[curr]
        curr+=2
    return

if __name__=='__main__':

    a=[int(x) for x in input().split()]
    print(f1(a)) # N*N,1
    print(f2(a)) # N+N ,B-A+1
    print(f3(a)) # N+1, N
    print(f4(a)) #N+N,N
    print(f5(a)) # N,1
    print(f6(a)) # NlogN + N/2 , N

