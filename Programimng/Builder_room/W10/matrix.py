m = [[1,2,3],
     [4,5,6],
     [7,8,9]]
# i = 0
# while i < len(m):
#     j = 0 
#     while j < len(m):
#         print(m[j][i],end=" ")
#         j+=1
#     print()
    # i+=1
# num = input().split()
# row = int(num[0])
# column = int(num[1])
# m = []
# i = 0

# while i < row:
#     part = input().split()
#     r = []
#     j = 0
#     while j < column:
#         r.append(int(part[j]))
#         j +=1
#     i +=1
#     m.append(r)
# print(m)

i = 0 
while i < len(m):
    j = 0
    sum = 0 
    while j < len(m):
        sum += m[i][j]
        j +=1
    print(sum,end=" ")
    i+=1
i = 0 
print()
while i < len(m):
    j = 0
    sum = 0 
    while j < len(m):
        sum += m[j][i]
        j +=1
    print(sum, end= " ")
    i+=1