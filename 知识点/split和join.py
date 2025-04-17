'''''
split
拆分字符串，通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list)
'''''
#语法
'''''
str.split(str='',num=string.count(str))
'''''
#str:
# 表示分隔符，默认为空格，不能为空（‘’）
#无分隔符，整个字符串为列表的元素

#num:
#表示分割次数，num则分割为num+1个字符串
#默认-1，分割所有

#[n]:
#选取第几个分片

string='www.gz.com.cn'

#1
print(string.split('.'))  #['www', 'gz', 'com', 'cn']
#2
print(string.split('.',2)) #['www', 'gz', 'com.cn']
#3
print(string.split('.',2)[1]) #gz
#4
u1,u2,u3=string.split('.',2)
print(u1)  #www
print(u2)  #gz
print(u3)  #com.cn
#5多次分割
str='hello boy<[www.baidu.com]>byebye'
print(str.split('[')[1].split(']')[0])
#www.baidu.com]>byebye  先执行str.split('[')[1]的结果
#www.baidu.com

#join
#语法
#str.join(sequence)
#sequence应该是字符串类型，列表，元组元素为字符串，字典的key为字符串
str='-'
l=['2016','5','9']
t=('2016','5','9')
print(str.join(l))
print(str.join(t))

#输入多个数据分割
x=input().split()
print(x)
#一行输入两个数
a,b=input().split()
print(a)
print(b)
print(type(a))
print(type(b))
#a,b为str