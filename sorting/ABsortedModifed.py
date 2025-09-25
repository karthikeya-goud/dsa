from selectionsort import selectionsort
def f1(a,b):
    x=len(a)-len(b)
    for i in range(x,len(a)):
        a[i]=b[i-x]
    
    selectionsort(a)
    print(a)

def f2(a,b):

    for i in range(len(b)):
        x=b[i]
        j=len(a)-len(b)-1+i
        while j>=0 and a[j]>x:
            a[j+1]=a[j]
            j-=1
        a[j+1]=x
    print(a)

def f3(a,b):
    temp=[]
    p1=0
    p2=0
    x=len(a)-len(b)
    while p1<x and p2<len(b):
        if a[p1]<b[p2]:
            temp.append(a[p1])
            p1+=1
        else:
            temp.append(b[p2])
            p2+=1
    
    while p1<x:
        temp.append(a[p1])
        p1+=1
    while p2<len(b):
        temp.append(b[p2])
        p2+=1
    for i in range(len(temp)):
        a[i]=temp[i]
    print(a)

def f4(a,b):

    p1=len(a)-len(b)-1
    p2=len(b)-1
    idx=len(a)-1

    while p1>=0 and p2>=0:
        if a[p1]>b[p2]:
            a[idx]=a[p1]
            p1-=1
        else:
            a[idx]=b[p2]
            p2-=1
        idx-=1
    
    while p1>=0:
        a[idx]=a[p1]
        idx-=1
        p1-=1
    while p2>=0:
        a[idx]=b[p2]
        idx-=1
        p2-=1
    print(a)
    

a=[3,5,12,18,35,0,0,0,0,0,0,0,0]
b=[-1,2,5,7,10,12,15,17]
f1(a.copy(),b)#M+N**2,1
f2(a.copy(),b)#M*(N-M),1
f3(a.copy(),b)#(N-M)+M + N , N
f4(a.copy(),b)#(N-M)+M,1