'''
for语句调用iter()函数，返回一个iterator object
iterrator对象有__next__()方法一次返回一个值
直到没有元素 raise StopIteration exception
用内置next()函数可以调用iterator的__next__()方法
'''
s='abc'
it=iter(s)
print(next(it))     #a
print(next(it))     #b
print(next(it))     #c
print(next(it))     #StopIteration

'''__iter__()返回一个带有__next__()方法的对象，如果定义了__next__()方法就返回本身就行了'''
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]