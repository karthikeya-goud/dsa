

def f1(a,x):
    ans=-(1<<31)
    for i in a:
        if i<=x:
            ans=max(ans,i)
    return ans

def f2(a,x):
    ans=-(1<<31)
    l=0
    h=len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m]>x:
            h=m-1
        else:
            ans=a[m]
            l=m+1
    return ans


def queries(fun):
    for i in q:
        print(fun(a,i))
a=[12,21,15,-3,10,-8,5,29,18]
q=[14,0,46,-5,10,-15]

queries(f1) # q*n

a.sort()
queries(f2)# NlogN + Q*LogN , N

