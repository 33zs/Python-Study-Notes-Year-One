#一行输入多个&输入多行数据
#1.input().split()用法
username,passwd=input("请输入用户名，密码").split()
#注意：input（）的返回类型是str，如果是整数需要转化为int才能正常使用
print(username,passwd)
#lilian 123456
#2.str.split(）用法
txt1="google#facebook#runoob#taobao"
x1=txt1.split("#",1)
print(x1)
#3.map()用法
"""
pyth0n 2.x返回列表
python 3.x返回迭代器
所以python3.x要加list（）函数将迭代器转化为列表
"""
print(list(map(lambda x:x**2,range(11))))