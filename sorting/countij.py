
def f1(a):
    c=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                c+=1
    return c

def f2(a):
    c=0
    def ms(a,l,h):
        nonlocal c
        if l<h:
            m=(l+h)//2
            ms(a,l,m)
            ms(a,m+1,h)

            p1=l
            p2=m+1
            k=[]
            while p1<=m and p2<=h:

                if a[p1]<=a[p2]:
                    k.append(a[p1])
                    p1+=1
                else:
                    k.append(a[p2])
                    c+=(m-p1+1)
                    p2+=1
            
            while p1<=m:
                k.append(a[p1])
                p1+=1
            
            while p2<=h:
                k.append(a[p2])
                p2+=1
            
            for i in range(l,h+1):
                a[i]=k[i-l]
    ms(a,0,len(a)-1)
    return c

a=[3,15,8,20,-4,12,8,-2,10,7]
print(f1(a))#N*N,1
print(f2(a))#NlogN + N*N, N