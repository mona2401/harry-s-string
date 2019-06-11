t=int(input())
while t!=0:
    s=input()
    l=[]
    for i in s:
        if i in 'aeiou':
            l.append(i)
    s1=sorted(l)
    s2=sorted(l,reverse=True)
    if s1==l:
        print("Good")
    elif s2==l:
        print("Worst")
    else:
        print("Bad")
    t=t-1
