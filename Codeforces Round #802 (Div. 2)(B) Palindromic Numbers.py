     for iii in range(int(input())):
        n=int(input())
        q=input()
        q=[int(i) for i in q]
        flag=True
        # for i in q:
        if q[0]==9:
                flag=False
                # break
        if flag:
            for i in q:
                print(9-i,end='')
            print()
        else:
            flag=True
            s1=''
            q1=[1 for i in range(n+1)]
            for i in range(n,0,-1):
                summ=q1[i-1]*10+q1[i]
                q1[i-1]-=1
                x=summ-q[i-1]
                if x>9:
                    q1[i-1]+=1
                x=x%10
                s1=str(x)+s1

            print(s1)
