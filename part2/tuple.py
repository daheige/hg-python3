b=[1,2,3,4]
print(tuple(b)) #将slice转换为tuple

x=reversed(b) #x是一迭代器
y=list(x) #必须调用list才可以转换为list
print(y)
