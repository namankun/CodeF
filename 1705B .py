for iii in range(int(input())):
    n=int(input())
    q = list(map(int, input().split()))
    ind=n-1
    for i in range(n-1):
        if q[i]>0:
            ind=i
            break
    summ=0
    for i in range(ind,n-1,1):
        if q[i]>0:
            summ+=q[i]
        else:
            summ+=1

    print(summ)
