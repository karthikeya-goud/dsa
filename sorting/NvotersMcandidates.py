

def f1(a,m):
    ans=0
    max=-1
    for i in range(1,m+1):
        c=0
        for ele in a:
            if ele==i:c+=1
        if c>max:
            max=c
            ans=i
    return ans

def f2(a,m):
    c=[0]*(m+1)

    for i in a:
        c[i]+=1
    
    ans=0
    for i in range(1,m+1):
        if c[i]>c[ans]:
            ans=i
    return ans

def f3(a,m):
    hm={}

    for i in a:
        if i in hm:
            hm[i]+=1
        else:
            hm[i]=1
    
    ans=list(hm.keys())[0]
    for i in range(1,m+1):
        if i in hm:
            if hm[i]>hm[ans]:
                ans=i
    return ans


a=[3,5,8,3,1,10,5,5,3,8,5,5]
m=10
print(f1(a,m)) #M*N,1
print(f2(a,m)) #N+M,M
print(f3(a,m)) #N+M,M
