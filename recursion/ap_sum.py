
def f1(a,n,d):
    s=0
    for i in range(1,n+1):
        s+= a+(i-1)*d
    return s

def f2(a,n,d):
    
    if n==0:
        return 0
    # return a+(n-1)*d + f2(a,n-1,d)
    return a + f2(a+d,n-1,d)

def f3(a,n,d):
    return (n*(2*a + (n-1)*d))//2

if __name__=='__main__':
    a,n,d=list(map(int,input().split()))
    print(f1(a,n,d))#N,1
    print(f2(a,n,d))#N,N
    print(f3(a,n,d))#1,1