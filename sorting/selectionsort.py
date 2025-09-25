
def selectionsort(a):

    for i in range(len(a)):
        m=i
        for j in range(i,len(a)):
            if a[j]<a[m]:
                m=j
        a[i],a[m]=a[m],a[i]


if __name__=="__main__":
    a=[3,5,8,3,1,10,5,5,3,8,5,5]
    selectionsort(a)
    print(a)