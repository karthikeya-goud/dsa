

def countsort(a,minvalue=None,maxvalue=None):
    if minvalue is None:
        minvalue=min(a)#N
    if maxvalue is None:
        maxvalue=max(a)#N

    c=[0]*(maxvalue-minvalue+1)#R

    for i in a: #N
        c[i-minvalue]+=1
    idx=0
    for i in range(len(c)):#R
        for j in range(c[i]):#total N only
            a[idx]=i+minvalue
            idx+=1
    return a
if __name__=="__main__":
    a=[3,5,8,3,1,10,5,5,3,8,5,5]
    print(countsort(a))#N+N+R+N,R
    a=[3,5,8,-3,-1,10,500,5,3,8,5,5,1000]
    print(countsort(a))