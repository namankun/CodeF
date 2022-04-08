import math
mod=10**9
mod+=7
for iii in range(int(input())):
        n,m=map(int,input().split())
        summ=0
        while m>0:
            x=int(math.log2(m))
            # print()
            summ=(summ+(n**x)%mod)%mod
            m=m-2**x
        print(summ)
