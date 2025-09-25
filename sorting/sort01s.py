


def f1(a):

    c1=0
    for i in a:
        if i==1:c1+=1
    idx=0
    for i in range(len(a)-c1):
        a[idx]=0
        idx+=1
    for i in range(c1):
        a[idx]=1
        idx+=1

def f2(a):
    p1=0
    p2=len(a)-1

    while p1<=p2:

        while a[p1]!=1:
            p1+=1
        
        while a[p2]!=0:
            p2-=1
        
        a[p1],a[p2]=a[p2],a[p1]

a=[0,1,1,0,0,0,1]
f1(a)
print(a)
a=[0,1,1,0,0,0,1]
f2(a)
print(a)