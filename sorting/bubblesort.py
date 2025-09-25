
def bubblesort(a):

    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]


if __name__=="__main__":
    a=[3,5,8,3,1,10,5,5,3,8,5,5]
    bubblesort(a)
    print(a)