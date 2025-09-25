


def f(s1,s2,i,j,s):
    if i==len(s1):
        print(s+s2[j:])
        return
    if j==len(s2):
        print(s+s1[i:])
        return
    if s1[i]<s2[j]:
        f(s1,s2,i+1,j,s+s1[i])
        f(s1,s2,i,j+1,s+s2[j])
    else:
        f(s1,s2,i,j+1,s+s2[j])
        f(s1,s2,i+1,j,s+s1[i])

f("AB","PQRS",0,0,'')# (m+n)!/(m!xn!),M+N