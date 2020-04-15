"""
如果用大括号括起来一堆数字，但是没体现对应关系，那么Python就会自动认为这堆玩意就是集合
集合的特点:
1、唯一，会自动过滤一些重复的数据
2、无序性，无法通过索引集合中的某一个数
"""
num1 = {}
print(type(num1))
num2 ={1,2,3,5,3,3,2,1,1,24,43,43}
print(type(num2))
print(num2)
# 2、无序性，无法通过索引集合中的某一个数
# print(num2[2])


# 创建集合
# 方法一： 直接把一堆元素用大括号（{}）括起来，用逗号分隔元素
set1 = {1,2,2,4,2,11,11,'hi','hello word'}
set2 = set([1,2,2,4,2,11,11,'hi','hello word'])   # 方法二: 用 set()  创建
print(set1 == set2)

# 现在如果要求要除去列表  [1,3,35,33,2,1,3,2,1,2,5,1,1,24,4,4] 中重复的元素。
list1 = [1,3,35,33,2,1,3,2,1,2,5,1,1,24,4,4]
temp = list1[:]
list1.clear()
for each in temp:
    if each not in list1:
        list1.append(each)

print(list1)

list2 = [1,2,31,11,11,2,2,24]
list2 = list(set(list2))
print(list2)

"""
访问集合
因为集合中的元素是无序的，所以并不能像序列那样用下标进行访问，但是可以使用迭代，把集合中的数据一个个读取出来：
"""
set1 = {1,2,3,4,5,4,32,12,3,2,1,1}
for each in  set1:
    print( each,end=" ")

# 当然也可以用in 和 not in来判断一个元素是否在集合中存在：
print(0 in set1)
print(11 not in set1)

# 也可以使用 add()方法 在集合的末尾添加元素，使用remove()方法删除集合中已知的元素：
set1.add(60)
print(set1)
set1.remove(5)
print(set1)


# 不可变的集合
# 有时候希望集合中的数据具有稳定性，也就是说，像元组一样不能随意地增加或删除集合的元素。那么我们可以定义不可变集合，
# 这里使用的是 frozenset() 函数，没错，就是把函数 frozen(冰冻)起来：
set3= frozenset({1,2,3,4,5})
print(set3)

set3.add(125)    # 冰冻的集合不能进行修改