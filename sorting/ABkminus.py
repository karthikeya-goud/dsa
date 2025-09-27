

def f1(a,k):

    for i in range(len(a)):
        for j in range(len(a)):
            if i==j:continue
            if a[i]-a[j]==k:
                # print(a[i],a[j])
                return True
    
    return False


def f2(a,k):
    a.sort()
    p1=0
    p2=1

    while p2<len(a) and p1<len(a):
        r=a[p2]-a[p1]
        if r==k:return True
        elif r<k:
            p2+=1
        else:
            p1+=1
    return False

def binarysearch(a,k,l=0): 
    h=len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m]==k:
            return True
        elif a[m]>k:
            h=m-1
        else:
            l=m+1
    return False

def f3(a,k):
    a.sort()
    for i in range(len(a)):
        b=k+a[i]
        if binarysearch(a,b,i+1):return True
    return False
a=a=[2,5,-5,2,99,12,34,56,-87,34,100,9,6]
print(f1(a,k=47))#N*N,1
print(f2(a.copy(),k=47))#NlogN + N, N
print(f3(a.copy(),k=47))#NlogN+ NlogN , N
