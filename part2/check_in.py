users = [
    ['daheige','1234'],
    ['xiaoming','3456'],
    ['heige','1235']
]

username = input('your name: ')
code = input("your pin code: ")
if [username,code] in users:
    print("access sucess")
else:
    print("access not allowed")

'''
运行结果
[heige@daheige part2]$ python check_in.py
your name: daheige
your pin code: 1234
access sucess
[heige@daheige part2]$ python check_in.py
your name: daheige
your pin code: 1234
access sucess
'''
