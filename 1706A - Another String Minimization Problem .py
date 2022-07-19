    for iii in range(int(input())):
        # n=int(input())
        n,m=map(int,input().split())
        q=list(map(int,input().split()))
        q1=["B" for i in range(m)]
        for i in range(n):
            x=q[i]-1
            y=m-q[i]
            if x>y:
                x,y=y,x
            if q1[x]=="B":
                q1[x]="A"
            else:
                q1[y]="A"
        for i in range(m):
            print(q1[i],end='')
        print()
