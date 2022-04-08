for iii in range(int(input())):
        n=int(input())
        q=[]
        for i in range(n):
            q.append(list(map(int,input().split())))
        flag=True
        for i in range(5):
            if not flag:
                break
            for j in range(i+1,5):
                a=0
                b=0
                both=0
                for k in range(n):
                    if q[k][i]==1 and q[k][j]==1:
                        both+=1
                    elif q[k][i]==1:
                        a+=1
                    elif q[k][j]==1:
                        b+=1
                if a+b+both==n and a<=(n//2) and b<=(n//2):
                    flag=False
        if flag:
            print('NO')
        else:
            print("YES")
