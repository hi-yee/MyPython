"""
函数  和  过程

在许多的编程语言中， 函数和过程其实是区分开的。
一般认为函数是： 有返回值得，  而过程是：简单，特殊并且没有返回值得。

Python严格来说只有函数，没过程，
当不写return 语句的时候，默认Python会认为函数是 return None。
所以说Python所有的函数都是有返回值的。 如以下的例子：


"""

def hello():
    print('hello')

temp = hello()
print(temp)

"""
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""


"""
函数的返回值
"""
# Python 可以动态确定函数的类型，而且函数还能返回不同类型值。还记得以前说过的’Python没有变量，只有名字‘这句话吗，
# 只需要知道Python会返回一个东西，然后拿来用就可以了。
# 另外Python似乎还可以返回多个值：
def test():
    return [1,3,5,7,9,'小小瞒','你最棒']
#     通过列表的方式
print(test())

# python可以利用列表打包多种类型的值一次性返回。当然，你也可以直接用元组的形式返回多个值。
def test():
    return 1,'小小瞒','himan',1122

print(test())


"""
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
"""
函数变量的作用域
"""
"""
变量的作用域也就说平时所说的变量可见性， 如上所说，一般的编程语言都有局部变量(Local Variable) 和全局变量(Global Variable)
"""
# 分析以下的代码块，变量 old_price, rate, new_price, 是全局变量，而 final_orice 是局部变量
# def discounts(price,rate):
#     final_price  = price * rate
#     return final_price
#
# old_price = float(input('请输入原价：'))
# rate = float(input('请输入折扣率：'))
# new_price = discounts(old_price,rate)
# print('折扣价格是：',new_price)

"""
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

# 在以下代码块中，试图打印出局部变量 final_price 的值，程序便会报错，因为final_price没有被定义，
# 它的作用域只在于 discount() 的定义范围内-----有效
# def discounts(price,rate):
#     final_price  = price * rate
#     return final_price
#
# old_price = float(input('请输入原价：'))
# rate = float(input('请输入折扣率：'))
# new_price = discounts(old_price,rate)
# print('折扣价格是：',new_price)
# print('这里试图打印局部变量final_price 的值：',final_price)

"""
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

# 以下修改的代码块中，在 函数discount()中，打印局部变量'final_price'就不会报错
# def discounts(price,rate):
#     final_price  = price * rate
#     print('这里试图打印局部变量final_price 的值：', final_price)
#     return final_price
#
# old_price = float(input('请输入原价：'))
# rate = float(input('请输入折扣率：'))
# new_price = discounts(old_price,rate)
# print('折扣价格是：',new_price)

"""
总结：
1、 final_price 没有被定义过，也就说，Python找不到 final_price  这个变量， 这是因为 final_price  只是一个局部变量，它的作用范围
只在它的地盘是哪个-----discount() 函数的定义范围内-----有效，出了这个范围，就不在属于它的地盘了，它将什么都不是。

2、 在函数里面定义的参数以及变量，都称为： 局部变量 ，出来这个函数，这些变量都是无效的。 事实上的原理是，Python 在运行函数的时候，
利用栈进行存储，当执行完该函数后，函数中的所有的数据都会被删除，在所以在函数外边是无法访问到函数每部的布局变量的。

3、 与局部变量相对的是全局变量，在程序中old_price 、new_price、rate都是函数后定义的。
他们都是全局变量，全局变量用于更大的作用域，例如可以在函数中访问它们。如以下的代码块：
"""
# def discounts(price,rate):
#     final_price  = price * rate
#     print('这里试图打印全局变量old_price 的值：', old_price)
#     return final_price
#
# old_price = float(input('请输入原价：'))
# rate = float(input('请输入折扣率：'))
# new_price = discounts(old_price,rate)
# print('折扣价格是：',new_price)


"""
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""


#  使用全局变量的时候一定要小心，任何一种编程语言中都是如此。在Python中，你可以在函数中肆无忌惮的访问一个全局变量，
#  但是你试图修改它，就会有奇怪的事情出现，

def discounts(price,rate):
    final_price  = price * rate
    old_price = 50  # 这里试图修改全局变量
    print('在局部变量中修改后的old_price 的值是：', old_price)
    return final_price

old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price,rate)
print('全局变量old_price 现在的值是：',old_price)
print('折扣价格是：',new_price)


"""
总结： 
1 、如果试图在局部变量中试图修改全局变量， 那么Python会创建新的局部变量代替（名字跟全局变量相同）
三真正的全局变量是纹丝不动的，所以实现的结果和大家的预期不同。

2 、 全局变量在整个代码段中都是可以访问到的，但是不要试图在内部函数中修改全局变量的值，
因为那样Python会自动在函数内部新建一个名称一样的局部变量代替
"""