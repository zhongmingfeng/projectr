# array = [1,2,3,6,5,4]
#
# for i in range(len(array))[::-1]:
#     for j in range(i):
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]
#
# print(array)


ls = [10, 12, 32, 45, 88, 5, 96, 58, 3, 45]
print("初始list：%s" % ls)
for i in range(1, len(ls)):
    for j in range(0,len(ls)-i):
        if ls[j] > ls[j+1]:
            ls[j], ls[j+1] = ls[j+1], ls[j]
print(ls)