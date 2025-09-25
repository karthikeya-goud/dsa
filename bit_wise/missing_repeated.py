def f1(a):
    ms=0
    for i in range(1,len(a)+1):
        for j in a:
            if i==j:
                break
        else:
            ms=i
    rs=0
    for i in a:
        c=0
        for j in a:
            if i==j:
                c+=1
        if c==2:
            rs=i
    
    return ms,rs

def f2(a):
    l=a.copy()
    l.sort()
    ms=0
    rs=0
    for i in range(len(l)):
        if i+1!=l[i]:
            ms=i+1
            break
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            rs=l[i]
            break
    return ms,rs
def f3(a):
    c=[0]*(len(a)+1)
    ms=0
    rs=0
    for i in a:
        c[i]+=1
    
    for i in range(1,len(a)+1):
        if c[i]==0:
            ms=i
        elif c[i]==2:
            rs=i
    return ms,rs

def f4(a):
    ms=0
    rs=0
    s=set()
    for i in a:
        if i not in s:
            s.add(i)
        else:
            rs=i
    for i in range(1,len(a)+1):
        if i not in s:
            ms=i
            break
    return ms,rs

def f5(a):
    ms=0
    rs=0
    hm={}
    for i in a:
        if i not in hm:
            hm[i]=1
        else:
            hm[i]+=1
    for i in range(1,len(a)+1):
        if i not in hm:
            ms=i
        elif hm[i]==2:
            rs=i
    return ms,rs

from checkbit import checkbit_1
from linearsearch import linear_search
def f6(a):
    n=0
    for i in range(1,len(a)+1):
        n=a[i-1]^i
    A=0
    B=0   
    for i in range(31):

        if checkbit_1(n,i):
            for idx in range(1,len(a)+1):

                if checkbit_1(a[idx-1],i):
                    A=A^a[idx-1]
                else:
                    B=B^a[idx-1]
                
                if checkbit_1(idx,i):
                    A=A^idx
                else:
                    B=B^idx
            break
    if linear_search(a,A):
        return B,A
    return A,B

if __name__=='__main__':
    a=[int(x) for x in input().split()]
    print(f1(a)) # N*N + N*N , 1
    print(f2(a)) # NlogN + N+ N,1
    print(f3(a)) # N + N , N
    print(f4(a)) # N=N, N
    print(f5(a)) # N + N, N
    print(f6(a)) # N + (31+N) + N ,1