# continu 语句作用是终止本轮循环并开始下一论循环（开始下一轮之前，会先测试循环条件）
for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
    print(i)