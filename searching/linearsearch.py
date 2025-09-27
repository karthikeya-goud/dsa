

def linearsearch(a,k):

    for i in a:
        if i==k: return True
    
    return False

def linearsearch_recursive(a,k,idx):
    if idx==len(a):return False

    if a[idx]==k:return True

    return linearsearch_recursive(a,k,idx+1)


if __name__=="__main__":
    a=[1,2,3,4,5,6]
    print(linearsearch(a,4))#N,1
    print(linearsearch_recursive(a,4,0))#N,N