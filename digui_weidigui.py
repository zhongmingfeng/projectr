# 使用递归函数需要注意防止栈溢出，在计算机中，函数调用是通过栈（stack）这种数据结构实现的
# 每次调用函数的时候，栈会加一层栈帧，每次返回的时候，栈会减一层栈帧
# 由于栈的大小部署无限的，所以递归调用次数多了，会导致栈溢出的现象
__author__ = 'Administrator'

# 下面函数是求阶乘和
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(999))  # 迭代次数n超过998会报错，其实就是栈溢出


# 解决栈溢出的方法就是使用尾递归，尾递归跟循环的效果是一样的，把循环看成是一种特殊的尾递归也是可以的
# 尾递归就是在返回的时候调用函数本身，并且return返回的不能含有表达式
# 这样，编译器或者解释器可以把函数进行优化，使递归不论调用多少次，都只使用一个栈帧，不会出现溢出的情
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, total):
    if num == 1:
        return total
    return fact_iter(num - 1, num * total)


print(fact_iter(999, 1))
