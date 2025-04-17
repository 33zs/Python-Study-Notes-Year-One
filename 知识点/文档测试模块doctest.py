#doctest
"""
是python自带的一个模块。doctest有两种使用方式：一种是嵌入到python源码中，另外一种是放到一个独立文件。
doctest模块会搜索那些看起来像是python交互式会话中的代码片段，然后尝试执行并验证结果。
'>>>' 开头的行就是doctest测试用例。
不带 '>>>' 的行就是测试用例的输出。
如果实际运行的结果与期望的结果不一致，就标记为测试失败。

测试用例可以放在
1、模块的最开头
2、函数声明语句的下一行
其他地方放了也不会执行
verbose参数，如果设置为True则在执行测试的时候会输出详细信息。
默认是False，表示运行测试时，只有失败的用例会输出详细信息，成功的测试用例不会输出任何信息。
"""
def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b
if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
#在cmd中输入
#python naruto.py
#输出为
"""
Trying:
    multiply(4, 3)
Expecting:
    12
ok
Trying:
    multiply('a', 3)
Expecting:
    'aaa'
ok
1 items had no tests:
    __main__
1 items passed all tests:
   2 tests in __main__.multiply
2 tests in 2 items.
2 passed and 0 failed.
Test passed.

"""
"""
如果__main__函数有其他用途，不方便调用doctest.testmod()方法，那么可以用另外一种执行测试的方法，在cmd中输入：

$ python -m doctest naurto.py 
$ python -m doctest -v naruto.py

上面，-m 表示引用一个模块，-v 等价于 verbose=True。运行输出与上面基本一样。
"""
#2 doctest 放到独立文件中
#sasuke.txt
"""
>>> from naruto import multiply
>>> multiply(4, 3)
12
>>> multiply('a', 3)
'aaa'
"""
#cmd输入
#python -m doctest -v sasuke.txt
#输出
"""
Trying:
    from naruto import multiply
Expecting nothing
ok
Trying:
    multiply(4, 3)
Expecting:
    12
ok
Trying:
    multiply('a', 3)
Expecting:
    'aaa'
ok
1 items passed all tests:
   3 tests in sasuke.txt
3 tests in 1 items.
3 passed and 0 failed.
Test passed.

"""