def f1(n,s,o,c):
    if len(s)==n:
        print(s)
        return
    if o<n//2:
        f1(n,s+'(',o+1,c)
    if c<o:
        f1(n,s+')',o,c+1)
    


n=int(input())
f1(n,'',0,0)