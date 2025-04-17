#eval
#将字符串当成有效的表达式来求值并返回计算结果
#基本的数字计算
print(eval("1+1"))
print(eval("'*'*10"))
print(type(eval("[1,2,3,4,5]")))
print(type(eval("{'name':'xiaoming','age':18}")))
#计算器
string1=input("请输入一个计算题")
print(eval(string1))
#不要滥用eval函数
#在开发时千万不要使用eval直接转换input的结果
__import__("os").system("is")
#等价
"""
import os
os.system("终端命令")
"""
#用户会直接进行终端命令

#exec
"""
能够执行存储在字符串或文件中的python语句，
eval()函数只能执行计算数学表达时的结果的功能
而evec()能够动态地在执行负责的python代码
将python代码存入txt文件中时可以利用exec()函数调用
"""
exec("def test():print('test1')")
test()
