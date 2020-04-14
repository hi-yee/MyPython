
'''
for循环其实还有一个小伙伴，range（）内建函数
语法： range（[star,]stop[,step=1]）
这个BIF有三个参数，其中用括号括起来的两个表示这两个参数的可选的，
step=1表示第三个参数默认为：1.
range()这个BIF的作用是，生成一个从star参数的值开始，到stop参数的值计算的数字序列。
常于for循环混迹于各种计数循环之间
只传递一个参数时，列如“range(5),它将会第一个参数默认设置为：0，生成0~5的所有数字
但是并不包括：5
'''

# 只传递一个参数
for i in range(5):
    print(i)
# 传递两个参数
for i in range(5,40):
    print(i)
# 传递三个参数

for i in range(0,21,3):
    print(i)

print(list(range(5)))


