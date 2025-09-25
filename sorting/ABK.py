

def f1(a,k):

    for i in range(len(a)):
        for j in range(len(a)):
            if i==j:continue
            if a[i]+a[j]==k:return True
    
    return False


def f2(a,k):
    a.sort()
    p1=0
    p2=len(a)-1

    while p1<p2:
        r=a[p1]+a[p2]
        if r==k:return True

        elif r>k:
            p2-=1
        else:
            p1+=1
    return False


a=[2,5,-5,2,99,12,34,56,-87,34,100,9,6]
print(f1(a,k=46))#N*N
print(f2(a.copy(),k=46))#NlogN+ N,1
