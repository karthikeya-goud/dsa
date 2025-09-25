

def merge(a,l,m,h):
    p1=l
    p2=m+1
    k=[]

    while p1<=m and p2<=h:
        if a[p1]<a[p2]:
            k.append(a[p1])
            p1+=1
        else:
            k.append(a[p2])
            p2+=1
    
    while p1<=m:
        k.append(a[p1])
        p1+=1
    
    while p2<=h:
        k.append(a[p2])
        p2+=1
    
    for i in range(l,h+1):
        a[i]=k[i-l]

def mergesort(a,l,h):
    if l<h:
        m=(l+h)//2
        mergesort(a,l,m)
        mergesort(a,m+1,h)
        merge(a,l,m,h)


if __name__=="__main__":
    a=[3,5,8,3,1,10,5,5,100,3,8,5,5]
    mergesort(a,0,len(a)-1)
    print(a)