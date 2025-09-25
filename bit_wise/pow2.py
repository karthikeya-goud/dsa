
# 2^N
def pow2n_1(n):
    ans=1
    for i in range(1,n+1):
        ans=2*ans
    return ans

def pow2n_2(n):
    return 1<<n
if __name__=='__main__':
    n=int(input())
    print(pow2n_1(n)) # N,1
    print(pow2n_2(n))# 1,1