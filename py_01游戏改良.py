# hi_瞒的 第一个小游戏
import random
secret = random.randint(1,10)
temp = input("来猜猜小小瞒心中所想的数字，猜中有奖哦！\n请输入数字：")
guess = int(temp)
while guess == secret:
    print("你真棒,猜对了呢")
    print("但是也没有奖励,哈哈哈")
while guess != secret:
    temp = input("哎呀猜错啦！请输入数字：")
    guess = int(temp)
    # guess = temp
    # if guess == "7":
    if guess == secret:
        print("你真棒,猜对了呢")
        print("但是也没有奖励,哈哈哈")

    if guess > secret:
        print("亲爱的,大了大了")
    else:
        print("亲爱的,小了小了")
        # print("你猜错啦，小小瞒心中的所想的数据是：7啦！")

print('游戏结束啦！不玩啦，哈哈')



