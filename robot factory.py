import sys
# ba=['0000','0001','0010,','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
fast=sys.stdin.readline
n,m=map(int,fast().split())
q=[]
for i in range(n):
        q.append(list(map(int,fast().split())))

dp=[[False for i in range(m)] for j in range(n)]
ans=[0 for i in range((n*m)+1)]

def bfs(i,j):
        if i<0 or j<0 or i>=n or j>=m or dp[i][j]:
            return 0
        dp[i][j]=True
        summ=1
        c=q[i][j]
        adj=[(i-1,j),(i,j+1),(i+1,j),(i,j-1)]
        adj.reverse()
        for x,y in adj:
            if c%2==0:
                summ=summ+bfs(x,y)
            c=c//2



        # if ba[q[i][j]][0]=='0':
        #     summ=summ+bfs(i-1,j)
        # if ba[q[i][j]][1]=='0':
        #     summ=summ+bfs(i,j+1)
        # if ba[q[i][j]][2]=='0':
        #     summ=summ+bfs(i+1,j)
        # if ba[q[i][j]][3]=='0':
        #     summ=summ+bfs(i,j-1)
        return summ



for i in range(n):
        for j in range(m):
            if not dp[i][j]:
                summ=bfs(i,j)
                ans[summ]+=1
for i in range(n*m,-1,-1):
        if ans[i]>=1:
            for j in range(ans[i]):
                print(i,end=' ')
# print()
# print(ans)

