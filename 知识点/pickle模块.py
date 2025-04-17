#pickle模块介绍
"""
pickle是一种用于存储的持久化技术

首先从英文来理解一下这个模块：pickle 是腌渍的意思，也就是把东西腌起来保存成文件，要用的时候读出来洗洗还能用。

专业点的说法是：pickle是python序列化的一个工具!可以用来把对象来以文件的形式存储起来，用的时候再加载！

注意：pickle模块只能在python中使用，python中的几乎所有的数据类型都可以序列化！但是序列化以后得到的文件人看不懂！

pickle模块内部实现了用于序列化和反序列化Python对象结构的二进制协议

“Pickling”是将python对象层次结构转换成为字节流

“unpickling”是反向操作，即字节流（二进制文件或者类似字节的对象）转换成python对象层次结构。
"""
#dump()
"""
实行python对象的序列化，将obj保存到file中
"""
"""
pickle.dump(obj,file[,protocol])
obj:需要持久化保存的对象
file:将对象序列化以后保存到的类文件对象 
protocol(default=4):可选参数，取值为0，1，2，3，4，5
3，4，5对应python3.x版本及之后的版本
"""
import pickle
my_dict={"name":"xuebi","age":24}
with open("text.txt","wb")as f:
    pickle.dump(my_dict,f)
#dumps()函数
"""
返回一个字符串，而不存入文件
"""
"""
pickle.dumps(obj[,protocal])
"""
p1=pickle.dumps(my_dict)
print(p1)
#load函数
"""
用于反序列化，将序列化的对象重新恢复成python对象
"""
file_path='./text.txt'
with open(file_path,'rb')as f:
    my_dict=pickle.load(f)
    print(my_dict)
    print(type(my_dict))
#loads()函数
"""
作用：从字符串中恢复对象
"""
t1=pickle.loads(p1)
print(t1)
#pickler()函数
"""
作用：使用该对象调用dump,load等方法
class pickle.Pickler(file[,protocol])
"""
#总结
"""
强大的 pickle 模块，也有它的短板，即 pickle 不支持并发地访问持久性对象，在复杂的系统环境下，尤其是读取海量数据时，使用 pickle 会使整个系统的I/O读取性能成为瓶颈。

这种情况下，可以使用 ZODB。
ZODB 是一个健壮的、多用户的和面向对象的数据库系统，专门用于存储 Python 语言中的对象数据，它能够存储和管理任意复杂的 Python 对象，并支持事务操作和并发控制。

并且，ZODB 也是在 Python 的序列化操作基础之上实现的，因此要想有效地使用 ZODB，必须先学好 pickle。
————————————————
版权声明：本文为CSDN博主「桉夏与猫」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_28790663/article/details/115496733
"""