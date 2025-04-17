# 装饰函数
def funA(fun):
    def funB(*args, **kw):
        print('函数 ' + fun.__name__ + ' 开始执行')
        fun(*args, **kw)
        print('函数 ' + fun.__name__ + ' 执行完成')
    return funB

@funA
# 业务函数
def funC(name):
  print('Hello', name)

funC('Jhon')

#装饰器可以接受参数
# 装饰函数
def funA(flag):
    def funB(fun):
        def funC(*args, **kw):
            if flag == True:
                print('==========')
            elif flag == False:
                print('----------')
            fun(*args, **kw)
        return funC
    return funB

@funA(False)
# 业务函数
def funD(name):
  print('Hello', name)

funD('Jhon')
#基于类的实现

class Test(object):
    def __init__(self, func):
        print('函数名是 %s ' % func.__name__)
        self.__func = func

    def __call__(self, *args, **kwargs):
        self.__func()


@Test
def hello():
    print('Hello ...')


hello()