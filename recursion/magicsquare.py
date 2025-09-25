perm=[]

def row(u):
    return (u[0]+u[1]+u[2])==(u[3]+u[4]+u[5])==(u[6]+u[7]+u[8])
def col(u):
    return (u[0]+u[3]+u[6])==(u[1]+u[4]+u[7])==(u[2]+u[5]+u[8])
def diag(u):
    return (u[0]+u[4]+u[8])==(u[2]+u[4]+u[6])
def check(u):
    return row(u) and col(u) and diag(u) #1
itc=0
it=0
def f(u=[]):
    global itc,it
    if len(u)==9:
        if check(u):
            perm.append(u)
            print(u)
        return
    for i in range(1,10):#9
        if not i in u:#
            f(u+[i])#(9-1)
            itc+=1
        it+=1

f()
print(itc,it)
a=[1,2,3,4,5,6,7,8,9]
cost=1<<31
ans=None
for u in perm:
    c=0
    for i in range(9):
        c+=abs(a[i]-u[i])
    if c<cost:
        ans=[c,u]
print(ans)


# from itertools import permutations

# l=permutations(range(1,10))
# for i in l:print(i)
# # from this pick the valid ones