from checkbit import checkbit_1

def count_setbits_1(n):
    ans=0
    for bit in range(31):
        if checkbit_1(n,bit):
            ans+=1
    return ans

def count_setbits_2(n):
    ans=0
    while n:
        if n&1==1:
            ans+=1
        n=n>>1
    return ans

def count_setbits_3(n):
    ans=0
    while n:
        n=n&(n-1)
        ans+=1
    return ans

if __name__=='__main__':
    n=int(input())
    print(count_setbits_1(n))# 32*1,1
    print(count_setbits_2(n))# log(n) + 1,1
    print(count_setbits_3(n))# number of set bits,1