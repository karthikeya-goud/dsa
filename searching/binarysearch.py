

def binarysearch(a,k):

    l=0
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


def binarysearch_recursive(a,k,l,h):

    if l<=h:
        m=(l+h)//2
        if a[m]==k:return True
        elif a[m]>k:
            return binarysearch_recursive(a,k,l,m-1)
        return binarysearch_recursive(a,k,m+1,h)
    return False
if __name__=="__main__":
    a=[1,2,3,4,5,6,7,8,9,10]
    print(binarysearch(a,10))#logN,1
    print(binarysearch_recursive(a,11,0,len(a)-1))#logN,logN