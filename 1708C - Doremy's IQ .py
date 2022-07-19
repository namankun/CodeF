for iii in range(int(input())):
        n,c=map(int,input().split())
        q=list(map(int,input().split()))
        q=q[::-1]
        cq=0
        s=''
        for i in range(n):
           if cq==c:
               if q[i]<=cq:
                   s="1"+s
               else:
                   s="0"+s
           else:
               if q[i]<=cq:
                   s='1'+s
               else:
                   s='1'+s
                   cq+=1
        print(s)
