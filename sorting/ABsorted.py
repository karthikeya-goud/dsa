from selectionsort import selectionsort
def f1(a,b):
    t=[]
    for i in range(len(a)):t.append(a[i])
    for i in range(len(b)):t.append(b[i])
    selectionsort(t)
    print(*t)

def f2(a,b):
    from countsort import countsort
    t=[]
    for i in range(len(a)):t.append(a[i])
    for i in range(len(b)):t.append(b[i])
    countsort(t,min(a[0],b[0]),max(a[-1],b[-1]))
    print(*t)

def f3(a,b):

    p1=0
    p2=0
    while p1<len(a) and p2<len(b):
        if a[p1]<b[p2]:
            print(a[p1],end=' ')
            p1+=1
        else:
            print(b[p2],end=' ')
            p2+=1
    
    while p1<len(a):
        print(a[p1],end=' ')
        p1+=1
    while p2<len(b):
        print(a[p2],end=' ')
        p2+=1

def f4(a,b):
    temp=[0]*(len(a)+len(b))
    for i in range(len(a)):
        temp[i]=a[i]
    for i in range(len(b)):
        x=b[i]
        j=len(a)+i-1
        while j>=0 and temp[j]>x:
            temp[j+1]=temp[j]
            j-=1
        temp[j+1]=x
    print(*temp)
a=[3,5,12,18,35]
b=[-1,2,5,7,10,12,15,17]
f1(a,b)#N+M+(N+M)**2,N+M
f2(a,b)#N+M+R+N+M,R+N+M
f4(a,b)#N+M*N,N+M
f3(a,b)#N+M,1
