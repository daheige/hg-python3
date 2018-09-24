#!/usr/bin/env python3

user_list = [
    ["daheige", 1234],
    ["xiaoming", 3456],
    ["xxx", 7890]
]

for [user, pwd] in user_list:
    print(user)
    print(pwd)

x = [1, 3, 4, 5]

print(x * 2)  # 对切片进行叠加 [1, 3, 4, 5, 1, 3, 4, 5]

# 初始化空列表
y = []

# 下面的赋值会报错
# y[0]=1
# y[2]=34
# print(y)

z = [None] * 2  # 初始化列表
z[0] = 1
z[1] = 2
# z[2] = 3 #不能越过列表的index range IndexError: list assignment index out of range
print(z)
