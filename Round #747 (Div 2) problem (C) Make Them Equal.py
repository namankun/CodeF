for iiii in range(int(input())):
        n,s=map(str,input().split())
        n=int(n)
        s1=input()
        if s1.count(s)==n:
            print(0)
            continue
        flag=True
        ind=-1
        for i in range((n//2),n,1):
            if s1[i]==s:
                flag=False
                ind=i
                break
        if not flag:
            print(1)
            print(ind+1)
        else:
            print(2)
            print(n-1,n)
