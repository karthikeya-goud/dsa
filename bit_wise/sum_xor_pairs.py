from checkbit import checkbit_1
def f(a):
    ans=1
    for i in range(31):
        c=0
        for e in a:
            if checkbit_1(e,i):
                c+=1
        print(f'{(1<<i)} X {c}')
        ans=ans+ (c*(len(a)-c)*(1<<i))
    return 2*ans

if __name__=="__main__":
    a=[int(x) for x in input().split()]
    print(f(a))


