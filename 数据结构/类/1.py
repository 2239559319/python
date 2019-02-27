class Counter(object):
    '''Models a counter'''

    #class variable
    instances=0

    #constructor
    def __init__(self):
        '''set up the counter'''
        Counter.instances+=1
        self.reset()

    def reset(self):
        self._value=0               #视为私有变量

    def increment(self,amount=1):
        self._value+=amount

    def decrement(self,amount=1):
        self._value-=amount

    def getValue(self):
        return self._value

    def __str__(self):          #把对象作为参数传递时运行 print
        return str(self._value)

    def __eq__(self, other):    # ==会运行这个方法
        if self is other:
            return True
        if type(self)!=type(other):
            return False
        return self._value==other._value

counter=Counter()
print(counter.__doc__)      # Models a counter
print(counter)              # 0