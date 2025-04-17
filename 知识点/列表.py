
#列表
#创建列表
'''
1、使用中括号
2、内置函数list
'''

#切片
'''
1、步长是正数，从左往右取
2、步长是负数、从右往左取
3、默认步长为1,step的绝对值决定了步长
'''
alist=['item1','item2','item3','item4']
print(alist[:2])
print(alist[1:])
alist[0:2]=['item']
print(alist)

for i  in range(1,10,2):
    print(i)
#end的数不取
#列表生成式
'''
1、for循环后加if语句筛选
2、两层循环
'''
list_=list(x*x for x in range(1,11) if x%2==0)
print('list_',list_)

list__=[m+n for m in 'ABC' for n in 'XYZ']
print('list__',list__)

#增加元素
#1 append函数：在列表末尾添加一个元素
'''''
list.append('element')  element可以是任意类型
'''

list1=[1,2,3,4,5]
list1.append(['hello','python'])
print(list1)

#2 extend函数:在列表末尾至少添加一个元素
''''
list.extend(element)
element是可迭代对象数据  (可迭代对象：能用for循环进行迭代的对象，例如：字符串，列表，元组，字典，集合)
'''

list2=[1,2,3,4,5]
list2.extend(['hello','python'])
print(list2)

#3 insert函数：在列表的任意位置添加一个元素
''''
list.insert(index,element)
'''

list3=[1,2,3,4,5]
list3.insert(2,['hello','python'])
print(list3)

#4 切片在任意位置上增加N多个元素
list4=[1,2,3,4,5]
list5=['hello','python']
list4[5:]=list5
print(list4)
list4[0:]=list5
print(list4)

#删除元素
#1 pop函数  移除列表中的一个元素（默认是最后一个） 并将该元素作为返回值返回
'''''
list.pop(index)
'''
list6=[1,2,3,4,5]
a1=list6.pop()
print('删除的元素：',a1)
print('删除后的列表',list6)
#a2=list6.pop(4) #索引不存在则indexerror

#2 remove函数 根据元素内容来删除，删除首次出现的元素，一次删除一个元素
#无返回值
'''''
list.remove(element)
'''''
list7=[1,2,3,4,5,5,5]
list7.remove(5)
print('remove',list7)

#3 del函数 删除一个或连续几个元素
''''
del list[index]
del list[index1:index2]
del list 删除列表后无法访问
'''
list8=[1,2,3,4,5,6]
del list8[1]
print(list8)

list9=[1,2,3,4,5,6]
del list9[1:3]
print(list9)

'''''
list10=[1,2,3,4,5,6]
del list10
print('list10',list10)
'''
#出现error not defined

#clear：清除列表
list11=[1,2,3,4,5,6]
b=list11.clear()
print(b)

#index函数：查找元素在列表中的索引位置，有重复元素时则索引值为最开始检索到的元素位置，
# 有返回值，返回值为索引位置
'''''
list.index(element)
'''''
list12=[1,1,2,3,4,5,6]
c=list12.index(1)
print(c)
print(list12[1:].index(1))

#count函数 统计某个元素在列表中出现的次数，有返回值
'''
list.count(element)
'''
list13=[1,1,1,1,2,3,4,5,6]
d=list13.count(1)
print(d)
e=list13.count(7)
print(e)


#reverse函数: 反转列表 修改原来列表，没有返回值
'''
list.reverse()
'''
list14=[1,2,3,4,5,6,7,8,9,10]
list14.reverse()
print(list14)

#reversed函数:对于给定的序列（包括列表 、元组、字符串以及range（）区间）进行逆序排列
#不会修改原来序列中元素的顺序,返回逆序排列后的列表
'''
list(reversed(list_original))
'''
list15=[1,2,3,4,5,6]
liast5_reverse=list(reversed(list15))
print(liast5_reverse)
print(list15)

#sort/sorted函数
#sort会改变原有列表，无返回值
#sorted不会改变原有列表，返回新列表
list16=[1,2,3,4,5,6]
list16.sort()
print('list16',list16)
f=sorted(list16,reverse=True)
print('sorted_True',f)
f=sorted(list16)
print(list16)

#copy方法
list17=list16.copy()
print(list17)

#列表操作的函数
"""
1、len(list) 列表元素个数
2、max(list) 返回元素最大值
"""
"""
3、min(list) 返回元素最小值
如果列表为嵌套列表，则比较第一个值,第一个值相同则比较下一个值
"""
listC=[[3,3,"AAAA"],[4,4,"aa11"],[3,3,"aaa"],[3,3,"111bb"],[4,1,"aa"]]
print(min(listC))
stulist=[[85.0,"zhansan","80","85","90"],[89,"lisi","90","81","96"],[86.0,"wangwu","79","88","91"],[91.0,"chenliu","92","87","94"]]
print(min(stulist))
"""
4、list(seq) 将元组转化为列表
5、cmp(list1,list) 比较两个列表的元素
'''

#脚本操作符
#+
print([1,2,3]+[4,5,6])
#*
print(['1']*4)
#将列表转化为字符串拼接
lis=[1,2,3,4,5,6]
rec=''
for i in lis:
    rec=rec+str(i)+" "
print(rec)
#列表生成式
li=[[]]*3
print(li)
li[0].append(3)
print(li)
li2=[[] for i in range(3)]
print(li2)

"""
sort(*,key=None,reverse=False)
