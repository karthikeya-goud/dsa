def toh(n,src,des,temp):
    if n==0:return

    toh(n-1,src,temp,des)
    print(f"{n} : {src} -> {des}")
    toh(n-1,temp,des,src)


n=int(input())
print((1<<n)-1)
toh(n,'A',"B","C")