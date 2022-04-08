 
for iii in range(int(input())):
        n=int(input())
        s=input()
        s=[i for i in s]
        q=[]
        while True:
            q1=[]
            flag=True
            for i in range(n):
                if s[i]=='1':
                    for j in range(n-1,i,-1):
                        if s[j]=='0':
                            flag=False
                            s[i],s[j]=s[j],s[i]
                            q1.append(i+1)
                            q1.append(j+1)

                            break
            if len(q1)>0:
                q.append(q1)
            if flag:
                break
        print(len(q))
        for x in q:
            print(len(x),end=' ')
            x.sort()
            print(*x)
