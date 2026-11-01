n = int(input())
for i in range(n):
    l,r = map(int, input().split())
    if (l+r)%3==0 and max(l,r)<= 2*min(l,r):
        print("YES")  
    else:
        print("NO")
    

