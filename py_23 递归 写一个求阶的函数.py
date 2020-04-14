# 正整数的阶数指的是：1乘以2乘以3乘以4乘以5一直到所要求的数。
# 非递归版本：
def recuision(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
number = int(input('请输入一个整数：'))
result = recuision(number)
print("%d 的阶乘是：%d" % (number,result))

# 上面的普通函数，以下使用递归演示

def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input('请输入一个整数：'))
result = factorial(number)
print("%d 的阶乘是：%d" % (number,result))