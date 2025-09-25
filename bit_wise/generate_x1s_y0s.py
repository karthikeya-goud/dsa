from pow2 import pow2n_2

def x1_y0_1(x,y):
    ans=0
    for i in range(y,x+y):
        ans=ans+(1<<i)
    return ans

def x1_y0_2(x,y):
    # 1<<(x+y) - 1<<(y)
    return pow2n_2(x+y)-pow2n_2(y)

def x1_y0_3(x,y):
    #(1<<(x+y)-1)-(1<<y -1)
    return (pow2n_2(x+y)-1)-(pow2n_2(y)-1)
def x1_y0_4(x,y):
    # (1<<(x+y)-1)^(1<<y-1)
    return (pow2n_2(x+y)-1)^(pow2n_2(y)-1)
if __name__=='__main__':
    x=int(input())
    y=int(input())
    print(x1_y0_1(x,y))
    print(x1_y0_2(x,y))
    print(x1_y0_3(x,y))
    print(x1_y0_4(x,y))