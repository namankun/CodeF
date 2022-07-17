for iii in range(int(input())):
    n,c,q=map(int,input().split())
    s=input()
    q1=[]

    for i in range(c):
        q2=list(map(int,input().split()))
        q1.append(q2)

    pre=[n]
    for i in range(c):
        x=pre[i]+q1[i][1]-q1[i][0]+1
        pre.append(x)

    # print(*pre)

    def qwe(x):
        if x<=n:
            return s[x-1]
        dis=-1
        ind=-1
        for i in range(c+1):
            if x<=pre[i]:
                dis=x-pre[i-1]
                ind=i-1
                break
        dis1=q1[ind][0]+dis-1
        # print(dis,dis1)
        return qwe(dis1)

    for i in range(q):
        x=int(input())
        print(qwe(x))

