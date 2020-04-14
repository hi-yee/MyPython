# 按照100分制，90以上成绩为：A，80-90为：B，60-80为：C，60以下为：D
# 当用户输入分数时，自动转换为：A/B/C/D的形式打印
# 方法一：每次输入完一次，判断完程序就退出了
# score = float(input("请输入分数："))
# if 100>score>=90:
#     print('A')
# if  90>score>=80:
#     print('B')
# if 80>score>=60:
#     print('C')
# if score <= 60:
#     print('D')
# if score<0 or score>100:
#     print("输入错误")


# 方法二：使用if  else语句进行判断，判断完成之后退出了
# 条件多了会造成诸多的不便
score = float(input("请输入分数："))
if 100>=score>=90:
    print('A')
else:
    if 90>score>=80:
        print('B')
    else:
        if 80>score>=60:
            print('C')
        else:
            if score<60:
                print('D')
            else:
                if score<0 or score>100:
                    print('输入错误')


# 方法三：使用if elif，避免悬挂else

score = float(input("请输入分数："))
if 100>=score>=90:
    print('A')
elif 90>score>=80:
    print('B')
elif 80>score>=60:
    print('C')
elif score<60:
    print('D')
elif score<0 or score>100:
    print('输入错误')
