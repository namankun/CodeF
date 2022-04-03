
for iii in range(int(input())):
    n=int(input())
    q=list(map(int,input().split()))
    q.sort()
    x=q[0]
    summ=q[0]
    for i in range(1,n):

        summ=max(q[i]-q[i-1],summ)
    # print(q)
    print(summ)
