"""
列表 、 元组 、 字符串  之间的共同点
1 、 都是可以通过索引得到每一个元素
2 、 默认索引都是从 0 开始，（当然灵活的Python 还支持附属索引）
3 、 可以通过分片的方式得到一个范围内的元素集合
4 、 很多共同的操作符（重复操作符， 拼接操作符， 成员关系操作符）
eg: 重复操作符  *     拼接操作符  +     成员关系蔡操作符 in  /  not in

"""
list2 = [12,'hi hello',2.21,'我最棒']
list1 = list2[:] + ['插入的元素哈哈哈'] + list2[:1]
print(type(list2))
print(list2[2])
print(list1)
tuple5 = 1,5,25,'hi'
tuple1 = ('ni','wo','ta')
print(type(tuple5))
print(type(tuple1))
print(tuple1[2])
a = '我是最棒的，我是小仙女'
print(type(a))
print(a[5])


# help(list)

#  1 、 list([iterable]) 方法， 用于把一个可迭代对象转化为列表。
#  迭代:就是重复反馈过程的活动,其目的通常是为了接近并到达所需的目标或结果.
#  每一次 对过程的重复被称为一次'迭代',而每一次迭代得到的结果会被用来作为下一次迭代的初始值.
#  就目前来说,迭代还就是一个for循环.
# list()方法, 要么不带参数, 要么带一个可迭代对象作为参数,俄日这个序列天生就是可迭代对象.

# 创建空列表
a = list()
print(a)

# 将字符串的每一个字符迭代到存放列表中
b = list('hi xiaoxiaoman')
print(b)

# 将元组中的每一个元素迭代存放到列表中
c = list((1.123,5820,125,125,2,5,5,5,))
print(c)

c = list(c)
print(c)


#  2 、 tuple([iterable]) 方法， 把一个可迭代对象转换成元组

# 将字符串的每一个字符迭代到存放列表中
b = tuple('jhhkf h kh fkhk h')
print(b)

#  3 、 str(obj) 方法， 用于把 obj 对象换换成 字符串，这个方法在前面结合 int()  和  float()用法一样
a = 123
print(type(a))
a = str(a)
print(type(a))

#  4 、 len(sub) 方法， 的作用是 返回sub参数的长度
#  字符串的长度
str = 'hi my name is xiaoxiaoman'
print(len(str))
#  列表的长度
list1 = [1,12,4545,445454,44444,'nihao']
print(len(list1))
# 元组的长度
tuple1 = 'zhe','shi','一个','元组'
print(len(tuple1))

#  5 、 max() 方法， 的作用是 返回 序列或集合中  的最大值
#  max() 参数可以是一个序列，返回值是该序列中的最大值；也可以是多个参数，那么
list = [1,18,15,0,-98,25,76,985]
print(max(list))
str = 'hi my name is xiaoxiaoman'
print(max(str))
tuple1 = 'zhe','shi','一个','元组'
print(max(tuple1))


#  6 、 min() 方法， 的作用是 返回 序列或集合中  的最小值
#  需要注意的是， max()方法和 min()方法， 都要保证序列或参数的数据类型统一。否者会出错。

list = [1,18,15,0,-98,25,76,985]
print(min(list))
str = 'hi my name is xiaoxiaoman'
print(min(str))
tuple1 = 'zhe','shi','一个','元组'
print(min(tuple1))

#  7 、 sum(iterable[stare]) 方法， 用于返回iterable的总和，用法和 max()方法和 min()方法是一样，
#  但是sum（）方法有一个参数(start),如果设置参数，表示从该值开始加起， 默认是 ：0

list = [1,18,15,0,-98,25,76,985]
print(sum(list))
tuple1 = -100,556,1,36
print(sum(tuple1,100))

#  8 、 sorted(iterable，key=None，reverse=False) 方法， 的作用是 返回一个排序列表
# sort()方法的和sorted()的实现效果一致，但是列表的内建方法sort() 是实现列表原地排序，
# 而sorted()方法 是返回一个排序后的新列表

list1 = [1,18,15,0,-98,25,76,985]
list2 = list[:]
print(list1)
list1.sort()
print(sorted(list2))
print(list1,list2,sep='\n')

#  9 、 reversed(sequence) 方法， 的作用是 返回逆向迭代序列的值，
#  实现的效果和列表的内建方法 reverse()方法一致，
# 但是列表的内建方法reverse() 是实现列表原地排序，
# 而reverseed()方法 是返回一个排序后的新列表

list1 = [1,18,15,0,-98,25,76,985]
list2 = list[:]
print(list1 ,'\n')
list1.reverse()
print(reversed(list2))
print(list1,list2,sep='\n')


#  10 、 enumerate(iterable) 方法， 的作用是 生成由二元组（二元组就是元素数量为二的元组） 构成的一个迭代对象，
#  每个二元组的由可迭代参数的索引号及其对应的元素组成的，

str1 = 'hi xiaoxiaoman '
for each in enumerate(str1):
    print(each)

#  11 、 zip(iter1,[,iter2,[]])  方法作用于 返回由各个可迭代参数共同组成的元组，
list1 = [1,3,5,7,9,11,15,15]
str1 = 'hixiaohi'
for  each in zip(list1,str1):
    print(each)

tuple1 = (2,4,6,8,10)
for each in zip(list1,str1,tuple1):
    print(each)