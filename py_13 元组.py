"""
列表和元组之间的亲近关系
列表可以随意添加， 删除， 排序等操作

元组 是不能改变的，不能添加， 删除， 排序

"""
tupel1 = (1,1,2,4,5,4,5,4,5)

# 列表的标志性符号是中括号[]，
# 元组的标志性符号是 ，逗号，

# 1 、可以通过切片的方式来复制元组
print(tupel1[:])

tupel2 = tupel1[:]
print(tupel2)
# 没有逗号是int类型
temp = (1)
print(type(temp))
# 有逗号就是一个元组，没小括号不是标识
temp1 = 2,3,4,4
print(type(temp1))
# 创建空元组， 在变量名后加空号的小括号就行
temp3 = ()
print(type(temp3))


print(8 * 8)

print(8 * (8,))

# 如果添加，只有一个元素的元组，请在它后面加上一个逗号(,)
ie = 8,
ie1 = 8

print(type(ie))
print(type(ie1))


#  2、 更新元组
temp4 = ('小小瞒','小柠檬','小番茄','小西瓜')
temp5 = temp4[:3] + ('小冬瓜',) + temp4[3:]



print(temp4,temp5,sep='\n')

# 删除元组

del temp4