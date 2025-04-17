#异常

try:
    #尝试执行的代码
    pass
except 错误类型1：
    #针对错误类型1，对应的代码处理
    pass
except 错误类型2：
    #针对错误类型2，对应的代码处理
    pass
except(错误类型3，错误类型4)：
    #针对错误类型3，4对应的代码处理
    pass
except Exception as result:
    #打印错误信息
    print(result)
else:
    #没有异常才会执行的代码
    pass
finally:
    #无论是否有异常，都会执行的代码
    print("无论是否有异常，都会执行的代码")
#常见异常
"""
exception:大多数错误类型的基类
AttributeError:对象没有这个属性
EOFError:没有内建输入，到达EOF标记---即结尾
IOError:输入/输出操作失败
indexError:序列中没有此索引（index）
KeyError:集合或字典中不存在这个键
KeypboardInterrupt:使用ctrl-C中断执行
NameError:使用不存在的id、
Stoplteration:迭代器没有更多的值
TypeError:对类型无效的操作
ValueError:传入无效的参数
ZeroDivisonError:除零
"""