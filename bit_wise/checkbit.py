
def checkbit_1(n,b):

    return bool((n>>b)&1)


def checkbit_2(n,b):
    return bool((1<<b)&n)

if __name__=='__main__':
    n=int(input())
    b=int(input())
    print(str(bin(n))[2:])
    print(checkbit_1(n,b))
    print(checkbit_2(n,b))