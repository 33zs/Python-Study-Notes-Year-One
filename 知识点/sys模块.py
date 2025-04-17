#sys
"""
sys模块是与python解释器交互的一个接口。
sys 模块提供了许多函数和变量来处理 Python 运行时环境的不同部分。
"""
#sys.argv
"""
在sys.argv被调用时，其会返回一个列表List,列表的内容是在命令行中运行python文件时，输入的内容
1、sys.argv 是获取运行python文件的时候命令行参数，且以list形式存储参数

2、sys.argv[0]表示代码本身文件路径
3、sys.argv[1]表示第一个参数
"""
import sys
a=sys.argv
print(sys.argv)
print(sys.argv[0])
#sys.exit(n)退出程序，正常退出时exit(0)
b=2
if b<=2:
    sys.exit(8)
#注释：退出python执行程序，下面的代码将不会执行，如同shell中的exit一样。

#sys.version获取python解释程序的版本信息
print(sys.version)

#sys.platform返回操作系统平台的名称
print(sys.platform)

#sys.stdin.readline()与input
"""

①sys.stdin.readline()方式与input方式的区别是：
len(aa)元素中多了一个‘\n’换行符。即sys.stdin.readline()方式会读入换行符。

②还有一个区别在于，input()里面可以直接传入文本，然后打印出来。
"""
# sys.stdin.readline() 相当于input，区别在于input不会读入'\n'
aa = sys.stdin.readline()  # 输入数据多一个'\n'
bb = input('请输入：')

print(len(aa))
print(len(bb))
#结果
"""
i love DL
请输入：i love DL
10
9
"""

#sys.stdout与print
"""
注：sys.stdout.write(obj+‘\n’)中的obj只能是字符串。
"""
#等价
sys.stdout.write('hello' + '\n')
print('hello')

# sys.stdin.readline() 相当于input，区别在于input不会读入'\n'
aa = sys.stdin.readline()
bb = input('请输入：')

sys.stdout.write(str(len(aa)) + '\n')  # 默认无法实现print方式的sep参数功能，所以需要手动在后面添加一个换行符
print(len(bb))
#总结
"""
# -*- coding: utf-8 -*-
# Python中sys模块：该模块提供对解释器使用或维护的一些变量的访问，以及与解释器强烈交互的函数
#sys.winver#返沪python解释器主版号
# sys.argv #命令行参数List，第一个元素是程序本身路径
# sys.modules.keys() #返回所有已经导入的模块列表
# sys.exc_info() #获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
# sys.exit(n) #程序，正常退出时exit(0)
# sys.hexversion #获取Python解释程序的版本值，16进制格式如：0x020403F0
# sys.version #获取Python解释程序的版本信息
# sys.maxint #最大的Int值
# sys.maxunicode #最大的Unicode值
# sys.modules #返回系统导入的模块字段，key是模块名，value是模块
# sys.path #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform #返回操作系统平台名称
# sys.stdout #标准输出
# sys.stdin #标准输入
# sys.stderr #错误输出
# sys.exc_clear() 	#用来清除当前线程所出现的当前的或最近的错误信息
# sys.exec_prefix 	#返回平台独立的python文件安装的位置
# sys.byteorder 		#本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'
# sys.copyright 		#记录python版权相关的东西
# sys.api_version 	#解释器的C的API版本
# sys.version_info 	#获取Python解释器的版本信息
# sys.getwindowsversion #获取Windows的版本
# sys.getdefaultencoding #返回当前你所用的默认的字符编码格式
# sys.getfilesystemencoding #返回将Unicode文件名转换成系统文件名的编码的名字
# sys.setdefaultencoding(name) #用来设置当前默认的字符编码
# sys.builtin_module_names 	#Python解释器导入的模块列表
# sys.executable 					#Python解释程序路径
# sys.stdin.readline 				#从标准输入读一行，sys.stdout.write("a") 屏幕输出a
"""
dir(sys) #dir()方法查看模块中可用的方法
print(sys.getdefaultencoding()) #获取系统当前编码，一般默认为ascii.
print(sys.platform) # 获取当前系统平台. 如：win32、Linux等。
print(sys.argv) #sys.argv 变量是一个包含了命令行参数的字符串列表
# print(sys.path)
# print(sys.modules.keys())
# print(sys.modules.values())
sys.exit() # 一般情况下执行到主程序末尾，解释器自动退出，但是如果需要中途退出程序，可以调用sys.exit函数


