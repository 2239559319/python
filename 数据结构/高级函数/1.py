def funcMap():
    '''
    用第一参数函数对可迭代对象的每一项进行修改
    '''
    mylist=[i for i in range(10)]
    newList=list(map(str,mylist))
    print(newList)

    #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def funcFilter():
    '''
    对可迭代对象进行过滤删除
    '''
    mylist=[i for i in range(10)]
    newList=list(filter(lambda x:x%2==0,mylist))
    print(newList)

    #[0, 2, 4, 6, 8]
