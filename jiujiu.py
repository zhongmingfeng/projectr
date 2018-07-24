# print('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

#
# for x in range(1,10):
#     for y in range(1, x+1):
#         print('%d*%d=%d' %(y, x, x*y), end='\t')
#     print('\n')

# for i in range(1, 10):
#         for j in range(1, i+1):
#             print('{}x{}={}\t'.format(i, j, i*j), end='')
#         print()

for i in range(5, 0, -1):
    print(i)
