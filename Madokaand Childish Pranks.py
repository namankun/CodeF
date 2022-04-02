 
for iii in range(int(input())):
    n,m=map(int,input().split())
    q=[]
    for i in range(n):

        q.append([int(i) for i in input()])
    if q[0][0]==1:
        print(-1)
        continue
    def isvalid(x,y):
        if 0<=x<=n and 0<=y<=m:
            return True
        return False
    q1=[]
    # for i in q:
    #     print(i)
    summ=0
    for i in range(n):
        for j in range(m):
            if q[i][j]==1:
                summ+=1
    print(summ)
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if q[i][j]==1:
                if isvalid(i-1,j):
                    print(i,j+1,i+1,j+1)
                else:
                    print(i+1,j,i+1,j+1)
    # print(len(q1))
    # for i in q1:
        # print(*i)
