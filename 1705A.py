for iii in range(int(input())):
    n,x=map(int,input().split())
    q = list(map(int, input().split()))
    q.sort()
    flag=True
    for i in range(n):
        if q[i+n]-q[i]<x:
            flag=False
    if flag:
        print('YES')
    else:
        print('NO')
