mod=int(1e9+7)
from checkbit import checkbit_1
def apown_1(a,n):
    ans=1
    a=a%mod
    for i in range(n):
        ans=(ans*a)%mod
    
    return ans

def apown_2(a,n):
    x=a%mod
    ans=1

    # for i in range(31): # or log2(N)+1
    #     if checkbit_1(n,i):
    #         ans=(ans*x)%mod
    #     x=(x*x)%mod
    while n:
        if n&1==1:
            ans=(ans*x)%mod
        x=(x*x)%mod
        n=n>>1
    return ans

def apown_3(a,n):

    if n==0:
        return 1
    return (a*apown_3(a,n-1))%mod

def apown_4(a,n):

    if n==0:
        return 1
    if n&1==0:
        return (apown_4(a,n//2)*apown_4(a,n//2))%mod
    return (a*apown_4(a,n//2)*apown_4(a,n//2))%mod

def apown_5(a,n):

    if n==0:
        return 1
    x=apown_4(a,n//2)
    if n&1==0:
        return (x*x)%mod
    return (a*x*x)%mod

if __name__=='__main__':
    a=int(input())
    n=int(input())
    print(apown_2(a,n)) # at max 32 iterations or MSB set bit length=> logN , 1
    # print(apown_1(a,n)) # N, 1
    # print(apown_3(a,n)) # N+1, N
    # print(apown_4(a,n))#N,N
    print(apown_5(a,n))#logN+1, N//2