
def f1(c):
    a=[]

    for i in range(len(c)):
        if c[i]==0:continue

        for j in range(c[i]):
            a.append(i)
    return a


c=[0,1,0,3,0,5,0,0,2,0,1]
print(f1(c))