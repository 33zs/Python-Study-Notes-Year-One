import os
#文件打开
'''
open(文件名，访问模式)
'''

f=open('test.txt','w')

#关闭文件
'''
1、f.close()
f.closed()返回一个布尔值判断是否关闭文件 True/False
2、with 关键词自动关闭文件
3、
try:
    l=list(f)
    for line in l:
        print(line,end='')
finally:
        f.close()
'''
#访问模式
'''
r  以只读方式打开文件  文件的指针将会放在文件的开头，默认模式 如果文件不存在则出错
w  只用于写入，open时原文件会被清除，开始时光标处于开头第一个字节处  如果该文件已经存在则覆盖，  如果文件不存在则创建新文件 
a  打开一个文件用于追加 文件光标位于文件末尾 如果该文件已存在文件指针会放在文件的结尾  如果文件不存在创建新文件写入
x  创建指定文件， 如果文件不存在则error
r+ 打开一个文件用于读写。文件指针放在文件开头
W+ 打开一个文件用于读写 open时原文件会被清除，开始时光标处于开头第一个字节处  如果该文件已存在则覆盖 如果文件不存在则创建新文件
a+ 打开一个文件用于读写 文件光标位于文件末尾 如果文件已存在文件指针会放在文件的结尾 文件打开时是追加模式 文件不存你在则创建新文件写入
t  以文本模式打开 默认值
b  以二进制的格式打开文件
'''
'''
r+
1、先写后读
光标处于第一个字节，写入若有字符则覆盖，
读则读出此时光标后的字符
2、先读后写
光标处于第一个字节，读顺着光标的移动读出
写若无字符时为追加，有字符时为覆盖
总结：r、r+模式下，文件的光标处于开头第一个字节处
w+
1、先读后写
文件内容会被清除，无法读出
2、先写后读
写入沿着光标移动写入，
写完读无法读出，光标处于末尾
都无法读出
总结：w、w+模式下，open()原文件内容会被清除，开始时光标位于开头第一个光标
a+
1、先读后写
光标位于末尾，无法读出
移动光标到读取位置，写入时光标自动到末尾进行追加
2、先写后读
总结：a、a+模式下文件光标处于文件末尾，只要写入光标便会自动回到末尾，只会追加
'''
#文件读写
#写数据
'''
f.write() 
'''

f.write('hello world')
#f.close()
#print('\n',f.closed)

#读数据
'''
f.read(num)
可以从文件读取数据
num表示从文件读取数据的长度
不传入num 则读取所有数据
'''

content=f.read(5)
print(content)
content=f.read()
print(content)

#读取行
'''
f.readlines() 一次读取全部文件为列表，每一行为一个元素
'''

content=f.readlines()
print(content)

'''
f,readline() 一次读取一行
'''
content=f.readline()
print(content)
content=f.readline()
print(content)

'''
l=list(f)
for line in l:
    print(line,end='')
'''
#tell()
'''
返回一个整数告诉在文件的当前位置
'''
#seek()
'''
f.seek(offest,whence)移动光标
offest-开始的偏移量，也就是代表需要移动偏移的字节数
whence:默认值为0
0:代表从开头算起
1:代表从当前位置算起
2:代表从文件末尾算起
'''

#os模块
#文件重命名
'''
os.rename(需要修改的文件名，新的文件名)
'''

#删除文件
'''
os.remove(待删除的文件名)
'''
#创建文件夹
'''
os.mkdir(’‘）
如果文件已经存在则报错
os.makedirs(path1/path2...)
创建多级目录
'''
#获取当前的工作路径
'''
os.getcwd()
'''
#改变默认目录
'''
os.chdir()
'''
#os.listdir(path)
'''
返回路径下的所有文件和目录组成的列表
'''
#判断文件是否存在
'''
os.path.exists(path)
判定是否存在
存在则True 不存在则False

if os.path.exists(path1):
'''
#删除目录
'''
os.rmdir(path)
删除多级目录
os.removedirs(path1/path2...)
'''
#删除文件
'''
os.remove(path)
删除的是目录时会出错
'''
#将path设置为当前工作目录
'''
os.chdir(path)
'''
#shutil 模块
#复制文件
'''
shutil.copy(源文件，目标文件夹)
复制文件
目标文件夹不存在时不会报错
shutil.copy2(源文件，目标文件夹）保留元数据 拷贝文件的创建时间，修改时间
shutil.copytree(源文件夹，目标文件夹) 拷贝多个文件
只能移动到空文件夹中，目标文件夹非空报错
目标文件夹不存在则自动创建
'''
#移动文件或文件夹
'''
shutil.move(源文件/文件夹，目标文件夹）
目标文件夹不存在报错
'''
#删除文件夹
'''
shutil.remtree(源文件夹)
删除文件夹包括其文件
'''
