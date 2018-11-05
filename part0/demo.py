print("hello")
temp = input("请输入一个数字: ")
guess = int(temp)

if guess == 8:
    print("this num is 8")
else:
    print("输入的数字不对")

#采用换行符来进行控制代码块
print("game end")

a="abc"
b = a.replace("a","A")
print(b)
print("a",a)

'''
对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的
'''
