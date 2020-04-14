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
list2 = list2(set(list2))
print(list2)