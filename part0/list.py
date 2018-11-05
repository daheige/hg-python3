mylist=[1,2,3]
print(mylist[1])
# print(mylist[3]) #越界了报错

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
mylist.append("daheige")
print(mylist) #[1, 2, 3, 'daheige']

# 弹出一个元素
print(mylist.pop())

#替换元素
mylist[1] = 123

print(mylist)

# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
l = []
print("l len is %d" % len(l))

l.append(1)
print(l)
