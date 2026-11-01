# n = 5
# i = 1
# while i <= n:
#     j = 1 
#     while j <= i:
#         print(j, end = " ")
#         j += 1
#     i += 1
#     print()
# i = 1
# while i <=n:
#     j = 1
#     while j <= n-i:
#         print(" ",end=" ")
#         j+=1
#     k = 1
#     while k <=i:
#         print(k, end=" ")
#         k+=1
#     print()
#     i+=1
# i = 1
# while i <=n:
#     j = 1
#     while j <= n-i:

#         print(" ",end=" ")
#         j+=1
#     k = i
#     while k >=1:
#         print(k, end=" ")
#         k-=1
#     print()
#     i+=1
n=5
i = 0
while i <= n:
    j = 0 
    while j < n-i:
        print(" ",end=" ")
        j+=1
    k = 1
    while k <= i:
        print(k, end=" ")
        k+=1
    l = i - 1
    while l >=1:
        print(l,end=" ")
        l-=1
    print()
    i+=1
i = 0
while i < n-1:
    j = 0
    while j <= i:
        print(" ", end=" ")
        j+=1
    k = 1
    while k<n-i:
        print(k,end=" ")
        k+=1
    l = (n-i)-2
    while l>=1:
        print(l,end=" ")
        l-=1
    print()
    i+=1





i = 1
while i <= n:
    j = 0 
    while j < n-i:
        print(" ",end=" ")
        j+=1
    k = 1
    while k <= 2*i-1:
        print("*", end=" ")
        k+=1
    print()
    i+=1
i = 1
while i < n:
    k = 1
    while k <= i:
        print(" ",end=" ")
        k+=1
    j = 2*(n-i)
    while j > 1 :
        print("*",end=" ")
        j-=1
    i+=1
    print()
