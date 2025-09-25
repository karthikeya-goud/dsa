# Enter your code here. Read input from STDIN. Print output to STDOUT
mod=int(1e9+7)
def f(a,n):
    hm={}
    for i in a:
        if i in hm:
            hm[i]+=1
        else:
            hm[i]=1
    l=list(hm.keys())
    ans=1
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            c=hm[l[i]]*hm[l[j]]
            xv=l[i]^l[j]
            ans=(ans*pow(xv,c,mod))%mod
            
    return ans

a=[int(x) for x in input().split()]
print(f(a,len(a)))



# 1 2 3 7



# (1^1) (1^2) (1^3) (1^7)
# (2^1) (2^2) (2^3) (2^7)
# (3^1) (3^2) (3^3) (3^7)
# (7^1) (7^2) (7^3) (7^7)

# 3 2 6
#   1 5
#     4

# 1 - 001
# 2 - 010
# 3 - 011
# 4 - 100
# 5 - 101
# 6 - 110
# 7 - 111

# 3*1*1 3*1*2 4*3*1