
def insertionsort(a):

    for i in range(1,len(a)):
        j=i-1
        val=a[i]
        while j>=0 and a[j]>val:
            a[j+1]=a[j]
            j-=1
        a[j+1]=val


if __name__=="__main__":
    a=[3,5,8,3,1,10,5,5,3,8,5,5]
    insertionsort(a)
    print(a)