def linear_search(ls,key):

    for i in ls:
        if key==i:
            return True
    return False


if __name__=='__main__':
    a=[int(x) for x in input().split()]
    key=int(input())
    print(linear_search(a,key))