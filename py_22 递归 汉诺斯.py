"""

递归求解汉诺塔
●对于游戏的玩法，我们可以简单分解为三个步骤
-将前63个盘子从X移动到Y上。
-将最底下的第64个盘子从X移动到Z上。
-将Y上的63个盘子移动到Z上。
●
问题一:将X上的63个盘子借助Z移到Y上;
问题二:将Y上的63个盘子借助X移到Z上。

问题一(“ 将X上的63个盘子借助Z移到Y上”)拆解为:
-将前62个盘子从X移动到Z上。
-将最底下的第63个盘子移动到Y上。
-将Z止的62个盘子移动到Y上。
问题二(“ 将Y上的63个盘子借助X移到Z上”)拆解为:
●将前62个盘子从Y移动到X上。
将最底下的第63个盘子移动到Z上。
●将X上的62个盘子移动到Y上。

"""
def hanmos(n,x,y,z):
    if n == 1:
        print(x,'-->','z')
    else:
        hanmos(n-1,x,z,y)# 将前n-1个，从x 移到  y 上
        print(x,'-->',z) #将最低下的最后一个，从 x 移动到 z 上

        hanmos(n-1,y,x,z)#将 y 上的 n-1 个移动到 z 上


n = int(input('请输入汉诺塔的层数：'))
hanmos(n,'x','y','z')


