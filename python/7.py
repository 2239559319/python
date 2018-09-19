import time

def deco(func):
    def wrapper(*args,**kwargs):
        print("Hello World")
        func(*args, **kwargs)
    return wrapper
@deco
def func1(a,b):
    print(a+b)
@deco
def func2(a,b,c):
    print(a+b+c)

if __name__=="__main__":
    f=func1
    f("12","34")
    func2("12","34","56")

'''输出
Hello World
1234
Hello World
123456
'''