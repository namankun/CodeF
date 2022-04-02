 
    def find(q,x):
        n=len(q)
        high=n-1
        low=0
        while low<=high:
            mid=(low+high)//2
            if q[mid]==x:
                if mid==n-1:
                    return -1
                return q[mid+1]
            if q[mid]>x:
                high=mid-1
            else:
                low=mid+1



    for iii in range(int(input())):
        s=input()
        q={}
        n=len(s)
        for i in range(97,123,1):
            q[i]=[]
        for i in range(n):
            q[ord(s[i])].append(i)
        summ=0
        lim=-1
        for i in range(n-1):
            if i<=lim:
                continue
            if s[i]==s[i+1]:
                summ+=1
                # print(i)
                lim=i+1
                continue
            j=i
            lim=n-1
            pair=False
            while j<=lim:
                x=find(q[ord(s[j])],j)
                if x==-1:
                    pass
                else:
                    lim=min(lim,x)
                    if not pair:
                        summ+=1
                        # print(j)
                        pair=True
                j+=1
        # print(n-2*summ,summ)
        print(n-2*summ)
