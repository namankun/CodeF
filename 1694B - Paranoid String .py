for iii in range(int(input())):
    n=int(input())
    s=input()
    x=s[0]
    summ=n
    for i in range(1,n,1):
        if s[i]!=x:
            summ+=i
            x=s[i]
    print(summ)
