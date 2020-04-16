f = open('D:\\test\\reader.txt','r',encoding='utf-8') # 打开指定路径下的文件，“\” 反斜杠需要多一个 \ 来转译
print(f.read())  # 从文件

print(f.read(6))
