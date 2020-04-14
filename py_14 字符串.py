"""
字符串

1、 字符串和元组一样，一旦定下来就不能更改，如果需要更改只能
str = 'i love my family'
str =str[:6] + '插入的字符串' + str[6:]
比较操作符，逻辑操作符，成员关系操作符的操作与列表/元组是一样的


"""
#  2、 通过拼接就字符串的各部分得到新的字符串，并不是真正意义上的改变了原字符串，原来的那个‘家伙’
# 还在，只是将变量指向了新的字符串（旧的字符串一旦失去了变量的引用，就是会Python的垃圾回收机制释放掉）


str = 'i love my family'
str = str[:6]
print(str)
#  3、当需要访问字符串的其中一个字符的时候，只需要用索引列表或者元组的方法来索引字符串即可

"""
字符串和元组一样，一旦定下来就不能更改，如果需要更改只能， 通过拼接的方式来进行改变了
str = 'i love my family'
str =str[:6] + '插入的字符串' + str[6:]
"""

str1 = 'i love my family'
str1 =str[:6] + '我最棒' + str1[6:]
print(str1)

#  字符串的常见奇葩方法
#  1、capitalize() 方法， 把字符串的第一个字符爱称大写
str2 = 'i love you'
print(str2.capitalize())
#  2、casefold() 方法， 把字符串的第一个字符爱称大写
str2 = 'I love You'
print(str2.casefold())
#  3、casefold() 方法， 把字符串的第一个字符爱称大写
str2 = 'I love You'
print(str2.casefold())
