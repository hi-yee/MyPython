# 遍历favorite变量中的值
# end=''  表示打印值不换行

favourite = 'fishC'
for each in favourite:
    print(each,end='')
    # 去掉 end=''会把变量中的每一个字符都遍历出来
    # print(each)


number = ['小明','小红','小兰','小绿','小紫']
for i in number:
    print(i,len(number))