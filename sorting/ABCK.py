

def f1(a,k):

    for i in range(len(a)):
        for j in range(len(a)):
            for r in range(len(a)):
                if i==j==r:continue
                if a[i]+a[j]+a[r]==k:return True
    
    return False


def f2(a,k):
    a.sort()
    for i in range(len(a)):
        p1=i+1
        p2=len(a)-1
        nk=k-a[i]
        while p1<p2:
            r=a[p1]+a[p2]
            if r==nk:return True

            elif r>nk:
                p2-=1
            else:
                p1+=1
    return False


a=[2,5,-5,2,99,12,34,56,-87,34,100,9,6]
print(f1(a,k=106))#N*N*N, 1
print(f2(a.copy(),k=106))#NlogN + N*N, N
