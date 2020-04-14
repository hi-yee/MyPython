# break 语句的作用是，终止当前循环，跳出循环体
bingo = '你好有钱呀'
answer = input('请输入小小瞒最想听到的一句话：')
while True:
    if answer == bingo:
        break
    answer = input('抱歉，错了，请重新输入(只要输入正确的才能推出游戏):')
print('你真棒')
print('这都给你发现，优秀！')
