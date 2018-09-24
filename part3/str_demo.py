# 格式化替换
# 1 通过{}
print("{} is abc {} is haha".format("123", 456))

# 2 通过{0}占位符
print("{0} is abcedf {1} is 3455".format("1235", 4456))

# 3 通过指定的name进行格式化替换
print("{name} is abc,{age} is 30".format(name="xiaoming", age="age"))

# 设置字符串的替换格式
print("fefefe {num:s}".format(num="sss"))
print("your name is {name:s} and age is {age:d}".format(
    name="daheige", age=28))

# 浮点数替换 num:.3f 浮点数保留3位小数点
print("num is {num:.3f}".format(num=12.12))

print("num is {num:b}".format(num=123))  # 二进制的形式表示
print("score is {score:.2%}".format(score=123.34))  # 乘以100后加上%表示

# 设置对齐格式
print("your name is {name:<10s}".format(name="daheige"))  # 左边对齐
print("your name is {name:>10s}".format(name="daheige"))  # 右边对齐
print("num is {num:>10.2f}".format(num=123.4555))  # 右边对齐,保留2位小数
print("num is {0:>10.2f}, age is {1:d}".format(123.4555, 12))  # 右边对齐,保留2位小数

print("fefefe".center(23))  # 居中对齐

print("12345".center(12, "*"))  # 居中对齐,不足用*替代

# 字符串查找find
s = "1234abc $$$"
print(s.find("$$$"))  # 字符串出现的首次位置

print(s.startswith("1"))  # 以某某开头
print(s.find("$$", 1))
print(s.find("$$", 1, -3))  # 指定开始位置,结束位置
x = ["fefe", "sss"]
print("".join(x))  # 字符串拼接
print("ABC".lower())

s = "this is a test"
print(s.replace("test", "page"))
print("1-2-3-4".split("-"))  # 分割字符串为序列
print("1234".split(" "))

print("   fefefe  ".strip())  # 去掉字符串左右两边的空格
print("fefe ".strip())
print("fefe".upper())
