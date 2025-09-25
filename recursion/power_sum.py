
def f(n,k,idx):
    if n==0:
        return 1
    if n<0 or idx**k>n:
        return 0
    return f(n-(idx**k),k,idx+1) + f(n,k,idx+1)



n,k=list(map(int,input().split()))
print(f(n,k,1))
