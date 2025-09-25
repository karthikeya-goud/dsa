

def partition(a,l,h):

    pivot=a[h]
    i=l-1

    for j in range(l,h):
        if a[j]<=pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
    
    a[i+1],a[h]=a[h],a[i+1]
    return i+1


def quicksort(a,l,h):

    if l<h:

        pi=partition(a,l,h)
        quicksort(a,l,pi-1)
        quicksort(a,pi+1,h)


if __name__=="__main__":
    a=[3,5,8,3,1,10,5,5,100,3,8,5,5]
    quicksort(a,0,len(a)-1)
    print(a)
