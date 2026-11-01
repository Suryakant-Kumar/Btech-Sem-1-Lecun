x1,x2,x3,x4 = map(int,input().split())
lis = [x1,x2,x3,x4]
lis.sort()
for i in range(len(lis)-1):
    print(lis[3] - lis[i],end=" ")