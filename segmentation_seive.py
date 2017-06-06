#segmented seive
from math import sqrt

n = int(raw_input())
p = [0]*100000
p[0] = 1
p[1] = 1
for i in range(2,100000):
    if p[i]==0:
        j = 2
        while (j*i)<100000:
            p[j*i] = 1
            j = j+1
        
for i in range(n):
    x,y = raw_input().split()
    x = int(x)
    y = int(y)
    a = [0]*(y-x+1)
    for j in range(2,(int(sqrt(y))+1)):
        if p[j]==0:
            print j
            for k in range(x,y+1):
                if k==1:
                    a[k] =1
                elif (k%j)==0 && k!=j:
                    a[k-x] = 1
                k = k+1

for i in range(n):
    if a[i]==0:
        print i
    
