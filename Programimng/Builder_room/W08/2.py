n = int(input())
maxi = float('-inf')
for i in range(n):
    m = int(input())
    if maxi <= m:
        maxi = m
    else:
        pass
    # maxi = max(maxi,m)
print(maxi)