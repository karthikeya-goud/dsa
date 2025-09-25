
def f1(n):
    a=1
    b=1
    while n-2:
        c=a+b
        a,b=b,c
        n-=1
    return c

def f2(n):
    if n==1 or n==2:
        return 1
    return f2(n-1)+f2(n-2)
if __name__=="__main__":
    n=int(input())
    print(f1(n))#N,1
    print(f2(n))#2^N,N