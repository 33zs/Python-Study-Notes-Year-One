#enumerate
"""
枚举，列举的意思
对于一个可迭代的/可遍历的对象（列表，字符串），可组成一个索引序列，利用它可以同时获得索引和值
可以用于计数
"""
list1=["这","是","一","个","测","试"]
for index, item in enumerate(list1):
    print(index,item)
#可以接受第二个参数，用于指定索引的起始值
for index1,item1 in enumerate(list1,1):
    print(index1,item1)
#统计文件的行数
count=0
for index2,line in enumerate(open(filename,"r")):
    count+=1