for iiiii in range(int(input())):
    n,l,r=map(int,input().split())
    q=[]
    flag=True
    for i in range(1,n+1,1):
        x=l%i
        if x==0:
            q.append(l)
        else:
            if l+i-x<=r:
                q.append(l+i-x)
            else:
                flag=False
    if flag:
        print('YES')
        print(*q)
    else:
        print("NO")
