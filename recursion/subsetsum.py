from bit_wise.checkbit import checkbit_1
def f1(a,k):
    
    for n in range(1,1<<len(a)):
        ts=0
        l=[]
        for i in range(31):
            if checkbit_1(n,i):
                ts+=a[i]
                l.append(i)
        if ts==k:
            print(l)
            return True
    return False

def f2(a,k,l,idx=0,s=0,):
    if k==s:
        return True
    if idx>=len(a) or s>k:
        return False
    if f2(a,k,l,idx+1,s+a[idx]):
        l.append(idx)
        return True
    if f2(a,k,l,idx+1,s):
        return True
    return False



if __name__=='__main__':
    a=[int(x) for x in input().split()]
    k=int(input())
    print(f1(a,k)) # 2^N * 31 , 1
    l=[]
    print(f2(a,k,l)) # 2^N,1
    print(l)