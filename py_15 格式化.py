"""
格式化：  一 、 format（）  方法
"""
# format（） 方法， 接受位置参数和关键字参数，
# 二者均可以传递一个叫做  replacement  的字段，而这个replacement字段在字符串内
# 由大括号（ {} ） 表示：
# 如下参数 a 为例子

#  字符串中的{0}、{1}、{2}应该跟位置有关，依次被format（）的三个参数替换，
# 那么format（）中的三个参数为  位置参数

parameter1 = '{0} love {1}.{2} '.format('i','xiaoxiaoman','com')
print(parameter1)
#  字符串中的{a}、{b}、{c}相当于标签，format（）讲参数中等值的字符串替换进去，这就是  关键字参数

parameter2 = '{a} love {b}.{c}'.format(a='i',b='man',c='com')
print(parameter2)

# 位置参数和关键字参数可以 混合 一起使用，  但是 位置参数一定要在  关键字参数 之前 ，否者会报错
parameter2 = '{0} love {b}.{c}'.format('i',b='little-man',c='com')
print(parameter2)

# 打印{} 号,
parameter2 = '{{0}} love {b}.{c}'.format('i',b='little-man',c='com')
print(parameter2)

#  打印花括号{}， 参数位置的  ’不打印‘ 没有被输出，这是因为 {0} 的特殊功能，
# 被外层的大括号{} 给剥夺了，没有字段可以输出。
print('{{a}}'.format('不打印'))
# 打印反斜杠
print('//')

# 看下面列子， 位置参数{1} 和平常的有些不同，后面多了一个冒号，在替换域中，冒号表示格式化符号的开始，
# “.2” 的意思是四舍五入到保留两位小数点，而 f 的意思是 浮点数，所以按照 格式化符号的要求打印出了  3.14

parameter3 = '{0} : {1:.2f}'.format('圆周率',3.141592)
print(parameter3)



"""
格式化操作符： %
"""

# 1 、%C  格式化字符及其ASCII码
parameter4 ='%c' % 97
parameter5 ='%c %c %c %c%c %c %c %c ' %(104,120,99,97,105,121,120,100)
print(parameter4)
print(parameter5)


# 2 、%s  格式化字符串
parameter4 ='%s' % 'i love my famliy'
parameter5 ='%s %s %s ' %(104,120,99)
print(parameter4)
print(parameter5)

# 3 、%d  格式化整数
parameter4 ='%d + %d = %d' %(1314,520,1314+520 )
print(parameter4)


# 4 、%o  格式化无符号八进制数
parameter4 ='%o' %10
print(parameter4)

# 5 、%x  格式化无符号十六进制数
parameter4 ='%x'  %10
print(parameter4)

# 6 、%X  格式化无符号十六进制数（大写）
parameter4 ='%X' %160
print(parameter4)

# 7 、%f  格式化浮点数， 可指定小数点后的精度
parameter4 ='%.2f' % 1314.520527
print(parameter4)

# 8 、%e  用科学计数法格式化浮点数
parameter4 ='%e' % 1314.52
print(parameter4)


# 9 、%E  同 %e 用科学计数法格式化浮点数
parameter4 ='%e' % 1314.520527
print(parameter4)

# 10 、%g  根据值得大小，决定使用 %f 或 %e
parameter4 ='%.2f' % 1314.520527
print(parameter4)

# 11 、%G  作用同%g， 根据值得大小，决定使用 %f 或 %E
parameter4 ='%.2f' % 1314.520527
print(parameter4)

#  格式化操作符的辅助指令
#  符号                                      含义
#  m.n                 m是显示的最小总宽度，n是小数点后的位数
#  -                   结果左对齐
#  +                   在正数前面显示加好（+）
#  #                  在八进制数前 ，显示 ‘0O’，在十六进制数前显示 ‘0x’ 或者 ‘0X’
#  0                  显示的数字前面填充 ‘0’ 代替空格

a = '%5.1f' % 27.658
b = '%.2e' % 27.658
c = '%-10d %d' % (5,6)
d = '%+d %d' % (5,6)
e = '%# X %d' % (100,6)
f = '%# o %d' % (100,6)
g = '%# d %d' % (100,6)
h = '%010d %d' % (100,6)
i = '%-010d %d' % (100,6)

print(a,b,c,d,e,f,g,h,i,sep='\n')


# Python的转义字符  及含义： %
# 符号              说明                          符号              说明
# \'               单引号                        \r              回车符
# \"              双引号                         \f              换页符
# \a              发出系统响铃声                  \o             八进制数代表的字符
# \b              退格符                          \x             十六进制数代表的字符
# \n              换行符                          \0             表示空字符
# \t              横向制表符（TAB）                \\            反斜杠
# \v              纵向制表符

print('i\'m here!, \"hello\" \n \\hi liming')