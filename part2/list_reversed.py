'''
>>> x
[1, 1, 2, 3, 123, 123, 234]
>>> reversed(x)
<list_reverseiterator object at 0x7fcbac86b9e8>
>>> list(reversed(x))
[234, 123, 123, 3, 2, 1, 1]
>>> x
[1, 1, 2, 3, 123, 123, 234]
>>> x
[1, 1, 2, 3, 123, 123, 234]
>>> x
[1, 1, 2, 3, 123, 123, 234]
'''
x = [1,1,2,4,5]

print(list(reversed(x)))
