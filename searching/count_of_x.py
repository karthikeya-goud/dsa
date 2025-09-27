a=[3 ,10 ,8 ,15 ,10 ,10 ,-2 ,15 ,3 ,-5 ,3 ,10 ,25 ,10 ,-5]
q=[10,20,15,8,-5,10,12,3]


def f1(a,q):

    for x in q:

        c=0
        for i in a:
            if i==x:c+=1
        print(f'{x} : {c}')


def f2(a,q):
    minv=min(a)
    maxv=max(a)
    c=[0]*(maxv-minv+1)
    for i in a:
        c[i-minv]+=1
    for x in q:
        if x>maxv or x<minv:
            print(f'{x} : 0')
        else:
            print(f'{x} : {c[x-minv]}')


def f3(a,q):
    
    def binarysearch1(a,x):
        p1=0
        l=0
        h=len(a)-1
        while l<=h:
            m=(l+h)//2
            if a[m]>x:
                h=m-1
            elif a[m]<x:
                l=m+1
            else:
                p1=m
                h=m-1
        return p1
    
    def binarysearch2(a,x):
        p2=-1
        l=0
        h=len(a)-1
        while l<=h:
            m=(l+h)//2
            if a[m]>x:
                h=m-1
            elif a[m]<x:
                l=m+1
            else:
                p2=m
                l=m+1
        return p2
    
    a.sort()

    for x in q:

        i=binarysearch1(a,x)
        j=binarysearch2(a,x)
        print(f'{x} : {j-i+1}')

f1(a,q)#Q*N ,1
f2(a,q)#N+Q*1,R ,same for hashmap too 
f3(a,q)#NlogN + Q*(logN+logN) , N
