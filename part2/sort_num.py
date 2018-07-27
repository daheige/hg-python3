nums = [1,2,3,56,89]
nums.sort()
print(nums)

# sort可以接收key或者reverse

x = ["fefe","ss","daheige","a"]
x.sort(key=len)
print(x)

#翻转
x.sort(reverse=True)
print(x)

'''
[1, 2, 3, 56, 89]
['a', 'ss', 'fefe', 'daheige']
['ss', 'fefe', 'daheige', 'a']
'''

