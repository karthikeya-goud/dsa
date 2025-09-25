
def gcd_1(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def gcd_2(a,b):
    while b:
        a,b=b,a%b
    return a

def gcd(*ls):
    ls=list(ls)
    if len(ls)==0:
        return 0
    if len(ls)==1:
        return ls[0]
    ls.sort()
    
    def f(a,b):
        if b==0:
            return a
        return f(b,a%b)
    r=ls[0]
    for i in range(1,len(ls)):
        r=f(max(r,ls[i]),min(r,ls[i]))
    return r


if __name__=='__main__':
    a=list(map(int,input().split()))
    print(gcd(*a))
    # print(gcd_1(*a))
    # print(gcd_2(*a))