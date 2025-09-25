def count_divisors_1(n):

    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c

def count_divisors_2(n):
    # from math import sqrt
    
    c=0
    # for i in range(1,int(sqrt(n))+1):
    #     if n/i==i:
    #         c+=1
    #     elif n%i==0:
    #         c+=2
    i=1
    while i*i<=n:
        if n/i==i:
            c+=1
        elif n%i==0:
            c+=2
        i+=1
    return c

if __name__=='__main__':
    n=int(input())
    print(count_divisors_1(n))#N,1
    print(count_divisors_2(n))#sqrt(N),1
