names = ["fefefe","bob","trace"]
for name in names:
    print("current name is ",name)

sum = 0
for x in [1,2,3,4,45,43,321]:
    sum += x

print(sum)

#range(n) 产生0-n-1之间的数字
for x in list(range(5)):
    print(x)

# 在循环内部变量n不断自减
# 直到变为-1时，不再满足while条件，循环退出。
n = 99
sum = 0
while n > 0:
    sum +=n
    n -=2

print(sum)
