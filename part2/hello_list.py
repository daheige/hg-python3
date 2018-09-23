x = list("heige")
print(x)

#通过列表方式修改元素,然后拼接成字符串
x[0] = "dah"

print(x)

print("".join(x)) #daheige

'''运行结果
['h', 'e', 'i', 'g', 'e']
['dah', 'e', 'i', 'g', 'e']
daheige
'''
