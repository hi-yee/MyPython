# 明确得到变量的类型
# 可以通过 type（）和isinstance（）两个BIF来得到
# type（）可以直接得到变量的参数
# isinstance（）有连个参数，第一个是待确定类型的数据，第二个是指定一个数据类型，
# isinstance()会根据两个参数返回一个布尔类型的值，true表示类型一致，FALSE表示类型不一致

print(type(250))
print(type('520'))
print(type(25.0))
print(type(0))
print(type(True))

  # 这个函数会判断，如果是真的会返回True，如果是假的，会返回False
print(isinstance(520,float))