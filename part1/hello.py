#!/usr/bin/env python3
#输入名字
x = input("please input your name")
print("your name is:",x)

# 将str转换为bytes
s = "daheige"
b = bytes(s,"utf-8") #相当于golang fmt.Println([]byte(str))
for x in b:
    print(x)

x = "大黑哥"
print(x)
