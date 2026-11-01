n = int(input())
n_copy = n
s = 0
l = len(str(n))
while n_copy>0:
    m = n_copy%10
    n_copy=n_copy//10
    s = s + m**l
if s == n:
    print(s , n , "armstrong")
else:
    print(s,n,"No")
