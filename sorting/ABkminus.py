

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


a=a=[2,5,-5,2,99,12,34,56,-87,34,100,9,6]
print(f1(a,k=47))
print(f2(a.copy(),k=47))
