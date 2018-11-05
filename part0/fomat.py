#格式化字符串
#%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，
#后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
print('%d-%d' % (2,1))

'''
占位符 替换内容
%d  整数
%f  浮点数
%s  字符串
%x  十六进制整数
其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
'''

print("%.2f" % 12.345) #12.35

print("age %s gender: %s" % (12,True)) #多个变量格式化需要，隔开