
def fact_1(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def fact_2(n):
    if n==0 or n==1:
        return 1
    return n*fact_2(n-1)

if __name__=='__main__':
    n=int(input())
    print(fact_1(n))#N,1
    print(fact_2(n))#N,N